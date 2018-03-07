<template>
  <div class="container">
    <div class="columns">

      <div class="column" v-if="results">
        <profile :type="topScore()" />
      </div>
      <div class="column" v-else>
        <h1 class="title">Du mangler at udfylde spørgeskemaet!</h1>
        <h2 class="subtitle">Vi kan ikke klassificere dig uden dine besvarelser</h2>
        <h2 class="subtitle">
          <router-link to="/questions" class="button is-primary">Start!</router-link>
        </h2>
      </div>

      <div class="column">
        <graph :graphData="results" :base_height="height" :base_width="width" v-if="results"/>
      </div>
    </div>
  </div>
</template>

<script>
  import {getUrl, URLS} from "../../api/api";
  import Scores from "./Scores";
  import Graph from "./Graph";
  import Profile from "./Profiles";

  export default {
    name: "status",
    components: {
      'scores': Scores,
      'graph': Graph,
      'profile': Profile
    },
    data() {
      return {
        results: undefined,
        height: 240,
        width: 480
      }
    },
    methods: {
      topScore() {
        const maxVal = Math.max(...this.results.map(o => o.percentScore));
        return this.results.find(o => o.percentScore === maxVal).profileName
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
