<template>
  <b-container fluid="lg">

</b-container>
</template>

<script>
export default {
  name: 'CourseClassRoom',
  beforeCreate () {
    this.$store.dispatch('courses/getList')
  },
  computed: {
    course: function () {
      return this.$store.state.courses.course
    }
  },
  methods: {
  }
}

</script>

<style scoped>
</style>
