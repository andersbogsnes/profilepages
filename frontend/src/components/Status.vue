<template>
  <div class="container">
    <div class="columns">

      <div class="column">
        <scores v-if="results" :results="results"/>
        <div v-else>
          <h1 class="title">Du mangler at udfylde spørgeskemaet!</h1>
          <h2 class="subtitle">Vi kan ikke klassificere dig uden dine besvarelser</h2>

          <h2 class="subtitle">
            <router-link to="/questions" class="button is-primary">Start!</router-link>
          </h2>
        </div>
      </div>

      <div class="column">
        <graph2 :graphData="results" :height="height" :width="width" v-if="results"/>
      </div>
    </div>
  </div>
</template>

<script>
  import {getUrl, URLS} from "../api/api";
  import Scores from "./Scores";
  import Graph from "./Graph";
  import Graph2 from "./Graph2";
  export default {
    name: "status",
    components: {
      'scores': Scores,
      'graph': Graph,
      'graph2': Graph2
    },
    data() {
      return {
        results: undefined,
        height: 480,
        width: 640
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
