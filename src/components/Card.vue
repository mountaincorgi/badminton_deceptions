<template>
    <div
        id="card"
        @mouseover="changeActivePositions(positions)"
        @click="changeActiveCard(cardData)">
        <p class="header">{{cardData.name}}</p>
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
    color: #5c6b7a;
}
.header {
    margin-top: 5px;
    font-size: 18px;
    font-weight: 500;
    color: #222831;
}
#card {
    width: 200px;
    height: 300px;
    word-wrap: break-word;
    margin: 20px;
    padding: 10px;
    background-color: white;
    border: 2px solid #30475e;
    border-radius: 5px;
    transition: box-shadow 0.1s;
}
#card:hover {
    cursor: pointer;
    border-color: #f05454;
    box-shadow: 0 4px 8px 0 #36495c73, 0 4px 8px 0 #36495c73;
}
</style>