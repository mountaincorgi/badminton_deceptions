<template>
  <div id="app">
    <CardModal
      id="modal"
      :isOpen="state.modalOpen" 
      :modalData="state.activeCard" />
    <Sidebar
      id="sidebar"
      :filterOptions="filterOptions"
      :activeHand="handedness"
      @change-handedness="changeHandedness"/>
    <Table
      id="table"
      :tableData="filteredDeceptionData" />
  </div>
</template>



<script>
import Sidebar from './components/Sidebar.vue';
import Table from './components/Table.vue';
import CardModal from './components/CardModal.vue'
import { store } from './store.js';


// load json data from external file
import jsonLeft from './deceptionDataLeft.json' 
import jsonRight from './deceptionDataRight.json' 

export default {
  name: 'App',
  components: {
    Sidebar,
    Table,
    CardModal
  },
  data() {
    return {
      state: store.state,
      deceptionDataL: jsonLeft,
      deceptionDataR: jsonRight,
      handedness: "R",
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
      }
    }
  },
  methods: {
    changeHandedness: function(newHandedness) {
      if (this.handedness !== newHandedness) {
        this.handedness = newHandedness;
      } 
    },
    getDeceptionDataByHandedness: function() {
      if (this.handedness === "L") {
        return this.deceptionDataL;
      } else {
        return this.deceptionDataR;
      }
    },
    filterByPosition: function(data) {
      return data.filter(d => this.selectedCategories.includes(d.category));
    },
    filterByGrip: function(data) {
      return data.filter(d => this.selectedGrips.includes(d.grip));
    } 
  },
  computed: {
    selectedCategories: function() {
      return ["net", "front", "mid", "back"].filter(
        c => this.filterOptions.positionOptions[c] === true
      );
    },
    selectedGrips: function() {
      return ["forehand", "backhand"].filter(
        g => this.filterOptions.gripOptions[g] === true
      );
    },
    filteredDeceptionData: function() {
      let d1 = this.getDeceptionDataByHandedness().deceptions;
      let d2 = this.filterByPosition(d1);
      let d3 = this.filterByGrip(d2);
      let selectedCategories = this.selectedCategories;

      // build filtered data object
      let filteredData = {categories: []};

      // add each category to filteredData if filter is true
      for (let i=0; i<selectedCategories.length; i++) {
        let categoryName = selectedCategories[i];
        let deceptions = d3.filter(d => d.category === categoryName);
        if (deceptions.length !== 0) {
          filteredData.categories.push({
            id: i+1,
            name: categoryName,
            deceptions: deceptions
          });
        }
      }
      return filteredData;
    }  // filteredDeceptionData 
  }  // computed
}
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  color: #515070;
  background-color: #f6f6f6;
}
p {
  font-size: 1rem;
}
#table {
  margin-left: 370px;
  padding-top: 0px;
}
#modal {
  margin-left: 370px;
  padding-top: 40px;
}
.stuff {
  margin-left: 400px;
}
.test {
  margin-left: 400px;
}
</style>
