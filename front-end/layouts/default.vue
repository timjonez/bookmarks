<template>
  <div>
    <nav-bar />
    <div class="msg-modal-container msg-modal" :class="{'hidden': !$store.state.messageModalOpen, 'flex': $store.state.messageModalOpen }">
      <message-modal v-for="message in $store.state.messages" :key="message.id" :message="message" />
    </div>
    <nuxt />
  </div>
</template>

<script>
import NavBar from '../components/NavBar.vue'
import MessageModal from '../components/MessageModal.vue'

export default {
  name: 'DefaultLayout',
  components: {
    NavBar,
    MessageModal
  }
}
</script>

<style>
input {
  border: solid 1px;
}

</style>
