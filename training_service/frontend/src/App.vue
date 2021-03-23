<template lang="pug">
  div#app
    b-container(fluid="lg")
      b-row
        b-col(lg=6)
          b-nav
            b-nav-item
              b-button
                router-link(to="/") Home
            b-nav-item
              b-button Course List
        b-col(lg=3 offset-lg=3)
          b-nav
            b-nav-item
              b-button
                router-link(to="/login") Log in
            b-nav-item
              b-button
                router-link(to="/sign-up") Sing up
            b-nav-item
              b-button
                router-link(to="/update") Update
    router-view
</template>

<script>
import SignUp from './components/SignUp'
import Login from './components/Login'
import UpdateUser from './components/UpdateUser'

export default {
  name: 'App',
  components: {
    SignUp,
    Login,
    UpdateUser
  }
}
</script>

<style>
body{
  margin: 0;
  padding: 0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.error{
  color: red;
  margin: 0;
  padding: 0;
}
</style>
