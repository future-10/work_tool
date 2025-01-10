from lavis.models import load_model_and_preprocess
import torch
from PIL import Image
from transformers import BertTokenizer
from common.File_process import make_dir
from flask import send_file
import os, shutil
from common.zip import unzip_file
import time

def text2img_score(prompt, img_path):
    device = torch.device("cuda") if torch.cuda.is_available() else "cpu"
    bert_path = "/ihoment/wuyingdong/work_tool/dataAPP/bert"
    tokenizer = BertTokenizer.from_pretrained(bert_path, truncation_side='right')
    tokenizer.add_special_tokens({"bos_token": "[DEC]"})
    model_path = "/ihoment/wuyingdong/work_tool/dataAPP/model/fga_blip2.pth"

    model, vis_processors, text_processors = load_model_and_preprocess("fga_blip2", "coco", device=device, is_eval=True)
    model.load_checkpoint(model_path)
    img = Image.open(img_path).convert('RGB')
    img = vis_processors["eval"](img).unsqueeze(0).to(device)
    txt = text_processors["eval"](prompt)

    itm_scores = model({"image": img, "text_input": txt}, match_head="itm", inference=True)
    # itm_scores = torch.nn.functional.softmax(itm_output, dim=1) * 4 + 1
    overall_score = itm_scores.item()
    return overall_score

def eval_aigc(input):
    filename = os.path.split(input)[-1]
    # print(filename)
    extract_file_dir = os.path.dirname(input)
    make_dir(extract_file_dir)

    unzip_file(input, extract_file_dir)
    extract_file_path = os.path.join(extract_file_dir, os.path.splitext(filename)[0])
    t = time.time()
    t = int(round(t * 1000))
    result = os.path.join(extract_file_dir, f"result_aigc_{t}.txt")
    _, name = os.path.split(result)
    with open(result, "a") as t:
        t.write("keyword\tfile_name\tscore\n")
        for root, dirs, files in os.walk(extract_file_path):
            for file in files:
                if os.path.splitext(file)[1] in ['.jpg', '.png']:
                    file_path = os.path.join(root, file)
                    prompt = os.path.split(os.path.split(file_path)[0])[-1] #获取提示词
                    prompt = prompt.replace('_', ' ') # 短语提示词处理
                    overall_score = text2img_score(prompt, file_path)
                    t.write(f"{prompt}\t{file}\t{overall_score}\n")

    # 删除临时文件
    shutil.rmtree(extract_file_path)
    os.remove(input)

    response = send_file(
        result,
        mimetype='text/plain',
        as_attachment=True,
        download_name=name
    )

    return response, 200



