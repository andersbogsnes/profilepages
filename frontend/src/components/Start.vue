<template>
    <div class="container">
      <div class="section">
      <h2 class="subtitle">Du vil blive stillet 11 spørgsmål - baseret på det vil du få at vide hvilken personalitet du er</h2>
      <router-link class="button is-large" to="/signup" v-if="!isLoggedIn">Start!</router-link>
      <router-link class="button is-large" to="/questions" v-else>Start!</router-link>
        </div>
    </div>
</template>

<script>
  export default {
    name: 'start',
    props: ['isLoggedIn']
  }
</script>
<style scoped lang="scss">
</style>
