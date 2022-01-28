<template>
  <div>
    <folder-item v-for="folder in $store.state.folders" :key="'f'+folder.id" :folderId="folder.id" />
    <bookmark-item v-for="bookmark in $store.state.bookmarks" :key="bookmark.id" :bookmarkId="bookmark.id" />
    <add-bookmark />
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import BookmarkItem from '../components/BookmarkItem.vue'
import AddBookmark from '../components/AddBookmark.vue'
import FolderItem from '../components/FolderItem.vue'
import { BASEURL } from '../constants'

export default {
  name: 'BookmarkList',
  components: {
    BookmarkItem,
    AddBookmark,
    FolderItem
  },
  methods: {
    ...mapActions(['appendBookmark', 'appendFolder', 'addMessage', 'removeAllBookmarks'])
  },
  async fetch () {
    this.removeAllBookmarks()
    try {
      const { data } = await axios.get(
        BASEURL + '/bookmarks',
        {
          headers: { Authorization: this.$store.state.auth.token }
        }
      )
      data.forEach((bookmark) => {
        this.appendBookmark({
          ...bookmark,
          editing: false
        })
      })

      const { data: folderData } = await axios.get(
        BASEURL + '/folders',
        {
          headers: { Authorization: this.$store.state.auth.token }
        }
      )
      folderData.forEach((folder) => {
        this.appendFolder(folder)
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
