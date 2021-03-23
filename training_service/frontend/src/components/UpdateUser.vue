<template>
  <b-container fluid="lg">
    <b-row class="mb-5">
        <b-col sm="4" offset-sm="4">
            <h1>Update User</h1>
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
            <b-col class="text-left" sm="2" offset-sm="3"><label>Group:</label></b-col>
            <b-col sm="4">
                <b-form-select v-model="group" :options="options" required="required"></b-form-select>
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
  name: 'UpdateUser',
  data () {
    return {
      username: this.$store.state.authUser.username,
      email: this.$store.state.authUser.email,
      firstName: this.$store.state.authUser.firstName,
      lastName: this.$store.state.authUser.lastName,
      group: this.$store.state.authUser.group,
      options: [
        {value: null, text: 'Choose you role', disabled: true},
        {value: 1, text: 'Teacher'},
        {value: 2, text: 'Student'}
      ]
    }
  },
  computed: {
    errors: function () {
      return this.$store.state.errors
    }
  },
  methods: {
    submitForm (event) {
      this.errors = []
      this.updateUser()
      event.preventDefault()
    },
    updateUser () {
      this.setUserUpdateData()
      this.$store.dispatch('updateUser', {
        user: this.$store.state.authUser,
        data: this.setUserUpdateData()
      }).then(response => {
        this.username = ''
        this.email = ''
        this.firstName = ''
        this.lastName = ''
        this.password = ''
        this.group = this.options[0]
      })
        .catch(err => {
          this.$store.dispatch('setErrors', err)
        })
    },
    setUserUpdateData () {
      let data = {}
      if (this.username !== this.$store.state.authUser.username) {
        data['username'] = this.username
      }
      if (this.firstName !== this.$store.state.authUser.firstName) {
        data['firstName'] = this.firstName
      }
      if (this.lastName !== this.$store.state.authUser.lastName) {
        data['lastName'] = this.lastName
      }
      if (this.email !== this.$store.state.authUser.email) {
        data['email'] = this.email
      }
      if (this.group !== this.$store.state.authUser.group) {
        data['group'] = this.group
      }
      return data
    }
  }
}

</script>

<style scoped>

</style>
