<template>
    <div>
        <h1>Court</h1>
        <div id="court-container">
            <img 
                id="court-svg"
                src="../assets/court_path_y.svg"
                alt="court"
                height="440"
                width="200"
                style="stroke: white;">

            <div id="court">
                <div class="OL8 gi"></div>
                <div class="OL7 gi"></div>
                <div class="OR7 gi"></div>
                <div class="OR8 gi"></div>
                <div class="OL6 gi"></div>
                <div class="OL5 gi"></div>
                <div class="OR5 gi"></div>
                <div class="OR6 gi"></div>
                <div class="OL4 gi"></div>
                <div class="OL3 gi"></div>
                <div class="OR3 gi"></div>
                <div class="OR4 gi"></div>
                <div class="OL2 gi"></div>
                <div class="OL1 gi"></div>
                <div class="OR1 gi"></div>
                <div class="OR2 gi"></div>
                <div class="PL2 gi"></div>
                <div class="PL1 gi"></div>
                <div class="PR1 gi"></div>
                <div class="PR2 gi"></div>
                <div class="PL4 gi"></div>
                <div class="PL3 gi"></div>
                <div class="PR3 gi"></div>
                <div class="PR4 gi"></div>
                <div class="PL6 gi"></div>
                <div class="PL5 gi"></div>
                <div class="PR5 gi"></div>
                <div class="PR6 gi"></div>
                <div class="PL8 gi"></div>
                <div class="PL7 gi"></div>
                <div class="PR7 gi"></div>
                <div class="PR8 gi"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "Court",
    components: {},
    props: []
}
</script>

<style scoped>
#court-container {
    height: 440px;
    width: 200px;
}
#court-svg {
    position: absolute;
    z-index: -1;
}
#court {
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-template-rows: 3fr 3fr 2fr 1fr 1fr 2fr 3fr 3fr;
    height: 440px;
    width: 200px;
    position: absolute;
    z-index: 10;
}
.gi:hover {
    background-color: red;
    opacity: 0.5;
}
</style>