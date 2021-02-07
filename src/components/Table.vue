<template>
    <div>
        <p>Table</p>
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

</style>