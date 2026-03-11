#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
麻将牌图片下载脚本
下载所有麻将牌图片到本地 images 目录
"""

import os
import urllib.request
from urllib.parse import unquote

# 麻将牌配置：34 张牌
MAJIANG_TILES = {
    # 万 (m) 1-9
    1: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/1m.png",
    2: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/2m.png",
    3: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/3m.png",
    4: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/4m.png",
    5: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/5m.png",
    6: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/6m.png",
    7: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/7m.png",
    8: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/8m.png",
    9: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/9m%E8%AF%97%E7%BB%8F.png",
    # 筒 (p) 1-9
    10: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/1p.png",
    11: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/2p.png",
    12: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/3p.png",
    13: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/4p.png",
    14: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/5p.png",
    15: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/6p.png",
    16: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/7p.png",
    17: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/8p.png",
    18: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/9p%E7%BB%84%E5%90%88.png",
    # 条 (s) 1-9
    19: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/1s.png",
    20: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/2s.png",
    21: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/3s.png",
    22: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/4s.png",
    23: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/5s.png",
    24: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/6s.png",
    25: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/7s.png",
    26: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/8s.png",
    27: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/9s%E7%9C%8B%E4%BD%8E.png",
    # 风牌
    28: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/A%E4%B8%9C.png",
    29: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/B%E5%8D%97.png",
    30: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/C%E8%A5%BF.png",
    31: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/D%E5%8C%97.png",
    # 三元牌
    32: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/%E4%B8%ADE.png",
    33: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/%E5%8F%91F.png",
    34: "https://image.secopuzzle.com/SECO2/%E6%89%93%E7%89%8C%E7%8E%8B/%E7%99%BDG.png",
}

# 图片文件名映射（使用有意义的中文名）
TILE_FILENAMES = {
    1: "1m.png",
    2: "2m.png",
    3: "3m.png",
    4: "4m.png",
    5: "5m.png",
    6: "6m.png",
    7: "7m.png",
    8: "8m.png",
    9: "9m.png",
    10: "1p.png",
    11: "2p.png",
    12: "3p.png",
    13: "4p.png",
    14: "5p.png",
    15: "6p.png",
    16: "7p.png",
    17: "8p.png",
    18: "9p.png",
    19: "1s.png",
    20: "2s.png",
    21: "3s.png",
    22: "4s.png",
    23: "5s.png",
    24: "6s.png",
    25: "7s.png",
    26: "8s.png",
    27: "9s.png",
    28: "dong.png",
    29: "nan.png",
    30: "xi.png",
    31: "bei.png",
    32: "zhong.png",
    33: "fa.png",
    34: "bai.png",
}


def download_image(url, filepath):
    """下载单张图片"""
    try:
        print(f"下载：{url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Referer': 'https://image.secopuzzle.com/'
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=30) as response:
            with open(filepath, 'wb') as out_file:
                out_file.write(response.read())
        print(f"  ✓ 成功保存到：{filepath}")
        return True
    except Exception as e:
        print(f"  ✗ 下载失败：{e}")
        return False


def main():
    # 获取脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, 'images')
    
    # 创建 images 目录
    os.makedirs(images_dir, exist_ok=True)
    print(f"图片保存目录：{images_dir}")
    print("=" * 50)
    
    success_count = 0
    fail_count = 0
    
    for tile_id, url in MAJIANG_TILES.items():
        filename = TILE_FILENAMES[tile_id]
        filepath = os.path.join(images_dir, filename)
        
        # 如果文件已存在，跳过
        if os.path.exists(filepath):
            print(f"跳过（已存在）：{filename}")
            success_count += 1
            continue
        
        if download_image(url, filepath):
            success_count += 1
        else:
            fail_count += 1
    
    print("=" * 50)
    print(f"下载完成！成功：{success_count}, 失败：{fail_count}")
    
    # 生成图片映射文件（供 HTML 使用）
    mapping_file = os.path.join(images_dir, 'mapping.json')
    import json
    mapping = {str(tile_id): TILE_FILENAMES[tile_id] for tile_id in MAJIANG_TILES}
    with open(mapping_file, 'w', encoding='utf-8') as f:
        json.dump(mapping, f, ensure_ascii=False, indent=2)
    print(f"图片映射已保存到：{mapping_file}")


if __name__ == '__main__':
    main()
