<template>
    <div>
        <p>Court</p>
        <div id="court-container">
            <svg
                id="court-svg"
                xmlns="http://www.w3.org/2000/svg"
                width="619.987"
                height="1347.278"
                viewBox="0 0 164.038 356.467">
                <g stroke-width="3.8">
                    <path d="M82.02 125.876V2.467M14.53 178.793V1.64m134.98 177.154V1.64m13.154 22.01H2.432m160.232 102.194H2.432m159.706 52.424H1.9V1.9h160.238v176.367zM82.02 230.591V354m67.49-176.326V354.83M14.529 177.674V354.83M1.374 332.817h160.232M1.374 230.625h160.232M1.9 178.2h160.238v176.367H1.9V178.2z" fill="none"/>
                </g>
            </svg>

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
    height: 480px;
    width: 240px;
    background-color: rgb(33, 161, 118);
    border-radius: 20px;
}
#court-svg {
    position: absolute;
    height: 440px;
    width: 200px;
    stroke: white;
    padding: 20px;
}
#court {
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-template-rows: 3fr 3fr 2fr 1fr 1fr 2fr 3fr 3fr;
    height: 436px;
    width: 196px;
    position: absolute;
    z-index: 10;
    padding: 20px;
    grid-gap: 2px;
}
.gi {
    background-color: white;
    opacity: 0.2;
}
.gi:hover {
    opacity: 0.6;
}
</style>