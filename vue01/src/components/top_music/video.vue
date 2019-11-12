<template>
  <div class="video">
    <a href="http://www.cuteyuchen.xyz" class="movie" >
      <img src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1573292455543&di=0de69f61ca71935a246f5fc50eefd8df&imgtype=0&src=http%3A%2F%2Fattachments.gfan.com%2Fforum%2F201606%2F30%2F2309595niylptnmolzzkli.jpg" alt="">
    </a>

  </div>

</template>

<script>
  export default {
      name:'video',
      data(){
          return{
          }
      },
      methods:{

      },
      mounted:{
      }
  }
</script>

<style scoped>
  *{
    width: 100%;
  }
  .video{
    width: 100%;
  }
  .moive{
    display: flex;
    flex-direction: row;
    width: 100%;
  }
  .moive img{
    display: flex;
    width: 100%;
    overflow: hidden;
    vertical-align: middle;
  }
</style>
