<template>

  <div :class="`main  ${isLoggedIn? ' container': ''}`">
    <img v-if="isLoggedIn" class="mini-logo" :src="`${publicPath}img/logo.svg`" alt="">
    <router-view/>
  </div>
  <img class="back" :src="`${publicPath}img/background-artifact.svg`" alt="">
</template>
<script lang="ts">
import { Vue, Options, } from 'vue-class-component'
import { mapGetters, } from 'vuex'
import router from '@/router'

@Options({
  computed: { ...mapGetters(['isLoggedIn',]), },
})
export default class App extends Vue {
  publicPath: string = (process.env as any).BASE_URL
  isLoggedIn: boolean | undefined
  store = (this as any).$store

  created (): void {
    /**
     * Ce hook permet de vérifier que l'utilisateur est connecté avant de passer
     * à une autre page : s'il ne l'est pas, il est redirigé vers la page de connexion
     */
    router.beforeEach((to, from, next) => {
      (!this.isLoggedIn && to.name !== 'Login') ? next({ name: 'Login', }) : next()
    })
  }
}

</script>

<style lang="stylus">
@import 'main.styl'

.back {
  position fixed
  top 30vh
  left 0
  min-width 95vw
  min-height 70vh
  z-index 0
}
.main {
  z-index 100
  position relative
}
.container {
  background LIGHT
  margin 10vh auto 0 auto
  padding 36px 32px
  border-radius 8px
  box-shadow: 4px 4px 64px rgba(66, 66, 66, 0.25)
}
.main.container {
  margin 10vh 64px 64px 48px
  min-height 60vh
  padding 1px 64px 18px 96px
}
.mini-logo {
  width 100px
  position absolute
  top 18px
  left -5px
}

</style>