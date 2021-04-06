import axios from 'axios'

const HTTP = axios.create({baseURL: 'http://localhost:8000/api/v1/'})

HTTP.interceptors.request.use(req => {
  req.headers.authorization = 'Bearer '.concat(localStorage.getItem('token'))
  return req
})

export default HTTP
