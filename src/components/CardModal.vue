<template>
  <div>
    <transition name="modal">
      <div v-if="isOpen">
        <div class="overlay" @click="toggleModal">
          <div class="modal" @click.stop>

            <!-- Media container -->
            <div class="video-container">
              <!-- Tabs -->
              <div class="video-tabs">
                <!-- Video tabs -->
                <div v-for="(link, index) in modalData.links" :key="index" class="tab">
                  <input type="radio" :id="'t' + index" name="tab-group" :checked="index==0">
                  <label :for="'t' + index">{{index + 1}}</label>
       
                  <div class="video-content">
                    {{ link }}
                  </div> 
                </div>
                <!-- Tutorial tab -->
                <div class="tab">
                  <input type="radio" id="tutorial-tab" name="tab-group">
                  <label for="tutorial-tab">Tutorial</label>
       
                  <div class="video-content">
                    <p>Coming soon!</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Modal content -->
            <div class="content">
              <p>Good for catching the opponent out!</p>
            </div>

            <!-- Toggle visibility button -->
            <button @click="toggleModal">Close</button>
          </div>
        </div>
      </div>
    </transition>
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
  width: 500px;
  height: 500px;
  margin: 0px auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px 3px;
  transition: visibility 1s;
  overflow-y: scroll;
  border-radius: 20px;
}
.fadeIn-enter {
  opacity: 0;
}
.fadeIn-leave-active {
  opacity: 0;
  transition: opacity 1s;
}
.fadeIn-enter .modal,
.fadeIn-leave-active.modal {
  transform: scale(1.1);
}

/* Tabs */
.video-tabs {
  position: relative;
  min-height: 200px;
  clear: both;
  margin: 25px 0;
}
.tab {
  float: left;
  width: 50px;
}
.tab label {
  background: #eee; 
  padding: 10px; 
  border: 1px solid #ccc; 
  margin-left: -1px; 
  position: relative;
  left: 1px;
}
.tab [type=radio] {
  display: none;   
}
.video-content {
  position: absolute;
  top: 28px;
  left: 0;
  background: white;
  right: 0;
  bottom: 0;
  padding: 20px;
  border: 1px solid #ccc; 
}
[type=radio]:checked ~ label {
  background: white;
  border-bottom: 1px solid white;
  z-index: 20;
}
[type=radio]:checked ~ label ~ .video-content {
  z-index: 1;
}

/* Modal button */
button {
  padding: 7px;
  margin-top: 10px;
  background-color: green;
  color: white;
  font-size: 1.1rem;
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
  background: #00000094;
  z-index: 999;
  transition: opacity 0.2s ease;
}
</style>