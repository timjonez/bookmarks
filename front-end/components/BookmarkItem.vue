<template>
  <div>
    <a v-if="!bookmark.editing" :href="bookmark.url" class="bookmark-list-item" target="_blank">
      <img class="favicon" :src="bookmark.icon" alt="">
      <p>{{ bookmark.title }}</p>
      <div class="bookmark-actions">
        <button class="bg-green-700 text-gray-100" @click.prevent="editBookmark(bookmark)">Edit</button>
        <button class="bg-red-600 text-gray-100" @click.prevent="deleteBookmark(bookmark)">X</button>
      </div>
    </a>
    <ValidationProvider v-else method="post" class="bookmark-list-item">
      <img class="favicon" :src="bookmark.icon" alt="">
      <input type="text" :value="bookmark.title" name="title" @change="saveBookmark">
      <div class="bookmark-actions">
        <button class="bg-green-700 text-gray-100" type="submit">Save</button>
        <button class="bg-red-600 text-gray-100" @click.prevent="deleteBookmark(bookmark)">X</button>
      </div>
    </ValidationProvider>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
import { ValidationProvider } from 'vee-validate'

export default {
  name: 'BookmarkItem',
  components: {
    ValidationProvider
  },
  props: {
    bookmark: Object
  },
  methods: {
    ...mapActions(['editBookmark', 'deleteBookmark', 'saveBookmark']),
    updateBookmark (e) {
      this.$store.commit('saveBookmark', e.target.value)
    }
  }
}
</script>

<style scoped>
.bookmark-list-item {
  display: flex;
  flex-direction: row;
  padding:  .4rem;
  background-color: rgb(232, 232, 232);
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
