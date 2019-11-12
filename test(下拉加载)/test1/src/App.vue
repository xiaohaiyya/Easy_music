<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import test01 from './components/test01'
import test02 from './components/test02'

export default {
  name: 'App',
  components:{
    test01,
    test02
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
