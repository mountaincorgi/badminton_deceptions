<template>
    <div>
        <h1>{{category.name}}</h1>
        <div id="table-category">
            <div v-bind:key="deception.id" v-for="deception in category.deceptions">
                <Card v-bind:cardData="deception" />
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
    props: ["category"]
}
</script>

<style scoped>
#table-category {
    display: flex;
    flex-wrap: wrap;
}
</style>