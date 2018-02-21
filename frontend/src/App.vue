<template>
  <div id="app">
    <nav-bar :logged-in="loggedIn"/>
    <hero />
    <div class="container">
      <start v-if="!started" @start="started = !started"/>
      <question v-else
                :question="currentQuestion"
                :end="questionNr === questions.length - 1"
                @next="updateQuestionNr"
      @submit="submit"/>
    </div>
  </div>
</template>

<script>
  import Navbar from './components/Navbar';
  import Hero from './components/Hero';
  import Start from './components/Start';
  import Question from './components/Question';

export default {
  name: 'app',
  components: {
    'NavBar': Navbar,
    'Hero': Hero,
    'Start': Start,
    'Question': Question
  },
  data () {
    return {
      loggedIn: true,
      started: false,
      questionNr: 0,
      questions: [
        {
          questionText: "Test 1",
          questionScore: undefined
        },
        {
          questionText: "Test 2",
          questionScore: undefined
        }
      ],
    }
    },
  computed: {
    currentQuestion() {
      return this.questions[this.questionNr]
    },

  },
  methods: {
    updateQuestionNr(value, choice) {
      console.log(value);
      console.log(choice);
      this.questions[this.questionNr].questionScore = choice;

      if (this.questionNr + value < 0) {
        this.questionNr = 0;
      }
      else if (this.questionNr + value >= this.questions.length) {
        this.questionNr = this.questions.length - 1
      }
      else {
        this.questionNr += value;
      }
    },
    submit() {
      console.log(this.questions)
    }
  }
}
</script>

<style lang="scss">
  @import '/sass/base.scss';
  @import '~bulma';
  @import url('https://fonts.googleapis.com/css?family=Work+Sans');
  html {
    background-color: $white;
  }
  #app {
    font-family: 'Work Sans', sans-serif;
  }
</style>
