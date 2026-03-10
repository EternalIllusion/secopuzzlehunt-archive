#!/usr/bin/env python3
"""
下载 snowfall.html 所需的所有图片，并用 MD5 重命名。
生成一个可以离线运行的 HTML 文件。
"""

import os
import hashlib
import urllib.request
import urllib.parse
import json
from pathlib import Path

# 配置
OUTPUT_DIR = Path(__file__).parent
IMAGES_DIR = OUTPUT_DIR / "images"
IMAGES_DIR.mkdir(exist_ok=True)

# 图片 URL 模板
BASE_URL = "https://image.secopuzzle.com/SECO2/%E9%9B%AA%E5%B4%A9/%E9%9B%AA%E5%B4%A9/"
TOTAL_SNOWFLAKES = 66

# MD5 缓存文件
CACHE_FILE = OUTPUT_DIR / "image_cache.json"


def load_cache():
    """加载已有的 MD5 缓存"""
    if CACHE_FILE.exists():
        with open(CACHE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_cache(cache):
    """保存 MD5 缓存"""
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def compute_md5(file_path):
    """计算文件的 MD5 值"""
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def download_image(url, original_index):
    """下载图片并返回 MD5 重命名后的文件名"""
    # 从 URL 中提取文件名
    parsed_url = urllib.parse.urlparse(url)
    original_filename = os.path.basename(parsed_url.path)
    
    # 本地临时文件名（使用原始编号）
    temp_filename = f"{original_index:02d}.png"
    temp_path = IMAGES_DIR / temp_filename
    
    # 如果已经下载过，直接使用缓存
    cache = load_cache()
    if str(original_index) in cache:
        cached_md5 = cache[str(original_index)]
        cached_filename = f"{cached_md5}.png"
        if (IMAGES_DIR / cached_filename).exists():
            print(f"[OK] 使用缓存：{original_index:02d}.png -> {cached_filename}")
            return cached_filename
    
    print(f"[下载] {original_filename} ({original_index:02d})")
    
    try:
        # 添加 User-Agent 避免 403 错误
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(temp_path, 'wb') as out_file:
                out_file.write(response.read())
        
        # 计算 MD5
        md5_hash = compute_md5(temp_path)
        new_filename = f"{md5_hash}.png"
        new_path = IMAGES_DIR / new_filename
        
        # 重命名为 MD5
        if temp_path != new_path:
            if new_path.exists():
                # 如果 MD5 相同的文件已存在，删除刚下载的文件
                os.remove(temp_path)
                print(f"[OK] 重复文件：{original_index:02d}.png -> {new_filename}")
            else:
                os.rename(temp_path, new_path)
                print(f"[OK] 下载完成：{original_index:02d}.png -> {new_filename}")
        else:
            print(f"[OK] 下载完成：{new_filename}")
        
        # 更新缓存
        cache[str(original_index)] = md5_hash
        save_cache(cache)
        
        return new_filename
        
    except Exception as e:
        print(f"[FAIL] 下载失败 {original_index:02d}: {e}")
        if temp_path.exists():
            os.remove(temp_path)
        return None


def generate_offline_html(image_mapping):
    """生成离线版本的 HTML 文件"""
    # 读取原始 HTML 模板
    template_path = Path(__file__).parent.parent / "puzzles" / "templates" / "puzzle_bodies" / "snowfall.html"
    
    with open(template_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 生成新的图片 URL 数组（使用本地相对路径）
    local_image_urls = []
    for i in range(1, TOTAL_SNOWFLAKES + 1):
        if str(i) in image_mapping and image_mapping[str(i)]:
            local_image_urls.append(f"images/{image_mapping[str(i)]}")
        else:
            # 如果下载失败，使用占位符或跳过
            print(f"警告：图片 {i:02d} 下载失败，将使用空 URL")
            local_image_urls.append("")
    
    # 构建新的 JavaScript 代码
    new_image_array_js = "const imageUrls = " + json.dumps(local_image_urls, ensure_ascii=False) + ";"
    
    # 替换原 HTML 中的 imageUrls 定义
    old_pattern = "const imageUrls = Array.from({length: config.totalSnowflakes}, (_, i) => {"
    old_pattern += "            const index = String(i + 1).padStart(2, '0');"
    old_pattern += "            return `https://image.secopuzzle.com/SECO2/%E9%9B%AA%E5%B4%A9/%E9%9B%AA%E5%B4%A9/${index}.png`;"
    old_pattern += "        });"
    
    # 读取原文件找到确切的代码块
    lines = content.split('\n')
    new_lines = []
    skip_until_semicolon = False
    
    for i, line in enumerate(lines):
        if 'const imageUrls = Array.from({length: config.totalSnowflakes}' in line:
            skip_until_semicolon = True
            new_lines.append("        " + new_image_array_js)
            continue
        
        if skip_until_semicolon:
            if line.strip().endswith('});'):
                skip_until_semicolon = False
            continue
        
        new_lines.append(line)
    
    # 移除 Django 模板标签，生成独立 HTML
    offline_content = '\n'.join(new_lines)
    
    # 移除模板继承和 block 标签
    offline_content = offline_content.replace('{% extends "puzzle.html" %}', '')
    offline_content = offline_content.replace('{% block puzzle-body-html %}', '')
    offline_content = offline_content.replace('{% endblock %}', '')
    
    # 添加完整的 HTML 结构
    full_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>雪崩 - 离线版</title>
""" + offline_content + """
</html>
"""
    
    # 写入文件
    output_file = OUTPUT_DIR / "index.html"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"\n[OK] 离线 HTML 文件已生成：{output_file}")


def main():
    print("=" * 50)
    print("Snowfall 离线版生成器")
    print("=" * 50)
    
    # 下载所有图片
    image_mapping = {}
    successful_count = 0
    
    for i in range(1, TOTAL_SNOWFLAKES + 1):
        url = f"{BASE_URL}{i:02d}.png"
        filename = download_image(url, i)
        image_mapping[str(i)] = filename
        if filename:
            successful_count += 1
    
    print("\n" + "=" * 50)
    print(f"下载完成：{successful_count}/{TOTAL_SNOWFLAKES} 张图片")
    print("=" * 50)
    
    # 生成离线 HTML
    generate_offline_html(image_mapping)

    print("\n所有文件已保存到:", OUTPUT_DIR)
    print("打开 index.html 即可离线运行")


if __name__ == "__main__":
    main()
