<template lang="pug">
  b-container(fluid="lg")
    b-row.mb-5
      b-col(sm=4 offset-sm=4)
        h1 Log In
    b-form(@submit="submitForm")
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Username
        b-col(sm=4)
          b-form-input(type="text" v-model="username" required)
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Password
        b-col(sm=4)
          b-form-input(type="password" v-model="password" required)
      b-row
        b-col(sm=2 offset-sm=3)
          p.error(v-for="err in errors") {{ err }}
      b-row.mt-3
        b-col(sm=2 offset-sm=5)
          b-button.mr-2(type="submit" variant="primary") Submit
          b-button(type="reset" variant="danger") Reset
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: '',
      errors: []

    }
  },
  methods: {
    submitForm (event) {
      this.login()
      event.preventDefault()
    },
    login () {
      this.$store.dispatch('login', {
        username: this.username,
        password: this.password
      }).then(response => {
        console.log(this.$store.state.authUser)
        console.log(this.$store.state.isAuth)
        console.log(this.$store.state.jwt)
      })
        .catch(err => {
          for (let key in err.response.data) {
            err.response.data[key].forEach(element => {
              this.errors = [element, ...this.errors]
            })
          }
        })
    }
  }
}

</script>

<style scoped>

</style>
