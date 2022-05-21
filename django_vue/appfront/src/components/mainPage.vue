<template>
  <div class="main">
    <div class="container containerHeight">
      <div class="row h-100">
        <div class="col-9 h-100 row pt-4 text-white">
          <div class="col-xl-4 col-md-6 col-12" v-for="item in court">
            <img class="img-fluid courtImg pb-5" :src="getImgUrl(item)" />
          </div>
          <div>
            <div class="fs-2 px-5">正在使用</div>
            <div class="fs-2 px-5">無人使用</div>
          </div>
        </div>
        <div class="col-3 h-100 d-flex flex-column px-5">
          <div class="text-white mt-5 mb-4">
            <div class="fs-1">{{ headcount }}</div>
            <div class="fs-5">及時人數</div>
          </div>
          <div class="text-white mb-4">
            <div class="fs-1">{{ enviroment.temperature }}</div>
            <div class="fs-5">溫度</div>
          </div>
          <div class="text-white">
            <div class="fs-1 ">{{ enviroment.humidity }}</div>
            <div class="fs-5">濕度</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.main {
  background-color: #01161e;
}
.containerHeight {
  height: 90vh;
}
.courtImg {
  padding: 0px 30px;
}
</style>

<script>
import axios from 'axios'

export default {
  data: function () {
    return {
      court: [1, 2, 0, 3, 2, 4],
      headcount: 2500,
      enviroment: {
        temperature: 25,
        humidity: '80%'
      }
    }
  },
  methods: {
    getImgUrl: function (courtIndex) {
      var images = require.context('../assets/', false, /\.png$/)
      return images('./court' + courtIndex + '.png')
    }
  },
  mounted () {
    axios
      .get('https://www.runoob.com/try/ajax/json_demo.json')
      .then(response => (this.info = response))
      .catch(function (error) {
        // 请求失败处理
        console.log(error)
      })
  }
}
</script>
