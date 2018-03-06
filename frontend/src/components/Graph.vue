<template>
  <svg :height="this.height" :width="this.width">
    <g :transform="`translate(${margins.top}, ${margins.bottom})`">
    <text :x="d.x + d.width / 2" :y="d.y - 5" text-anchor="middle" v-for="d in layout">{{ d.value.toFixed(1) }}</text>
      <rect :x="d.x"
            :y="d.y"
            :height="d.height"
            :width="d.width" v-for="d in layout">
      </rect>
      </g>
  </svg>
</template>

<script>
  import * as d3 from 'd3';

  export default {
    name: "graph",
    props: ['graphData'],
    data() {
      return {
        width: undefined,
        height: undefined,
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
    mounted() {
      this.width = this.$el.clientWidth || 300;
      this.height = this.$el.clientHeight || 150;
    },
    computed: {
      layout() {
        const max_y = d3.max(this.graphData.map(d => d.percentScore));
        const x_values = this.graphData.map(d => d.profileName);
        this.yscale.range([0, this.height - this.margins.top - this.margins.bottom]).domain([0, max_y]);
        this.xscale.rangeRound([0, this.width]).padding(0.1).domain(x_values);

        return this.graphData.map((d) => {
          return {
            x: this.xscale(d.profileName),
            height: this.yscale(d.percentScore),
            value: d.percentScore,
            width: this.xscale.bandwidth(),
            y: this.yscale.range()[1] - this.yscale(d.percentScore)
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
