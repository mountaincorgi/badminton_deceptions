<template>
    <div
        id="card"
        @mouseover="changeActivePositions(positions)"
        @click="changeActiveCard(cardData)">
        <h5>{{cardData.name}}</h5>
        <p>Grip: {{cardData.grip}}</p>
        <p>Position: {{cardData.category}}</p>
    </div>
</template>

<script>
import { store } from '../store.js'

export default {
    name: "Card",
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
            store.changeActivePositions(positions);
        },
        changeActiveCard: function(activeCardData) {
            store.changeActiveCard(activeCardData);
            store.toggleModal();
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