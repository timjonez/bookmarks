<template>
  <div>
    <div
      class="modal"
      :class="{'bg-error': (message.type === 'error'), 'bg-success': (message.type === 'success') }"
      v-closable="{
        exclude: [],
        handler: 'removeMessageWithoutId'
      }">
      <div class="grid justify-end pr-1">
        <button class="text-white font-black" @click="removeMessage(message.id)">X</button>
      </div>
      <div class="p-5 pt-0">
        <h1 id="msgTitle">{{ message.title }}</h1>
        <p id="msgDetails">{{ message.details }}</p>
      </div>
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
  padding: 0.5rem;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.bg-error {
  background-color: rgba(255, 0, 0, 0.9);
}

.bg-success {
  background-color: rgba(0, 133, 0, 0.9);
}
</style>
