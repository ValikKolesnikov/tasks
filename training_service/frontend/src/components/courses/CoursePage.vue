<template>
  <b-container fluid="lg">
    <b-row>
      <b-col md="6" offset-md="3">
        <h1>{{course.name}}</h1>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <p>{{course.description}}</p>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <h3>Course task list:</h3>
      </b-col>
    </b-row>
    <b-row v-for="task in course.tasks" v-bind:key="task.id">
      <b-col>
        <p>{{task.position_number}}. {{task.name}}{{task.title}}</p>
      </b-col>
    </b-row>
    <b-row>
      <b-col>
        <b-btn v-on:click="participate()">Join</b-btn>
      </b-col>
    </b-row>
</b-container>
</template>

<script>
export default {
  name: 'CreateCourse',
  beforeCreate () {
    this.$store.dispatch('courses/getCourse', this.$route.params.id)
  },
  computed: {
    course: function () {
      return this.$store.state.courses.course
    }
  },
  methods: {
    participate: function () {
      this.$store.dispatch('accounts/enrollAsStudent', this.$route.params.id)
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
