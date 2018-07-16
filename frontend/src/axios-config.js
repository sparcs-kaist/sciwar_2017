import axios from 'axios'

/* Set header name */
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
// axios.xsrfCookieName = 'XSRF-TOKEN';
// axios.xsrfHeaderName = 'X-XSRF-Token';

/* Get token from cookie (from Django doc) */
function getCookie (name) {
  let cookieValue = null
  if (document.cookie && document.cookie !== '') {
    let cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim()
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))
        break
      }
    }
  }
  return cookieValue
}

const cookieValue = getCookie('csrftoken')

/* Set up an instance and its interceptor */
const instance = axios.create({
  // baseURL: 'http://localhost:8000/api',
  headers: {
    common: {
      'X-CSRFToken': cookieValue
    }
  }
})

/* export default */
export default instance
