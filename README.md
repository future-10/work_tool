## 项目简介
本项目使用flask作为后端框架，Vue为前端框架
#### 安装依赖库
python=3.12  
pip install -r dataAPP/requirements.txt
#### 下载预训练模型
bert模型:https://huggingface.co/, 搜索"bert-base-uncased"  
如果是pytorch框架，下载config.json、pytorch_model_bin、tokenizer.json、tokenizer_config.json和vocab.txt这几个文件，放入一个文件夹，以便后期访问路径  
下载评估模型:
   [[Huggingface](https://huggingface.co/hanshuhao/FGA-BLIP2/resolve/main/fga_blip2.pth?download=true)]
   or [[Baidu Cloud](https://pan.baidu.com/s/1spi1E9AjQ6xNW_Wqufgm9w?pwd=tgyq)].

#### 安装Vue组件
npm install axios  

notes: 需安装vue、node.js和npm工具

### 处理工具：
1. 图片损坏检测
2. 数据划分
3. 视频抽帧
4. 图片去重
5. 文生图评分