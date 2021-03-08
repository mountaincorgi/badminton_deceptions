<template>
    <div id="table">
        <div class="title-card">
            <p class="header">Badminton Deceptions</p>
            <p class="description">
                This website exists to help everyone learn badminton deception
                techniques. Hover over a card and see its on-court representation
                on the right. Click on a card to see the technique in action.
            </p>
        </div>
        <div :key="category.id" v-for="category in tableData.categories">
            <TableCategory :category="category" />
        </div>
    </div>
</template>

<script>
import TableCategory from "./TableCategory.vue";

export default {
    name: "Table",
    components: {
        TableCategory
    },
    props: ["tableData"]
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap');
#table {
    z-index: 2;
}
.title-card {
    background-color: rgba(255, 255, 255, 0.938);
    position: relative;
    z-index: 3;
    left: 18px;
    padding-bottom: 10px;
    margin-right: 40%;
    border-radius: 20px;
    min-width: 400px;
    margin-bottom: 20px;
}
.header {
    font-family: "courier";
    margin-top: 14px;
    margin-bottom: 0px;
    margin-left: 20px;
    font-size: 50px;
    font-weight: 500;
    color: #222831;
}
.description {
    margin-left: 20px;
    margin-right: 20px;
    padding-bottom: 5px;
    font-size: 18px;
    color: #5c6b7a;
}
</style>