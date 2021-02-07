<template>
    <div>
        <p>{{category.name}}</p>
        <div id="table-category">
            <div :key="deception.id" v-for="deception in category.deceptions">
                <Card :cardData="deception" />
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