import HTTP from './common'

export const Accounts = {
  create (data) {
    return HTTP.post('accounts/users/', data)
  },
  authUser (data) {
    return HTTP.post('accounts/tokens/obtain/', data)
  },
  update (user, data, config) {
    return HTTP.patch(`accounts/users/${user.id}/`, data, config)
  },
  getGroups () {
    return HTTP.get('accounts/groups/')
  },
  getUser (data, config) {
    return HTTP.post(`accounts/users/current/`, data, config)
  },
  getParticipations (user, config) {
    return HTTP.get(`accounts/users/${user.id}/participation_list/`, config)
  },
  participate (courseId, config) {
    return HTTP.post(`courses/${courseId}/participate/`, {}, config)
  }
}
