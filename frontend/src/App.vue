<template>
  <div id="app">
    <nav-bar :logged-in="loggedIn" @loggedOut="logOut"/>
    <hero />
    <section class="section">
      <router-view @loggedIn="logIn" :isLoggedIn="loggedIn"/>
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
      loggedIn: false,
      started: false,
    }
  },
  methods: {
    logIn(data) {
      this.loggedIn = true;
      window.localStorage.setItem('token', data.auth)
    },

    logOut() {
      this.loggedIn = false;
      window.localStorage.removeItem('token')
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
