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
        <div  ref="term1" @click.stop="isshow1 = !isshow1">
                        <div><button class="dropbtn">数据处理工具</button></div>
                    </div>
                    <div v-show="isshow1"  ref="drop1">

                            <!-- 功能1.1：图片损坏检测 -->
                            <li style="height: 10px;"></li>
                            <li>
                                <div>
                                    <div class="mask" v-if="box11" @click="box11 = false"></div>      <!--修改对应的模组尾数box_,必须相同-->
                                    <div class="pop" v-if="box11">
                                        <button @click="box11 = false" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box11 = true" class="btn">>>图片损坏检测<<</button> <!--功能标签按钮-->
                                </div>
                            </li>

                            <!-- 功能1.2：数据切分 -->
                            <li>
                                <div>
                                    <div class="mask" v-if="box12" @click="box12 = false"></div>
                                    <div class="pop" v-if="box12">
                                        <button @click="box12 = false" class="close-btn">&times;</button>
                                        <split_data :someProp="splitdatavalue" :split-ratio="splitRatio" @custom-event="handleSplitdataEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box12 = true" class="btn">>>数据切分工具<<</button> <!--功能标签按钮-->
                                </div>
                            </li>

                            <!-- 功能1.3：视频抽帧 -->
                            <li>
                                <div>
                                    <div class="mask" v-if="box13" @click="box13 = false"></div>
                                    <div class="pop" v-if="box13">
                                        <button @click="box13 = false" class="close-btn">&times;</button>
                                        <cut_video :someProp="cutvideovalue" @custom-event="handleCutvideoEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box13 = true" class="btn">>>视频抽帧工具<<</button> <!--功能标签按钮-->
                                </div>
                            </li>

                             <!-- 功能1.4：图片去重 -->
                             <li>
                                <div>
                                    <div class="mask" v-if="box14" @click="box14 = false"></div>
                                    <div class="pop" v-if="box14">
                                        <button @click="box14 = false" class="close-btn">&times;</button>
                                        <dedup_data :someProp="dedupdatavalue" @custom-event="handleDedupdataEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box14 = true" class="btn">>>图片去重工具<<</button> <!--功能标签按钮-->
                                </div>
                            </li>

                    </div>
                    </div>

                    <div class="btn-div">
                    <div ref="term2" @click.stop="isshow2 = !isshow2">
                        <button class="dropbtn">算法处理工具</button>
                    </div>
                        <div v-show="isshow2"  ref="drop2">
                            
                            <!-- 功能2.1：xxx -->
                            <li style="height: 10px;"></li>
                            <li>
                                <div>
                                    <div class="mask" v-if="box21" @click="box21 = false"></div>
                                    <div class="pop" v-if="box21">
                                        <button @click="box21 = false" class="close-btn">&times;</button>
                                        <dedup_data :someProp="dedupdatavalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box21 = true" class="btn">xxx</button> <!--功能标签按钮-->
                                </div>
                            </li>

                            <!-- 功能2.2：xxx -->
                            <li>
                                <div>
                                    <div class="mask" v-if="box22" @click="box22 = false"></div>
                                    <div class="pop" v-if="box22">
                                        <button @click="box22 = false" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box22 = true" class="btn">xxx</button> <!--功能标签按钮-->
                                </div>
                            </li>

                            <!-- 功能2.3：xxx -->
                            <li>
                                <div>
                                    <div class="mask" v-if="box23" @click="box23 = false"></div>
                                    <div class="pop" v-if="box23">
                                        <button @click="box23 = false" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box23 = true" class="btn">xxx</button> <!--功能标签按钮-->
                                </div>
                            </li>
                            
                        </div>
                        </div>

                        
                        <div class="btn-div">
                        <div ref="term3" @click.stop="isshow3 = !isshow3">
                        <button class="dropbtn">其他处理工具</button>
                        </div>
                        <div v-show="isshow3"  ref="drop3">
                           
                             <!-- 功能3.1：xxx -->
                             <li style="height: 10px;"></li>
                             <li>
                                <div>
                                    <div class="mask" v-if="box31" @click="box31 = false"></div>
                                    <div class="pop" v-if="box31">
                                        <button @click="box31 = false" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box31 = true" class="btn">xxx</button> <!--功能标签按钮-->
                                </div>
                            </li>

                            <!-- 功能3.2：xxx -->
                            <li>
                                <div>
                                    <div class="mask" v-if="box32" @click="box32 = false"></div>
                                    <div class="pop" v-if="box32">
                                        <button @click="box32 = false" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box32 = true" class="btn">xxx</button> <!--功能标签按钮-->
                                </div>
                            </li>

                            <!-- 功能3.3：xxx -->
                            <li>
                                <div>
                                    <div class="mask" v-if="box33" @click="box33 = false"></div>
                                    <div class="pop" v-if="box33">
                                        <button @click="box33 = false" class="close-btn">&times;</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box33 = true" class="btn">xxx</button> <!--功能标签按钮-->
                                </div>
                            </li>

                        </div>
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
      box11: false,     /*功能模组匹配按钮*/
      box12: false,
      box13: false,
      box14: false,
      box21: false,
      box22: false,
      box23: false,
      box31: false,
      box32: false,
      box33: false,
      isshow1: false, //
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
  }
}

</script>

<style src="./assets/style/app.css"></style>
