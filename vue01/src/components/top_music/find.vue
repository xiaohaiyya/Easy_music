<template>
  <div>
    <div class="swiper-container">
        <div class="swiper-wrapper">
            <div class="swiper-slide">
              <a href=""><img src="https://p1.music.126.net/hoYLHvnEsvs08oX2c9pgPg==/109951164455147691.jpg
" alt="" class="img1"></a>
            </div>
            <div class="swiper-slide">
              <a href=""><img src="https://p1.music.126.net/HxB599gOkeBkZEkMm4lXjg==/109951164456527827.jpg
" alt="" class="img1"></a>
            </div>

            <div class="swiper-slide">
              <a href=""><img src="https://p1.music.126.net/C37WAY_IftgoFmF4_MoD5w==/109951164453369881.jpg
" alt="" class="img1"></a>
            </div>
        </div>
        <!-- 如果需要分页器 -->
      <div class="swiper-pagination" slot="pagination"></div>
<!--        <div class="swiper-pagination"></div>-->
        <!-- 如果需要导航按钮 -->
<!--        <div class="swiper-button-prev"></div>-->
<!--        <div class="swiper-button-next"></div>-->
        <!-- 如果需要滚动条 -->
<!--        <div class="swiper-scrollbar"></div>-->
    </div>
    <ul class="select_Grouping">
      <li @click="fntuijian" >
        <div class="everyday1 iconfont">&#xe60e;</div><br>
        <div class="tuijian1">推荐</div><br>
      </li>
      <li @click="fngedan">
        <div class="songlist1 iconfont" >&#xe642;</div><br>
        <div class="gedan1">歌单</div>
      </li>
      <li @click="fnsinger">
        <div class="singer_broadcast1 iconfont"  >&#xe619;</div><br>
        <div class="singer1">歌手</div>

      </li>
      <li @click="fntops">
        <div class="Leaderboard1 iconfont">&#xe67b;</div><br>
        <div class="paihang1" >排行榜</div>
      </li>
    </ul>


    <div class="Song_Square">
      <div class="Song_Square_title">
        <div class="recommend">推荐歌单</div>
        <div href="" class="song_square">歌单广场</div>
      </div>
      <ul class="Song_Square_content">
        <li class="content_first" @click="fnfirstsong(item.songlist_id)" v-for="(item,index) in song_list_des_list" :key="index">
          <img v-lazy=item.songlist_img :src=item.songlist_img alt="">
<!--          <div class="content_first_bottom">-->
<!--            <span class="headset iconfont">&#xe64e;</span>-->
<!--            <span>14万</span>-->
<!--            <span class="play iconfont">&#xe8a3;</span>-->
<!--          </div>-->
          <p class="copywriting2">{{item.songlist_title}}</p>
        </li>
      </ul>
    </div>
  </div>

</template>

<script>
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import Swiper from 'swiper';
import 'swiper/dist/css/swiper.min.css';
export default {
    name:'find',
    data () {
      return {
        song_list_des_list:"",
      }
    },

    mounted:function() {
      this.getRandomList();

		var mySwiper = new Swiper('.swiper-container', {
                // 方向
                direction: 'horizontal',
                effect:"fade",
                // 循环
                autoplay: true,
                speed:3000,
                autoplayDisableOnInteraction : false,
                loop: true,
                pagination:{
                    el:'.swiper-pagination',
                    clickable:true,
        },
              });
        },
    methods:{
        fnfirstsong(id){
            if(true){
                this.$router.push(
                  {
                    path:'/details_page_first',
                    query:{
                      id:id
                    }
                  })
            }
        },
        fntuijian() {
            if (true) {
                this.$router.push('/recommend')
            }
        },
        fnsinger(){
            if(true){
                this.$router.push('/singer')
            }
        },
        fngedan(){
            if(true){
                this.$router.push('/song_list')
            }
        },
        fntops(){
            if(true){
                this.$router.push('/tops')
            }
        },
        //获取随机歌单
        getRandomList(){
          this.$http.get(this.$store.state.baseUrl+"/songlist/randomsonglist/api")
          //成功的回调
          .then((res)=>{
            this.song_list_des_list=res.data;
          })
          //失败的回调
          .catch((res)=>{
            console.log('失败的回调',res)
          })
        },
    },

}
</script>

<style scoped>
  .Song_Square_content{
    display: flex;
    flex-wrap:wrap;
    justify-content:space-between;
  }
  .Song_Square_title{
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    margin-top: 0.5rem;
  }
  .select_Grouping li{
    display: inline-block;
  }

.img1{
  width: 100%;
  height: 10rem;
}
.select_Grouping{
  /*text-align: center;*/
  border-bottom: 0.01rem solid gainsboro;
  /*padding-bottom: 1rem;*/
  /*margin-bottom: 1rem;*/
  display: flex;
  flex-direction: row;
  justify-content:space-between;

}
.everyday1,.songlist1,.singer_broadcast1,.Leaderboard1{
  display: flex;
  width: 3rem;
  height: 3rem;
  color: gold;
  font-size: 1.4rem;
  line-height: 3rem;
  background: blanchedalmond;
  border-radius: 50%;
  justify-content:center;
}

.recommend{
  padding-left: 1rem;
  font-weight: 400;
  color: black;
}
.song_square{
  font-size: 1rem;
  border: 0.07rem solid gainsboro;
  color: black;
  /* font-weight: 400; */
  /*padding: 0.3rem;*/
  border-radius: 1rem 1rem;
  /*margin-left:13rem ;*/

}
.select_description{
  /*margin-top: 1rem;*/
  padding-right: 3.5rem;
}
.tuijian1,.gedan1,.paihang1,.singer1{
  font-size: 1rem;
  display: flex;
  justify-content:center;
}


.content_first{
  width: 30%;
  /* height: 6.5rem; */
  /*border:0.05rem solid;*/
  border-radius: 0.2rem;
  position: relative;
  margin-top: 0.4rem;
  display: inline-block;
  padding-left: 0.4rem;
  margin-bottom: 1rem;
}
.content_first img,.content_second img,.content_third img{
  width: 100%;
  height: 100%;
  /*border:0.05rem solid;*/
  border-radius: 0.2rem;
}
.content_first_bottom{
  font-size:0.5rem ;
  /*opacity:0.5;*/
  background: rgba(0,0,0,0.5);
  position: absolute;
  bottom: -0.05rem;
  line-height: 1.5rem;
  width: 95%;
  height: 1.5rem;
  /*border:0.05rem solid;*/
  border-radius: 0.2rem;
}
.copywriting2{
  font-size: 1rem;
  width: 100%;
  height: 1.2rem;
  line-height: 1.2rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.headset{
  padding-left: 0.7rem;
}
.play{
  padding-left: 2rem;
}


@font-face {
  font-family: 'iconfont';  /* project id 1482310 */
  src: url('//at.alicdn.com/t/font_1482310_w6rkten5bh.eot');
  src: url('//at.alicdn.com/t/font_1482310_w6rkten5bh.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1482310_w6rkten5bh.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1482310_w6rkten5bh.woff') format('woff'),
  url('//at.alicdn.com/t/font_1482310_w6rkten5bh.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1482310_w6rkten5bh.svg#iconfont') format('svg');
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
