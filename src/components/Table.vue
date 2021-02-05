<template>
    <div>
        <h1>Table</h1>
        <div :key="category.id" v-for="category in tableData.categories">
            <TableCategory :category="category" @change-active-positions="changeActivePositions($event)" />
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
    props: ["tableData"],
    methods: {
        changeActivePositions: function(positions) {
            console.log("Table positions: " + positions);
            this.$emit("change-active-positions", positions);
        }
    }
}
</script>

<style scoped>

</style>