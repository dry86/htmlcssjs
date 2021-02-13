<template>
	<div>
    <h1> Compute Similarity </h1>
    <h3>计算输入的字符相似度：</h3>

    <div>
      <span>第一个字符串：</span><br /><br />
      <textarea v-model="mytext1" placeholder="请输入第一个字符串"></textarea><br /><br />
      <span>第二个字符串：</span><br /><br />
      <textarea v-model="mytext2" placeholder="请输入第二个字符串"></textarea><br /><br />
    </div>


    <div>
      结果   &nbsp;  计算：<button @click="request()">compute</button>
      <br /><br />
      {{result}}
    </div>
    <text_similar></text_similar>

	</div>
</template>

<script>
import axios from "axios"
import text_similar from "./components/text_similar.vue"

export default {
  data () {
    return {
      mytext1:'',
      mytext2:'',
      result:''

    }
  },
  components:{
    text_similar
  },
  methods:{
    request(){

      axios.get("http://127.0.0.1:5000/compare_string",{
        params:{
          a:this.mytext1,
          b:this.mytext2
        }
      }).then(res =>{console.log(res.data)
        var percent = Number(res.data*100).toFixed(5)
        percent+="%"
        this.result = percent
      })
      .catch(err => {
        this.result = "输入不能为空，请重新输入"
         console.log(err)
      })
    },
    update(){

    }

  },
  computed:{

  },

}
</script>

<style>

</style>
