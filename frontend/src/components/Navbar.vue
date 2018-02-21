<template>
  <nav class="navbar" role="navigation">
    <div class="navbar-brand">
      <a href="#" class="navbar-item">
        <img src="../assets/logo.png">
      </a>
    </div>
  <div class="navbar-start">
    <a class="navbar-item">
      Home
    </a>
  </div>
  <div class="navbar-end">
    <a class="navbar-item" v-if="!loggedIn">
      Login
    </a>
    <a class="navbar-item" v-if="loggedIn">
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
    props: ['loggedIn']
  }
</script>

<style scoped lang="scss">
  @import "../sass/base";
  $navbar-background-color: $primary;
  @import '~bulma';

</style>
