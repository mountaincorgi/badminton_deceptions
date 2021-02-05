<template>
    <div>
        <h1>{{category.name}}</h1>
        <div id="table-category">
            <div :key="deception.id" v-for="deception in category.deceptions">
                <Card :cardData="deception" @change-active-positions="changeActivePositions($event)" />
            </div>
        </div>
    </div>
</template>

<script>
import Card from './Card.vue'

export default {
    name: "TableCategory",
    components: {
        Card
    },
    props: ["category"],
    methods: {
        changeActivePositions: function(positions) {
            console.log("ategory positions: " + positions);
            this.$emit("change-active-positions", positions);
        }
    }
}
</script>

<style scoped>
#table-category {
    display: flex;
    flex-wrap: wrap;
}
</style>