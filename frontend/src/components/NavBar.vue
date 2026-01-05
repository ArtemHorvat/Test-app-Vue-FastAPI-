<template>
  <div class="mainWindow">
    <div class="mainWindowNav">
      <div class="logo">
        <span class="logoText">Comment Creator</span>
      </div>
      <div class="menu">
        <span class="menuItem" @click="openCommentWindow">Create comment</span>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['openWindow'])

function openCommentWindow() {
  emit('openWindow') // Посылаем в App событие-открытие
}

</script>

<style scoped>
.logoText {
  font-family: 'Raleway';
  font-weight: 700;
}

.mainWindowNav {
    width: 100%;
    height: 50px;

    padding-left: 15px;
    padding-right: 15px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background-color: #375592;
    box-sizing: border-box;
}

.logoText {
    font-weight: 800;
    color: rgb(235, 235, 235);
    cursor: pointer;
}
.menuItem {
    font-family: 'Raleway';
    font-weight: 400;
    font-size: 20px;
    color: rgb(235, 235, 235);
    
    margin-right: 20px;

    cursor: pointer;
}
</style>
