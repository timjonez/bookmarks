<template>
  <div>
    <div
      class="modal"
      :class="{'bg-error': (message.type === 'error'), 'bg-success': (message.type === 'success') }"
      v-closable="{
        exclude: [],
        handler: 'removeMessageWithoutId'
      }">
      <h1 id="msgTitle">{{ message.title }}</h1>
      <p id="msgDetails">{{ message.details }}</p>
      <button class="bg-white" @click="removeMessage(message.id)">Ok</button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'MessageModal',
  props: {
    message: Object
  },
  methods: {
    ...mapActions(['removeMessage']),
    removeMessageWithoutId () {
      this.removeMessage(this.message.id)
    }
  }
}
</script>

<style>
.msg-modal-container {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  padding: 0.5rem;
}

.msg-modal {
  justify-content: start;
  align-items: flex-end;
  flex-direction: column;
}

.msg-modal div.modal {
  margin-bottom: 0.5rem;
}

.error-modal {
  background-color: rgba(0, 0, 0, 0.4);
  justify-content: center;
  align-items: center;
}

.modal {
  position: relative;
  padding: 1rem 2rem;
}

.bg-error {
  background-color: rgba(255, 0, 0, 0.75);
}

.bg-success {
  background-color: rgba(0, 133, 0, 0.75);
}
</style>
