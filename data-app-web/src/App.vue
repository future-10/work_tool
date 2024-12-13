<template>
  <div class="image-with-title">
    <img alt="Vue logo" src="./assets/logo.png" width="100px" height="auto" class="image">
    <div class="title">处理工具平台</div>
  </div>
    

  <HelloWorld msg="Welcome to Your Vue.js App"/>
  <div id="app">
    <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />
    <split_data :someProp="splitdatavalue" :split-ratio="splitRatio" @custom-event="handleSplitdataEvent" />
    <cut_video :someProp="cutvideovalue" :fps="fps" :file-ext="fileExt" @custom-event="handleCutvideoEvent" />
  </div>
</template>

<script>
import check_file from './components/check_file.vue';
import split_data from './components/split_data.vue';
import cut_video from './components/cut_video.vue';


export default {
  name: 'App',
  components: {
    check_file,
    split_data,
    cut_video
  },
  data(){
    return {
      checkfilevalue: "someValue",
      splitdatavalue: "someValue",
      splitRatio: 0.2,
      cutvideovalue: "someValue", 
      fps: 1, 
      fileExt: "someValue"
    };
  },
  methods: {
    handleCheckfileEvent(data) {
      console.log('Custom event triggered with:', data);
    },
    handleSplitdataEvent(data){
      console.log('Custom event triggered with:', data);
    }, 
    handleCutvideoEvent(data) {
      console.log('Custom event triggered with:', data);
    }
  }
}
</script>

<style src="./assets/style/app.css"></style>
