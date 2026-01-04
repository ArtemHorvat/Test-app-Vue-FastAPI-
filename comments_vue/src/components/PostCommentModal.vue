<template>
    <div class="modalView" v-if="isActiveProp">
        <div class="modal">
            <form class="modalViewForm" @submit.prevent="submitData">
                <div class="modalViewFormComp">
                    <label for="name">User name</label>
                    <input type="text" id="name" v-model="userName"/>
                </div>
                <div class="modalViewFormComp">
                    <label for="comment">Put your comment</label>
                    <textarea type="text" id="comment" v-model="userComment"/>
                </div>
                <button class="submitButton">Submit comment!</button>
            </form>
            <button class="closeModalView" @click="closeCommentWindow">&#215;</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const userName = ref('')
const userComment = ref('')

defineProps(['isActiveProp'])

const emit = defineEmits(['closeWindow', 'sendData'])

function closeCommentWindow() {
    emit('closeWindow') // Здесь посылаем сообщение в App, что окно закрываем
}

function generateCode(length = 8) {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  let result = '';
  const charsLength = chars.length;

  for (let i = 0; i < length; i++) {
    result += chars.charAt(Math.floor(Math.random() * charsLength));
  }

  return result;
}

function submitData() {
    const key = generateCode()
    emit('sendData', {id: key, username: userName, comment: userComment})
    emit('closeWindow')
}
</script>

<style scoped>
.modalView {
    position: fixed;
    inset: 0;
    z-index: 1000;

    display: flex;
    align-items: center;
    justify-content: center;

    background: rgba(0, 0, 0, 0.3);
    backdrop-filter: blur(6px);
}

.modal {
    background-color: #6076A7;
    padding: 24px;
    border-radius: 12px;
    min-width: 300px;
    position: relative;
}

.modalViewForm {
    margin-bottom: 25px;
}

.modalViewFormComp {
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
}

textarea {
    width: 500px;
    height: 200px;
    resize: none;
}

.closeModalView {
    position: absolute;
    width: 30px;
    height: 30px;

    top: 0;
    right: 0;

    background-color: #CFD8E0;
    border-radius: 8px;
}
.closeModalView:hover {
    background-color: #bfc7ce;
}

.submitButton {
    width: 100%;
    border-radius: 8px;
    background-color: #CFD8E0;
}

.submitButton:hover {
    background-color: #bfc7ce;
}

label {
    font-family: 'Raleway';
    font-weight: 400;
    font-size: 20px;
    color: rgb(235, 235, 235);
}

input {
    border-radius: 8px;
    border: none;
}
textarea {
    border-radius: 8px;
    border: none;
}
</style>