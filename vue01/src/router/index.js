import Vue from 'vue'
import Router from 'vue-router'

import index from '@/components/index'
import details_page_first from '@/components/details_page_first'
import first_login from '@/components/first_login'
import singer from '@/components/singer'
import song_list from '@/components/song_list'
import details_singer from '@/components/details_singer'
import tops from '@/components/tops'
import top_one from '@/components/top_one'
import details_singer_des from '@/components/details_singer_des'
import play_page from '@/components/play_page'
import recommend from '@/components/recommend'

import login from '@/components/top_music/login'
import mine from '@/components/top_music/mine'
import find from '@/components/top_music/find'
import cool from '@/components/top_music/cool'
import video from '@/components/top_music/video'
import search from '@/components/search'

Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path:"/",
      component:index,
    },
    {
      path:"/first_login",
      name:"/first_login",
      component:first_login
    },
    {
      path:"/singer",
      component:singer,
      name:"/singer"
    },{
      path:"/song_list",
      name:"/song_list",
      component:song_list
    },{
      path:"/recommend",
      name:"/recommend",
      component:recommend
    },

    {
      path:"/details_singer",
      name:'/details_singer',
      component:details_singer
    },{
      path:"/details_singer_des",
      component:details_singer_des,
      name:"/details_singer_des"
    },
    {
      path:"/details_page_first",
      component:details_page_first,
      name:"/details_page_first"
    },{
      path:"/play_page",
      name:"/play_page",
      component:play_page
    },
    {
      path:"/tops",
      name:"/tops",
      component:tops
    },
    {
      path: "/top_one",
      name:'top_one',
      component:top_one,

    },
    {
      path: '/search',
      name:"/search",
      component: search
    },
    {
      path: '/index',
      name: "index",
      component: index,

      children: [{
        path: '/index/login',
        name:'/index/login',
        component: login
      }, {
        path: '/index/mine',
        name:'/index/mine',
        component: mine
      }, {
        path: '/index/find',
        name:'/index/find',
        component: find
      }, {
        path: '/index/cool',
        name:'/index/cool',
        component: cool
      }, {
        path: '/index/video',
        name:'/index/video',
        component: video
      }]
    },
  ]
})
