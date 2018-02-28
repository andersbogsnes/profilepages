<template>
  <div id="app">
    <nav-bar :logged-in="loggedIn"/>
    <hero />
    <section class="section">
      <start v-if="!started" @start="started = !started"/>
      <questions v-else/>

  </section>
  </div>
</template>

<script>
  import Navbar from './components/Navbar';
  import Hero from './components/Hero';
  import Start from './components/Start';
  import Questions from './components/Questions';

export default {
  name: 'app',
  components: {
    'NavBar': Navbar,
    'Hero': Hero,
    'Start': Start,
    'Questions': Questions
  },
  data () {
    return {
      loggedIn: true,
      started: false,
    }
  }
}
</script>

<style lang="scss">
  @import '/sass/base.scss';

  html {
    background-color: $white;
  }
  #app {
    font-family: 'Work Sans', sans-serif;
  }
</style>
