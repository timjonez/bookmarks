<template>
  <a :href="bookmark.url" class="bookmark-list-item" target="_blank">
    <img class="favicon" :src="bookmark.icon" alt="">
    <p>{{ bookmark.name }}</p>
    <div class="bookmark-actions">
      <button class="bg-green-700 text-gray-100" @click.prevent="editBookmark">Edit</button>
      <button class="bg-red-600 text-gray-100" @click.prevent="deleteBookmark">X</button>
    </div>
  </a>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'BookmarkItem',
  props: {
    bookmark: Object
  },
  methods: {
    ...mapActions(['editBookmark', 'deleteBookmark'])
  }
}
</script>

<style scoped>
.bookmark-list-item {
  display: flex;
  flex-direction: row;
  padding:  .4rem;
  background-color: rgb(167, 167, 167);
  margin: .5rem;
}

.bookmark-list-item p {
  padding: 0px 5px;
}

.bookmark-actions {
  margin-left: auto;
}

.bookmark-actions button {
  padding:  2px 10px;
}

.favicon {
  height: 1.2rem;
  width: 1.2rem;
  align-self: center;
}

</style>
