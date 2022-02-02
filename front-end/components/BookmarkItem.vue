<template>
  <div>
    <a v-if="!bookmark.editing" :href="bookmark.url" class="bookmark-list-item" target="_blank">
      <img class="ml-3 favicon" :src="bookmark.favicon_url" alt="">
      <p class="ml-3">{{ bookmark.title }}</p>
      <div class="bookmark-actions">
        <button class="bg-green-700 text-gray-100" @click.prevent="editBookmark(bookmark)">
          <v-icon name="edit" />
        </button>
        <button class="bg-red-600 text-gray-100" @click.prevent="deleteBookmark(bookmark)">
          <v-icon name="trash" />
        </button>
      </div>
    </a>
    <form v-else method="post" class="bookmark-list-item" @submit.prevent="updateBookmarkHelper">
      <img class="favicon" :src="bookmark.favicon_url" alt="">
      <input type="text" :value="bookmark.title" name="title">
      <input type="url" :value="bookmark.url" name="url">
      <div class="bookmark-actions">
        <button class="bg-green-700 text-gray-100" type="submit">
          <v-icon name="save" />
          Save
        </button>
        <button class="bg-red-600 text-gray-100" @click.prevent="editBookmark(bookmark)">
          <v-icon name="window-close" />
          Cancel
        </button>
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

<style>
.fa-icon {
  height: 1rem;
  width: auto;
}

.bookmark-list-item {
  display: flex;
  flex-direction: row;
  padding:  .4rem;
  background-color: rgb(232, 232, 232);
  margin: .5rem;
  align-items: center;
}

.bookmark-list-item p {
  padding: 0px 5px;
}

.bookmark-actions {
  margin-left: auto;
  align-self: center;
}

.bookmark-actions button {
  padding: 0.3rem 0.7rem;
}

.favicon {
  height: 1.2rem;
  width: 1.2rem;
  align-self: center;
}

input {
  margin: 0.2rem 1rem;
  padding: 0.3rem 0.7rem;
}
</style>
