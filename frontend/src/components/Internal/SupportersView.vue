<template>
  <div class="supporters-view noto-sans">
    <div class="head">서포터즈 조회하기</div>
    <div class="supporter-reg">
      <table class="team-info">
        <tr>
          <th>Team name</th>
          <td>{{ supporterTeam.fields.name }}</td>
        </tr>
        <tr>
          <th>Members</th>
          <td class="supporter-list">
            <ul v-for="member in members" class="supporter-info">{{ member.fields.name }} {{ showLeader(member.fields.is_leader) }}
              <li>{{ sex[member.fields.sex] }}</li>
              <li class="student-id">{{ member.fields.student_id }}</li>
              <li>{{ member.fields.department }}</li>
              <li>{{ member.fields.contact }}</li>
              <li>Size {{ size[member.fields.size] }}</li>
            </ul>
          </td>
        </tr>
      </table>
      <div class="link-container">
        <router-link :to="{ name: 'supporters_check' }" class="link link1">목록으로</router-link>
        <router-link :to="{ name: 'supporters_check' }" class="link2">
          <button class="link" v-on:click="del">삭제하기</button>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'supporters_view',
  data () {
    return {
      theRightPassword: '',
      certified: false,
      supporter: [],
      size: ['80', '85', '90', '95', '100', '105', '110'],
      sex: ['남', '여'],
      supporterTeam: {},
      members: []
    }
  },
  created () {
    let uri = '/api/supporters/complete/' + this.$route.params.id + '/'
    this.$http.get(uri)
      .then((response) => {
        this.supporterTeam = JSON.parse(response.data['supporter_team'])[0]
        this.members = JSON.parse(response.data['members'])
        for (let i = 0; i < this.members.length; i++) {
          if (this.members[i].fields.sex === 1 && this.members[i].fields.is_leader) this.currentLeaderF = i + 1
          if (this.members[i].fields.sex === 0 && this.members[i].fields.is_leader) this.currentLeaderM = i + 1
        }
      })
  },
  methods: {
    del: function () {
      this.$http.delete('/api/supporters/' + this.$route.params.id + '/')
        .then((response) => {
          console.log('successful')
        })
    },
    showLeader: function (bool) {
      if (bool) return '/ 조장'
      return ''
    }
  }
}

</script>

<style scoped>
.head {
  font-size: 64px;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.classified {
  display: block;
  font-size: 28px;
}

.classified > input {
  font-size: 20px;
}

.classified > button {
  background-color: #555555;
  text-align: center;
  font-size: 20px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}

.team-info > tr {
  height: 30px;
}

.team-info > tr > th {
  font-size: 32px;
  width: 230px;
}

.team-info > tr > td {
  font-size: 28px;
}

.supporter-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

.supporter-info {
  border-radius: 10px;
  background-color: #efefef;
  margin-right: 10px;
  margin-top: 10px;
  width: 150px;
  padding: 5px 9px 5px 9px;
  text-align: center;
}

.supporter-info > li {
  font-size: 20px;
  font-weight: 300;
  margin: 0 auto;
}

.link {
  background-color: #555555;
  text-align: center;
  font-size: 22px;
  border: none;
  color: white;
  cursor: pointer;
  padding: 5px 11px;
}

.link-container {
  margin-top: 20px;
}

.link1 {
  float: left;
}

.link2 {
  float: right;
}


.team-info > tr {
  height: 30px;
}

.team-info > tr > th {
  font-size: 32px;
  width: 230px;
}

.team-info > tr > td {
  font-size: 28px;
}

.supporter-list {
   display: flex;
   flex-direction: row;
   flex-wrap: wrap;
 }

 .supporter-info {
   border-radius: 10px;
   background-color: #efefef;
   margin-right: 10px;
   margin-top: 10px;
   width: 200px;
   padding: 10px 10px 10px 10px;
   text-align: center;
   font-size: 28px;
 }

 .supporter-info > li {
   font-size: 20px;
   font-weight: 300;
   margin: 0 auto;
 }

</style>
