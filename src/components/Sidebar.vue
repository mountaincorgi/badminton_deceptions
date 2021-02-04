<template>
    <div id="sidebar">
        <h1>Sidebar</h1>
        <Court />
        <Filters v-bind:filterOptions="filterOptions" />
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
    props: ["filterOptions"]
}
</script>

<style scoped>
#sidebar {
  height: 100%;
  width: 300px;
  position: fixed;
  z-index: 1;
  top: 0;
  bottom: 0;
  left: 0;
  background-color: beige;
  padding-top: 45px;
  padding-left: 40px;
  overflow-y: scroll;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
#sidebar::-webkit-scrollbar {
  display: none;
}
</style>