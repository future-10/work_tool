import os, shutil
from flask import send_file, jsonify
from common.zip import unzip_file, zip_file
import json, time
from common.File_process import make_dir

def json_format(input):
    filename = os.path.split(input)[-1]

    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    if not os.path.exists(extract_file_path): # 确保解压后的路径存在
        return jsonify({'error':'压缩包内文件夹名与压缩包名不同'}), 400

    json_file_path = []
    non_json = []
    jsonfiles = os.listdir(extract_file_path)
    for jsonfile in jsonfiles:
        if os.path.splitext(jsonfile)[1] == '.json':
            json_path = os.path.join(extract_file_path, jsonfile)
            with open(json_path, 'r', encoding='utf-8') as j:
                data = json.load(j)
            output_file = json_path
            with open(output_file, 'w', encoding='utf-8') as jo:
                json.dump(data, jo, ensure_ascii=False, indent=4)
            json_file_path.append(output_file)
        else:
            non_json.append(jsonfile)

    if non_json:
        non_jsonfile = os.path.join(extract_file_path, "non_json.txt")
        with open(non_jsonfile, 'a', encoding='utf-8') as t:
            t.write("以下文件不属于json文件:\n")
            for nj in non_json:
                t.write(nj+'\n')
        json_file_path.append(non_jsonfile)

    result = zip_file(json_file_path)
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