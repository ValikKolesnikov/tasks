import { Courses } from '../../api/courses'
import { SET_COURSES, SET_COURSE, GET_COURSE_DETAILS } from '../mutation-types'
import axios from 'axios'

const state = {
  courses: [],
  nextPage: null,
  prevPage: null,
  totalPages: null,
  currentPage: null,
  course: {},
  tasks: [],
  courseProgress: {}
}

const getters = {
}

const mutations = {
  [SET_COURSES] (state, result) {
    state.courses = result.results
    state.nextPage = result.links.next
    state.prevPage = result.links.previous
    state.totalPages = result.total_pages
    state.currentPage = result.current_page
  },
  [SET_COURSE] (state, course) {
    state.course = course
  },
  [GET_COURSE_DETAILS] (state, data) {
    state.course = data.course
    state.courseProgress = data.course_progress
    state.course = data.tasks
  }
}

const actions = {
  getList ({commit}) {
    Courses.getList().then(response => commit(SET_COURSES, response.data))
  },
  getCourseListPage ({commit}, url) {
    axios.get(url).then(response => commit(SET_COURSES, response.data))
  },
  getCourse ({commit}, id) {
    return Courses.getCourse(id).then(response => commit(SET_COURSE, response.data))
  },
  getCourseDetail ({commit}, id) {
    return Courses.getCourseDetail(id).then(response => commit(GET_COURSE_DETAILS, response.data))
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
