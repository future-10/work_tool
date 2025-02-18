import shutil
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os
from common.File_process import make_dir
from function.Check_Image import check_image
from function.Split_Data import data_split
from function.Cut_Video import video_cut
from function.Dedup_Data import data_dedup
from function.AIGC_eval import eval_aigc
from function.Format_Json import json_format
from function.Convert_Image import image_convert

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:8080"}})
# socketio = SocketIO(app)
if os.environ.get("FLASK_ENV") == "development":
    app.debug = True

uploader_path = 'data' # 上传文件的存储路径
make_dir(uploader_path)
# app.config['UPLOAD_PATH'] = uploader_path


# 图片损坏检测
@app.route("/check_img", methods=['POST'])
def check_img():

    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file'] # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400
    filename = secure_filename(file.filename)
    # print(filename)
    file_path = os.path.join(uploader_path, filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.stream, f)
    # file.save(file_path)
    # 调用图像检查函数
    response, status_code = check_image(file_path)

    # print('---------------------')
    return response, status_code

# 数据切分
@app.route("/split_data", methods=['POST'])
def split_data():

    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(uploader_path, filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.stream, f) # 以流式获取文件
    thresh = eval(request.form.get('splitRatio')) # 获取切分比例
    # print(type(thresh), thresh)
    # 调用数据划分函数
    response, status_code = data_split(file_path, thresh)
    return response, status_code

# 视频抽帧
@app.route("/cut_video", methods=['POST'])
def cut_video():

    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400

    filename = secure_filename(file.filename)

    file_path = os.path.join(uploader_path, filename)

    # file.save(file_path)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.stream, f)

    fps = eval(request.form.get('fps')) # 从前端获取帧率
    file_ext = request.form.get('fileExt') # 获取图片保存格式
    response, status_code = video_cut(file_path, fps, file_ext)
    return response, status_code

# 数据去重
@app.route('/dedup_data', methods=['POST'])
def dedup_data():

    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400

    filename = secure_filename(file.filename)

    file_path = os.path.join(uploader_path, filename)
    file.save(file_path)
    threshold = eval(request.form.get('simThresh')) # 获取相似度阈值
    response, status_code = data_dedup(file_path, threshold)
    return response, status_code

# 文生图匹配度评分
@app.route('/aigc_eval', methods=['POST'])
def aigc_eval():
    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400

    filename = secure_filename(file.filename)

    file_path = os.path.join(uploader_path, filename)
    file.save(file_path)
    response, status_code = eval_aigc(file_path)
    return response, status_code

# json格式化
@app.route('/format_json', methods=['POST'])
def format_json():
    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400

    filename = secure_filename(file.filename)

    file_path = os.path.join(uploader_path, filename)
    file.save(file_path)
    response, status_code = json_format(file_path)
    return response, status_code

@app.route('/convert_image', methods=['POST'])
def convert_image():
    if 'file' not in request.files:
        return jsonify({'error': '未上传文件'}), 400
    file = request.files['file']  # 获取文件

    if file.filename == '':
        return jsonify({'error': '文件未找到'}), 400

    filename = secure_filename(file.filename)

    file_path = os.path.join(uploader_path, filename)
    file.save(file_path)
    format = request.form.get('imgFormat')
    response, status_code = image_convert(file_path, format)
    return response, status_code


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
