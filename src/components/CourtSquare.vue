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
    background-color: rgb(150, 240, 240);
    opacity: 1;
}
.expected {
    background-color: rgb(240, 240, 150);
    opacity: 1;
}
.actual {
    background-color: rgb(240, 150, 240);
    opacity: 1;
}
</style>