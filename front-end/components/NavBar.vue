<template>
  <header class="px-4 py-3">
    <nav class="flex justify-between">
      <nuxt-link to="/" class="">
        <h1>Bookmarker</h1>
      </nuxt-link>
      <div class="">
        <nuxt-link to="/login">Login</nuxt-link>
        <nuxt-link to="/register">Signup</nuxt-link>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  name: 'NavBar'
}
</script>

<style scoped>
header {
  background-color: #003049ff;
  color: #eae2b7;
}

</style>
