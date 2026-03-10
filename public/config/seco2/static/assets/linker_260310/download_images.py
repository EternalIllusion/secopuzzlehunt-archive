#!/usr/bin/env python3
"""下载连线小游戏所需的所有图片"""

import os
import urllib.request

# 图片 URL 列表
IMAGES = [
    ("1.png", "https://image.secopuzzle.com/SECO2/%E8%BF%9E%E7%BA%BF%E5%B0%8F%E5%90%88%E9%9B%86/1.png"),
    ("2.png", "https://image.secopuzzle.com/SECO2/%E8%BF%9E%E7%BA%BF%E5%B0%8F%E5%90%88%E9%9B%86/2.png"),
    ("3.png", "https://image.secopuzzle.com/SECO2/%E8%BF%9E%E7%BA%BF%E5%B0%8F%E5%90%88%E9%9B%86/3.png"),
    ("4.png", "https://image.secopuzzle.com/SECO2/%E8%BF%9E%E7%BA%BF%E5%B0%8F%E5%90%88%E9%9B%86/4.png"),
    ("5.png", "https://image.secopuzzle.com/SECO2/%E8%BF%9E%E7%BA%BF%E5%B0%8F%E5%90%88%E9%9B%86/5.png"),
    ("returntonormal.png", "https://image.secopuzzle.com/SECO2/%E8%BF%9E%E7%BA%BF%E5%B0%8F%E5%90%88%E9%9B%86/returntonormal.png"),
]

DOWNLOAD_DIR = os.path.dirname(os.path.abspath(__file__))

# 添加 User-Agent 头来模拟浏览器
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Referer': 'https://image.secopuzzle.com/',
}

def download_image(filename, url):
    """下载单张图片"""
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    if os.path.exists(filepath):
        print(f"✓ 已存在：{filename}")
        return True
    
    try:
        print(f"正在下载：{filename}")
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"✓ 下载成功：{filename}")
        return True
    except Exception as e:
        print(f"✗ 下载失败 {filename}: {e}")
        return False

def main():
    print("开始下载连线小游戏图片...")
    print(f"保存目录：{DOWNLOAD_DIR}\n")
    
    success_count = 0
    for filename, url in IMAGES:
        if download_image(filename, url):
            success_count += 1
    
    print(f"\n下载完成：{success_count}/{len(IMAGES)} 张图片")
    
    if success_count == len(IMAGES):
        print("所有图片下载成功！")
    else:
        print("部分图片下载失败，请检查网络连接后重新运行脚本。")

if __name__ == "__main__":
    main()
