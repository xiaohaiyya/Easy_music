<template>
  <div class="details_singer_des">

    <div class="fnreturn" >
      <span class="return_left iconfont" @click="fnreturngo" >&#xe625;</span>
      <span>{{singers_des.singer_name}}</span>
<!--      <span>{{index.singer_name}}</span>-->
      <span class="attention iconfont">&#xe60f;</span>
    </div>


    <div class="singer_img">
      <img :src=singers_des.singer_pic alt="">
    </div>
    <div class="hot">播放热门</div>
    <div class="list_bottom">
      
      <!-- <ul class="singer_song_list" v-for="(item,index) in singers_des.info" :key="index">
        <li @click="goTosong(item.song_id,item.song_name,item.song_download_url,item.singer_name)">
          <span class="li_left_num">{{index+1}}</span>
          <div class="li_right">
            <span>{{item.song_name}}</span><br>
            <span>专辑:{{item.song_album}}</span>
          </div>
        </li>
      </ul> -->

      <ul class="songlistinfos">
          <li class="songlistinfo" @click="goTosong(item.song_id,item.song_name,item.song_download_url,item.singer_name)" v-for="(item,index) in singers_des.info" :key="index" >
            <div class="song">
              <p class="song_left" >{{index+1}}</p>
              <div class="song_center">
                <p class="song_center_t">{{item.song_name}}</p>
                <p class="song_center_b">专辑:{{item.song_album}}</p>
              </div>
              <p class="song_right iconfont">&#xe613;</p>
            </div>
          </li>
        </ul>

    </div>


  </div>

</template>

<script>
  export default {
      name:'details_singer_des',
      data(){
          return{
              singers_des:'',
              singer_id: this.$route.query.id
          }
      },
      methods:{
          fnreturngo(){
              if(true){
                  this.$router.go(-1)
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
          getsinger_des(){
            this.$http.get(this.$store.state.baseUrl+"/singer/artist/api/?"+"singer_id="+this.singer_id)
            // 成功的回调
            .then((res)=>{
                this.singers_des=res.data
            })
            .catch((res)=>{
                console.log("失败的回调",res)
            })
        },
      },
      mounted() {
          this.getsinger_des()
      }
  }
</script>

<style scoped>
  *{
    list-style: none;
  }
  .search{
    width: 100%;
    /* height: 1000px; */
    background: goldenrod;
  }
  .fnreturn {
    width: 100%;
    background: #FAFFF0;
    color: #292421;
    margin-top: 0;
    position:fixed;
    top:0;
    font-size: 1.2rem;
    font-weight: 300;
    line-height: 3.75rem;
    z-index: 10000;
  }
  .return_left{
    padding-left: 1.5rem;
  }
  .attention{
    position: fixed;
    right: 2rem;
  }
  .singer_img img{
    width: 100%;
  }
  .singer_img{
    display: flex;
  }
  .singer_song_list{
    width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .singer_song_list li{
    height: 4rem;
    border-bottom: 0.05rem solid whitesmoke;
  }
  .li_left_num{
    position: absolute;
    left: 0.5rem;
    font-size: 1.5rem;
  }
  .li_right{
    position: absolute;
    left:2.6rem;
  }
  .list_bottom{
    padding: 0.5rem 1rem 0.5rem 1rem;
    background: rgba(0, 0, 0, 0.3);
    color:whitesmoke;
  }
  .hot{
    font-size: 1.4rem;
    padding: 1rem 0 1rem 1rem;
    background:rgba(0, 0, 0, 0.3); 
    border-top-left-radius: 2rem ;
    border-top-right-radius: 2rem ;
    color: paleturquoise;
    border-bottom: 0.1rem solid wheat;
    margin-top: -0.3rem;
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
    color: rgb(248, 240, 240);
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
    color: white;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .song_center_b{
    height: 2rem;
    font-size: 0.8rem;
    color: white;
    text-overflow: ellipsis;
    white-space: nowrap;
    overflow: hidden;
  }
  .song_right{
    position: absolute;
    top: 0;
    right: 0;
    width: 15%;
    color: rgb(248, 240, 240);
    font-size: 2rem;
    line-height: 4rem;
    font-weight: 200;
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


</style>
