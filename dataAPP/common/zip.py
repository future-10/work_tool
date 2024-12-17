import zipfile
from io import BytesIO
import os
from pathlib import Path

def unzip_file(zip_src, dst_dir):
    """
    解压zip文件
    :param zip_src: zip文件的全路径
    :param dst_dir: 要解压到的目的文件夹
    :return:
    """
    r = zipfile.is_zipfile(zip_src)
    if r:
        fz = zipfile.ZipFile(zip_src, "r")
        fz.extractall(dst_dir)
    else:
        return "请上传zip类型压缩文件"
# 多个文件压缩
def zip_file(input:list):
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w') as zipf:
        for path in input:
            zipf.write(path, os.path.basename(path))
    zip_buffer.seek(0)

    return zip_buffer


def zip_files(folder_paths, output):
    """
    将多个文件夹打包成一个临时压缩包。
    :param folder_paths: 要打包的文件夹路径列表
    :return: 临时压缩包的路径
    """

    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folder_paths:
            # folder_name = os.path.basename(os.path.normpath(folder))
            for root, dirs, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)

                    arcname = os.path.relpath(file_path, start=Path(folder).parent)

                    zipf.write(file_path, arcname)

    return output