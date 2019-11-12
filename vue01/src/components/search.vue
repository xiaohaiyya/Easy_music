<template>
  <div class="search">
    <div class="fnreturn_s" >
      <span class="return_left_s iconfont" @click="fnreturngo" >&#xe625;</span>
      <span class="attention_s iconfont">&#xe60f;</span>
    </div>


    <div style="margin-top: 15px;" @mouseenter="clearFlag">
      <el-input placeholder="请输入要查询的内容" v-model="input1" class="input-with-select">
        <el-select v-model="select" slot="prepend" placeholder="请选择">
          <el-option label="歌手名" value="1">歌手名</el-option>
          <el-option label="歌曲名" value="2">歌曲名</el-option>
        </el-select>
        <el-button slot="append" icon="el-icon-search" @click="InputSearch"></el-button>
      </el-input>
    </div>


    <div class="songer_list_des">
      <ul>
        <li class="singer_li" v-for="(item,index) in singerlist" :key="index" @click="goToDetails(item.singer_id)" v-show="flag1==1">
          <img :src=item.singer_pic  alt="" class="singer_img">
          <span>{{item.singer_name}}</span>
        </li>
        <span v-show="flag1==2" class="sp1">{{notfind1}}</span>
      </ul>
    </div>

    <div class="songlist_s">
      <ul class="songlistinfos">
          <li class="songlistinfo" @click="goTosong(a.song_id,asong_name,a.song_download_url,a.singer_name)" v-for="(a,j) in songlist" :key="j" v-show="flag==1">
              <div class="song">
              <p class="song_left" >{{j+1}}</p>
              <div class="song_center">
                <p class="song_center_t">{{a.song_name}}</p>
                <p class="song_center_b">{{a.singer_name}}</p>
              </div>
              <p class="song_right iconfont">&#xe613;</p>
            </div>
          </li>
          <span v-show="flag==2" class="sp1">{{notfind}}</span>
        </ul>
        
    </div>

  </div>

</template>

<script>
  import {Select, Input, Option, Button} from 'element-ui'
  export default {
      name:'search',
      data(){
          return{
            input1: '',
            select: '1',
            singerlist:'',
            songlist:'',
            notfind:'',
            flag:1,
            notfind1:'',
            flag1:1,
          }
      },
      components:{
        'el-select': Select,
        'el-input': Input,
        'el-option': Option,
        'el-button': Button
      },
      methods:{
          fnreturngo(){
              if(true){
                  this.$router.go(-1)
              }
          },
          clearFlag(){
            this.flag1=3,
            this.flag=3
          },
          InputSearch(){
            if (this.select==1){             
              this.$http.get(this.$store.state.baseUrl+"/singer/searchsinger/api/?singer_name="+this.input1)
              //成功的回调
              .then((res)=>{
                if (res.data.Status == 200){
                  this.flag1=1
                  this.singerlist=res.data.Data
                }
                else if(res.data.Status == 404){
                  this.flag1=2
                  this.notfind1=res.data.Data
                }
              })
              //失败的回调
              .catch((res)=>{
                console.log('失败的回调',res)
              })
            }
            else if(this.select==2){
              this.$http.get(this.$store.state.baseUrl+"/singer/searchsong/api/?song_name="+this.input1)
              //成功的回调
              .then((res)=>{
                if (res.data.Status ==200){
                  this.flag=1
                  this.songlist=res.data.Data
                }
                else if(res.data.Status == 404){
                  this.flag=2
                  this.notfind=res.data.Data
                }
              })
              //失败的回调
              .catch((res)=>{
                console.log('失败的回调',res)
              })
            }
          },
          //跳转指定歌手
          goToDetails(id){
            if(true){
              this.$router.push(
                {
                  name:'/details_singer_des',
                  query:{
                    id:id
                  }
                })
            }
          },
          //跳转指定歌曲
          goTosong(id,song_name,song_url,singer_name){
            if(true){
              this.$router.push({
                path:'/play_page',
                query:{
                  id:id,
                  song_name:song_name,
                  song_url:song_url,
                  singer_name:singer_name
                }
              })
            }
          },
      },
  }
</script>

<style>
  .search{
    width: 100%;
    
  }
  .fnreturn_s{
    background: gainsboro;
    position: relative;
    margin-top: -3.7rem;
    height: 4rem;
    font-size: 1.5rem;
    line-height: 4rem;
  }
  .return_left_s{
    position:absolute;
    left: 2rem;
  }
  .attention_s{
    position: absolute;
    right: 2rem;
  }
  .songer_list_des li{
    height: 2.5rem;
    line-height: 2.5rem;
    border: 1px solid #f1f1f1;
    border-radius: 10%;
  }
  .sp1{
    display: block;
    height: 2.5rem;
    line-height: 2.5rem;
    border: 1px solid #f1f1f1;
    border-radius: 10%;
    font-size: 1.2rem;
    text-align: center;
    color: #666;
  }
  .songer_list_des{
    margin-top: 0.8rem;
  }
  .singer_li{
    vertical-align: middle;
    background: white;
  }
  .singer_li span{
    padding-left: 3rem;
  }
  .singer_img{
    height: 100%;
    border: 0.1rem solid #f1f1f1;
    border-radius: 20%;
    vertical-align: middle;
  }
  .song{
    width: 100%;
    height: 4rem;
    position: relative;
  }
  .song_left{
    position: absolute;
    top: 0;
    left: 0;
    width: 10%;
    height: 4rem;
    line-height: 4rem;
    text-align: center;
    font-size: 1.5rem;
    color: #999;
  }
  .song_center{
    position: absolute;
    top: 0;
    left: 10%;
    width: 75%;
  }
  .song_center_t{
    height: 2rem;
    line-height: 2rem;
    font-size: 1.2rem;
    font-weight: 200;
    color: black;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .song_center_b{
    height: 2rem;
    font-size: 0.8rem;
    color: #888;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .song_right{
    position: absolute;
    top: 0;
    right: 0;
    width: 15%;
    color: #333;
    font-size: 2rem;
    line-height: 4rem;
  }

  @font-face {
  font-family: 'iconfont';  /* project id 1482310 */
  src: url('//at.alicdn.com/t/font_1482310_vi9nci9xgb9.eot');
  src: url('//at.alicdn.com/t/font_1482310_vi9nci9xgb9.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1482310_vi9nci9xgb9.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1482310_vi9nci9xgb9.woff') format('woff'),
  url('//at.alicdn.com/t/font_1482310_vi9nci9xgb9.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1482310_vi9nci9xgb9.svg#iconfont') format('svg');
}
  .iconfont {
    font-family: "iconfont" !important;
    /* font-size: 30rem; */
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.1rem;
    -moz-osx-font-smoothing: grayscale;
  }
  .el-select .el-input {
    width: 110px;
  }
  .input-with-select .el-input-group__prepend {
    background-color: #fff;
  }
</style>
