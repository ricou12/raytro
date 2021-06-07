import Feedback from '@/models/Feedback'
import store from '@/store'

const API_ROOT_PATH = process.env.VUE_APP_API_ROOT_PATH

/**
 * Cette fonction permet de vérifier si les informations de connexion sont
 * correctes auprès du serveur et de récupérer un token d'identification
 * si tout s'est bien passé (JWT stateless).
 *
 * @param login   Identifiant de l'utilisateur
 * @param password
 */
function login (login: string, password: string): Promise<JSON|any> {
  return new Promise((resolve, reject) => {
    if (login.length > 0 && password.length > 0) {
      fetch(API_ROOT_PATH + 'login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', },
        body: JSON.stringify({
          login: login,
          password: password,
        }),
      })
        .then(response => response.json())
        .then(data => {
          if (data.status === 'success') {
            resolve(data)
          }
          else {
            reject(data)
          }
        })
        .catch(error => {
          reject(error)
        })
    }
    else {
      reject(new Error('Le login et le mot de passe doivent être non nuls'))
    }
  })
}

function signup (firstName: string, login: string, password: string): Promise<JSON|any> {
  return fetch(API_ROOT_PATH + '/signup', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', },
    body: JSON.stringify({
      login, firstName, password,
    }),
  })
    .then(response => response.json())
    // .then(data => {
    //   if (data.status !== 'success') {
    //     throw (data)
    //   }
    // })
    // .catch(error => {
    //   throw (error)
    // })
}

function sendFeedback (feedback: Feedback): Promise<JSON|any> {
  const myHeaders = new Headers()
  myHeaders.append('Content-Type', 'application/json')
  myHeaders.append('Authorization', `Bearer ${store.getters.token}`)
  return fetch(API_ROOT_PATH + '/feedback', {
    method: 'POST',
    headers: myHeaders,
    body: JSON.stringify(feedback),
  })
    .then(response => response.json())
}

function getFeedbacks (year: number|any, week: number|any): Promise<Array<any>> {
  const myHeaders = new Headers()
  myHeaders.append('Content-Type', 'application/json')
  myHeaders.append('Authorization', `Bearer ${store.getters.token}`)
  return fetch(`${API_ROOT_PATH}feedback/${year}/${week}`, {
    method: 'GET',
    headers: myHeaders,
  })
    .then(response => response.json())
}

export {
  API_ROOT_PATH,
  login,
  signup,
  sendFeedback,
  getFeedbacks,
}
