<template>
  <form method="post" @submit.prevent="addBookmarkerHelper">
    <input type="text" v-model="title" name="title" placeholder="Name">
    <input type="text" v-model="url" name="url" placeholder="Url">
    <div class="">
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

<style>

</style>
