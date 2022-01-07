<template>
  <div>
    <a v-if="!bookmark.editing" :href="bookmark.url" class="bookmark-list-item" target="_blank">
      <img class="favicon" :src="bookmark.favicon_url" alt="">
      <p>{{ bookmark.title }}</p>
      <div class="bookmark-actions">
        <button class="bg-green-700 text-gray-100" @click.prevent="editBookmark(bookmark)">Edit</button>
        <button class="bg-red-600 text-gray-100" @click.prevent="deleteBookmark(bookmark)">X</button>
      </div>
    </a>
    <form v-else method="post" class="bookmark-list-item" @submit.prevent="updateBookmarkHelper">
      <img class="favicon" :src="bookmark.favicon_url" alt="">
      <input type="text" :value="bookmark.title" name="title">
      <input type="url" :value="bookmark.url" name="url">
      <div class="bookmark-actions">
        <button class="bg-green-700 text-gray-100" type="submit">Save</button>
        <button class="bg-red-600 text-gray-100" @click.prevent="deleteBookmark(bookmark)">X</button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'BookmarkItem',
  props: {
    bookmarkId: Number
  },
  computed: {
    bookmark () {
      return this.$store.getters.getBookmarkById(this.bookmarkId)
    }
  },
  methods: {
    ...mapActions(['editBookmark', 'deleteBookmark', 'updateBookmark']),
    async updateBookmarkHelper ({ target }) {
      await this.updateBookmark({
        id: this.bookmarkId,
        title: target.title.value,
        url: target.url.value
      })
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
