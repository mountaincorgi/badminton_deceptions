<template>
  <div id="app">
    <Sidebar id="sidebar" :filterOptions="filterOptions" :activePositions="activePositions" />
    <Table id="table" :tableData="filteredDeceptionData" @change-active-positions="changeActivePositions" />
  </div>
</template>



<script>
import Sidebar from './components/Sidebar.vue';
import Table from './components/Table.vue';

// load json data from external file
import json from './deceptionData.json' 

export default {
  name: 'App',
  components: {
    Sidebar,
    Table
  },
  data() {
    return {
      deceptionData: json,
      filterOptions: {
        gripOptions: {
          forehand: true,
          backhand: true
        },
        positionOptions: {
          net: true,
          front: true,
          mid: true,
          back: true
        }
      },
      activePositions: {
        fromPosition: null,
        expectedPosition: null,
        actualPosition: null
      }
    }
  },
  computed: {
    filteredDeceptionData: function() {
      let filteredData = {
        categories: []
      }
      // add each category to filteredData if filter is true
      for (let c_id in this.deceptionData.categories) {
        let c = this.deceptionData.categories[c_id];

        if (this.filterOptions.positionOptions[c.name] == true) {
          let filteredCategory = {name: c.name, id: c.id, deceptions: []};

          // add each deception to filteredData if filter is true
          for (let d_id in c.deceptions) {
            let d = c.deceptions[d_id];
            if (this.filterOptions.gripOptions[d.grip] == true) {
              filteredCategory.deceptions.push(d);
            }
          }
          // only add the category if it contains 1 or more items
          if (filteredCategory.deceptions.length >= 1) {
            filteredData.categories.push(filteredCategory);
          }
        }
      }
      return filteredData;
    }  // filteredDeceptionData 
  },  // computed
  methods: {
    changeActivePositions(positions) {
      console.log("App positions before: " + this.activePositions);
      console.log("App positions to update: " + positions);
      this.activePositions = positions;
      console.log("App positions after: " + this.activePositions);

    }
  }
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
}
#table {
  margin-left: 370px;
  padding-top: 40px;
}
</style>
