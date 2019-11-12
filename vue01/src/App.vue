<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import index from './components/index'
import first_login from './components/first_login'
import details_page_first from './components/details_page_first'
import singer from './components/singer'
import song_list from './components/song_list'
import tops from './components/tops'
import top_one from './components/top_one'
import details_singer_des from './components/details_singer_des'
import play_page from './components/play_page'
import recommend from './components/recommend'



export default {
  name: 'App',
    data(){
      return{

      }
    },
    components:{
      index,
      first_login,
      details_page_first,
      singer,
      song_list,
      tops,
      top_one,
      details_singer_des,
      play_page,
      recommend,
    }
}
</script>

<style>

*{
  margin: 0;
  padding: 0;
  text-decoration: none;
}
body{
  background: #f5f5f5;
  font-family: 'FZCYJ' !important;
}
#app {
  font-family: 'FZCYJ','Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /*text-align: center;*/
  color: #2c3e50;
  margin-top: 60px;
}

@font-face {  
  font-family: 'FZCYJ'; 
  src: url('./assets/fonts/STXINWEI.ttf'); 
  font-weight: normal;  
  font-style: normal;  
  }
  

</style>
