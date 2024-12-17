import os
from PIL import Image
import imagehash

def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

# 计算图片哈希值
def calculate_phash(image_path):
    try:
        with Image.open(image_path) as img:
            return imagehash.phash(img)
    except Exception as e:
        return None