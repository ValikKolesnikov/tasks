<template>
  <b-container fluid="lg">
    <b-row class="mb-5">
        <b-col sm="4" offset-sm="4">
            <h1>Registration</h1>
        </b-col>
    </b-row>
    <b-form @submit="submitForm">
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Username:</label></b-col>
            <b-col sm="4">
                <b-form-input type="text" v-model="username" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Email:</label></b-col>
            <b-col sm="4">
                <b-form-input type="email" v-model="email" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>First Name:</label></b-col>
            <b-col sm="4">
                <b-form-input type="text" v-model="firstName" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Last Name:</label></b-col>
            <b-col sm="4">
                <b-form-input type="text" v-model="lastName" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Password:</label></b-col>
            <b-col sm="4">
                <b-form-input type="password" v-model="password" required="required"></b-form-input>
            </b-col>
        </b-row>
        <b-row class="mb-2">
            <b-col class="text-left" sm="2" offset-sm="3"><label>Group:</label></b-col>
            <b-col sm="4">
                <b-form-select v-model="group" required="required">
                    <b-form-select-option :key="group_item.id" v-for="group_item in this.$store.state.accounts.groups" :value="group_item.id">{{ group_item.name }}</b-form-select-option>
                </b-form-select>
            </b-col>
        </b-row>
        <b-row>
            <b-col sm="4" offset-sm="4">
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
  name: 'SignUp',
  beforeCreate () {
    this.$store.state.accounts.errors = []
    this.$store.dispatch('accounts/getGroups')
  },
  data () {
    return {
      username: '',
      email: '',
      firstName: '',
      lastName: '',
      password: '',
      group: null
    }
  },
  computed: {
    errors: function () {
      return this.$store.state.accounts.errors
    }
  },
  methods: {
    submitForm (event) {
      this.$store.state.accounts.errors = []
      this.createAccount()
    },
    createAccount () {
      this.$store.dispatch('accounts/createUser', {
        username: this.username,
        email: this.email,
        first_name: this.firstName,
        last_name: this.lastName,
        password: this.password,
        groups: [this.group]
      }
      ).then(response => {
        this.username = ''
        this.email = ''
        this.firstName = ''
        this.lastName = ''
        this.password = ''
        this.group = ''
        this.$router.push('login')
      }).catch(err => {
        console.log(err)
        this.$store.dispatch('accounts/setErrors', err)
      })
    }
  }
}

</script>

<style scoped>

</style>
