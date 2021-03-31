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
  [SET_COURSES] (state, {links, currentPage, totalPages, results}) {
    state.courses = results
    state.nextPage = links.next
    state.prevPage = links.previous
    state.totalPages = totalPages
    state.currentPage = currentPage
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
