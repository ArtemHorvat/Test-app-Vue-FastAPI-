<template>
    <div class="commentsWindow">
        <div class="commentItem" v-for="item in commentsData" :key="item.id" >
            <div class="commentItemImage">
                
            </div>
            <div class="commentItemContent">
                <span class="userName">{{ item.username }}</span>
                <span class="commentText" v-if="editingCommentId !== item.id">{{ item.comment }}</span>
                <form v-else class="replaceForm" :id="item.id" @submit.prevent="replaceData(item)">
                    <input type="text" v-model="newComment"/>
                    <button type="submit">&#10004;</button>
                </form>
            </div>
            <div class="adminContent">
                <div class="updateComment" @click="changeActive(item)"><span class="updateCommentSymbol">&#9998;</span></div>
                <div class="deleteComment" @click="deleteComment(item)"><span class="deleteCommentSymbol">&#215;</span></div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'

const API_URL = 'http://127.0.0.1:8000/comments'

defineProps(['commentsData'])
const emit = defineEmits(['updatePage'])

async function deleteComment(item) {
    await fetch(API_URL+`/${item.id}`, {
        method: "DELETE",
    })
    
    emit('updatePage')
}

const editingCommentId = ref(null)
const newComment = ref('')

async function replaceData(item) {
    await fetch(API_URL+`/${item.id}`, {
        method: "PATCH",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({comment: newComment.value})
    })
    editingCommentId.value = null
    const newComment = ref('') // Очищаем данные
    emit('updatePage')
}

function changeActive(item) {
    editingCommentId.value = item.id
}
</script>


<style scoped>
.commentsWindow {
    width: 100%;
    padding: 20px;

    display: flex;
    flex-direction: column;
    align-items: center;

    background-color: #CFD8E0;

    box-sizing: border-box;
}

.commentItem {
    min-width: 300px;
    max-width: 900px;
    display: flex;
    align-items: center;
    position: relative;

    padding: 5px;
    margin-bottom: 10px;

    background-color: #6076A7;
    border-radius: 8px;
}

.commentItemImage {
    width: 50px;
    height: 50px;

    margin-right: 20px;

    background-color: rgb(142, 142, 142);
}

.commentItemContent {
    width: 250px;

    display: flex;
    flex-direction: column;
}

.userName {
    font-family: 'Raleway';
    font-weight: 500;
    font-size: 16px;
    color: rgb(235, 235, 235);
    margin-bottom: 10px;
}

.commentText {
    font-family: 'Raleway';
    font-weight: 400;
    font-size: 16px; 
    color: rgb(235, 235, 235);
}

.adminContent {
    position: absolute;
    top: 5px;
    right: 5px;

    display: flex;
}
.deleteComment {
    margin-left: 10px;
    cursor: pointer;
}

.updateComment {
    cursor: pointer;
}

.replaceForm {
    display: flex;
}
</style>