<template>
  <div>
    <h1>Home Page</h1>
    <bookmark-item v-for="bookmark in bookmarks" :key="bookmark.id" :bookmark="bookmark" />
  </div>
</template>

<script>
import BookmarkItem from '../components/BookmarkItem.vue'

export default {
  name: 'BookmarkList',
  components: {
    BookmarkItem
  },
  data () {
    return {
      bookmarks: [...this.$store.state.bookmarks]
    }
  }
}
</script>
