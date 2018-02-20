<template>
  <div id="app">
    <nav-bar :logged-in="loggedIn"/>
    <hero />
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
    }
  }
}
</script>

<style lang="scss">
  @import '/sass/base.scss';
  @import '~bulma';
  @import url('https://fonts.googleapis.com/css?family=Work+Sans');
  html {
    background-color: $primary;
  }
  #app {
    font-family: 'Work Sans', sans-serif;
  }
</style>
