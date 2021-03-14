<template>
  <div id="app">
    <img class="main-bg-img" src="./static/tty.png">
    <CardModal
      id="modal"
      :isOpen="state.modalOpen" 
      :modalData="state.activeCard" />
    <Sidebar
      id="sidebar"
      :filterOptions="filterOptions"
      :activeHand="handedness"
      :class="{closed: hideSidebar}"
      @change-handedness="changeHandedness"/>
    <Table
      id="table"
      :tableData="filteredDeceptionData"
      :class="{open: !hideSidebar}"
      @toggle-sidebar="toggleSidebar" />
  </div>
</template>



<script>
import Sidebar from './components/Sidebar.vue';
import Table from './components/Table.vue';
import CardModal from './components/CardModal.vue'
import { store } from './store.js';


// load json data from external file
import jsonLeft from './static/deceptionDataLeft.json' 
import jsonRight from './static/deceptionDataRight.json' 

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
      hideSidebar: window.innerWidth <= 600,
      deceptionDataL: jsonLeft,
      deceptionDataR: jsonRight,
      handedness: "R",
      filterOptions: {
        gripOptions: {
          F: true,
          B: true
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
    toggleSidebar: function() {
      this.hideSidebar === true ? this.hideSidebar = false : this.hideSidebar = true;
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
      return ["F", "B"].filter(
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
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap');
.main-bg-img {
  background-repeat: no-repeat;
  width: 1500px;
  opacity: 0.1;
  position: absolute;
  right: 0;
}
#app {
  font-family: Noto Sans JP, Helvetica, Arial, sans-serif;
  color: #222831;
  background-color: white;
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


/* MEDIA QUERIES */
@media (max-width: 600px) {
  /* #app {
    overflow-x: hidden;
  } */
  #table {
    margin-left: 30px;
  }
  .closed {
    display: none;
  }
  .open {
    padding-left: 300px;
  }
}
</style>
