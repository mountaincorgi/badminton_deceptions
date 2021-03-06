<template>
  <div>
    <transition name="modal">
      <div v-if="isOpen">
        <div class="overlay" @click="toggleModal">
          <div class="modal" @click.stop>
            <p>{{modalData.name}}</p>
            <iframe width="400px" height="270px" src="https://www.youtube.com/embed/s-HfFmgkPQ8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            <p>{{modalData.links}}</p>
            <p>{{modalData.grip}}</p>
            <p>{{modalData.category}}</p>
            <p>{{modalData.fromPosition}}</p>
            <p>{{modalData.expectedPosition}}</p>
            <p>{{modalData.actualPosition}}</p>
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
button {
  padding: 7px;
  margin-top: 10px;
  background-color: green;
  color: white;
  font-size: 1.1rem;
}

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