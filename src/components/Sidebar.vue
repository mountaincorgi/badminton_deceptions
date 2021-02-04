<template>
    <div>
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

</style>