<template>
    <div id="card">
        <h5>{{cardData.name}}</h5>
        <p>This is a short description of the technique.</p>
    </div>
</template>

<script>
export default {
    name: "Card",
    props: ["cardData"]
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
</style>