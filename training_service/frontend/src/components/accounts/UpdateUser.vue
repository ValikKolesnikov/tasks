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
  name: 'UpdateUser',
  beforeCreate () {
    this.$store.dispatch('accounts/getGroups')
    this.$store.dispatch('accounts/getUser',
      {token: localStorage.getItem('token')
      })
    this.$store.state.accounts.errors = []
  },
  computed: {
    errors: function () {
      return this.$store.state.accounts.errors
    },
    username: function () {
      return this.$store.state.accounts.authUser.username
    },
    email: function () {
      return this.$store.state.accounts.authUser.email
    },
    firstName: function () {
      return this.$store.state.accounts.authUser.firstName
    },
    lastName: function () {
      return this.$store.state.accounts.authUser.lastName
    },
    group: function () {
      return this.$store.state.accounts.authUser.group
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
      this.$store.dispatch('accounts/updateUser', {
        user: this.$store.state.accounts.authUser,
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
          this.$store.dispatch('accounts/setErrors', err)
        })
    },
    setUserUpdateData () {
      let data = {}
      if (this.username !== this.$store.state.accounts.authUser.username) {
        data['username'] = this.username
      }
      if (this.firstName !== this.$store.state.accounts.authUser.firstName) {
        data['firstName'] = this.firstName
      }
      if (this.lastName !== this.$store.state.accounts.authUser.lastName) {
        data['lastName'] = this.lastName
      }
      if (this.email !== this.$store.state.accounts.authUser.email) {
        data['email'] = this.email
      }
      if (this.group !== this.$store.state.accounts.authUser.group) {
        data['group'] = this.group
      }
      return data
    }
  }
}

</script>

<style scoped>

</style>
