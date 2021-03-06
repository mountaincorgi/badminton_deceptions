<template>
    <div id="filters">
        <p class="header">Position</p>
            <input type="checkbox" id="net" name="net" value="net" v-model="computedFilterOptions.positionOptions.net">
            <label class="cbl" for="net"> Net</label><br>

            <input type="checkbox" id="front" name="front" value="front" v-model="computedFilterOptions.positionOptions.front">
            <label class="cbl" for="front"> Front</label><br>

            <input type="checkbox" id="mid" name="mid" value="mid" v-model="computedFilterOptions.positionOptions.mid">
            <label class="cbl" for="mid"> Mid</label><br>

            <input type="checkbox" id="back" name="back" value="back" v-model="computedFilterOptions.positionOptions.back">
            <label class="cbl" for="back"> Back</label><br>
        <p class="header">Grip</p>
            <input type="checkbox" id="forehand" name="forehand" value="forhand" v-model="computedFilterOptions.gripOptions.forehand">
            <label class="cbl" for="forehand"> Forehand</label><br>

            <input type="checkbox" id="backhand" name="backhand" value="backhand" v-model="computedFilterOptions.gripOptions.backhand">
            <label class="cbl" for="backhand"> Backhand</label><br>
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
input[type="checkbox"] { /* change "blue" browser chrome to yellow */
  filter: hue-rotate(140deg) brightness(0.9);
}
.header {
    margin-bottom: 5px;
    font-size: 18px;
}
.cbl {
    font-size:16px;
}
#filters {
    padding-top: 10px;
}
</style>