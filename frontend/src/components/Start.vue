<template>
<section class="section">
    <div class="container">
      <a class="button is-large" @click="startQuiz">Start!</a>
    </div>
</section>
</template>

<script>
  export default {
    name: 'start',
    methods: {
      startQuiz: function () {
        this.$emit('start')
      }
    },
  }
</script>
<style scoped lang="scss">
</style>
