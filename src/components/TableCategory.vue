<template>
    <div>
        <p class="header">{{nameMapping[category.name]}}</p>
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
    data() {
        return {
            nameMapping: {
                net: "Net",
                front: "Front",
                mid: "Mid",
                back: "Back",
            }
        }
    },
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
.header {
    margin-left: 20px;
    margin-bottom: 0px;
    font-size: 25px;
    font-weight: 500;
}
</style>