<template>
    <div class="tops">
        <div class="tops_top">
            <span class="iconfont top_1" @click="fngo">&#xe61b;</span>
            <span class="top_2" >排行榜</span>
        </div>
        <ul class="ul_1">
            <li v-for="(item,index) in tops" :key="index" @click="goToTopOne(item.top_name)" >
                <img :src=item.top_img>
                <p>{{item.top_name}}</p>
            </li>
        </ul>

    </div>
</template>
<script>
export default {
    data(){
        return{
            tops:'',
        }

    },

    name:'tops',
    methods: {
		goToTopOne(topname){
            if(true){
                this.$router.push(
                    {
                        name:"top_one",
                        query:{
                            topname:topname
                        }
                    })
            }
        },
        fngo(){
            if(true){
                this.$router.go(-1)
            }
        },
        gettops(){
            this.$http.get(this.$store.state.baseUrl+"/songtops/alllist/api/")
            // 成功的回调
            .then((res)=>{
                this.tops=res.data
            })
            .catch((res)=>{
                console.log("失败的回调",res)
            })
        },
    },
    mounted() {
        this.gettops()
    },
}
</script>
<style>
.iconfont {
    font-family: "iconfont" !important;
    /* font-size: 10rem; */
    font-style: normal;
    -webkit-font-smoothing: antialiased;
    -webkit-text-stroke-width: 0.02rem;
    -moz-osx-font-smoothing: grayscale;
}
@font-face {
  font-family: 'iconfont';  /* project id 1487997 */
    src: url('//at.alicdn.com/t/font_1487997_0z7c78kf9m4.eot');
    src: url('//at.alicdn.com/t/font_1487997_0z7c78kf9m4.eot?#iefix') format('embedded-opentype'),
    url('//at.alicdn.com/t/font_1487997_0z7c78kf9m4.woff2') format('woff2'),
    url('//at.alicdn.com/t/font_1487997_0z7c78kf9m4.woff') format('woff'),
    url('//at.alicdn.com/t/font_1487997_0z7c78kf9m4.ttf') format('truetype'),
    url('//at.alicdn.com/t/font_1487997_0z7c78kf9m4.svg#iconfont') format('svg');
}
*{
    margin: 0;
    padding: 0;
    text-decoration: none;
    list-style: none;
}
body{
    background-color: rgb(241, 242, 243);
}
.tops_top{
    display: flex;
    flex-direction: row;
    /*justify-content:space-between;*/
    position: fixed;
    margin-top:-3.8rem;
    font-size: 1.4rem;
    font-weight: 250;
    background: #FAFFF0;
    color: #292421;
    width: 100%;
    height: 4rem;
    line-height: 4rem;
}
.tops_top span{
    margin-left: 1rem;
}
.ul_1{
    padding-top :0.2rem;
    margin-left: 1rem;
}
.ul_1 li{
    width: 100%;
    margin-top: 1rem;
}
.ul_1 li img{
    width: 30%;
    display: inline-block;
    vertical-align: top;
    border-radius: 7%;

}
.ul_1 li p{
    width: 50%;
    display: inline-block;
    text-align: center;
    font-size: 1.2rem;
    padding-top:2.2rem;
}

</style>>

