<template>
  <div class="noto-sans">
    <div class="head">응원의 한마디 남기기</div>
    <div class="first-form">
      <p class="question">하실 말씀을 적어주세요!&nbsp; &nbsp; &nbsp; {{ message.length }}자/140자</p>
      <textarea v-model="message"></textarea>
    </div>
    <div class="second-form">
      <p class="question">응원하는 학교</p>
      <select id="school-selector">
        <option value="1" selected>KAIST</option>
        <option value="2">POSTECH</option>
      </select>
    </div>
    <div class="third-form">
      <p class="question">응원하는 경기</p>
      <select id="event-selector">
        <option value="1" selected>축구</option>
        <option value="7">야구</option>
      </select>
    </div>
    <button class="submit-button" v-on:click="submit()">쓰기</button>
  </div>
</template>

<script>
export default {
  name: 'cheermessage-write',
  data () {
    return {
      message: ''
    }
  },
  created () {
  },
  methods: {
  }
}
</script>

<style>
.head{
   font-size: 64px;
   font-weight: 700;
   padding-bottom: 10px;
   margin-bottom: 1.5rem;
 }
</style>
