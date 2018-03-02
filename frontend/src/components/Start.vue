<template>
<section class="section">
    <div class="container">
      <router-link class="button is-large" to="/signup" v-if="!isLoggedIn">Start!</router-link>
      <router-link class="button is-large" to="/questions" v-else>Start!</router-link>
    </div>
</section>
</template>

<script>
  export default {
    name: 'start',
    props: ['isLoggedIn']
  }
</script>
<style scoped lang="scss">
</style>
