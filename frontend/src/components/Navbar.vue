<template>
  <nav class="navbar" role="navigation">
    <div class="navbar-brand">
      <a href="#" class="navbar-item">
        <figure class="image is-64x64">
          <router-link to="/">
            <img src="../assets/logo.png">
          </router-link>
        </figure>
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
    <a class="navbar-item" v-if="loggedIn">
      Status
    </a>
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
