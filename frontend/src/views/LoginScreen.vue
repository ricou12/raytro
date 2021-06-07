<template>
    <form class="shadowed container form" @submit.prevent="handleSubmit">
      <img class="logo" :src="`${publicPath}img/logo.svg`" alt="logo de l'application Raytro">
      <div v-if="signupMode">
        <label for="first-name">Prénom</label>
        <input class="field" id="first-name" type="text" v-model="firstName">
      </div>
      <label for="identifiant">Identifiant</label>
      <input class="field" id="identifiant" type="email" v-model="login">
      <br>
      <label for="password">Mot de passe</label>
      <input class="field" id="password" type="password" v-model="password">
      <br>

      <BubbleBox type="error" :duration="2" v-if="state === 'wrongCredentials'"
                 :content="`&#128574; ${errorMessage}`"/>
      <BubbleBox type="error" v-if="state === 'serverError'"
                 content="&#128128; Notre serveur à rencontré une erreur... Si le problème persiste, contactez-nous"/>

      <div v-if="state !== 'waitingServerResponse'">
        <input v-if="!signupMode" class="cta button" type="submit" value="Me connecter !">
        <button v-if="signupMode" class="cta button" @click.prevent="handleSubmit">M'inscrire</button>

        <button v-if="signupMode" @click.prevent=" signupMode = false" class="text button">Me connecter plutôt</button>
        <button v-if="!signupMode" @click.prevent=" signupMode = true" class="text button">Créer un compte</button>
      </div>
      <BubbleBox v-else-if="state !== ''" type="waiting" content="&#128373; Identification en cours"/>
<!--      <BubbleBox :duration="2" type="good" content="&#128373; Identification en cours"/>-->

  </form>
</template>

<script lang="ts">
import { mapGetters, mapMutations, } from 'vuex'
import { Options, Vue, } from 'vue-class-component'
import router from '@/router'
import { login, signup, } from '@/api/feedback'
import BubbleBox from '@/components/BubbleBox.vue'

enum LoginScreenStates {
  ready = 'ready',
  waitingServerResponse = 'waitingServerResponse',
  wrongCredentials = 'wrongCredentials',
  serverError = 'serverError',
}

// eslint-disable-next-line no-use-before-define
@Options({
  computed: { ...mapGetters(['firstName', 'isLoggedIn',]), },
  methods: { ...mapMutations(['FIRST_NAME', 'IS_LOGGED_IN', 'TOKEN', 'EMAIL',]), },
  name: 'LoginScreen',
  components: { BubbleBox, },

  watch: {
  },

})
export default class LoginScreen extends Vue {
  login = ''
  firstName = ''
  password = ''
  publicPath = process.env.BASE_URL
  isLoggedIn: string | undefined
  state: LoginScreenStates = LoginScreenStates.ready
  signupMode = false
  errorMessage = ''

  created (): void {
    if (this.isLoggedIn) {
      router.push('/')
    }

    this.$watch('signupMode', (value: boolean): void => {
      setTimeout(() => {
        const selector = value ? '#first-name' : '#identifiant'
        this.$el.querySelector(selector).focus()
      }, 250)
    })
  }

  mounted (): void {
    this.$el.querySelector('#identifiant').focus()
  }

  handleSubmit (): void {
    this.state = LoginScreenStates.waitingServerResponse
    if (this.signupMode) {
      console.log('Tentative de création')
      signup(this.firstName, this.login, this.password)
        .then(response => { this.handleSubmitResponse(response) })
        .catch(error => { console.error(error) })
    }
    else {
      console.log('Tentative de connexion')
      login(this.login, this.password)
        .then(response => {
          console.log(response)
          this.handleSubmitResponse(response)
        })
        .catch(error => {
          console.log(error); this.errorMessage = error.description; this.state =
          LoginScreenStates.wrongCredentials
        })
    }
  }

  handleSubmitResponse (response: any): void {
    console.log(response)
    if (response.status === 'success') {
      const payload = JSON.parse(atob(response.access_token.split('.')[1]));
      (this as any).FIRST_NAME(payload.first_name);
      (this as any).TOKEN(response.access_token);
      (this as any).EMAIL(payload.email);
      (this as any).IS_LOGGED_IN(true)
      router.push('write-feedback')
    }
    else {
      this.errorMessage = response.description
      this.state = LoginScreenStates.wrongCredentials
    }
  }
}
</script>

<style lang="stylus" scoped>
@import "../main.styl"

.form {
  width 432px
  min-height 591px
  margin 10vh auto 60px auto
  padding 36px 32px
  text-align center
}

.logo {
  margin-bottom 60px
}
label {
  margin-top 25px
}
input, button {
  width 100%
}
.field {
  margin-bottom 14px
}
.cta.button {
  margin-top 50px
}
</style>
