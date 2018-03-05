<template>
  <nav class="navbar" role="navigation">
    <div class="navbar-brand">
      <a href="#" class="navbar-item">
        <router-link to="/">
          <figure class="image is-64x64">
            <img src="../assets/logo.png">
          </figure>
        </router-link>
      </a>
    </div>
  <div class="navbar-start">
    <router-link class="navbar-item" to="/">
      Home
    </router-link>
  </div>
  <div class="navbar-end">
    <router-link class="navbar-item" v-if="!loggedIn" to="/login">
      Login
    </router-link>
    <a class="navbar-item" v-if="loggedIn" @click="logOut">
      Logout
    </a>
    <router-link class="navbar-item" v-if="loggedIn" to="/status">
      Status
    </router-link>
  </div>
  </nav>
</template>

<script>
  export default {
    name: "navbar",
    props: ['loggedIn'],
    methods: {
      logOut() {
        this.$emit('loggedOut');
        this.$router.push('/');
      }
    }
  }
</script>

<style scoped lang="scss">
  @import "../sass/base";
  $navbar-background-color: $secondary;
  $navbar-item-color: $white;
  $navbar-item-img-max-height: 64px;
  @import '~bulma';

</style>
