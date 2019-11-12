<template>
<div class="details_page_first">
<div>
    <div class="details_page_first_top">
        <span class="return_go iconfont" @click="fnreturn">&#xe625;</span>
        <span class="gedan_details">榜单</span>
    </div>
    <div class="details_page_first_middle" >
        <div class="details_page_first_middle_left">
            <img src="../assets/img/bangdantu.jpeg" alt="">
            <p>{{topname}}</p>
        </div>
    <div class="details_page_first_middle_bottom">
        <ul class="song_description">
            <li>
                <div class="conversation iconfont">&#xe79f;</div><br>
                <div class="pinglun">210</div>
            </li>
            <li>
                <div class="share iconfont">&#xe607;</div><br>
                <div class="fenxiang">129</div>
            </li>
            <li>
                <div class="download iconfont">&#xe6dd;</div><br>
                <div class="xiazai">下载</div>
            </li>
            <li>
                <div class="favorite iconfont">&#xe7a9;</div><br>
                <div class="shoucang">收藏</div>
            </li>
        </ul>
    </div>
    </div>

    </div>

    <div class="song_content">
        <div class="song_all_bofang">
            <span class="song_first_bofang iconfont">&#xe613;</span>
            <span class="bofang_all">播放全部</span>
        </div>
        <ul class="songlistinfos">
            <li class="songlistinfo" @click="goTosong(item.song_id,item.song_name,item.song_download,item.singer_name)" v-for="(item,index) in songslist" :key="index" >
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

</template>
<script>
export default {
    name:'top_one',
    data(){
        return {
            oj:'',//榜单对象
            listinfo:'',  //榜单内容
            songslist:'',  //歌曲列表
            topname:this.$route.query.topname,
        }
    },

    methods: {
        fnreturn(){
            if(true){
                this.$router.go(-1)
            }
        },
        goTosong(id,song_name,song_href,singer_name){
            if(true){
                this.$router.push({
                path:'/play_page',
                query:{
                    id:id,
                    song_name:song_name,
                    song_url:song_href,
                    singer_name:singer_name
                    }
                })
            }
        },
        //获取榜单详情
        getListInfo(){
            this.$http.get(this.$store.state.baseUrl+'/songtops/onelist/api/?name='+this.$route.query.topname)
          //成功的回调
            .then((res)=>{
                this.oj=res.data
                this.listinfo = this.oj[0]
                this.songslist = this.listinfo.songs_list


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
<style >
.details_page_first{
    width: 100%;
    }
.details_page_first_top{
    top: 0;
    left: 0;
    width: 100%;
    height: 4.2rem;
    margin-top: 0;
    position:fixed;
    font-size: 1.2rem;
    line-height: 3.75rem;
    z-index: 10000;
    background: #FAFFF0;
    color: #292421;
    display: flex;


}
.details_page_first_middle{
    background: rgb(0,0,0,0.5);
    margin-top: 3rem;
}
.song_description li{
  display: inline-block;
}
.details_page_first_middle_left{
    width: 40%;
    height: 5rem;
    border-radius: 0.2rem;
    position: relative;
    margin-top: 4.16rem;
    padding-left: 0.6rem;
}
.details_page_first_middle_left img{
    border-radius: 0.8rem;
    width:110%;
    display: inline-block;
    padding-top: 0.5rem;
}
.details_page_first_middle_left p{
    margin:-3rem 0 0 1rem;
}
.return_go{
    padding-left: 1.5rem;
    font-size: 1.8rem;
}
.gedan_details{
    font-size: 1.5rem;
    padding-left: 1rem;
}
.sousuo_details{
    font-size: 2rem;
    padding-left: 4rem;
}
.content_first_bottom{
    font-size:0.5rem ;
    background: rgba(0,0,0,0.4);
    position: absolute;
    margin-top: 2rem;
    line-height: 1.5rem;
    width: 88%;
    height: 1.5rem;
    color: #f1f1f1;
    border-radius: 0.2rem 0.2rem 0.8rem 0.8rem;
}
.copywriting{
    width: 55%;
    height: 2.5rem;
    padding-left: 10rem;
    padding-top: -5rem;
    text-overflow: ellipsis;
    overflow: hidden;
    display: inline-block;
    font-size: 1rem;
    color: #f1f1f1;
}


.details_page_first_middle_bottom{
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    margin-bottom: 1rem;
    font-size: 1.2rem;
    padding-top: 1rem;
}
.conversation,.share,.download,.favorite{
    width: 3rem;
    height: 3rem;
    color: gold;
    font-size: 1.5rem;
    line-height: 3rem;
    display: flex;
    flex-direction: row;
    justify-content:center;
    background: blanchedalmond;
    border-radius: 50%;
}
.song_description{
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content:space-between;
    color: #f1f1f1;
    padding-top: 0.5rem;
    margin-top: 0.5rem;
}
.pinglun{
    font-size: 1rem;
    display: flex;
    flex-direction: row;
    justify-content:center;
}
.fenxiang{
    font-size: 1rem;
    display: flex;
    flex-direction: row;
    justify-content:center;
}
.xiazai{
    font-size: 1rem;
    display: flex;
    flex-direction: row;
    justify-content:center;
}
.shoucang{
    font-size: 1rem;
    display: flex;
    flex-direction: row;
    justify-content:center;
}

.song_content{
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
    border-top: 0.05rem solid rgba(0,0,0,0.1);
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
