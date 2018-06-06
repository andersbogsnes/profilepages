<template>
    <picture :type="type"> </picture>
</template>

<script>
  import Picture from './Billede';

  export default {
    name: "raadgiversoegende",
    components: {
      'picture': Picture,
    },
    data() {
      return {
        type: 'Rådgiversøgende'
      }
    }
  }
</script>

<style scoped>

</style>
