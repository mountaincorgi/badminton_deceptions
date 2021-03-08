<template>
  <div>
    <transition name="modal">
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
  width: 680px;
  height: 480px;
  margin: 0px auto;
  padding: 20px;
  background-color: #222831;
  box-shadow: 0 1px 2px 2px;
  transition: visibility 1s;
  overflow-y: scroll;
  overflow: hidden;
  border-radius: 5px;
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
  color: white;
  position: relative;
  min-height: 350px;
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
  background-color: #30475e;
}
.tutorial-label {
  display: inline-block;
  width: 100px!important;
}
.tab [type=radio] {
  display: none;   
}
.video-content {
  position: absolute;
  top: 60px;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 20px;
  background: #222831;
}
[type=radio]:checked ~ label {
  z-index: 20;
  background-color: #30475e;
}
[type=radio]:checked ~ label ~ .video-content {
  z-index: 1;
}

/* Modal button */
button {
  position: absolute;
  padding: 7px;
  margin-top: 10px;
  background-color: #222831;
  border: 0px;
  border-radius: 5px;
  color: white;
  left: 400px;
  outline: none;
}
button:hover {
  cursor: pointer;
  background-color: #30475e;
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
  background: #00000094;
  z-index: 100;
}
</style>