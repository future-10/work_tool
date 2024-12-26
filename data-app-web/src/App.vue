<!-- eslint-disable vue/no-use-v-if-with-v-for -->
<!-- eslint-disable vue/no-parsing-error -->
<template>
 <div class="fa">
    <div class="outside">
    <div class="son">
        <HelloWorld msg="Welcome to Your Vue.js App"/>
        <table align="center"  width="600px" cellpadding="8">
            <tbody>
            <tr align="center" width="400px">
                <th colspan="5">
                    <div class="image-with-title">
                        <img alt="Vue logo" src="./assets/style/govee.png" width="400px" height="auto" class="image">
                    </div>
                </th>
            </tr>
            <tr>
                <th colspan="5" >
                    <h1>处理工具平台</h1>
                </th>
            </tr>
        </tbody>
        </table>
        <div class="out-btn-div">
        <div class="btn-div">
                        <div>
                          <button class="dropbtn" ref="term1" @click.stop="isshow1 = !isshow1">数据处理工具</button>
                        </div>
                    <div v-show="isshow1"  ref="drop1">
                        
                            
                            <li style="height: 10px;"></li>

                            <!-- 功能1.1：图片损坏检测 -->
                            <li>
                                <!-- 使用v-for生成按钮 -->
                                <button class="btn" @click="openModal('modal11')">>>图片损坏检测<<</button>
                            </li>

                            <!-- 功能1.2：数据切分 -->
                            <li>
                                <button class="btn" @click="openModal('modal12')">>>数据切分工具<<</button>
                            </li>

                            <!-- 功能1.3：视频抽帧 -->
                            <li>
                                <button class="btn" @click="openModal('modal13')">>>视频抽帧工具<<</button>
                            </li>
                            
                             <!-- 功能1.4：图片去重 -->
                             <li>
                                <button class="btn" @click="openModal('modal14')">>>图片去重工具<<</button>
                            </li>

                    </div>
                    </div>

                    <div class="btn-div">
                    <div>
                        <button class="dropbtn" ref="term2" @click.stop="isshow2 = !isshow2">算法处理工具</button>
                    </div>
                        <div v-show="isshow2"  ref="drop2">
                            
                            <!-- 功能2.1：xxx -->
                            <li style="height: 10px;"></li>
                            <li>
                                <button class="btn" @click="openModal('modal21')">XXX</button>
                            </li>

                            <!-- 功能2.2：xxx -->
                            <li>
                                <button class="btn" @click="openModal('modal22')">XXX</button>
                            </li>

                            <!-- 功能2.3：xxx -->
                            <li>
                                <button class="btn" @click="openModal('modal23')">XXX</button>
                            </li>
                            
                        </div>
                    </div>

                        
                    <div class="btn-div">
                        <div>
                        <button class="dropbtn" ref="term3" @click.stop="isshow3 = !isshow3">其他处理工具</button>
                        </div>
                        <div v-show="isshow3"  ref="drop3">
                           
                             <!-- 功能3.1：xxx -->
                             <li style="height: 10px;"></li>
                             <li>
                                <button class="btn" @click="openModal('modal31')">XXX</button>
                            </li>

                            <!-- 功能3.2：xxx -->
                            <li>
                                <button class="btn" @click="openModal('modal32')">XXX</button>
                            </li>

                            <!-- 功能3.3：xxx -->
                            <li>
                                <button class="btn" @click="openModal('modal33')">XXX</button>
                            </li>

                        </div>
                    </div>
            </div>


                                <!-- 1.按钮菜单列表第一列-->

                                <!-- 功能1.1：图片损坏检测 -->
                                <div v-if="showBox11" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal11')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                               <!-- 功能1.2：数据切分 -->
                                <div v-if="showBox12" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal12')" class="close-btn">&times;</button>
                                        <split_data :someProp="splitdatavalue" :split-ratio="splitRatio" @custom-event="handleSplitdataEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                                <!-- 功能1.3：视频抽帧 -->
                                <div v-if="showBox13" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal13')" class="close-btn">&times;</button>
                                        <cut_video :someProp="cutvideovalue" @custom-event="handleCutvideoEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                                <!-- 功能1.4：图片去重 -->
                                <div v-if="showBox14" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal14')" class="close-btn">&times;</button>
                                        <dedup_data :someProp="dedupdatavalue" @custom-event="handleDedupdataEvent" />  <!--功能链接-->
                                    </div>
                                </div>



                                <!-- 2.按钮菜单列表第二列-->

                                <!-- 弹窗2.1 -->
                                <div v-if="showBox21" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal21')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>
                                <!-- 弹窗2.2 -->
                                <div v-if="showBox22" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal22')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                                <!-- 弹窗2.3 -->
                                <div v-if="showBox23" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal23')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>



                                <!-- 3.按钮菜单列表第三列-->
                                <!-- 弹窗3.1 -->
                                <div v-if="showBox31" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal31')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                                <!-- 弹窗3.2 -->
                                <div v-if="showBox32" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal32')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                                <!-- 弹窗3.3 -->
                                <div v-if="showBox33" class="modal">
                                    <div class="modal-content">
                                        <button @click="closeModal('modal33')" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                </div>

                                
        </div>
        </div>
    </div>

