import shutil

from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from common.File_process import make_dir
from function.Check_Image import check_image
from function.Split_Data import data_split

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})

uploader_path = 'data' # 上传文件的存储路径
make_dir(uploader_path)
if os.listdir(uploader_path):
    print("data中含文件")
    for up in os.scandir(uploader_path):
        up_path = os.path.join(uploader_path, up.name)
        if up.is_dir():
            shutil.rmtree(up_path)
        if up.is_file():
            os.remove(up_path)

# 图片损坏检测
@app.route("/check_img", methods=['POST'])
def check_img():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file'] # 获取文件

    if file.filename == '':
        return jsonify({'error': 'file not found'}), 400

    file_path = os.path.join(uploader_path, file.filename)
    file.save(file_path)
    # 调用图像检查函数
    response, status_code = check_image(file_path)
    # print('---------------------')
    return response

# 数据切分
@app.route("/split_data", methods=['POST'])
def split_data():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': 'file not found'}), 400

    file_path = os.path.join(uploader_path, file.filename)
    file.save(file_path)
    thresh = eval(request.form.get('splitRatio')) # 获取切分比例
    # print(type(thresh), thresh)
    # 调用数据划分函数
    response, status_code = data_split(file_path, thresh)
    return response

# 视频抽帧
@app.route("/cut_video", methods=['POST'])
def cut_video():
    pass


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000, debug=True)


