<template>
  <div id="app">
    <b-container fluid="lg">
        <b-row>
            <b-col lg="6">
                <b-nav>
                    <b-nav-item>
                        <b-button>
                            <router-link to="/">Home</router-link>
                        </b-button>
                    </b-nav-item>
                    <b-nav-item>
                        <router-link to="/courses"><b-button>Courses</b-button></router-link>
                    </b-nav-item>
                </b-nav>
            </b-col>
            <b-col lg="3" offset-lg="3">
                <b-nav>
                    <b-nav-item>
                        <b-button>
                            <router-link to="/login">Log in</router-link>
                        </b-button>
                    </b-nav-item>
                    <b-nav-item>
                        <b-button>
                            <router-link to="/sign-up">Sing up</router-link>
                        </b-button>
                    </b-nav-item>
                    <b-nav-item>
                        <b-button>
                            <router-link to="/update">Update</router-link>
                        </b-button>
                    </b-nav-item>
                </b-nav>
            </b-col>
        </b-row>
    </b-container>
    <router-view></router-view>
</div>
</template>

<script>
import SignUp from './components/accounts/SignUp'
import Login from './components/accounts/Login'
import UpdateUser from './components/accounts/UpdateUser'
import CoursesList from './components/courses/CoursesList'

export default {
  name: 'App',
  components: {
    SignUp,
    Login,
    UpdateUser,
    CoursesList
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
