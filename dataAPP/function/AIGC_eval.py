from lavis.models import load_model_and_preprocess
import torch
from PIL import Image
from transformers import BertTokenizer
from common.File_process import make_dir
from flask import send_file
import os, shutil
from common.zip import unzip_file
import time


def eval_aigc(input):
    # 初始化模型和分词器，确保只加载一次
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    bert_path = "/ihoment/wuyingdong/work_tool/dataAPP/bert"
    model_path = "/ihoment/wuyingdong/work_tool/dataAPP/model/fga_blip2.pth"

    # 加载BERT分词器
    tokenizer = BertTokenizer.from_pretrained(bert_path, truncation_side='right')
    tokenizer.add_special_tokens({"bos_token": "[DEC]"})

    # 加载模型和预处理器
    model, vis_processors, text_processors = load_model_and_preprocess("fga_blip2", "coco", device=device, is_eval=True)
    model.load_checkpoint(model_path)
    # 文件处理
    filename = os.path.split(input)[-1]
    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    timestamp = int(round(time.time() * 1000))
    result_txt = os.path.join(extract_file_dir, f"result_aigc_{timestamp}.txt")
    _, name = os.path.split(result_txt)

    # 初始化结果文件
    with open(result_txt, "w") as t:
        t.write("keyword\tfile_name\tscore\n")

        for root, dirs, files in os.walk(extract_file_path):
            for file in files:
                if os.path.splitext(file)[1].lower() in ['.jpg', '.png']:
                    file_path = os.path.join(root, file)
                    prompt = os.path.split(os.path.split(file_path)[0])[-1]  # 获取提示词
                    prompt = prompt.replace('_', ' ')  # 短语提示词处理
                    img = Image.open(file_path).convert('RGB')
                    img = vis_processors["eval"](img).unsqueeze(0).to(device)
                    txt = text_processors["eval"](prompt)
                    itm_scores = model({"image": img, "text_input": txt}, match_head="itm", inference=True)
                    overall_score = itm_scores.item()
                    t.write(f"{prompt}\t{file_path}\t{overall_score}\n")

                    # 清理资源
                    del img, txt, itm_scores
                    if device != 'cpu':
                        torch.cuda.empty_cache()

    # 删除临时文件
    shutil.rmtree(extract_file_path, ignore_errors=True)
    os.remove(input)

    response = send_file(
        result_txt,
        mimetype='text/plain',
        as_attachment=True,
        download_name=name
    )

    return response, 200



