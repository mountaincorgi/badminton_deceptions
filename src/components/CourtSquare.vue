<template>
    <div class="grid-item" :class="activeClass"></div>
</template>

<script>
export default {
    name: "CourtSquare",
    props: ["activeClass"]
}
</script>

<style scoped>
.grid-item {
    background-color: white;
    opacity: 0;
    border-radius: 100%;
}
.from {
    background-color: cyan;
    opacity: 1;
}
.expected {
    background-color: yellow;
    opacity: 1;
}
.actual {
    background-color: red;
    opacity: 1;
}
</style>