<template>
  <svg :height="base_height" :width="base_width"></svg>
</template>

<script>
  import * as d3 from 'd3';

  export default {
    name: "graph2",
    props: ['graphData', 'base_height', 'base_width'],
    data() {
      return {
        width: 0,
        height: 0,
        margins: {
          top: 15,
          bottom: 25,
          left: 90,
          right: 40
        }
      }
    },
    mounted() {
      this.drawGraph()
    },
    methods: {
      drawGraph() {
        this.height = this.base_height - this.margins.top - this.margins.bottom;
        this.width = this.base_width - this.margins.left - this.margins.right;
        let data = this.graphData.sort((a, b) => d3.ascending(a.percentScore, b.percentScore));
        let svg = d3.select(this.$el);
        let g = svg.append("g")
          .attr("transform", `translate(${this.margins.left}, ${this.margins.top})`);
        let x = d3.scaleLinear().range([0, this.width]).domain([0, d3.max(data, (d) => d.percentScore)]);
        let y = d3.scaleBand().rangeRound([this.height, 0]).padding(0.1).domain(data.map(d => d.profileName));

        g.append("g")
          .attr("class", "axis axis--x")
          .attr("transform", `translate(0, ${this.height})`)
          .call(d3.axisBottom(x).ticks(10));

        g.append("g")
          .attr("class", "axis axis--y")
          .call(d3.axisLeft(y));

        let bars = g.selectAll('.bar')
          .data(data)
          .enter()
          .append('g');

        bars.append('rect')
          .attr("class", "bar")
          .attr("x", 0)
          .attr("y", (d) => y(d.profileName))
          .attr("width", 0)
          .transition()
          .ease(d3.easeExpInOut)
          .duration(2000)
          .attr("width", (d) => x(d.percentScore))
          .attr("height", y.bandwidth());

        bars.append('text')
          .attr("class", "labels")
          .attr("y", (d) => y(d.profileName) + y.bandwidth() / 2 + 4)
          .attr("x", (d) => x(d.percentScore) + 3)
          .text((d) => d.percentScore.toFixed(1))
      }
    }
  }
</script>

<style lang="scss">
  @import '../../sass/base';
  .bar {
    fill: $primary;

  }

  .axis path {
    display: none;
  }

</style>
