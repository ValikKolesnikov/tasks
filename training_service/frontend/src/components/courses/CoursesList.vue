<template>
  <b-container fluid="lg">
        <b-row v-for="course in courses" v-bind:key="course.id">
            <b-col md=3>
                {{course.name}}
            </b-col>
            <b-col md=2>
                <b-btn>Join</b-btn>
            </b-col>
        </b-row>
</b-container>
</template>

<script>

export default {
  name: 'CreateCourse',
  beforeCreate () {
    this.$store.dispatch('courses/getList')
  },
  computed: {
    courses: function () {
      return this.$store.state.courses.courses
    }
  }
}

</script>

<style scoped>

</style>
