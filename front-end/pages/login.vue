<template>
  <div>
    <h1>Login</h1>
    <form method="post" @submit.prevent="login">
      <label for="email">Email</label>
      <input type="email" name="email" placeholder="Email"> <br>
      <label for="password">Password</label>
      <input type="password" name="password" placeholder="Password">
      <button class="bg-green-700 text-gray-100" type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'userLogin',
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style>

</style>
