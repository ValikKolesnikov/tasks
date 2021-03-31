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
      set: function () {
        this.userData['username'] = this.username
      }
    },
    email: {
      get: function () {
        return this.$store.state.accounts.authUser.email
      },
      set: function () {
        this.userData['email'] = this.email
      }
    },
    firstName: {
      get: function () {
        return this.$store.state.accounts.authUser.first_name
      },
      set: function () {
        this.userData['first_name'] = this.firstName
      }
    },
    lastName: {
      get: function () {
        return this.$store.state.accounts.authUser.last_name
      },
      set: function () {
        this.userData['last_name'] = this.lastName
      }
    },
    group: {
      get: function () {
        return this.$store.state.accounts.authUser.group
      },
      set: function () {
        this.userData['groups'] = [this.group]
      }
    }
  },
  methods: {
    submitForm (event) {
      this.updateUser()
      event.preventDefault()
    },
    updateUser () {
      console.log(this.$store.state.accounts.authUser)
      this.$store.dispatch('accounts/updateUser', {
        user: {
          id: 1
        },
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
          console.log(err)
          this.$store.dispatch('accounts/setErrors', err)
        })
    },
    setUserUpdateData () {
      let data = {}
      if (this.userData['username'] !== this.$store.state.accounts.authUser.username) {
        data['username'] = this.username
      }
      if (this.userData['first_name'] !== this.$store.state.accounts.authUser.first_name) {
        data['first_name'] = this.firstName
      }
      if (this.userData['last_name'] !== this.$store.state.accounts.authUser.last_name) {
        data['last_name'] = this.lastName
      }
      if (this.userData['email'] !== this.$store.state.accounts.authUser.email) {
        data['email'] = this.email
      }
      if (this.userData['groups'] !== this.$store.state.accounts.authUser.group) {
        data['groups'] = this.group
      }
      return data
    }
  }
}

</script>

<style scoped>

</style>
