<template>
 <div class="fa">
    <div class="outside">
    <div class="son">
        <table align="center">
            <tr>
                <th>
                    <div class="image-with-title">
                        <img alt="Vue logo" src="./assets/logo.png" width="100px" height="auto" class="image">
                    </div>
                </th>
            </tr>
            <tr>
                <th>
                    <h1>处理工具平台</h1>
                </th>
            </tr>
        </table>
        
            
        <HelloWorld msg="Welcome to Your Vue.js App"/>
        <table align="center"  width="600px" cellpadding="8">
            <tr align="center" width="300px">
                <th >
                    <div class="dropdown">
                        <button class="dropbtn">数据处理工具</button>
                        <div class="dropdown-content">

                            <!-- 功能1.1：图片损坏检测 -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box11" @click="box11 = false"></div>      <!--修改对应的模组尾数box_,必须相同-->
                                    <div class="pop" v-if="box11">
                                        <button @click="box11 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box11 = true" class="btn">图片损坏检测</button> <!--功能标签按钮-->
                                </div>
                            </a>

                            <!-- 功能1.2：数据切分 -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box12" @click="box12 = false"></div>
                                    <div class="pop" v-if="box12">
                                        <button @click="box12 = false" class="btn">关闭</button>
                                        <split_data :someProp="splitdatavalue" :split-ratio="splitRatio" @custom-event="handleSplitdataEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box12 = true" class="btn">数据切分工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                            <!-- 功能1.3：视频抽帧 -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box13" @click="box13 = false"></div>
                                    <div class="pop" v-if="box13">
                                        <button @click="box13 = false" class="btn">关闭</button>
                                        <cut_video :someProp="cutvideovalue" @custom-event="handleCutvideoEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box13 = true" class="btn">视频抽帧工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                        </div>
                    </div>
                </th>
                <th width="2px">
                    <!--空-->
                </th>
                <th>
                    <div class="dropdown">
                        <button class="dropbtn">算法处理工具</button>
                        <div class="dropdown-content">
                            
                            <!-- 功能2.1：xxx -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box21" @click="box21 = false"></div>
                                    <div class="pop" v-if="box21">
                                        <button @click="box21 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box21 = true" class="btn">待添加工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                            <!-- 功能2.2：xxx -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box22" @click="box22 = false"></div>
                                    <div class="pop" v-if="box22">
                                        <button @click="box22 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box22 = true" class="btn">待添加工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                            <!-- 功能2.3：xxx -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box23" @click="box23 = false"></div>
                                    <div class="pop" v-if="box23">
                                        <button @click="box23 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box23 = true" class="btn">待添加工具</button> <!--功能标签按钮-->
                                </div>
                            </a>
                            
                        </div>
                    </div>
                </th>
                <th width="2px">
                    <!--空-->
                </th>
                <th>
                    <div class="dropdown">
                        <button class="dropbtn">其他处理工具</button>
                        <div class="dropdown-content">
                           
                             <!-- 功能3.1：xxx -->
                             <a>
                                <div>
                                    <div class="mask" v-if="box31" @click="box31 = false"></div>
                                    <div class="pop" v-if="box31">
                                        <button @click="box31 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box31 = true" class="btn">待添加工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                            <!-- 功能3.2：xxx -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box32" @click="box32 = false"></div>
                                    <div class="pop" v-if="box32">
                                        <button @click="box32 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box32 = true" class="btn">待添加工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                            <!-- 功能3.3：xxx -->
                            <a>
                                <div>
                                    <div class="mask" v-if="box33" @click="box33 = false"></div>
                                    <div class="pop" v-if="box33">
                                        <button @click="box33 = false" class="btn">关闭</button>
                                        <check_file :someProp="checkfilevalue" @custom-event="handleCheckfileEvent" />  <!--功能链接-->
                                    </div>
                                    <button @click="box33 = true" class="btn">待添加工具</button> <!--功能标签按钮-->
                                </div>
                            </a>

                        </div>
                    </div>
                </th>
            </tr>
        </table>
        </div>
        </div>
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
      //output: 'box11',
      splitdatavalue: "someValue",
      splitRatio: 0.2,
      cutvideovalue: "someValue",
      fps: 1,
      fileExt: "someValue",
      box11: false,     /*功能模组匹配按钮*/
      box12: false,
      box13: false,
      box21: false,
      box22: false,
      box23: false,
      box31: false,
      box32: false,
      box33: false,
      
    };
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
    }
  }
}
</script>

<style src="./assets/style/app.css"></style>
