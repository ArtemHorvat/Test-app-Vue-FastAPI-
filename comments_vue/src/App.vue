<template>
  <div class="appWindow">
    <NavBar @openWindow="openCommentWindow" />
    <CommentsWindow :commentsData="userData"/>
    <Teleport to="body">
      <PostComment :isActiveProp="isActive" 
                   @closeWindow="closeCommentWindow"
                   @sendData="pushData"
      />
    </Teleport>
  </div>  
</template>


<script setup>
import { ref, reactive } from 'vue'

import PostComment from './components/PostCommentModal.vue'
import NavBar from './components/NavBar.vue'
import CommentsWindow from './components/CommentsWindow.vue'

const isActive = ref(false)

function openCommentWindow() { // На действие из NavBar открываем окно
  isActive.value = true
}

function closeCommentWindow() { // На действие из PostCommentModal закрываем окно
  isActive.value = false
}

const userData = reactive([
    {name: 'Alice', comment: 'Thats app so fun!'},
    {name: 'Bob', comment: 'Like FaceBook but boring...'},
    {name: 'James', comment: 'Pretty cool :)'},
    {name: 'Peter', comment: 'This app for training skills lmao.'}
])

function pushData(data) {
  userData.push(data)
}
</script>

<style scoped>
</style>
