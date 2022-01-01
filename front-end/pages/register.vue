<template>
  <div>
    <h1>Create Account</h1>
    <form method="post" @submit.prevent="createValidUser">
      <label for="email">Email</label>
      <input type="email" name="email" placeholder="Email"> <br>
      <label for="password">Password</label>
      <input type="password" name="password" placeholder="Password"> <br>
      <label for="confirmPassword">Confirm Password</label>
      <input type="password" name="confirmPassword" placeholder="Type Password again">
      <button class="bg-green-700 text-gray-100" type="submit">Create</button>
    </form>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'RegisterUser',
  methods: {
    ...mapActions(['createUser', 'addMessage']),
    createValidUser (payload) {
      const email = payload.target.email.value
      const password = payload.target.password.value
      const confirmPassword = payload.target.confirmPassword.value
      if (password === confirmPassword) {
        this.createUser({ email, password })
      } else {
        this.addMessage({
          id: null,
          title: 'Error',
          details: 'Passwords do not match. Please try again',
          type: 'error'
        })
      }
    }
  }
}
</script>

<style>

</style>
