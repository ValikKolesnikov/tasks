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
    this.$store.dispatch('accounts/getUser',
      {token: localStorage.getItem('token')
      })
    this.$store.state.accounts.errors = []
  },
  data () {
    return {
      userData: {}
    }
  },
  computed: {
    errors: function () {
      return this.$store.state.accounts.errors
    },
    username: {
      get: function () {
        return this.$store.state.accounts.authUser.username
      },
      set: function (username) {
        this.userData['username'] = username
      }
    },
    email: {
      get: function () {
        return this.$store.state.accounts.authUser.email
      },
      set: function (email) {
        this.userData['email'] = email
      }
    },
    firstName: {
      get: function () {
        return this.$store.state.accounts.authUser.first_name
      },
      set: function (firstName) {
        this.userData['first_name'] = firstName
      }
    },
    lastName: {
      get: function () {
        return this.$store.state.accounts.authUser.last_name
      },
      set: function (lastName) {
        this.userData['last_name'] = lastName
      }
    }
  },
  methods: {
    submitForm (event) {
      this.updateUser()
      event.preventDefault()
    },
    updateUser () {
      this.$store.dispatch('accounts/updateUser', {
        user: this.$store.state.accounts.authUser,
        data: this.setUserUpdateData()
      }).then(response => {
        this.username = ''
        this.email = ''
        this.firstName = ''
        this.lastName = ''
        this.password = ''
      })
        .catch(err => {
          this.$store.dispatch('accounts/setErrors', err)
        })
    },
    setUserUpdateData () {
      let data = {}
      if (this.userData['username'] !== this.$store.state.accounts.authUser.username) {
        data['username'] = this.userData['username']
      }
      if (this.userData['first_name'] !== this.$store.state.accounts.authUser.first_name) {
        data['first_name'] = this.userData['first_name']
      }
      if (this.userData['last_name'] !== this.$store.state.accounts.authUser.last_name) {
        data['last_name'] = this.userData['last_name']
      }
      if (this.userData['email'] !== this.$store.state.accounts.authUser.email) {
        data['email'] = this.userData['email']
      }
      return data
    }
  }
}

</script>

<style scoped>

</style>
