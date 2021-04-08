import HTTP from './common'

export const Accounts = {

  createTeacher (data) {
    return HTTP.post('accounts/users/teacher_create/', data)
  },
  createStudent (data) {
    return HTTP.post('accounts/users/student_create/', data)
  },
  authUser (data) {
    return HTTP.post('accounts/tokens/obtain/', data)
  },
  update (user, data, config) {
    return HTTP.patch(`accounts/users/${user.id}/`, data, config)
  },
  getUser (data, config) {
    return HTTP.post(`accounts/users/current/`, data, config)
  },
  getParticipations (user, config) {
    return HTTP.get(`accounts/participations/`, config)
  },
  enrollAsStudent (courseId, config) {
    return HTTP.post(`courses/${courseId}/enroll_as_student/`, {}, config)
  }
}
