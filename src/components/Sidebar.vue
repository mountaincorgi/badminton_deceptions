<template>
    <div id="sidebar">
        <div id="burger-close">
            <i class="burger-close-button material-icons" @click="toggleSidebarX()">clear</i>
        </div>
        <p class="header">Handedness</p>
        <div class="handedness-buttons">
            <span class="btn" @click="changeHandedness('L')">
                <i
                    class="left-hand material-icons"
                    :class="{'active-hand': activeHand === 'L'}">pan_tool</i>
            </span>
            <span class="btn" @click="changeHandedness('R')">
                <i
                    class="right-hand material-icons"
                    :class="{'active-hand': activeHand === 'R'}">pan_tool</i>
            </span>
        </div>
        <Court />
        <Filters :filterOptions="filterOptions" />
    </div>
</template>

<script>
import Court from './Court.vue'
import Filters from './Filters.vue'

export default {
    name: "Sidebar",
    components: {
        Court,
        Filters
    },
    props: ["filterOptions", "activeHand"],
    methods: {
        changeHandedness: function(newHandedness) {
            this.$emit('change-handedness', newHandedness);
        },
        toggleSidebarX: function() {
            this.$emit('toggle-sidebar-x');
        }
    }
}
</script>

<style scoped>
#sidebar {
  width: 300px;
  position: fixed;
  z-index: 1;
  top: 0;
  bottom: 0;
  left: 0;
  padding-top: 40px;
  padding-bottom: 100px;
  padding-left: 40px;
  overflow-y: scroll;
  background-color: #222831;
  color: white;
}
#burger-close {
    position: relative;
}
.burger-close-button {
    z-index: 5;
    color: white;
    position: relative;
    margin-left: 205px;
    font-size: 2rem;
}
.burger-button:hover {
    cursor: pointer;
    color: #f05454;
}
.header {
    margin-top: 0px;
    margin-bottom: 8px;
    font-size: 18px;
}
.handedness-buttons {
    padding-bottom: 10px;
    margin-bottom: 20px;
}
.btn {
    padding-left: 0px;
    padding-right: 5px;
}
.btn:hover {
    cursor: pointer;
    color: #f05454;
}
.right-hand {
    transform: scale(-1, 1);
}
.active-hand {
    color: #f05454;
}
</style>