<template>
  <div>
    <div v-for="result in results">
      <h1 class="title">{{ result.profileName }}</h1>
      <h2 class="subtitle"> {{ result.percentScore.toFixed(1) }}%</h2>
    </div>
  </div>
</template>

<script>

  export default {
    name: "status",
    props: ['results']
  }
</script>

<style scoped>

</style>
