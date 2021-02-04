<template>
    <div>
        <h1>Filters</h1>
        <h3>Position</h3>
            <input type="checkbox" id="net" name="net" value="net" v-model="computedFilterOptions.positionOptions.net">
            <label for="net"> Net</label><br>

            <input type="checkbox" id="front" name="front" value="front" v-model="computedFilterOptions.positionOptions.front">
            <label for="front"> Front</label><br>

            <input type="checkbox" id="mid" name="mid" value="mid" v-model="computedFilterOptions.positionOptions.mid">
            <label for="mid"> Mid</label><br>

            <input type="checkbox" id="back" name="back" value="back" v-model="computedFilterOptions.positionOptions.back">
            <label for="back"> Back</label><br>
        <h3>Grip</h3>
            <input type="checkbox" id="forehand" name="forehand" value="forhand" v-model="computedFilterOptions.gripOptions.forehand">
            <label for="forehand"> Forehand</label><br>

            <input type="checkbox" id="backhand" name="backhand" value="backhand" v-model="computedFilterOptions.gripOptions.backhand">
            <label for="backhand"> Backhand</label><br>
    </div>
</template>

<script>

export default {
    name: "Filters",
    components: {},
    props: ["filterOptions"],
    computed: {
        // v-model mutates parent data
        computedFilterOptions: function() {
            return this.filterOptions;
        }
    }
}
</script>

<style scoped>

</style>