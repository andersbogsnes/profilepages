<template>
  <div class="container">
    <div class="columns">
      <div class="column is-6">

        <div class="field">
          <label class="label">Navn</label>
          <div class="control">
            <input class="input" type="text" placeholder="Skriv dit navn" v-model="name">
          </div>
        </div>

        <div class="field">
          <label class="label">Initialer</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input" type="text" placeholder="Skriv dine AB initialer" v-model="initials">
            <span class="icon is-small is-left">
      <i class="fas fa-user"></i>
    </span>
            <span class="icon is-small is-right">
      <i class="fas fa-check"></i>
    </span>
          </div>
          <p class="help is-success">This username is available</p>
        </div>

        <div class="field">
          <label class="label">Email</label>
          <div class="control has-icons-left has-icons-right">
            <input class="input is-danger" type="email" placeholder="Skriv din email" v-model="email">
            <span class="icon is-small is-left">
      <i class="fas fa-envelope"></i>
    </span>
            <span class="icon is-small is-right">
      <i class="fas fa-exclamation-triangle"></i>
    </span>
          </div>
          <p class="help is-danger">This email is invalid</p>
        </div>


        <div class="field is-grouped">
          <div class="control">
            <button class="button is-link">Submit</button>
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
  export default {
    name: "login",
    data() {
      return {
        name: '',
        initials: '',
        email: ''
      }
    },
    methods: {
      submit() {
        let formData = {
          name: this.name,
          initials: this.initials,
          email: this.email
        };
        axios.post('http://localhost:5000/user', formData).then((e) => {
          this.$router.push('/questions')
        }).catch((error) => {
          console.log(error)
        })

      }
    }
  }
</script>

<style scoped>

</style>
