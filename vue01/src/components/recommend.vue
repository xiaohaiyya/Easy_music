<template>
  <div class="details_page_first">
    <div>
    <div class="details_page_first_top">
      <div class="return_go iconfont" @click="fnreturn">&#xe625;</div>
      <div class="gedan_details">每日推荐</div>
    </div>

    <div class="details_page_first_middle" >
      <div class="details_page_first_middle_left">
          <img :src=listinfo.songlist_img alt="">
      </div>
    </div>

    <div class="song_content">
        <div class="song_all_bofang">
          <span class="song_first_bofang iconfont">&#xe613;</span>
          <span class="bofang_all">播放全部</span>
        </div>

        <ul class="songlistinfos">
          <li class="songlistinfo" @click="goTosong(item.song_id,item.song_name,item.song_download_url,item.singer_name)" v-for="(item,index) in songinfo" :key="index" >
            <div class="song">
              <p class="song_left" >{{index+1}}</p>
              <div class="song_center">
                <p class="song_center_t">{{item.song_name}}</p>
                <p class="song_center_b">{{item.singer_name}}</p>
              </div>
              <p class="song_right iconfont">&#xe613;</p>
            </div>
          </li>
        </ul>
    </div>

  </div>
</div>
</template>
<script>
export default {
    name:'details_page_first',
    data() {
        return {
            input: '',
            listinfo:'',  //歌单内容
            songinfo:'',  //歌曲列表
            num:1,
        }
    },
    methods: {
        //返回上一级
        fnreturn(){
            if(true){
                this.$router.push("/index/find")
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
        //获取歌单详情内容
        getListInfo(){
          this.$http.get(this.$store.state.baseUrl+"/songlist/songlistinfo/api/?songlist_id=2695632861")
          //成功的回调
          .then((res)=>{
            this.listinfo=res.data
            this.songinfo = this.listinfo.songinfo
          })
          //失败的回调
          .catch((res)=>{
            console.log("失败的回调",res)
          })
        }
    },
    mounted(){
      this.getListInfo()
    }
}
</script>


<style scoped>
  .details_page_first{
    width: 100%;
  }
  .details_page_first_top{
    display: flex;
    flex-direction: row;
    /*justify-content:space-between;*/
    top: 0;
    left: 0;
    width: 100%;
    margin-top: 0;
    position:fixed;
    font-size: 1.2rem;
    line-height: 4.1rem;
    z-index: 10000;
    background: #FAFFF0;
    color: #292421;
  }
  .details_page_first_middle{
    background: #808080;
    margin-top: 3rem;
  }
  .song_description li{
    display: inline-block;
  }
  .details_page_first_middle_left{
    display: flex;
    width: 100%;
    height: 5rem;
    position: relative;
    margin-top: 4rem;
  }
  .details_page_first_middle_left img{
    width: 100%;
    height: 10rem;
  }
  .return_go{
    /*padding-left: 1.5rem;*/
    font-size: 1.8rem;
  }
  .gedan_details{
    display: flex;
    font-size: 1.2rem;

  }
  .sousuo_details{
    font-size: 2rem;
    padding-left: 4rem;
  }
  .star{
    font-size: 0.5rem;
    font-weight: 100;
  }

  .content_first_bottom{
  font-size:0.5rem ;
  background: rgba(0,0,0,0.4);
  position: absolute;
  margin-top: -1.75rem;
  line-height: 1.5rem;
  width: 88%;
  height: 1.5rem;
  color: #f1f1f1;
  border-radius: 0.2rem 0.2rem 0.8rem 0.8rem;
  }


  .details_page_first_middle_bottom{

  margin-bottom: 1rem;
  font-size: 1.2rem;
  padding-top: 1rem;
}
.conversation,.share,.download,.favorite{
  display: inline-block;
  width: 3rem;
  height: 3rem;
  text-align: center;
  color: gold;
  font-size: 1.5rem;
  line-height: 3rem;
  background: blanchedalmond;
  border-radius: 50%;
  justify-content:space-between;
}
.details_page_first_middle_right_top{
  width: 55%;
  margin-top: -4.5rem;
  margin-left: 10rem;
  color: #f1f1f1;
}
.song_description div{
  display: flex;
  flex-direction: row;

  justify-content:center;
}


.song_description{
  margin-top: 0.5rem;
  display: flex;
  flex-direction: row;
  justify-content:space-between;
  color: #f1f1f1;

}

  .pinglun,.fenxiang,.xiazai,.shoucang{
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    font-size: 1rem;
  }
  .song_all_bofang{
    margin-top: -0.5rem;
    border-bottom: 0.1rem solid gray;
  }
  .song_content{
    margin-top: 5.8rem;
    border: 0.2rem solid #f1f1f1 ;
    border-radius: 0.8rem 0.8rem 0 0;
  }
  .song_first_bofang{
    font-size: 2rem;
    padding-left: 2rem;
  }
  .bofang_all{
    padding-left: 2rem;
    font-size: 0.9rem;
  }
  .song_first{
    font-size: 1.5rem;
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
    font-size: 1.1rem;
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
  src: url('//at.alicdn.com/t/font_1482310_t3zu5ingot.eot');
  src: url('//at.alicdn.com/t/font_1482310_t3zu5ingot.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1482310_t3zu5ingot.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1482310_t3zu5ingot.woff') format('woff'),
  url('//at.alicdn.com/t/font_1482310_t3zu5ingot.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1482310_t3zu5ingot.svg#iconfont') format('svg');
}
  .iconfont {
    font-family: "iconfont" !important;
    /* font-size: 30rem; */
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.02rem;
    -moz-osx-font-smoothing: grayscale;
  }
</style>
