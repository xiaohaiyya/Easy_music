// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import 'bootstrap'

//导入仓库
import store from './store'

//mint-ui导入InfiniteScroll
import { InfiniteScroll } from 'mint-ui';
Vue.use(InfiniteScroll);

import { Spinner } from 'mint-ui';
Vue.component(Spinner.name, Spinner);

//懒加载
import VueLazyLoad from 'vue-lazyload'
import loading from './assets/img/loading.gif'
//使用懒加载插件,loading参数指定加载图片的gif地址,这个gif也要放在static文件夹里
Vue.use(VueLazyLoad,{
  preLoad:1.3,
  loading,
  attempt:1
})

import 'element-ui/lib/theme-chalk/index.css';

import axios from './api/axios';
Vue.prototype.$http = axios;


// axios.defaults.withCredentials=true


Vue.config.productionTip = false  //需要在单独把这个css引入
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/dist/css/swiper.css'
Vue.use(VueAwesomeSwiper)


import Router from 'vue-router'

const originalPush = Router.prototype.push
Router.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}



new Vue({
  el: '#app',
  router,
  store,
  
  components: { App },
  template: '<App/>'
})
