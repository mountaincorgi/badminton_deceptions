<template>
  <div id="modal-container">
    <div v-if="isOpen">
      <!-- Overlay -->
      <div class="overlay" @click="toggleModal">

        <!-- Modal -->
        <div class="modal" @click.stop>
          <!-- Media container -->
          <div class="video-container">

            <!-- Tabs -->
            <div class="video-tabs">
              <!-- Toggle visibility button -->
              <button @click="toggleModal">X</button>
              <!-- Video tabs -->
              <div v-for="(link, index) in modalData.links" :key="index" class="tab">
                <input type="radio" :id="'t' + index" name="tab-group" :checked="index==0">
                <label :for="'t' + index" class="tab">{{index + 1}}</label>
      
                <div class="video-content">
                  <div v-html="link"></div>
                </div> 
              </div>
              <!-- Tutorial tab -->
              <div class="tab">
                <input type="radio" id="tutorial-tab" name="tab-group">
                <label for="tutorial-tab" class="tutorial-label">Tutorial</label>
      
                <div class="video-content">
                  <p>Coming soon!</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Modal content -->
          <div class="modal-content">
            <!-- {{ modalData.description }} -->
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { store } from '../store.js';

export default {
    name: "CardModal",
    props: ["isOpen", "modalData"],
    methods: {
        toggleModal: function() {
            store.toggleModal();
        }
    }
}
</script>

<style scoped>
/* Modal */
.modal {
  width: 680px;
  height: 480px;
  padding: 20px;
  margin: 0px auto;
  background-color: white;
  color: #30475e;
  box-shadow: 0 1px 2px 2px;
  border-radius: 5px;
  overflow: hidden;
}

/* Tabs */
.video-tabs {
  position: relative;
  height: 80%;
  width: 80%;
  clear: both;
}
.tab {
  float: left;
}
.tab label {
  display: inline-block;
  text-align: center;
  border: 2px solid #30475e;
  border-radius: 5px;
  padding: 5px 15px 8px 15px;
  margin: 10px;
  position: relative;
  left: 8px;
}
.tab label:hover {
  cursor: pointer;
}
.tutorial-label {
  display: inline-block;
  width: 100px;
}
.tab [type=radio] {
  display: none;   
}
.video-content {
  position: absolute;
  height: 500px;
  width: 630px;
  left: 0;
  top: 60px;
  padding: 20px;
  background: white;
}
[type=radio]:checked ~ label {
  z-index: 20;
  border-color: #f05454;
  color: #f05454;
}
[type=radio]:checked ~ label ~ .video-content {
  z-index: 1;
}

/* Modal button */
button {
  position: absolute;
  padding: 7px;
  margin-top: 10px;
  background-color: white;
  border: 0px;
  border-radius: 5px;
  color: #30475e;
  left: 400px;
  outline: none;
}
button:hover {
  cursor: pointer;
  color: #f05454;
}

/* Modal overlay */
.overlay {
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
  background: #00000050;
  z-index: 100;
}


/* MEDIA QUERIES */
@media (max-width: 600px) {
  .modal {
    width: 80%;
  }
  .video-tabs {
    padding-top: 8px;
    height: 500px;
  }
  .tab label {
    margin: 5px;
    padding: 0px 5px 0px 5px;
  }
  .video-content {
    width: 108%;
    height: 400px;
  }
  button {
    left: 250px;
  }
}
</style>