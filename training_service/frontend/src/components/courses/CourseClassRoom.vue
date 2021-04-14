<template>
  <b-container fluid="lg">
    <b-row>
      <b-col md="6" offset-md="3">
        {{course.name}}
      </b-col>
    </b-row>
</b-container>
</template>

<script>
export default {
  name: 'CourseClassRoom',
  beforeCreate () {
    this.$store.dispatch('courses/getCourseDetail', this.$route.params.id)
  },
  computed: {
    course: function () {
      return this.$store.state.courses.course
    },
    courseProgress: function () {
      return this.$store.state.courses.courseProgress
    },
    tasks: function () {
      return this.$store.state.courses.tasks
    }
  },
  methods: {
  }
}

</script>

<style scoped>
</style>
