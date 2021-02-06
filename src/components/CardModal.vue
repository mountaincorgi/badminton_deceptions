<template>
   <div>
      <div v-if="isOpen">
          <h1>Modal heading</h1>
          <p>This my first modal using vue.js</p>
      </div>
   </div>
</template>

<script>
export default {
    name: "CardModal",
    props: ["activeCard", "isOpen"]
}
</script>

<style scoped>

</style>