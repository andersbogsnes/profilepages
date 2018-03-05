<template>
  <div class="container">
    <div class="columns">
      <div class="column is-6">
        <h1 class="title">Log Ind</h1>
        <h2 class="subtitle">Ikke tilmeldt endnu? <router-link to="/signup">Tilmeld dig!</router-link></h2>

        <div class="field">
          <label class="label">Email</label>
          <div class="control has-icons-left">
            <input class="input" type="email" placeholder="Skriv din email" v-model="email">
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
          </div>
        </div>

        <div class="field">
          <label class="label">Passord</label>
          <div class="control has-icons-left">
            <input class="input" type="password" placeholder="Skriv dit passord" v-model="password">
            <span class="icon is-small is-left">
              <i class="fas fa-key"></i>
            </span>
          </div>
        </div>

        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link" :disabled="!validForm" @click="submit">Submit</button>
          </div>
          <div class="control">
            <router-link to="/">
              <button class="button is-text">Cancel</button>
            </router-link>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  import { HTTP } from "../api/api";

  export default {
    name: "login",
    data() {
      return {
        email: '',
        password: '',
        invalidUser: false
      }
    },
    computed: {
      validForm() {
        return this.email !== '' && this.password !== '';
      },
    },
    methods: {
      submit() {
        let formData = {
          email: this.email,
          password: this.password
        };
        HTTP.post('/login', formData).then((response) => {
          this.invalidUser = false;
          this.$emit('loggedIn', response.data.data);
          this.$router.push('/questions');
        }).catch((error) => {
          if (error.response.status === 404)
            this.invalidUser = true;
        })
      },
    }
  }
</script>

<style scoped>

</style>
