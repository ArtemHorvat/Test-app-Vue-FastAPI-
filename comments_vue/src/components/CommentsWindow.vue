<template>
    <div class="commentsWindow">
        <div class="commentItem" v-for="item in commentsData" :key="item.id" >
            <div class="commentItemImage">
                
            </div>
            <div class="commentItemContent">
                <span class="userName">{{ item.username }}</span>
                <span class="commentText">{{ item.comment }}</span>
            </div>
        </div>
    </div>
</template>

<script setup>
defineProps(['commentsData'])
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
</style>