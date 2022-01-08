import axios from 'axios'
import Vue from 'vue'
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

export const getters = {
  getBookmarkById: (state) => {
    return (id) => {
      return state.bookmarks.find(item => item.id === id)
    }
  }
}

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
  appendBookmark ({ commit }, payload) {
    commit('addBookmark', payload)
  },
  async getBookmark ({ commit, state }, bookmarkId) {
    try {
      await axios.get(
        BASEURL + `/bookmark/${bookmarkId}/`,
        {
          headers: { Authorization: state.auth.token }
        }
      )
      commit('getBookmark', bookmarkId)
    } catch (error) {
      commit('addMessage', {
        id: null,
        title: 'Error',
        details: error.response.data.detail,
        type: 'error'
      })
    }
  },
  async addBookmark ({ commit, state }, payload) {
    try {
      const { data } = await axios.post(
        BASEURL + '/bookmark/create/',
        payload,
        {
          headers: { Authorization: state.auth.token }
        }
      )
      commit('addBookmark', data)
      commit('addMessage', {
        id: null,
        title: 'Success',
        details: 'You have successfully added a bookmark',
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
  editBookmark (context, payload) {
    context.commit('editBookmark', payload)
  },
  async updateBookmark ({ commit, state }, payload) {
    try {
      const { data } = await axios.patch(
        BASEURL + `/bookmark/${payload.id}/`,
        payload,
        {
          headers: { Authorization: state.auth.token }
        }
      )
      commit('updateBookmark', data)
      commit('addMessage', {
        id: null,
        title: 'Success',
        details: 'You have successfully updated a bookmark',
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
  async deleteBookmark ({ commit, state }, payload) {
    try {
      await axios.delete(
        BASEURL + `/bookmark/${payload.id}/`,
        {
          headers: { Authorization: state.auth.token }
        }
      )
      commit('deleteBookmark', payload)
      commit('addMessage', {
        id: null,
        title: 'Success',
        details: 'You have successfully deleted a bookmark',
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
  removeAllBookmarks ({ commit }) {
    commit('removeAllBookmarks')
  }
}

export const mutations = {
  updateBookmark (state, bookmark) {
    const bookmarkIndex = state.bookmarks.findIndex(item => item.id === bookmark.id)
    Vue.set(state.bookmarks, bookmarkIndex, {
      ...bookmark,
      editing: false
    })
  },
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
  deleteBookmark (state, bookmark) {
    const bookmarkIndex = state.bookmarks.findIndex(item => item.id === bookmark.id)
    state.bookmarks.splice(bookmarkIndex, 1)
  },
  removeAllBookmarks (state) {
    state.bookmarks = []
  },
  setToken (state, token) {
    state.auth.token = token
    state.auth.userLoggedIn = true
  }
}
