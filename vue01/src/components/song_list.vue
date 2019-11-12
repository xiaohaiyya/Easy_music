<template>
  <div class="song_list">
    <div class="singer_top">
      <span class="return_go iconfont" @click="fnreturn">&#xe625;</span>

      <span class="singer_details">歌单广场</span>
      </div>
      <div class="Song_Square">
        <ul v-infinite-scroll="loadMore"
            infinite-scroll-disabled="isLoading"
            infinite-scroll-distance="30"
            class="Song_Square_content">
          <li class="content_first" v-for="(item,index) in this.list" :key="index" @click="fnfirstsong(item.songlist_id)">
            <img v-lazy=item.songlist_img :src=item.songlist_img alt="" class="img2">
            <p class="copywriting1">{{item.songlist_title}}</p>
          </li>
          <!-- 加载动画 -->
          <li class="more_loading">
            <mt-spinner :type="2" :size="20" color="rgb(100, 100, 100)" v-show="is_loading_more"></mt-spinner>
            <span v-show="finished">已经加载全部内容啦</span>
          </li>
        </ul>
      </div>




  </div>

</template>

<script>
  export default {
      name:'song_list',
      computed:{

      },
      data() {
        return{
            list:[], //歌单列表
            isLoading:false, //默认是要响应上滑动作的
            pageindex:1,
            pagesize:21,
            requeTime:0,
            is_loading_more:false, //默认不显示，控制是否显示加载动画图标
            finished:false   
        }
      },
      methods:{
          fnreturn(){
              this.$router.go(-1)
          },
          fnfirstsong(id){
              if(true){
                  this.$router.push(
                    {
                      name: "/details_page_first",
                      query:{
                          id:id
                      }
                    })
              }
          },
          loadMore: function(){
            this.isLoading = true;
            this.is_loading_more = true;
            this.finished = false;
            if(!this.requeTime){
                clearInterval(this.requeTime)
            }
            var requeTime = setTimeout(() => {
                this.$http.get(this.$store.state.baseUrl+"/songlist/square/api/?pageindex="+this.pageindex+"&pagesize="+this.pagesize)
                .then((res)=>{
                    var data = res.data
                    if(data.Status==0){
                        this.list = this.list.concat(data.Data); //拼接两个数组，不能直接赋值
                        this.pageindex++;
                        this.isLoading = false;
                        this.is_loading_more = false;
                        if(data.Data.length < this.pagesize){ //此次请求的数据已经是最后一页
                            this.isLoading = true;
                            this.finished = true;
                        }
                    }else{
                      this.finished = true;
                    }
                })
                .catch((res)=>{
                    console.log("失败的回调",res)
                })
            }, 200);
        }
      },
      mounted () {
        // 调用一下
        this.loadMore();
    }
  }
</script>

<style>
  .singer_top{
    width: 100%;
    position: fixed;
    top: 0;
    z-index: 8000;
    height: 4rem;
    background: #FAFFF0;
    color: #292421;
    font-size: 1.3rem;
    line-height: 4rem;
  }
  .song_list{
    width: 100%;
  }


  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .img2{
  width: 100%;
  height: 10rem;
}
.select_Grouping{
  border-bottom: 0.01rem solid gainsboro;
  margin-bottom: 1rem;
}
.everyday,.songlist,.singer_broadcast,.Leaderboard{
  display: inline-block;
  width: 3rem;
  height: 3rem;
  text-align: center;
  color: gold;
  font-size: 1.5rem;
  line-height: 3rem;
  background: blanchedalmond;
  border-radius: 50%;
  margin-left: 2rem;
}
.recommend{
  padding-left: 1rem;
}
.song_square{
  font-size: 0.4rem;
  border: 0.07rem solid gainsboro;
  border-radius: 1rem 1rem;
  margin-left:13rem ;
  padding: 0.1rem 0.1rem;
}
.select_description{
  padding-right: 3.5rem;
}

.content_first{
  width: 30%;
  border-radius: 0.2rem;
  position: relative;
  margin-top: 0.4rem;
  display: inline-block;
  padding-left: 0.4rem;
}
.content_first img,.content_second img,.content_third img{
  width: 100%;
  height: 100%;
  border-radius: 0.2rem;
}
.content_first_bottom{
  font-size:0.5rem ;
  background: rgba(0,0,0,0.5);
  position: absolute;
  bottom: -0.05rem;
  line-height: 1.5rem;
  width: 96%;
  height: 1.5rem;
  border-radius: 0.2rem;
}
.copywriting1{
  font-size: 1rem;
  width: 100%;
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
.more_loading{
  text-align: center;
}
.mint-spinner-triple-bounce{
  position: relative;
  left: 45%;
}



  @font-face {
  font-family: 'iconfont';  /* project id 1482310 */
  src: url('//at.alicdn.com/t/font_1482310_c3dqdallbs7.eot');
  src: url('//at.alicdn.com/t/font_1482310_c3dqdallbs7.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1482310_c3dqdallbs7.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1482310_c3dqdallbs7.woff') format('woff'),
  url('//at.alicdn.com/t/font_1482310_c3dqdallbs7.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1482310_c3dqdallbs7.svg#iconfont') format('svg');
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
