<template>
  <div class="singer">
    <div>
      <div class="singer_top">
        <span class="return_go iconfont" @click="fnreturn">&#xe625;</span>
        <span class="singer_details">歌手分类</span>
      </div>
      <div class="show_hide">
        <span>全部歌手</span>
        <el-dropdown class="shaixuan">
          <div class="el-dropdown-link">
          <div class="filter iconfont" @click="fnshow">&#xe61e;</div>
          <div>筛选</div><i class="el-icon-arrow-down el-icon--right"></i>
          </div>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item v-for="(i, j) in kinds" :key="j">
              <p @click="get_singer(i)">{{i}}</p>
            </el-dropdown-item>
          </el-dropdown-menu> 
        </el-dropdown>
      </div>
    </div>

    <div class="hot-singers"><span class="hot-singer">{{ k }}</span></div>

    <div class="singers">
      <div class="songer_list_des">
        <ul>
          <li class="singer_li" v-for="(item,index) in singer.info" :key="index" @click="goToDetails(item.singer_id)">
            <img :src=item.singer_pic  alt="" class="singer_img">
            <span>{{item.singer_name}}</span>
          </li>
        </ul>
      </div>
    </div>


    <div>

    </div>


</div>


</template>

<script>
  import {Dropdown,slot,DropdownItem,DropdownMenu,}from 'element-ui'
  export default {
      name: 'singer',
      data() {
          return {
              rest: '',
              hot_singers: '',
              singer:'',
              kinds: '',
              page_num: 1,
              k: '',
          }
      },
      components:{
          'el-dropdown':Dropdown,
          'el-slot':slot,
          'el-dropdown-item':DropdownItem,
          'el-dropdown-menu':DropdownMenu,

      },

      methods: {
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
          fnshow(){
            if(true){
                hide_show = true;
                  }
              },
          fnreturn(){
            if(true){
                this.$router.push('/index/find')
            }
        },
        get_kinds() {
            this.$http.get(this.$store.state.baseUrl+"/singer/kinds/api")
                .then((res) => {
                    this.kinds = res.data
                })
                .catch((res) => {
                    console.log("失败的回调", res)
                })
        },
        get_singer(kind) {
            this.k = kind;
            this.$http.get(this.$store.state.baseUrl+"/singer/artist/cat/api/?"+"kind="+kind+"&page_num="+this.page_num)
                .then((res) => {
                    this.singer = res.data
                })
                .catch((res) => {
                    console.log("失败的回调", res)
                })
        },
        
      },
      mounted () {
        // 调用一下
        this.get_singer("华语男歌手");
        this.get_kinds();

    },

  }
</script>

<style scoped>
  .singer{
    list-style: none;
    width: 100%;
  }
  .return_go{
    padding-left: 0.6rem;
    font-size: 1.8rem;
  }
  .singer_top{
    top: 0;
    left: 0;
    width: 100%;
    background: #FAFFF0;
    color: #292421;
    margin-top: 0;
    position:fixed;
    font-size: 1.2rem;
    line-height: 3.75rem;
    z-index: 10000;
  }
  .mybox-leave-active,.mybox-enter-active{
      transition: all 1s ease;
}
.mybox-leave-active,.mybox-enter{
opacity:0 !important;
}
.show_hide{
  display: flex;
    flex-direction: row;
    justify-content:space-between;
  padding-top: 1rem;
}

.mybox-leave,.mybox-enter-active{
  opacity: 500;
}
.el-dropdown-link{
  display: flex;
  flex-direction: row;


  font-size: 1.2rem;
}
.show_hide{
  font-size: 1.2rem;
  margin-top: 1rem;
  padding-left: 1.2rem;
}
.hot-singers{
  font-size: 1.2rem;
}

.singers{
  border-top: 0.05rem solid black;
}
.hot-singer{
  padding-left: 1rem;
}


.block{
  margin-top: 1.5rem;
}
.songer_list_des li{
    height: 2.5rem;
    line-height: 2.5rem;
    border: 1px solid #f1f1f1;
    border-radius: 10%;
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







@font-face {
  font-family: 'iconfont';  /* project id 1482310 */
  src: url('//at.alicdn.com/t/font_1482310_mkfkyhuldc.eot');
  src: url('//at.alicdn.com/t/font_1482310_mkfkyhuldc.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1482310_mkfkyhuldc.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1482310_mkfkyhuldc.woff') format('woff'),
  url('//at.alicdn.com/t/font_1482310_mkfkyhuldc.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1482310_mkfkyhuldc.svg#iconfont') format('svg');
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


