<template>
<div id="graph"></div>
</template>

<script>
  import * as d3 from 'd3';
  export default {
    name: "graph2",
    props: ['graphData'],
    data() {
      return {
        width: 640,
        height: 480,
        margins: {
          top: 15,
          bottom: 25,
          left: 60,
          right: 25
        }
      }
    },
    mounted() {
      this.drawGraph()
    },
    methods: {
      drawGraph() {
        svg = d3.select('#graph').append('svg').attr("width", this.width + this.margins.right + this.margins.left).attr("height", this.height + this.margins.bottom + this.margins.top);
        g = svg.append("g")
          .attr("transform", `translate(${this.margin.left}, ${this.margin.top}`);
        let x = d3.scaleLinear().range([0, this.width]).domain([0, d3.max(this.graphData, (d) => d.percentScore)]);
        let y = d3.scaleBand().rangeRound([this.height, 0]).padding(0.1).domain(this.graphData.map(d => d.profileName));

        g.append("g")
          .attr("class", "axis axis--x")
          .attr("transform", `translate(0, ${this.height}`)
          .call(d3.axisBottom(x).ticks(10, '%'));

        g.append("g")
          .attr("class", "axis axis--y");

        bars = svg.selectAll('.bar')
          .data(this.graphData)
          .enter()
          .append('g');

        bars.append('rect')
          .attr("class", "bar")
          .attr("x", 0)
          .attr("y", (d) => y(d.profileName))
          .attr("width", (d) => x(d.percentScore));

        bars.append('text')
          .attr("class", "labels")
          .attr("y", (d) => y(d.profileName) + y.rangeBand() / 2 + 4)
          .attr("x", (d) => x(d.percentScore) + 3)
          .text((d) => d.percentScore)
      }
    }
  }
</script>

<style scoped>

</style>
