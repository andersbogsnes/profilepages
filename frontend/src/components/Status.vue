<template>
  <div class="container">
    <div class="columns">
      <scores v-if="results" :results="results"/>
      <div v-else>
        <h1 class="title">Du mangler at udfylde spørgeskemaet!</h1>
        <h2 class="subtitle">Vi kan ikke klassificere dig uden dine besvarelser</h2>
        <div class="columns">
          <h2 class="subtitle">
            <router-link to="/questions" class="button is-primary">Start!</router-link>
          </h2>
        </div>
      </div>
    </div>
    <div class="columns">
      <graph :graphData="results" v-if="results"/>
    </div>
  </div>
</template>

<script>
  import {getUrl, URLS} from "../api/api";
  import Scores from "./Scores";
  import Graph from "./Graph";

  export default {
    name: "status",
    components: {
      'scores': Scores,
      'graph': Graph
    },
    data() {
      return {
        results: undefined,
        height: 300,
        width: 300
      }
    },

    mounted() {
      getUrl(URLS.result).then((response) => {
        this.results = response.data.data;
      }).catch((error) => console.log(error))
    }
  }
</script>

<style scoped>

</style>
