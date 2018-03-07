<!--suppress ALL -->
<template>
  <div>
  <div class="columns">
      <div class="column is-flex">
        <billede :type="type"></billede>
      </div>
    </div>
    <div class="columns">
      <component :is="type"></component>
    </div>
    </div>
</template>

<script>
  import Billede from './Billede';
  import Raadgiver from './Raadgiversoegende';
  import Prisorienteret from './Prisorienteret';

  export default {
    name: "profiles",
    props: ['type'],
    components: {
      'Billede': Billede,
      'Raadgiversoegende': Raadgiver,
      'Prisorienteret': Prisorienteret,
    },
  }
</script>


<style scoped>
  .is-flex {
    justify-content: center;
  }
</style>
