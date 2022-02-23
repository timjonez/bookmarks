<template>
  <div>
    <div class="folder-container" target="_blank">
      <div class="folder-item">
        <v-icon name="folder-open" class="ml-2" />
        <p class="ml-3">{{ folder.name }}</p>
        <button @click.prevent="getFolderItems">Open</button>
      </div>
      <div>
        <bookmark-item v-for="bookmark in folder.bookmarks" :key="'fb'+bookmark.id" :bookmarkId="bookmark.id" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import { BASEURL } from '../constants'
import BookmarkItem from './BookmarkItem.vue'

export default {
  components: { BookmarkItem },
  name: 'FolderItem',
  props: {
    folderId: Number
  },
  computed: {
    folder () {
      return this.$store.getters.getFolderById(this.folderId)
    }
  },
  methods: {
    ...mapActions(['appendFolder', 'appendFolderItem']),
    async getFolderItems () {
      try {
        const { data } = await axios.get(
          `${BASEURL}/folder/${this.folderId}`,
          {
            headers: { Authorization: this.$store.state.auth.token }
          }
        )
        data.bookmarks.forEach((folder) => {
          this.appendFolderItem(folder)
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
}
</script>

<style scoped>
.folder-container {
  padding:  .4rem;
  background-color: rgb(232, 232, 232);
  margin: .5rem;
  align-items: center;
}

.folder-item {
  display: flex;
  flex-direction: row;
  padding:  .4rem;
  background-color: rgb(232, 232, 232);
  align-items: center;
}

</style>
