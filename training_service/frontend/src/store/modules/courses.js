import { Courses } from '../../api/courses'
import { SET_COURSES, SET_COURSE } from '../mutation-types'
import axios from 'axios'

const state = {
  courses: [],
  nextPage: null,
  prevPage: null,
  totalPages: null,
  currentPage: null,
  course: {}
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
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
