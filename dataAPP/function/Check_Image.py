import os, shutil
from PIL import Image
from flask import send_file
from common.zip import unzip_file, zip_file
from common.File_process import make_dir
import time
from concurrent.futures import ThreadPoolExecutor


def process_image(img_path):
    try:
        with Image.open(img_path) as image:
            image.load() # 验证图片能否加载
        return img_path, None  # 成功返回图像路径和None错误
    except Exception as e:
        return None, img_path  # 失败返回None和图像名称

def check_image(input):

    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])

    all_images = [os.path.join(extract_file_path, img) for img in os.listdir(extract_file_path)]

    wrong_imgs = []
    pass_imgs = []
    Image.MAX_IMAGE_PIXELS = 16777216 # 设置图片最大像素值-4096*4096
    # 损坏判断
    with ThreadPoolExecutor() as pool:
        results = pool.map(process_image, all_images)

    # print(results)
        for result in results:
            if result[0]:  # 如果第一个元素不是None，则表示成功
                pass_imgs.append(result[0])
            else:  # 否则添加到失败列表中
                wrong_imgs.append(os.path.basename(result[1]))

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


