<template lang="pug">
  b-container(fluid="lg")
    b-row.mb-5
      b-col(sm=4 offset-sm=4)
        h1 Registration
    b-form(@submit="submitForm")
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Username:
        b-col(sm=4)
          b-form-input(type="text" v-model="username" required)
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Email:
        b-col(sm=4)
          b-form-input(type="email" v-model="email" required)
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label First Name:
        b-col(sm=4)
          b-form-input(type="text" v-model="firstName" required)
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Last Name:
        b-col(sm=4)
          b-form-input(type="text" v-model="lastName" required)
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Password:
        b-col(sm=4)
          b-form-input(type="password" v-model="password" required)
      b-row.mb-2
        b-col.text-left(sm=2 offset-sm=3)
          label Group:
        b-col(sm=4)
          b-form-select(v-model="group" :options="options" required)
      b-row
        b-col(sm=4 offset-sm=4)
          p.error(v-for="err in errors") {{ err }}
      b-row.mt-3
        b-col(sm=2 offset-sm=5)
          b-button.mr-2(type="submit" variant="primary") Submit
          b-button(type="reset" variant="danger") Reset
</template>

<script>
export default {
  name: 'SignUp',
  data () {
    return {
      username: '',
      email: '',
      firstName: '',
      lastName: '',
      password: '',
      group: null,
      errors: [],
      options: [
        {value: null, text: 'Choose you role', disabled: true},
        {value: 1, text: 'Teacher'},
        {value: 2, text: 'Student'}
      ]
    }
  },
  methods: {
    submitForm (event) {
      this.errors = []
      this.createAccount()
      event.preventDefault()
      this.username = ''
      this.email = ''
      this.firstName = ''
      this.lastName = ''
      this.password = ''
      this.group = this.options[0]
    },
    createAccount () {
      this.$store.dispatch('createUser', {
        username: this.username,
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
        password: this.password,
        groups: [this.group]
      }).then(response => console.log(response))
        .catch(err => {
          for (let key in err.response.data) {
            err.response.data[key].forEach(element => {
              this.errors = [element, ...this.errors]
            })
          }
        })
      console.log()
    }
  }
}

</script>

<style scoped>

</style>
