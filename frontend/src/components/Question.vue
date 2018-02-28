<template>
        <div class="columns">
          <div class="column">
            <h1 class="title"> {{ questionText }}</h1>
            <div class="columns">
              <div class="column is-centered">
                <div class="control">
                  <label class="radio" v-for="n in 5">
                    <input type="radio"
                           :key="n"
                           :value="n"
                           :checked="questionScore === n"
                    @click.number="updateChoice($event.target.value)">
                    {{ n }}
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
</template>

<script>
  export default {
    name: "question",
    props: ["questionText", "questionScore"],
    methods: {
      updateChoice(value) {
        this.$emit('update:questionScore', Number.parseInt(value))
      }
    }
  }
</script>

<style scoped>

</style>