</template>

<script>
import check_file from './components/check_file.vue';
import split_data from './components/split_data.vue';
import cut_video from './components/cut_video.vue';
import  dedup_data from './components/dedup_data.vue';

export default {
  name: 'App',
  components: {
    check_file,
    split_data,
    cut_video,
    dedup_data
  },
  data(){
    return {
      checkfilevalue: "someValue",
      splitdatavalue: "someValue",
      splitRatio: 0.2,
      cutvideovalue: "someValue",
      fps: 1,
      fileExt: "someValue",
      dedupdatavalue:" someValue",
      simThresh: 1,
      showBox11: false,     //功能模组匹配按钮,重置
      showBox12: false,
      showBox13: false,
      showBox14: false,
      showBox21: false,
      showBox22: false,
      showBox23: false,
      showBox31: false,
      showBox32: false,
      showBox33: false,
      isshow1: false,       //下拉菜单显示控制，重置默认值
      isshow2: false,
      isshow3: false,
    };
  },
  mounted() {
    document.addEventListener("click", this.clickOut1);
    document.addEventListener("click", this.clickOut2);
    document.addEventListener("click", this.clickOut3);
  },
  methods: {
    handleCheckfileEvent(data) {
      console.log('Custom event triggered with:', data);
    },
    handleSplitdataEvent(data){
      console.log('Custom event triggered with:', data);
    },
    handleCutvideoEvent(data){
        console.log('Custom event triggered with:', data);
    },
    handleDedupdataEvent(data){
        console.log('Custom event triggered with:', data);
    },

    //当点击菜单以外的区域隐藏菜单
    //外按钮下拉菜单检测逻辑
    clickOut1(e) {
      let drop1 = this.$refs.drop1;
      let term1 = this.$refs.term1;
      if (
        drop1 &&
        !drop1.contains(e.target) &&
        term1 &&
        !term1.contains(e.target) &&
        this.isshow1
      ) {
        this.isshow1 = false;
      }
    },
    clickOut2(e) {
      let drop2 = this.$refs.drop2;
      let term2 = this.$refs.term2;
      if (
        drop2 &&
        !drop2.contains(e.target) &&
        term2 &&
        !term2.contains(e.target) &&
        this.isshow2
      ) {
        this.isshow2 = false;
      }
    },
    clickOut3(e) {
      let drop3 = this.$refs.drop3;
      let term3 = this.$refs.term3;
      if (
        drop3 &&
        !drop3.contains(e.target) &&
        term3 &&
        !term3.contains(e.target) &&
        this.isshow3
      ) {
        this.isshow3 = false;
      }
    },

    openModal(modal) {                  //所有的modal_和showBox_都必须对应一致
      if (modal === "modal11") {
        this.showBox11 = true;
      } else if (modal === "modal12") {
        this.showBox12 = true;
      }else if (modal === "modal13") {
        this.showBox13 = true;
      }else if (modal === "modal14") {
        this.showBox14 = true;
      }else if (modal === "modal21") {
        this.showBox21 = true;
      }else if (modal === "modal22") {
        this.showBox22 = true;
      }else if (modal === "modal23") {
        this.showBox23 = true;
      }else if (modal === "modal31") {
        this.showBox31 = true;
      }else if (modal === "modal32") {
        this.showBox32 = true;
      }else if (modal === "modal33") {
        this.showBox33 = true;
      }
    },
    closeModal(modal) {
        if (modal === "modal11") {
        this.showBox11 = false;
      } else if (modal === "modal12") {
        this.showBox12 = false;
      }else if (modal === "modal13") {
        this.showBox13 = false;
      }else if (modal === "modal14") {
        this.showBox14 = false;
      }else if (modal === "modal21") {
        this.showBox21 = false;
      }else if (modal === "modal22") {
        this.showBox22 = false;
      }else if (modal === "modal23") {
        this.showBox23 = false;
      }else if (modal === "modal31") {
        this.showBox31 = false;
      }else if (modal === "modal32") {
        this.showBox32 = false;
      }else if (modal === "modal33") {
        this.showBox33 = false;
      }
    },
  }
}

</script>

<style src="./assets/style/app.css"></style>
