<template>
    <div>
        <h3 class="header">{{nameMapping[category.name]}}</h3>
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
    padding-left: 20px;
    margin-bottom: 0px;
}
</style>