<template>
  <div class="container">
    <h2>图片损坏检测</h2>
    <p style="color:#2981e6;font-size:15px;font-weight:bold;margin:10px;">功能: 筛选损坏的图片文件, 返回正常图片文件</p>
    <p style="color:#2981e6;font-size:15px;font-weight:bold;margin:10px;">使用说明: 上传含图片的zip格式压缩包文件, 压缩包内应包含一个文件夹, 上传成功点击提交即可</p>
    <form @submit.prevent="uploadFile">
      <input type="file" ref="fileInput" accept=".zip,.rar,.7z"  class="file-input" required />
      <button type="submit" class="submit-button">提交</button>
    </form>
    <p v-if="message">{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';
//import FileSaver from 'file-saver';
import { saveAs } from 'file-saver'; //保存文件的库

export default {
  data() {
    return {
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
      
      try {
        // Show loading or processing message
        this.message = '正在处理文件...';

        const response = await axios.post('/api/check_img', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          },
          responseType: 'blob'  // 确保响应内容作为二进制数据处理
        });
        const fileName = response.headers['content-disposition'].substring(response.headers['content-disposition'].indexOf('=') + 1)
        // 使用 FileSaver.js 直接保存文件
        saveAs(response.data,fileName);
        
        // 显示下载成功的消息
        this.message = '文件处理完成.';

        // 清空文件输入框以便下次上传
        fileInput.value = '';
      } catch (error) {
        console.error('Error during file upload:', error);
        if (error.response && error.response.data) {
          this.message = error.response.data.error || 'An error occurred.';
        } else {
          this.message = '处理文件时发生错误';
        }
      }
    }
  }
};
</script>

<style scoped>
/* Add your styles here */
</style>