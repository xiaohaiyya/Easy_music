<template>
  <div class="play_page">
   <div class="fnreturn" >
      <div class="return_left iconfont" @click="fnreturngo" >&#xe625;</div>
      <div class="namefixes">{{song_name}}</div>
      <div class="attention iconfont">&#xe60f;</div>
    </div>
    <div class="bgimg"  :style="screen_height"><img src="../assets/img/backg.jpeg" alt=""></div>
    <div class="bofanglan" style="padding:10px 0;margin-bottom: 2rem" >
       <aplayer autoplay :music="musicList" class="bofangqi">
       </aplayer>
    </div>
  </div>

</template>

<script>
  import VueAplayer from 'vue-aplayer';
import aplayer from "vue-aplayer";
  export default {
      name:'play_page',
      url:'songerplay.song_download_url',
      components: {
    //别忘了引入组件
       'a-player': VueAplayer,
        aplayer: aplayer
  },
      data(){
          return{
              screen_height:{height:"500px"},
              songerplay:'',
              song_id:this.$route.query.id,
              song_name:this.$route.query.song_name,
              song_url:this.$route.query.song_url,
              singer_name:this.$route.query.singer_name,

                musicList: {

                  title: this.$route.query.song_name,
                  author: this.$route.query.singer_name,
                  url: this.$route.query.song_url,
                  pic: "",
                  lrc: "[00:00.00]lrc here\n[00:01.00]aplayer"
          }

          }
      },
      computed: {
        url() {
          return this.url;
        }
      },
      methods:{
          fnreturngo(){
              if(true){
                  this.$router.go(-1)
              }
          },


          getsinger_des(){

            this.$http.get(this.$store.state.baseUrl+"/songlist/songlistinfo/api/?songlist_id="+this.$route.query.id)
            // 成功的回调
            .then((res)=>{
                this.songerplay=res.data
            })
            .catch((res)=>{
                console.log("失败的回调",res)
            })
        },

      },
      mounted() {
          this.screen_height.height = window.screen.height - 60 + "px"
          this.goTosongplay();

            this.musicList = {
              title: this.song_name,
              author: this.singer_name,
              url: this.song_url,
              pic: "",
              lrc: "[00:00.00]lrc here\n[00:01.00]aplayer"

          }
      },
  }
</script>


<style scoped>
  .aplayer-info{
    display: flex;
    flex-direction: row;
    justify-content:space-between;
  }

  .play_page img{
    display: flex;
    width: 100%;
    overflow: hidden;
    vertical-align: middle;
  }
  .namefixes{

    display: inline-block;
    width: 15rem;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .fnreturn {
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    padding-top: 0.8rem;
    width: 100%;
    height: 3rem;
    background: #FAFFF0;
    color: #292421;
    margin-top: 0;
    position:fixed;
    top:0;
    font-size: 1.2rem;
    font-weight: 300;
    line-height: 2.5rem;
    z-index: 10000;
  }
  .return_left{
    vertical-align: top;
  }
  .attention{

    top: 0;
  }
.play_page{
  width: 100%;
  background: gray;
  background-repeat: no-repeat;
  background-size: cover;
}
.play_page img{
  width: 100%;
  height: 100%;
}
.aplayer .bofangqi{
   width: 100%;
   display: flex;
  flex-direction: row;
  justify-content:center;
}
.bofanglan{
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content:center;
  position: absolute;
  bottom: 1.5rem;

}
.bofangqi{
  flex-direction: row;
  justify-content:space-between;
  width: 100%;
  background: #ffd930;
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
  .bgimg{
    height: 100%;
    overflow: hidden;
  }
</style>

