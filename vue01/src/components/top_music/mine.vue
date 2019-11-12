<template>
  <div class="mine">
    <div class="top1">
      <ul>
        <li>
          <span class="icon_zi iconfont">&#xe691;</span><br>
          <span class="ziti">私人FM</span>
        </li>
        <li>
          <span class="icon_zi iconfont">&#xe68a;</span><br>
          <span class="ziti">最嗨电音</span>
        </li>
        <li>
          <span class="icon_zi iconfont">&#xe603;</span><br>
          <span class="ziti">爽乐专区</span>
        </li>
        <li>
          <span class="icon_zi iconfont">&#xe638;</span><br>
          <span class="ziti">ACG空间</span>
        </li>
      </ul>
    </div>
    <div class="top2">
      <div> <span class="incon_zi_2 iconfont">&#xe601;</span><span class="top2_2">本地音乐</span></div>
      <div> <span class="incon_zi_2 iconfont">&#xe605;</span><span class="top2_2">最近播放</span></div>
      <div> <span class="incon_zi_2 iconfont">&#xe600;</span><span class="top2_2">下载管理</span></div>
      <div> <span class="incon_zi_2 iconfont">&#xe608;</span><span class="top2_2">我的电台</span></div>
      <div> <span class="incon_zi_2 iconfont">&#xe631;</span><span class="top2_2">我的收藏</span></div>
    </div>

  </div>

</template>

<script>
  export default {
      name:'mine',
      data(){
          return{

          }
      },
      methods:{

      }
  }
</script>

<style scoped>
  body{
    width: 100%;
  }
  .mine{
    width: 100%;
    background: white;
  }
  @font-face {
  font-family: 'iconfont';  /* project id 1487997 */
  src: url('//at.alicdn.com/t/font_1487997_bmh2r5fl7zg.eot');
  src: url('//at.alicdn.com/t/font_1487997_bmh2r5fl7zg.eot?#iefix') format('embedded-opentype'),
  url('//at.alicdn.com/t/font_1487997_bmh2r5fl7zg.woff2') format('woff2'),
  url('//at.alicdn.com/t/font_1487997_bmh2r5fl7zg.woff') format('woff'),
  url('//at.alicdn.com/t/font_1487997_bmh2r5fl7zg.ttf') format('truetype'),
  url('//at.alicdn.com/t/font_1487997_bmh2r5fl7zg.svg#iconfont') format('svg');
}
  .iconfont {
    font-family: "iconfont" !important;
    /* font-size: 10rem; */
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.02rem;
    -moz-osx-font-smoothing: grayscale;
  }
  .icon_zi{
    font-size:2rem;
    background-color: antiquewhite;
    border-radius: 50%;
    padding:0.5rem;
    margin-bottom: 0.5rem;
    display: inline-block;
  }
  li{
    text-align: center;
    display:inline-block;
    width: 24%;
    margin-top: 0.8rem;
    box-sizing: border-box
  }
  span{
    text-align: center;
    font-size: 0.6rem;
  }
  .top2{
    margin-top: 1rem;
  }
  .top2 div{
    border-top: 0.01rem solid antiquewhite;
  }
  .incon_zi_2{
    font-size:1.5rem;
    color:black;
    display: inline-block;
    margin: 0.5rem 1.5rem 0.5rem 1.5rem;
  }
  .top2_2{
    color: black;
    font-size: 0.8rem;
  }

</style>
