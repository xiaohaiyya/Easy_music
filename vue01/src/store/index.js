import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state:{
        // 接口的基础路径
        baseUrl: "http://101.200.125.219",
    }
})
