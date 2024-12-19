import os, cv2
from common.File_process import make_dir
from common.zip import unzip_file, zip_files
import time, shutil
from flask import send_file


def video_cut(input, fps:int, img_ext:str): # fps--每隔fps秒取一帧
    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    video_list = os.listdir(extract_file_path) # 获取视频文件列表

    video_dict = {}
    for v in video_list:
        v_name, e = os.path.splitext(v)
        v_img_path = os.path.join(extract_file_path, v_name)
        make_dir(v_img_path) # 为每个视频创建抽帧文件夹
        video_dict[v_name] = video_dict.get(v_name, v_img_path)
        # 抽帧
        video_path = os.path.join(extract_file_path, v)
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            infotxt = os.path.join(v_img_path, "wrong_videos.txt")
            with open(infotxt, "w", encoding='utf-8') as t:
                t.write("该视频无法打开")
            continue

        frame_count = 0
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if cap.get(cv2.CAP_PROP_POS_FRAMES) % (fps * cap.get(cv2.CAP_PROP_FPS)) == 0:
                frame_name = os.path.join(v_img_path, f"{v_name}_{frame_count}{img_ext}")
                cv2.imencode(img_ext, frame)[1].tofile(frame_name)
                frame_count += 1

        cap.release()

    # 打包文件
    video2img_list = list(video_dict.values()) # 每个视频文件夹
    # print(video_dict)
    t = time.time()
    t = int(round(t * 1000))
    out_dir = os.path.join(extract_file_dir, f"{t}.zip")
    result = zip_files(video2img_list, out_dir)
    # 删除临时文件
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



