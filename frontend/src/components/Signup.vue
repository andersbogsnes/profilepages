<template>
  <div class="container">
    <div class="columns">
      <div class="column is-6">
        <h1 class="title">Tilmeld Dig!</h1>
        <h2 class="subtitle">Allerede tilmeldt? <router-link to="/login">Login!</router-link></h2>
        <div class="field">
          <label class="label">Navn</label>
          <div class="control">
            <input class="input" type="text" placeholder="Skriv dit navn" v-model="name">
          </div>
        </div>

        <div class="field">
          <label class="label">Initialer</label>
          <div class="control has-icons-left">
            <input class="input" type="text" placeholder="Skriv dine AB initialer" v-model="initials">
            <span class="icon is-small is-left">
              <i class="fas fa-user"></i>
            </span>
          </div>
        </div>

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

        <div class="field">
          <label class="label">Gentag dit Passord</label>
          <div class="control has-icons-left">
            <input class="input"
                   :class="{'is-danger': !validPass}"
                   type="password"
                   placeholder="Skriv dit passord igen"
                   v-model="repeatPass"
            >
            <span class="icon is-small is-left">
              <i class="fas fa-key"></i>
            </span>
          </div>
          <p class="help is-danger" v-if="!validPass">Passord matcher ikke</p>
        </div>

        <div class="field" v-if="userExists">
          <p class="help is-danger">Denne bruger eksistere allerede</p>
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
        name: '',
        initials: '',
        email: '',
        password: '',
        repeatPass: '',
        userExists: false,
      }
    },
    computed: {
      validForm() {
        return (this.name !== '' && this.initials !== ''
          && this.email !== '' && this.password !== ''
          && this.repeatPass !== '' && this.validPass);

      },
      validPass() {
        if (this.repeatPass === '') return true;
        return this.repeatPass === this.password
      }
    },
    methods: {
      submit() {
        let formData = {
          user_name: this.name,
          initials: this.initials,
          email: this.email,
          password: this.password
        };
        HTTP.post('/user', formData).then((e) => {
          this.userExists = false;
          this.$emit('loggedIn', e.data.data);
          this.$router.push('/questions')
        }).catch((error) => {
          if (error.response.status === 403)
            this.userExists = true;
        })

      },
    }
  }
</script>

<style scoped>

</style>
