import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'

Vue.use(Router)
import test01 from "@/components/test01"
import test02 from "@/components/test02"

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/test01',
      component:test01
    },
    {
      path: '/test02',
      component:test02
    },
  ]
})
