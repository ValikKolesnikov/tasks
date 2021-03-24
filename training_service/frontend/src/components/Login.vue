<template>
  <b-container fluid="lg">
    <b-row class="mb-5">
        <b-col sm="4" offset-sm="4">
            <h1>Log In</h1>
        </b-col>
    </b-row>
    <b-form @submit="submitForm">
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Username</label></b-col>
            <b-col sm="4">
                <b-form-input type="text" v-model="username" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Password</label></b-col>
            <b-col sm="4">
                <b-form-input type="password" v-model="password" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row>
            <b-col sm="2" offset-sm="3">
                <p class="error" :key="err" v-for="err in errors">{{ err }}</p>
            </b-col>
        </b-row>
        <b-row class="mt-3">
            <b-col sm="2" offset-sm="5">
                <b-button class="mr-2" type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-col>
        </b-row>
    </b-form>
</b-container>
</template>

<script>

export default {
  name: 'Login',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    errors: function () {
      return this.$store.state.errors
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
      }
      ).then(response => {})
        .catch(err => {
          this.$store.dispatch('setErrors', err)
        })
    }
  }
}

</script>

<style scoped>

</style>
