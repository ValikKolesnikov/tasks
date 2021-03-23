import {HTTP} from './common'

export const Accounts = {
  create (config) {
    return HTTP.post('users/', config)
  },
  authUser (config) {
    return HTTP.post('tokens/obtain/', config)
  },
  update (user, config) {
    return HTTP.patch(`users/${user.id}`)
  },
  getGroups () {
    return HTTP.get('groups/')
  }

}
