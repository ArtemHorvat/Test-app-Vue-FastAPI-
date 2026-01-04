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
  {
    id: "8dvsfJuK",
    username: "Bob",
    comment: "It's funny :)"
  },
  {
    id: "XuF8W0bo",
    username: "Alice",
    comment: "For what this?"
  },
  {
    id: "mvclTS2h",
    username: "James",
    comment: "Simple app, good for study"
  },
  {
    id: "2lclvZI1",
    username: "Artem",
    comment: "This is the end of comments. Try contimnue"
  }
])

function pushData(data) {
  userData.push(data)
}
</script>

<style scoped>
</style>
