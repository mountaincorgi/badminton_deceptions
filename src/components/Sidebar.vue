<template>
    <div id="sidebar">
        <h5 class="header">Handedness</h5>
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
  background-color: #f6f6f6;
  color: #515070;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
.header {
    margin-top: 0px;
    margin-bottom: 8px;
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
    color: #ff8e6e;
}
.right-hand {
    transform: scale(-1, 1);
}
.active-hand {
    color: #ff8e6e;
}
</style>