import os, shutil
from PIL import Image
from flask import send_file, jsonify
from common.zip import unzip_file, zip_file
from common.File_process import make_dir
import time
from concurrent.futures import ThreadPoolExecutor

def img_convert(image_path, format):
    try:
        savepath = os.path.dirname(image_path)
        savename, ext = os.path.splitext(os.path.basename(image_path))
        if ext == format:
            return image_path, None
        with Image.open(image_path) as image:
            save_path  = os.path.join(savepath, savename+format)
            image.save(save_path)
        return save_path, None
    except:
        return None, image_path

def image_convert(input, format):
    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    if not os.path.exists(extract_file_path): # 确保解压后的路径存在
        return jsonify({'error':'压缩包内文件夹名与压缩包名不同'}), 400
    all_images = [os.path.join(extract_file_path, img) for img in os.listdir(extract_file_path)]
    need_images = []
    wrong_images  = []
    formats = [format] * len(all_images) # 将格式作为列表传递给pool.map，对应每个图像转换的格式
    with ThreadPoolExecutor() as pool:
        results = pool.map(img_convert, all_images, formats)
        for result in results:
            if result[0] is not None:
                need_images.append(result[0])
            else:
                wrong_images.append(os.path.basename(result[1]))
    t = time.time()
    t = int(round(t * 1000))
    if wrong_images:
        infotxt = os.path.join(extract_file_path, f"wrong_images_{t}.txt")
        with open(infotxt, "a", encoding='utf-8') as t:
            t.write("以下图片文件无法打开:\n")
            for wi in wrong_images:
                t.write(wi + '\n')
            t.write("建议使用图片损坏检测工具进行处理！")
        need_images.append(infotxt)

    result = zip_file(need_images)  # 文件打包
    # 清理临时文件
    t_name = time.time()
    t_name = int(round(t_name * 1000))
    shutil.rmtree(extract_file_path)
    os.remove(input)
    response = send_file(
        result,
        mimetype='application/zip',
        as_attachment=True,
        download_name=f'{t_name}.zip'

    )
    return response, 200


