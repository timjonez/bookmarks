<template>
  <form method="post" @submit.prevent="addBookmarkerHelper" class="bookmark-list-item">
    <input type="text" v-model="title" name="title" placeholder="Name">
    <input type="text" v-model="url" name="url" placeholder="Url">
    <div>
      <button class="bg-green-700 text-gray-100" type="submit">Save</button>
    </div>
  </form>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'AddBookmark',
  data () {
    return {
      title: '',
      url: ''
    }
  },
  methods: {
    ...mapActions(['addBookmark']),
    addBookmarkerHelper () {
      this.addBookmark({
        title: this.title,
        url: this.url
      })
      this.title = ''
      this.url = ''
    }
  }
}
</script>

<style scoped>
input, div {
  margin: 0.2rem 1rem;
}

input {
  padding: 0.3rem 0.7rem;
}

button {
  padding: 0.3rem 0.7rem;
  background-color: #d62828ff;
}

</style>
