import os
import json
import sys

def decode_json_file(file_path):
    """读取 JSON 文件，解码 Unicode，并写回（格式化、可读）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            # ensure_ascii=False 不是这里用的，这里是反向：把 \uXXXX 变成真实字符
            data = json.load(f)  # 自动解码 Unicode 转义序列

        # 写回时确保不使用 ASCII 转义（即保留中文等字符）
        with open(file_path, 'w', encoding=' utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ 已处理: {file_path}")
    except Exception as e:
        print(f"❌ 处理失败 {file_path}: {e}")

def main(root_dir):
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.lower().endswith('.json'):
                file_path = os.path.join(dirpath, filename)
                decode_json_file(file_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python decode_json_unicode.py <目标目录>")
        sys.exit(1)
    target_dir = sys.argv[1]
    if not os.path.isdir(target_dir):
        print("错误: 指定的路径不是有效目录")
        sys.exit(1)
    main(target_dir)