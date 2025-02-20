import os
import shutil
from flask import send_file, jsonify
from common.File_process import make_dir, calculate_phash # 导入哈希计算函数
from common.zip import unzip_file, zip_file
import time

# 相似度对比函数
def is_similar(hash1, hash2, thresh):
    diff = hash1 - hash2
    return diff<=thresh

def data_dedup(input, thresh):
    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    if not os.path.exists(extract_file_path): # 确保解压后的路径存在
        return jsonify({'error':'压缩包内文件夹名与压缩包名不同'}), 400
    file_list = os.listdir(extract_file_path)
    hash_dict = {}

    for file in file_list:
        file_path = os.path.join(extract_file_path, file)
        if os.path.splitext(file)[-1].lower() not in ['.jpg', '.png', '.jpeg', '.bmp']:
            return jsonify({'error':'文件中含有不支持的格式的图片'}), 400
        # print(file_path)
        phash = calculate_phash(file_path)
        if phash is not None:
            if any(is_similar(phash, h, thresh) for h in hash_dict.values()):
                os.remove(file_path) # 删除重复度高的图片
            else:
                hash_dict[file] = phash

    set_files = [os.path.join(extract_file_path,fp) for fp in os.listdir(extract_file_path)]# 去重后的图片列表

    result = zip_file(set_files)
    t = time.time()
    t = int(round(t * 1000))
    shutil.rmtree(extract_file_path)
    os.remove(input)
    response = send_file(
        result,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{t}.zip'
    )
    # response.headers['Content-Disposition'] = f'attachment; filename="{t}.zip"'
    return response, 200



