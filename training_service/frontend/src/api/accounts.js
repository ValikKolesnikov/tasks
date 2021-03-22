import {HTTP} from './common'

export const Accounts = {
  create (config) {
    return HTTP.post('users/', config).then(response => {
      return response.data
    })
  },
  authUser (config) {
    return HTTP.post('tokens/obtain/', config).then(response => {
      return response.data
    })
  }
}
