<template>
    <div
        id="card"
        @mouseover="changeActivePositions(positions)"
        @click="changeActiveCard(cardData)">
        <h5 class="header">{{cardData.name}}</h5>
        <p>{{cardData.grip}}</p>
        <p>{{cardData.category}}</p>
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
p {
    font-size: 16px;
}
.header {
    margin-top: 5px;
}
#card {
    width: 200px;
    height: 300px;
    word-wrap: break-word;
    margin: 20px;
    padding: 10px;
    color: #515070;
    background-color: #ffffff;
    border: 2px solid #ffbb91;
    border-radius: 5px;
    transition: box-shadow 0.1s;
}
#card:hover {
    cursor: pointer;
    border-color: #ff8e6e;
    box-shadow: 0 4px 8px 0 rgba(51, 50, 70, 0.2), 0 4px 8px 0 rgba(51, 50, 70, 0.2);
}
</style>