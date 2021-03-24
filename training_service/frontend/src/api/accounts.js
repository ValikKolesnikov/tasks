import {HTTP} from './common'

export const Accounts = {
  create (data, config) {
    return HTTP.post('users/', data, config)
  },
  authUser (data) {
    return HTTP.post('tokens/obtain/', data)
  },
  update (user, data, config) {
    return HTTP.patch(`users/${user.id}`, data, config)
  },
  getGroups () {
    return HTTP.get('groups/')
  }

}
