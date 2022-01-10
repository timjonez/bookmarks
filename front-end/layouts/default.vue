<template>
  <div class="h-full w-full">
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
html, body, #__nuxt, #__layout {
  height: 100%;
  width: 100%;
}

.card {
  background-color: rgb(229, 231, 235);
  padding: 4rem 3rem;
  display: flex;
  flex-direction: column;
}

</style>
