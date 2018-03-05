<template>
  <div>
    <div v-for="result in results">
      <h1 class="title">{{ result.type_name }}</h1>
      <h2 class="subtitle"> {{ result.percent_score.toFixed(1) }}%</h2>
    </div>
  </div>
</template>

<script>
  import { HTTP} from "../api/api";

  export default {
    name: "status",
    props: ['id'],
    data() {
      return {
        results: undefined
      }
    },

    mounted() {
      HTTP.get(`/result/${this.id}`).then((response) => {
        console.log(response.data);
        this.results = response.data.data;
      }).catch((error) => console.log(error))
    }
  }
</script>

<style scoped>

</style>
