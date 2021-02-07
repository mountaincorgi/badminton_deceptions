<template>
    <div id="table">
        <h1 class="header"><u>Badminton Deceptions</u></h1>
        <p class="description">
            This website exists to help everyone learn badminton deception
            techniques. Hover over a card and see its on-court representation
            on the right. Click on a card to see the technique in action.
        </p>
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
.header {
    margin-top: 0px;
    margin-bottom: 0px;
    margin-left: 20px;
}
.description {
    margin-left: 20px;
    margin-right: 150px;
}
</style>