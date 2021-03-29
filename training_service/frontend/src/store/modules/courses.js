import { Courses } from '../../api/courses'
import { SET_COURSES } from '../mutation-types'

const state = {
  courses: []
}

const getters = {
}

const mutations = {
  [SET_COURSES] (state, courses) {
    state.courses = courses
  }
}

const actions = {
  getList ({commit}) {
    Courses.getList().then(response => commit(SET_COURSES, response.data))
  }
}

export default{
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
