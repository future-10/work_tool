import os, shutil
from PIL import Image
from flask import send_file
from common.zip import unzip_file, zip_file
from common.File_process import make_dir
import time


def check_image(input):

    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    # print(input, extract_file_path)
    wrong_imgs = []
    pass_imgs = []
    # 损坏判断
    for img in os.listdir(extract_file_path):
        img_path = os.path.join(extract_file_path, img)
        try:
            with Image.open(img_path) as image:
                pass_imgs.append(img_path)
        except:
            wrong_imgs.append(img)
    # print(pass_imgs, wrong_imgs)
    if wrong_imgs:
        infotxt = os.path.join(extract_file_path, "wrong_images.txt")
        with open(infotxt, "a", encoding='utf-8') as t:
            t.write("以下文件无法识别为有效图像:\n")
            for wi in wrong_imgs:
                t.write(wi+'\n')
        pass_imgs.append(infotxt)
    result = zip_file(pass_imgs) # 文件打包
    #清理临时文件
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
    return response, 200


