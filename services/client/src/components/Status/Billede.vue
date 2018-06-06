<!--suppress NonAsciiCharacters, JSNonASCIINames -->
<template>
  <figure class="image is-128x128">
    <img :src="getImage(type)">
  </figure>
</template>

<script>
  import Radgiver from '../../assets/radgiversogende.png';
  import Helhed from '../../assets/helhedsorienterede.png';
  import Pris from '../../assets/prisfokuserede.png';
  import Selv from '../../assets/selvkorende.png';

  export default {
    name: "billede",
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

</style>
