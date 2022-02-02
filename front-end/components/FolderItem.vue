<template>
  <div>
    <div class="bookmark-list-item" target="_blank">
      <v-icon name="folder-open" class="ml-2" />
      <p class="ml-3">{{ folder.name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'FolderItem',
  props: {
    folderId: Number
  },
  computed: {
    folder () {
      return this.$store.getters.getFolderById(this.folderId)
    }
  }
}
</script>

<style>

</style>
