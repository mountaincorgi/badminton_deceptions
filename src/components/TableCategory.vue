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
    margin-right: 30px;
}
.header {
    position: relative;
    margin-left: 20px;
    margin-bottom: 0px;
    font-size: 25px;
    font-weight: 500;
    color: #30475e;
    display: inline-block;
    clear: both;
    background-color: rgba(255, 255, 255, 0.918);
    padding: 2px 10px 5px 10px;
    border-radius: 5px;
}
</style>