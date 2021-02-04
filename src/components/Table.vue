<template>
    <div>
        <h1>Table</h1>
        <div v-bind:key="category.id" v-for="category in tableData.categories">
            <TableCategory v-bind:category="category"/>
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

</style>