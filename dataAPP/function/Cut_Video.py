import os, cv2

from common.File_process import make_dir
from common.zip import unzip_file, zip_files
import time, shutil
from flask import send_file
from concurrent.futures import ThreadPoolExecutor, as_completed
import ffmpeg


def extract_frame(video_path, output_folder, fps, img_ext):

    # ffmpeg.input(video_path).output(video_path, vcodec='libx264', overwrite_output=True).run() # 转换格式

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        infotxt = os.path.join(output_folder, "wrong_videos.txt")
        with open(infotxt, "w", encoding='utf-8') as t:
            t.write("该视频无法打开")
        return False

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    video_fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval = fps * video_fps
    frame_positions = range(0, total_frames, interval)
    for pos in frame_positions:
        cap.set(cv2.CAP_PROP_POS_FRAMES, pos) # 定位到要抽取的帧
        ret, frame = cap.read()
        if not ret:
            break
        frame_name = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(video_path))[0]}_{pos}{img_ext}")
        print(frame_name)
        cv2.imencode(img_ext, frame)[1].tofile(frame_name)
    cap.release()
    return True


def video_cut(input, fps:int, img_ext:str): # fps--每隔fps秒取一帧
    filename = os.path.split(input)[-1]
    print(filename)
    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    video_list = os.listdir(extract_file_path) # 获取视频文件列表

    video_dict = {}
    futures = []
    with ThreadPoolExecutor() as pool:
        for v in video_list:
            v_name, e = os.path.splitext(v)
            v_img_path = os.path.join(extract_file_path, v_name)
            make_dir(v_img_path) # 为每个视频创建抽帧文件夹
            video_dict[v_name] = video_dict.get(v_name, v_img_path)
            # 抽帧
            video_path = os.path.join(extract_file_path, v)
            futures.append(pool.submit(extract_frame,video_path, v_img_path, fps, img_ext))
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error processing video: {e}")

    # 打包文件
    video2img_list = list(video_dict.values()) # 每个视频文件夹
    # print(video2img_list)
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



