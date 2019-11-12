<template>
  <div class="index">
    <router-view></router-view>
      <div class="view">

      <!-- <router-link to="login"> -->
        <div class="header_login iconfont" @click="fnlogin">&#xe611;</div>
      <!-- </router-link> -->

      <!-- <router-link to="mine"> -->
        <div class="header_mine" @click="fnmine">我的</div>
      <!-- </router-link> -->

      <!-- <router-link to="find"> -->
        <div class="header_find" @click="fnfind">发现</div>
      <!-- </router-link> -->

      <!-- <router-link to="cool"> -->
        <div class="header_cool" @click="fncool">爽城</div>
      <!-- </router-link> -->

      <!-- <router-link to="video"> -->
        <div class="header_video" @click="fnvideo">视频</div>
      <!-- </router-link> -->

      <!-- <router-link to="search"> -->
        <div class="header_search iconfont" @click="fnsearch">&#xe633;</div>
      <!-- </router-link> -->

    </div>


  </div>

</template>

<script>
    export default {
        name: 'index',
        data() {
            return {
                type: ''
            }
        },
        methods: {
            fnlogin() {
                this.$router.push('/index/login');
                document.querySelector('.header_login').style.color = "#842b00";
                document.querySelector('.header_mine').style.color = "";
                document.querySelector('.header_find').style.color = "";
                document.querySelector('.header_cool').style.color = "";
                document.querySelector('.header_video').style.color = "";
                document.querySelector('.header_search').style.color = "";
            },
            fnmine() {
                this.$router.push('/index/mine');
                document.querySelector('.header_login').style.color = "";
                document.querySelector('.header_mine').style.color = "#842b00";
                document.querySelector('.header_find').style.color = "";
                document.querySelector('.header_cool').style.color = "";
                document.querySelector('.header_video').style.color = "";
                document.querySelector('.header_search').style.color = "";
            },
            fnfind() {
                this.$router.push('/index/find');
                document.querySelector('.header_login').style.color = "";
                document.querySelector('.header_mine').style.color = "";
                document.querySelector('.header_find').style.color = "#842b00";
                document.querySelector('.header_cool').style.color = "";
                document.querySelector('.header_video').style.color = "";
                document.querySelector('.header_search').style.color = "";
            },
            fncool() {
                this.$router.push('/index/cool');
                document.querySelector('.header_login').style.color = "";
                document.querySelector('.header_mine').style.color = "";
                document.querySelector('.header_find').style.color = "";
                document.querySelector('.header_cool').style.color = "#842b00";
                document.querySelector('.header_video').style.color = "";
                document.querySelector('.header_search').style.color = "";
            },
            fnvideo() {
                this.$router.push('/index/video');
                document.querySelector('.header_login').style.color = "";
                document.querySelector('.header_mine').style.color = "";
                document.querySelector('.header_find').style.color = "";
                document.querySelector('.header_cool').style.color = "";
                document.querySelector('.header_video').style.color = "#842b00";
                document.querySelector('.header_search').style.color = "";
            },
            fnsearch() {
                this.$router.push('/search');
                document.querySelector('.header_login').style.color = "";
                document.querySelector('.header_mine').style.color = "";
                document.querySelector('.header_find').style.color = "";
                document.querySelector('.header_cool').style.color = "";
                document.querySelector('.header_video').style.color = "";
                document.querySelector('.header_search').style.color = "#842b00";
            },

        },

    }
</script>

<style scoped>
  .view {
    width: 100%;
    background: #f1f1f1;
    margin-top: 0;
    position:fixed;
    top:0;
    font-size: 1.2rem;
    color: grey;
    line-height: 3.75rem;
    z-index: 10000;
    display: flex;
    flex-direction: row;
    justify-content:space-between;
  }
  .header_login {
    font-size: 1.5rem;
  }
  .header_mine {
    font-size: 1.2rem;

  }

  .header_search{
    padding-left: 2rem;
    font-size: 1.5rem;

  }

  a {
    color: gray;
    display: inline-block;
    text-align: center;

  }

  @font-face {
    font-family: 'iconfont';  /* project id 1482310 */
    src: url('http://at.alicdn.com/t/font_1482310_yvcgs2a8f1m.eot');
    src: url('http://at.alicdn.com/t/font_1482310_yvcgs2a8f1m.eot?#iefix') format('embedded-opentype'),
    url('http://at.alicdn.com/t/font_1482310_yvcgs2a8f1m.woff2') format('woff2'),
    url('http://at.alicdn.com/t/font_1482310_yvcgs2a8f1m.woff') format('woff'),
    url('http://at.alicdn.com/t/font_1482310_yvcgs2a8f1m.ttf') format('truetype'),
    url('http://at.alicdn.com/t/font_1482310_yvcgs2a8f1m.svg#iconfont') format('svg');
  }

  .iconfont {
    font-family: "iconfont" !important;
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.1rem;
    -moz-osx-font-smoothing: grayscale;
  }


</style>
