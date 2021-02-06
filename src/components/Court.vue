<template>
    <div>
        <p>Court</p>
        <p>{{activePositions}}</p>
        <p>{{activeClasses}}</p>
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
                <CourtSquare :activeClass="activeClasses['OL8']" />
                <CourtSquare :activeClass="activeClasses['OL7']" />
                <CourtSquare :activeClass="activeClasses['OR7']" />
                <CourtSquare :activeClass="activeClasses['OR8']" />
                <CourtSquare :activeClass="activeClasses['OL6']" />
                <CourtSquare :activeClass="activeClasses['OL5']" />
                <CourtSquare :activeClass="activeClasses['OR5']" />
                <CourtSquare :activeClass="activeClasses['OR6']" />
                <CourtSquare :activeClass="activeClasses['OL4']" />
                <CourtSquare :activeClass="activeClasses['OL3']" />
                <CourtSquare :activeClass="activeClasses['OR3']" />
                <CourtSquare :activeClass="activeClasses['OR4']" />
                <CourtSquare :activeClass="activeClasses['OL2']" />
                <CourtSquare :activeClass="activeClasses['OL1']" />
                <CourtSquare :activeClass="activeClasses['OR1']" />
                <CourtSquare :activeClass="activeClasses['OR2']" />
                <CourtSquare :activeClass="activeClasses['PL2']" />
                <CourtSquare :activeClass="activeClasses['PL1']" />
                <CourtSquare :activeClass="activeClasses['PR1']" />
                <CourtSquare :activeClass="activeClasses['PR2']" />
                <CourtSquare :activeClass="activeClasses['PL4']" />
                <CourtSquare :activeClass="activeClasses['PL3']" />
                <CourtSquare :activeClass="activeClasses['PR3']" />
                <CourtSquare :activeClass="activeClasses['PR4']" />
                <CourtSquare :activeClass="activeClasses['PL6']" />
                <CourtSquare :activeClass="activeClasses['PL5']" />
                <CourtSquare :activeClass="activeClasses['PR5']" />
                <CourtSquare :activeClass="activeClasses['PR6']" />
                <CourtSquare :activeClass="activeClasses['PL8']" />
                <CourtSquare :activeClass="activeClasses['PL7']" />
                <CourtSquare :activeClass="activeClasses['PR7']" />
                <CourtSquare :activeClass="activeClasses['PR8']" />
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
    data() {
        return {
            activePositions: store.state.activePositions
        }
    },
    computed: {
        activeClasses: function() {
            // also results in undefined added as a class to inactive squares
            let activeClasses = {}
            let keys = Object.values(this.activePositions);

            activeClasses[keys[0]] = 'from';
            activeClasses[keys[1]] = 'expected';
            activeClasses[keys[2]] = 'actual';
            return activeClasses;
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