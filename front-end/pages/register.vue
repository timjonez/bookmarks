<template>
  <div>
    <form method="post" class="card" @submit.prevent="createValidUser">
      <h1 class="text-4xl">Create Account</h1>
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

<style scoped>
div {
  height: 100%;
  display: grid;
}

form {
  align-self: center;
  justify-self: center;
}

h1, label {
  color: #003049ff;
}

input {
  padding: 0.7rem 1.3rem;
  min-width: 30vw;
  border-radius: 0.35rem;
  border: rgb(204, 205, 207)solid 1px;
}

label {
  padding-top: 0.7rem;
}

button {
  margin-top: 2rem;
  padding: 0.7rem 1.3rem;
  background-color: #d62828ff;
  width: 50%;
}
</style>
