<template>
  <div>
    <div class="bookmark-list-item" target="_blank">
      <v-icon name="folder-open" class="ml-2" />
      <p class="ml-3">{{ folder.name }}</p>
      <button @click.prevent="getFolderItems">Open</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'
import { BASEURL } from '../constants'
export default {
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
    ...mapActions(['appendFolder']),
    async getFolderItems () {
      try {
        const { data } = await axios.get(
          `${BASEURL}/folder/${this.folderId}`,
          {
            headers: { Authorization: this.$store.state.auth.token }
          }
        )
        data.forEach((folder) => {
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
}
</script>

<style>

</style>
