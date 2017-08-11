<template>
  <div id="cheermessage">
    <div class="info noto-sans">
      <p class="info-head">응원의 메세지</p>
      <img src="/static/images/message.png"  class="info-img">
      <p class="info-parag">어어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌어쩌구쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구어쩌구</p>
    </div>
    <table class="board noto-sans">
      <thead>
        <tr>
          <th>경기</th>
          <th>내용</th>
          <th>팀</th>
        </tr>
      </thead>
      <tbody v-for="message in messages">
        <tr>
          <td>{{ message.fields.event }}</td>
          <td>{{ message.fields.content }}</td>
          <td>{{ message.fields.school }}</td>
        </tr>
      </tbody>
    </table>
    <ul class="paginator">
      
    </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'cheermessage',
  data () {
    return {
      messages: []
    }
  },
  created () {
    this.$http.get('/api/cheermessage')
      .then((response) => {
        this.messages = JSON.parse(response.data)
        console.log(this.messages.length)
      })
    var len = this.messages.length
  },
  methods: {
  }
}
</script>

<style>
.info{
}

.info-head{ 
  font-size: 64px;
  font-weight: 700;
  padding-bottom: 10px;
  margin-bottom: 1.5rem;
}

.info-img{
  float: left;
  margin-top: -50px;
  margin-left: -30px;
  margin-bottom: -100px;
  padding-bottom: -100px;
  width: 350px;
}

.info-parag{
  display: inline;
  font-size: 32px;
}

.board{
  margin-top: 50px;
  margin-left: 10px;
  margin-right: 10px;
}  

.board > thead {
  font-size: 28px;
}
</style>
