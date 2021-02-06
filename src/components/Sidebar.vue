<template>
    <div id="sidebar">
        <p>Sidebar</p>
        <div class="handedness-buttons">
            <strong>
                <span class="left" @click="changeHandedness('L')">LEFT</span> | 
                <span class="right" @click="changeHandedness('R')">RIGHT</span>
            </strong></div>
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
    props: ["filterOptions"],
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
  background-color: beige;
  padding-top: 45px;
  padding-bottom: 100px;
  padding-left: 40px;
  overflow-y: scroll;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
#sidebar::-webkit-scrollbar {
  display: none;
}
.left:hover {
    color: red;
    cursor: pointer;
}
.right:hover {
    color: blue;
    cursor: pointer;
}
</style>