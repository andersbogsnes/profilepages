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
      started: false,
      token: ''
    }
  },
  mounted() {
    this.token = window.localStorage.getItem('token') || '';
  },
  computed: {
    loggedIn: function () {
      return this.token !== '';
    }
  },
  methods: {
    logIn(data) {
      window.localStorage.setItem('token', data.auth);
      this.token = data.auth;
    },

    logOut() {
      this.token = '';
      window.localStorage.removeItem('token');
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
