<template>
  <nav class="navbar" role="navigation">
    <div class="navbar-brand">
      <a href="#" class="navbar-item">
        <figure class="image is-64x64">
          <img src="../assets/logo.png">
        </figure>
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
    props: ['loggedIn'],
  }
</script>

<style scoped lang="scss">
  @import "../sass/base";
  $navbar-background-color: $secondary;
  $navbar-item-color: $white;
  $navbar-item-img-max-height: 64px;
  @import '~bulma';

</style>
