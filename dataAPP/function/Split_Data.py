import os, shutil
from flask import send_file
from common.File_process import make_dir
from common.zip import unzip_file, zip_files
from random import shuffle
import time

def data_split(input, thresh): # 此处thresh是测试集的占比
    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0]) # 解压后的文件夹路径
    print(extract_file_path)
    train_data_path = os.path.join(extract_file_path, "train")
    test_data_path = os.path.join(extract_file_path, "test")

    file_list = os.listdir(extract_file_path)
    shuffle(file_list) # 打乱文件顺序
    make_dir(train_data_path)
    make_dir(test_data_path)
    # print(train_data_path, test_data_path)
    test_num = int(len(file_list)*thresh)
    test_file_list = file_list[:test_num]
    for file in file_list:
        file_path = os.path.join(extract_file_path, file)
        # print(file_path)
        if file in test_file_list:
            shutil.move(file_path, test_data_path)
        else:
            shutil.move(file_path, train_data_path)
    t = time.time()
    t = int(round(t * 1000))
    out_dir = os.path.join(extract_file_dir, f"{t}.zip")
    result = zip_files([train_data_path, test_data_path], out_dir)
    shutil.rmtree(extract_file_path)
    os.remove(input)

    response = send_file(
        result,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{t}.zip'
    )
    return response, 200

