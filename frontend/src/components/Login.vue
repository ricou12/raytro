<!--
  Ce composant contient tous les éléments techniques permettant de se connecter.
-->
<template>
  <form>
    <label for="identifiant">Identifiant</label>
    <input id="identifiant" type="email" :value="login">
    <label for="password">Mot de passe</label>
    <input id="password" type="password" :value="password">
    <input type="submit" value="Me connecter !">
  </form>
</template>

<script lang="ts">
import { Vue } from 'vue-class-component'
import { login } from '@/api/feedback'

export default class LoginForm extends Vue {
  login = ''
  password = ''

  checkCredentials (): void {
    login(this.login, this.password)
  }
}

</script>
