import axios from 'axios'
import { BASEURL } from '../constants'

export const state = () => ({
  messageModalOpen: false,
  auth: {
    userLoggedIn: false,
    showAuthModal: false,
    token: null
  },
  messages: [],
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
      context.commit('addMessage', {
        id: null,
        title: 'Successful Login',
        details: 'You have successfully logged in!',
        type: 'success'
      })
    } catch (error) {
      context.commit('addMessage', {
        id: null,
        title: 'Error',
        details: error.response.data.detail,
        type: 'error'
      })
    }
  },
  async createUser ({ commit }, payload) {
    try {
      await axios.post(
        BASEURL + '/account/create/',
        {
          email: payload.email,
          password: payload.password
        }
      )
      commit('addMessage', {
        id: null,
        title: 'Successfully Created Account',
        details: 'You have successfully create an account. Login to get started',
        type: 'success'
      })
    } catch (error) {
      commit('addMessage', {
        id: null,
        title: 'Error',
        details: error.response.data.detail,
        type: 'error'
      })
    }
  },
  removeMessage ({ commit, state }, payload) {
    commit('removeMessage', payload)
  },
  addMessage ({ commit }, message) {
    commit('addMessage', message)
  },
  addBookmark ({ commit }, payload) {
    commit('addBookmark', payload)
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
  addMessage (state, message) {
    message.id = state.messages.length + 1
    state.messages.push(message)
    state.messageModalOpen = true
  },
  removeMessage (state, messageId) {
    state.messages = state.messages.filter((msg) => {
      return msg.id !== messageId
    })
    if (state.messages.length === 0) {
      state.messageModalOpen = false
    }
  },
  addBookmark (state, bookmark) {
    state.bookmarks.push(bookmark)
  },
  saveBookmark (state, bookmark) {
    console.log(bookmark)
  },
  setToken (state, token) {
    state.auth.token = token
    state.auth.userLoggedIn = true
  }
}
