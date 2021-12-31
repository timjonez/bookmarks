import axios from 'axios'
import { BASEURL } from '../constants'

export const state = () => ({
  auth: {
    userLoggedIn: false,
    showAuthModal: false,
    token: null
  },
  errors: [
    {
      title: 'Invalid credentials',
      details: 'The email/password that you provided are invalid. Please try again',
      seen: false
    }
  ],
  bookmarks: []
})

export const actions = {
  async login (context, payload) {
    try {
      const userCred = await axios.post(
        BASEURL + '/account/login/',
        {
          email: payload.target.email.value,
          password: payload.target.password.value
        }
      )
      context.commit('setToken', userCred.data.token)
    } catch (error) {
      console.log(error.response.data.detail)
    }
  },
  editBookmark (context, payload) {
    context.commit('editBookmark', payload)
  },
  saveBookmark (context, payload) {
    context.commit('saveBookmark', payload.target.name)
  },
  deleteBookmark (context, payload) {
    console.log(payload)
  }
}

export const mutations = {
  editBookmark (state, bookmark) {
    const bookmarkIndex = state.bookmarks.findIndex(item => item.id === bookmark.id)
    state.bookmarks[bookmarkIndex].editing = !state.bookmarks[bookmarkIndex].editing
  },
  saveBookmark (state, bookmark) {
    console.log(bookmark)
  },
  setToken (state, token) {
    state.auth.token = token
    state.auth.userLoggedIn = true
  }
}
