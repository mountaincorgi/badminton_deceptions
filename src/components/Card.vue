<template>
    <div id="card" @mouseover="changeActivePositions(positions)">
        <h5>{{cardData.name}}</h5>
        <p>This is a short description of the technique.</p>
    </div>
</template>

<script>
export default {
    name: "Card",
    data() {
        return {
            count: 1
        }
    },
    props: ["cardData"],
    computed: {
        positions: function() {
            return {
                fromPosition: this.cardData.fromPosition,
                expectedPosition: this.cardData.expectedPosition,
                actualPosition: this.cardData.actualPosition
            }
        }
    },
    methods: {
        changeActivePositions: function(positions) {
            console.log("Card positions: " + positions);
            this.$emit("change-active-positions", positions);
        }
    }
}
</script>

<style scoped>
#card {
    width: 200px;
    height: 300px;
    word-wrap: break-word;
    margin: 20px;
    padding: 10px;
    background-color: blanchedalmond;
}
#card:hover {
    background-color: lightblue;
    cursor: pointer;
}
</style>