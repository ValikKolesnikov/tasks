import HTTP from './common'

export const Courses = {
  create (data, config) {
    return HTTP.post('courses/', data, config)
  },
  update (course, data, config) {
    return HTTP.patch(`courses/${course.id}`, data, config)
  },
  getList () {
    return HTTP.get(`courses/`)
  },
  getCourse (id) {
    return HTTP.get(`courses/${id}/`)
  }
}
