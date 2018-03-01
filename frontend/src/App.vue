<template>
  <div id="app">
    <nav-bar :logged-in="loggedIn"/>
    <hero />
    <section class="section">
      <router-view />
  </section>
  </div>
</template>

<script>
  import Navbar from './components/Navbar';
  import Hero from './components/Hero';


export default {
  name: 'app',
  components: {
    'NavBar': Navbar,
    'Hero': Hero,
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
