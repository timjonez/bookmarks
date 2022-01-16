<template>
  <header class="px-4 py-3">
    <nav class="flex justify-between">
      <nuxt-link to="/" class="">
        <h1>Bookmarker</h1>
      </nuxt-link>
      <div class="" v-if="$store.state.auth.userLoggedIn">
        <button @click.prevent="logout">Logout</button>
      </div>
      <div class="" v-else>
        <nuxt-link to="/login">Login</nuxt-link>
        <nuxt-link to="/register">Signup</nuxt-link>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'NavBar',
  methods: {
    ...mapActions(['logout'])
  }
}
</script>

<style scoped>
header {
  background-color: #003049ff;
  color: #eae2b7;
}

a {
  margin: 0px 0.2rem;
}

</style>
