<template>
  <div>
    <h1>Home Page</h1>
    <bookmark-item v-for="bookmark in $store.state.bookmarks" :key="bookmark.id" :bookmark="bookmark" />
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import BookmarkItem from '../components/BookmarkItem.vue'
import { BASEURL } from '../constants'

export default {
  name: 'BookmarkList',
  components: {
    BookmarkItem
  },
  methods: {
    ...mapActions(['addBookmark', 'addMessage'])
  },
  async fetch () {
    try {
      const { data } = await axios.get(
        BASEURL + '/bookmarks',
        {
          headers: { Authorization: this.$store.state.auth.token }
        }
      )
      data.forEach((bookmark) => {
        this.addBookmark({
          ...bookmark,
          editing: false
        })
      })
    } catch (error) {
      let msg = error.response.data.detail
      if (error.response.status === 401) {
        msg = 'Please login to view this page'
      }
      this.addMessage({
        id: null,
        title: 'Error',
        details: msg,
        type: 'error'
      })
    }
  }
}
</script>
