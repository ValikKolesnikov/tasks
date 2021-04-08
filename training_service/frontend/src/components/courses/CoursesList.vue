<template>
  <b-container fluid="lg">
        <b-row v-for="course in courses" v-bind:key="course.id">
            <b-col class="course-block" md=6 offset-md="3">
              <router-link :to="{name: 'coursePage', params: {id: course.id}}">{{course.name}}</router-link>
            </b-col>
        </b-row>
        <b-row class="mt-5">
          <b-col md=12>
            <b-link v-on:click="changePage(prev)">
              <b-icon icon="arrow-left"></b-icon>
            </b-link>
            <span>{{current + 1}} of {{total}}</span>
            <b-link v-on:click="changePage(next)">
              <b-icon icon="arrow-right"></b-icon>
            </b-link>
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
    },
    prev: function () {
      return this.$store.state.courses.prevPage
    },
    next: function () {
      return this.$store.state.courses.nextPage
    },
    current: function () {
      return this.$store.state.courses.currentPage
    },
    total: function () {
      return this.$store.state.courses.totalPages
    }
  },
  methods: {
    changePage: function (url) {
      if (url !== null) {
        this.$store.dispatch('courses/getCourseListPage', url)
      }
    }
  }
}

</script>

<style scoped>
.course-block {
  border-bottom: 1px solid rgba(0,0,0, 0.3);
  padding: 10px;
  font-size: 18px;
}
</style>
