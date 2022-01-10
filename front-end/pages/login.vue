<template>
  <div>
    <form method="post" @submit.prevent="login" class="card">
      <h1 class="text-4xl">Log In</h1>
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
