<template>
    <div>
        <p class="header">Court Representation</p>
        <!-- Color selector -->
        <div id="color-selector">
            <div class="green-selector selector-item" @click="changeColor('green')"></div>
            <div class="blue-selector selector-item" @click="changeColor('blue')"></div>
            <div class="red-selector selector-item" @click="changeColor('red')"></div>
            <div class="black-selector selector-item" @click="changeColor('black')"></div>
        </div>

        <!-- Main court container -->
        <div id="court-container" :class="colorClasses[courtColor]">
            <!-- SVG Overlay -->
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
            
            <!-- Court grid -->
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

        <!-- Legend -->
        <ul class="legend">
            <li><i class="ci material-icons from">label</i> Player</li>
            <!-- TODO: mistake! Switch these around -->
            <li><i class="ci material-icons actual">label</i> Expected Shot</li>
            <li><i class="ci material-icons expected">label</i><span> Actual Shot</span></li>
        </ul>
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
            activePositions: store.state.activePositions,
            courtColor: "green",
            colorClasses: {
                green: "green-court",
                blue: "blue-court",
                red: "red-court",
                black: "black-court"
            }
        }
    },
    methods: {
        changeColor: function(newColor) {
            this.courtColor = newColor;
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
.header {
    margin-top: 0px;
    margin-bottom: 10px;
    font-size: 18px;
}

/* Color selector */
#color-selector {
    display: flex;
    width: 240px;
}
.selector-item {
    height: 14px;
    width: 14px;
    border-radius: 100%;
    margin-left: 5px;
    margin-right: 5px;
}
.selector-item:hover {
    cursor: pointer;
}
.green-selector {   
    background-color: rgb(40, 160, 120);
    border: 3px solid rgb(40, 160, 120);
}
.green-selector:hover {   
    border-color: rgb(50, 220, 160);
}
.blue-selector {    
    background-color: rgb(80, 140, 180);
    border: 3px solid rgb(80, 140, 180);
}
.blue-selector:hover {    
    border-color: rgb(100, 180, 220);
}
.red-selector {    
    background-color: rgb(180, 90, 90);
    border: 3px solid rgb(180, 90, 90);
}
.red-selector:hover {    
    border-color: rgb(220, 110, 110);
}
.black-selector {    
    background-color: rgb(100, 100, 100);
    border: 3px solid rgb(100, 100, 100);
}
.black-selector:hover {    
    border-color: rgb(160, 160, 160);
}

/* Court container */
#court-container {
    height: 550px;
    width: 240px;
    border-radius: 20px;
}
.green-court {
    background-color: rgb(40, 160, 120);
    transition: background-color 0.3s;
}
.blue-court {
    background-color: rgb(80, 140, 180);
    transition: background-color 0.3s;
}
.red-court {
    background-color: rgb(180, 90, 90);
    transition: background-color 0.3s;
}
.black-court {
    background-color: rgb(100, 100, 100);
    transition: background-color 0.3s;
}

/* Court SVG */
#court-svg {
    position: absolute;
    height: 440px;
    width: 200px;
    stroke: white;
    padding: 20px;
}

/* Court grid */
#court {
    display: grid;
    grid-template-columns: auto auto auto auto;
    grid-template-rows: 3fr 3fr 2fr 1fr 1fr 2fr 3fr 3fr;
    height: 432px;
    width: 200px;
    position: absolute;
    z-index: 10;
    padding: 24px 20px 20px 20px;
    grid-gap: 8px;
}

/* Legend */
.legend {
    font-size: 16px;
    color: white;
    list-style-type: none;
    padding-left: 20px;
    position: relative;
    top: 470px;
}
.ci {
    font-size: 12px;
}
.from {
    color: rgb(150, 240, 240);
}
.expected {
    color: rgb(171, 240, 150);
}
.actual {
    color: rgb(240, 150, 150);
}
</style>