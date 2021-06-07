import { createStore, } from 'vuex'

export default createStore({
  state: {
    isLoggedIn: false,
    token: null,
    firstName: 'bobbs',
    email: null,
  },

  getters: {
    isLoggedIn (state) { return state.isLoggedIn },
    token (state) { return state.token },
    firstName (state) { return state.firstName },
    email (state) { return state.email },
  },

  mutations: {
    FIRST_NAME (state, value) {
      state.firstName = value
    },
    IS_LOGGED_IN (state, value) {
      state.isLoggedIn = value
    },
    TOKEN (state, value) {
      state.token = value
    },
    EMAIL (state, value) {
      state.email = value
    },
  },

  actions: {
  },
  modules: {
  },
})
