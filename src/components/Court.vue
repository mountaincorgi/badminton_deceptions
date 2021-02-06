<template>
    <div>
        <p>Court</p>
        <p>{{activePositions}}</p>
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
                <!-- DO NOT DO THIS GET FROM SOME KIND OF OBJECT INSTEAD THIS IS FUCKING DUMB -->
                <CourtSquare
                    :isFrom="'OL8' === activePositions.fromPosition"
                    :isExpected="'OL8' === activePositions.expectedPosition"
                    :isActual="'OL8' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL7' === activePositions.fromPosition"
                    :isExpected="'OL7' === activePositions.expectedPosition"
                    :isActual="'OL7' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR7' === activePositions.fromPosition"
                    :isExpected="'OR7' === activePositions.expectedPosition"
                    :isActual="'OR7' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR8' === activePositions.fromPosition"
                    :isExpected="'OR8' === activePositions.expectedPosition"
                    :isActual="'OR8' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL6' === activePositions.fromPosition"
                    :isExpected="'OL6' === activePositions.expectedPosition"
                    :isActual="'OL6' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL5' === activePositions.fromPosition"
                    :isExpected="'OL5' === activePositions.expectedPosition"
                    :isActual="'OL5' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR5' === activePositions.fromPosition"
                    :isExpected="'OR5' === activePositions.expectedPosition"
                    :isActual="'OR5' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR6' === activePositions.fromPosition"
                    :isExpected="'OR6' === activePositions.expectedPosition"
                    :isActual="'OR6' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL4' === activePositions.fromPosition"
                    :isExpected="'OL4' === activePositions.expectedPosition"
                    :isActual="'OL4' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL3' === activePositions.fromPosition"
                    :isExpected="'OL3' === activePositions.expectedPosition"
                    :isActual="'OL3' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR3' === activePositions.fromPosition"
                    :isExpected="'OR3' === activePositions.expectedPosition"
                    :isActual="'OR3' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR4' === activePositions.fromPosition"
                    :isExpected="'OR4' === activePositions.expectedPosition"
                    :isActual="'OR4' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL2' === activePositions.fromPosition"
                    :isExpected="'OL2' === activePositions.expectedPosition"
                    :isActual="'OL2' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OL1' === activePositions.fromPosition"
                    :isExpected="'OL1' === activePositions.expectedPosition"
                    :isActual="'OL1' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR1' === activePositions.fromPosition"
                    :isExpected="'OR1' === activePositions.expectedPosition"
                    :isActual="'OR1' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'OR2' === activePositions.fromPosition"
                    :isExpected="'OR2' === activePositions.expectedPosition"
                    :isActual="'OR2' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL2' === activePositions.fromPosition"
                    :isExpected="'PL2' === activePositions.expectedPosition"
                    :isActual="'PL2' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL1' === activePositions.fromPosition"
                    :isExpected="'PL1' === activePositions.expectedPosition"
                    :isActual="'PL1' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR1' === activePositions.fromPosition"
                    :isExpected="'PR1' === activePositions.expectedPosition"
                    :isActual="'PR1' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR2' === activePositions.fromPosition"
                    :isExpected="'PR2' === activePositions.expectedPosition"
                    :isActual="'PR2' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL4' === activePositions.fromPosition"
                    :isExpected="'PL4' === activePositions.expectedPosition"
                    :isActual="'PL4' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL3' === activePositions.fromPosition"
                    :isExpected="'PL3' === activePositions.expectedPosition"
                    :isActual="'PL3' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR3' === activePositions.fromPosition"
                    :isExpected="'PR3' === activePositions.expectedPosition"
                    :isActual="'PR3' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR4' === activePositions.fromPosition"
                    :isExpected="'PR4' === activePositions.expectedPosition"
                    :isActual="'PR4' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL6' === activePositions.fromPosition"
                    :isExpected="'PL6' === activePositions.expectedPosition"
                    :isActual="'PL6' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL5' === activePositions.fromPosition"
                    :isExpected="'PL5' === activePositions.expectedPosition"
                    :isActual="'PL5' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR5' === activePositions.fromPosition"
                    :isExpected="'PR5' === activePositions.expectedPosition"
                    :isActual="'PR5' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR6' === activePositions.fromPosition"
                    :isExpected="'PR6' === activePositions.expectedPosition"
                    :isActual="'PR6' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL8' === activePositions.fromPosition"
                    :isExpected="'PL8' === activePositions.expectedPosition"
                    :isActual="'PL8' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PL7' === activePositions.fromPosition"
                    :isExpected="'PL7' === activePositions.expectedPosition"
                    :isActual="'PL7' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR7' === activePositions.fromPosition"
                    :isExpected="'PR7' === activePositions.expectedPosition"
                    :isActual="'PR7' === activePositions.actualPosition" />
                <CourtSquare
                    :isFrom="'PR8' === activePositions.fromPosition"
                    :isExpected="'PR8' === activePositions.expectedPosition"
                    :isActual="'PR8' === activePositions.actualPosition" />
            </div>
        </div>
    </div>
</template>

<script>
import { store } from '../store.js';
import CourtSquare from './CourtSquare.vue';

export default {
    name: "Court",
    components: {
        CourtSquare
    },
    props: [],
    data() {
        return {
            activePositions: store.state.activePositions
        }
    }
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
    height: 432px;
    width: 200px;
    position: absolute;
    z-index: 10;
    padding: 25px 20px 20px 20px;
    grid-gap: 6px;
}
.gi {
    background-color: white;
    opacity: 0.05;
}
</style>