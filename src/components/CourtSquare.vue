<template>
    <div 
        class="grid-item"
        :class="{
            'from-position': isFrom,
            'expected-position': isExpected,
            'actual-position': isActual}">
    </div>
</template>

<script>
export default {
    name: "CourtSquare",
    props: ["isFrom", "isExpected", "isActual"]
}
</script>

<style scoped>
.grid-item {
    background-color: white;
    opacity: 0.05;
    border-radius: 100%;
}
.from-position {
    background-color: cyan;
    opacity: 1;
}
.expected-position {
    background-color: yellow;
    opacity: 1;
}
.actual-position {
    background-color: red;
    opacity: 1;
}
</style>