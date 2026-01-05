<template>
  <div class="appWindow">
    <NavBar @openWindow="openCommentWindow" />
    <CommentsWindow :commentsData="userData"
                    @updatePage="getData"/>
    <Teleport to="body">
      <PostComment :isActiveProp="isActive" 
                   @closeWindow="closeCommentWindow"
                   @updatePage="getData"
      />
    </Teleport>
  </div>  
</template>


<script setup>
import { ref, reactive, onMounted } from 'vue'

import PostComment from './components/PostCommentModal.vue'
import NavBar from './components/NavBar.vue'
import CommentsWindow from './components/CommentsWindow.vue'

const API_URL = 'http://127.0.0.1:8000/comments'


const isActive = ref(false)
const userData = reactive([])

function openCommentWindow() { // На действие из NavBar открываем окно
  isActive.value = true
}

function closeCommentWindow() { // На действие из PostCommentModal закрываем окно
  isActive.value = false
}


// Получение всех комментариев при загрузке страницы
async function getData() {
  const res = await fetch(API_URL)
  const comments  = await res.json()

  userData.length = 0 // Очищаем перед тем как заполнить заново

  comments.forEach(comment => {
    userData.push(comment)
  });
}

onMounted(() => {
  getData()
})
</script>

<style scoped>
</style>
