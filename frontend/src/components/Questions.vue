<template>
  <div class="container">
    <div class="columns">
      <div class="column is-6">
        <transition name="slide" mode="out-in">
          <question :questionText="currentQuestion.questionText"
                    :questionScore.sync="currentQuestion.questionScore"
                    :key="questionNr"/>
        </transition>
      </div>
    </div>
    <div class="columns">
      <div class="column is-2">
        <a class="button is-primary"
           v-if="this.questionNr!==0"
           @click="next(-1)">
          Forrige
        </a>
      </div>
      <div class="column is-2">
        <a class="button is-primary"
           v-if="questionNr!==questions.length -1"
           @click="next(1)">
          Næste
        </a>
        <a class="button is-primary" v-else
           @click="submit()">
          Submit
        </a>
      </div>
    </div>
  </div>
</template>

<script>
  import Question from './Question';
  import axios from 'axios';
  import { HTTP }from '../api/api';

  export default {
    components: {
      question: Question,
    },
    mounted() {
      this.loadData();
    },

    data() {
      return {
        questionNr: 0,
        questions: [
          {
            questionText: "",
            questionScore: undefined
          },
        ],
      }
    },
    computed: {
      currentQuestion() {
        return this.questions[this.questionNr]
      }
    },

    methods: {
      next(value) {
        let new_choice = this.questionNr + value;

        if (new_choice < 0) {
          new_choice = 0;
        }

        if (new_choice > this.questions.length - 1) {
          new_choice = this.questions.length - 1;
        }

        this.questionNr = new_choice;
      },

      submit() {
        let responses = this.questions.map((e, i) => {
          return {
            "questionNr": i +1,
            "value": e.questionScore
          }
        });

        let data = {
          responses,
          token: window.localStorage.getItem('token')
      };
        console.log(data);
        HTTP.post('/answer', data).then((response) => {
          console.log(response.data)
        })
      },
      loadData() {
        HTTP.get('/questions').then((response) => {
          this.questions = response.data.map((e) => {
            return {
              id: e.id,
              questionText: e.text,
              questionScore: undefined
            }
          })
          }
        ).catch((error) => {
          console.log(error)
        })
      }
    }
  }
</script>

<style scoped>
  .slide-enter-active { animation: fade-in 300ms}
  .slide-leave-active { animation: fade-out 300ms}

  @keyframes fade-in {
    0% {
      transform: translateX(-100px);
      opacity: 0
    }
  50% {
    opacity: 0.5;
  }
    100% {
      transform: translateX(0px);
      opacity: 1;
    }
  }

  @keyframes fade-out {
    0% {
      transform: translateX(0);
      opacity: 1;
    }
    100% {
      transform: translateX(100px);
      opacity: 0;
    }
  }
</style>
