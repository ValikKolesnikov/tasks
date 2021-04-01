import { Courses } from '../../api/courses'
import { SET_COURSES } from '../mutation-types'
import axios from 'axios'

const state = {
  courses: [],
  nextPage: null,
  prevPage: null,
  totalPages: null,
  currentPage: null
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
  }
}

const actions = {
  getList ({commit}) {
    Courses.getList().then(response => commit(SET_COURSES, response.data))
  },
  getCourseListPage ({commit}, url) {
    axios.get(url).then(response => commit(SET_COURSES, response.data))
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
