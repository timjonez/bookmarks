<template>
  <div>
    <h1>Home Page</h1>
    <bookmark-item v-for="bookmark in bookmarks" :key="bookmark.id" :bookmark="bookmark" />
  </div>
</template>

<script>
import axios from 'axios'
import BookmarkItem from '../components/BookmarkItem.vue'
import { BASEURL } from '../constants'

export default {
  name: 'BookmarkList',
  components: {
    BookmarkItem
  },
  data () {
    return {
      bookmarks: [...this.$store.state.bookmarks]
    }
  },
  async created () {
    await this.getBookmarks()
  },
  methods: {
    async getBookmarks () {
      const { data } = await axios.get(
        BASEURL + '/bookmarks',
        {
          headers: { Authorization: this.$store.state.auth.token }
        }
      )
      data.forEach((bookmark) => {
        this.bookmarks.push({
          ...bookmark,
          editing: false
        })
      })
    }
  }
}
</script>
