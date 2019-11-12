<template>
  <div class="cool">
    <a href="http://122.51.131.172:8081/#/home_page
" class="movie">
      <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573292390141&di=d7f2784f6f2c297abda1d9c97ba3c31f&imgtype=0&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fq_70%2Cc_zoom%2Cw_640%2Fimages%2F20171005%2F21dd5b7a9bba4c45b86184dbec4d3c5d.jpeg" alt="">
    </a>

  </div>

</template>

<script>
  export default {
      name:'cool',
      data(){
          return{

          }
      },
      methods:{

      }
  }
</script>

<style scoped>
  *{
    width: 100%;
  }
  .cool{
    width: 100%;
  }
  .moive{
    display: flex;
    flex-direction: row;
    width: 100%;
    /* height: 100%; */
  }
  .moive img{
    display: flex;
    width: 100%;
    overflow: hidden;
    vertical-align: middle;
  }

</style>
