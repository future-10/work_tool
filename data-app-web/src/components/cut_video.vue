<template>
    <div class="container">
      <h2>视频抽帧</h2>
      <p style="color:#2981e6;font-size:15px;font-weight:bold;margin:10px;">功能: 将视频转为图片</p>
      <p style="color:#2981e6;font-size:15px;font-weight:bold;margin:10px;">使用说明: 上传含文件的zip格式压缩包文件, 压缩包内应包含一个视频文件夹, 上传成功后选择帧率和图片格式, 点击提交即可</p>
      <form @submit.prevent="uploadFile">
        <input type="file" ref="fileInput" accept=".zip,.rar,.7z"  class="file-input" required />
        <label for="fps" style="font-size: 13px;">输入抽帧帧率(即几秒一帧):</label>
        <input type="number" id="fps" v-model="fps" class="form-control" style="margin-right: 20px;width: 50px;">
        <label for="fileExt" style="font-size: 13px;">选择保存图片格式:</label>
        <select name="fileExt" id="fileExt" v-model="fileExt" style="margin-right: 20px;">
            <option value=".jpg">.jpg</option>
            <option value=".png">.png</option>
        </select>

        <button type="submit" class="submit-button">提交</button>
      </form>
      <p v-if="message">{{ message }}</p>
    </div>
  </template>

<script>
import axios from 'axios';
import { saveAs } from 'file-saver'; //保存文件的库

export default {
  data() {
    return {
      fps: 1, //默认抽帧帧率为1
      fileExt: '.jpg',
      message: '' // 用于存储并显示给用户的消息
    };
  },
  methods: {
    async uploadFile() {
      const fileInput = this.$refs.fileInput;
      const file = fileInput.files[0];

      if (!file) {
        this.message = 'Please select a file.';
        return;
      }

      const formData = new FormData();
      formData.append('file', file);
      formData.append('fps', this.fps)
      formData.append('fileExt', this.fileExt)

      try {
        // Show loading or processing message
        this.message = '正在处理文件...';

        const response = await axios.post('/api/cut_video', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          responseType: 'blob'  // 确保响应内容作为二进制数据处理
        });

        // 使用 FileSaver.js 直接保存文件
        saveAs(response.data, 'result.zip');

        // 显示下载成功的消息
        this.message = '文件处理完成.';

        // 清空文件输入框以便下次上传
        fileInput.value = '';
      } catch (error) {
        console.error('Error during file upload:', error);
        if (error.response && error.response.data) {
          this.message = error.response.data.error || '一个错误产生.';
        } else {
          this.message = '处理文件时发生错误';
        }
      }
    }
  }
};
</script>