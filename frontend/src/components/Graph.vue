<template>
  <svg :height="height + margins.top + margins.bottom" :width="width + margins.left + margins.right">
    <transition-group tag="g" :transform="`translate(${margins.left}, ${margins.top})`">
      <text :x="d.x + d.width / 2" :y="d.y - 5" text-anchor="middle" v-for="d in layout" :key="d.value">{{ d.value.toFixed(1) }}</text>
      <rect :x="d.x"
            :y="d.y"
            :height="d.height"
            :width="d.width"
            :key="`bar-${d.value}`"
            v-for="d in layout">
      </rect>
      </transition-group>
  </svg>
</template>

<script>
  import * as d3 from 'd3';

  export default {
    name: "graph",
    props: ['graphData', 'width', 'height'],
    data() {
      return {
        x: 0,
        y: 0,
        margins: {
          top: 20,
          bottom: 20,
          left: 20,
          right: 20
        }
      }
    },
    created() {
      this.xscale = d3.scaleBand();
      this.yscale = d3.scaleLinear();

    },
    computed: {
      layout() {
        this.xscale
          .rangeRound([0, this.width])
          .padding(0.1)
          .domain(this.graphData.map(d => d.profileName));
        this.yscale
          .rangeRound([this.height, 0])
          .domain([0, d3.max(this.graphData, function(d) {return d.percentScore})]);


        return this.graphData.map((d) => {
          return {
            x: this.xscale(d.profileName),
            height: this.height - this.yscale(d.percentScore),
            value: d.percentScore,
            width: this.xscale.bandwidth(),
            y: this.yscale(d.percentScore)
          }
        })
      },

      }
  }
</script>

<style scoped>
  rect {
    fill: #00b9ea;
  }
</style>
