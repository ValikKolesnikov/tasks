<template>
  <b-container fluid="lg">
    <b-row>
      <b-col md="6" offset-md="3">
        <h1>{{user.username}}</h1>
        </b-col>
    </b-row>
    <b-row v-for="participation in this.participations" v-bind:key="participation.id">
      <b-col md="6" offset-md="3">
        <h2>{{participation.course.name}}</h2>
      </b-col>
    </b-row>
</b-container>
</template>

<script>

export default {
  name: 'UserPage',
  beforeCreate () {
    this.$store.dispatch('accounts/getUser',
      {token: localStorage.getItem('token')
      })
  },
  mounted () {
    this.$store.dispatch('accounts/getParticipations', this.user)
  },
  computed: {
    user: function () {
      return this.$store.state.accounts.authUser
    },
    participations: function () {
      return this.$store.state.accounts.participations
    }
  },
  methods: {}
}

</script>

<style scoped>

</style>
