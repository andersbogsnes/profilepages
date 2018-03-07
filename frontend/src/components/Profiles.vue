<!--suppress ALL -->
<template>
<div>
    <div class="column is-flex">
      <figure class="image is-96x96">
        <img :src="getImage(type)">
      </figure>
    </div>
    <div class="columns">
      <div class="column">
      <section class="section">
        <h1 class="title">Prisorienteret</h1>
        <h2 class="subtitle">Du er prisorienteret!</h2>
      </section>
    </div>
      </div>
  </div>
</template>

<script>
  import Radgiver from '../assets/radgiversogende.png';
  import Helhed from '../assets/helhedsorienterede.png';
  import Pris from '../assets/prisfokuserede.png';
  import Selv from '../assets/selvkorende.png';

  export default {
    name: "profiles",
    props: ['type'],
    data() {
      return {
        images: {
          Rådgiversøgende: Radgiver,
          Helhedsorienteret: Helhed,
          Prisorienteret: Pris,
          Selvkørende: Selv
        }
      }
    },
    methods: {
      getImage(type) {
        return this.images[type]
      }
    }
  }
</script>


<style scoped>
  .is-flex {
    justify-content: center;
  }
</style>
