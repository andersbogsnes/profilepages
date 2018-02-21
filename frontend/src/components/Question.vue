<template>
  <div class="columns">
    <div class="column is-6 is-offset-3">
      <div class="box">
        <div class="columns">
          <div class="column is-offset-4">
            <h1 class="title"> {{ question.questionText }}</h1>
            <div class="columns">
              <div class="column is-centered">
                <div class="control">
                  <label class="radio" v-for="n in 5">
                    <input type="radio"
                           :key="n"
                           :value="n"
                           :checked="question.questionScore === n"
                           v-model="choice">
                    {{ n }}
                  </label>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="columns">
          <div class="column is-centered">
            <a class="button is-large is-pulled-left" @click="next(-1)">Sidste</a>
            <a class="button is-large is-pulled-right"
               @click="submit"
               v-if="end"
            >Submit</a>
            <a class="button is-large is-pulled-right"
               @click="next(1)"
               v-else
            >Næste</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: "question",
    props: ['question', "end"],
    data() {
      return {
        choice: 0
      }
    },
    methods: {
      next(value) {
        this.$emit('next', value, this.choice)
      },
      submit() {
        this.$emit('submit')
      }
    }
  }
</script>

<style scoped lang="scss">
</style>
