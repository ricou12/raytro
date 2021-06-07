<template>
  <div :class="`bubble shadowed ${type}`">
    <h2 class="title">{{ title }}</h2>
    <p class="text">{{ content }}</p>
    <div class="controls">

    </div>
  </div>
</template>

<script lang="ts">
import { Vue, Options, } from 'vue-class-component'
// import { stringifyQuery, } from 'vue-router'
// import { mapGetters, mapActions, mapMutations } from 'vuex'

// enum BubbleTypes {
//   waiting = 'waiting',
//   good = 'good',
//   warning = 'warning',
//   bad = 'bad',
// }

@Options({
  name: 'BubbleBox',
  props: {
    title: { type: String, },
    content: { type: String, default: 'Coucou', },
    type: { type: String, default: '', },
    duration: { type: Number, default: 0, },
  },
  // methods: { ...mapMutations[] },
  // components: { },
})
export default class BubbleBox extends Vue {
  title?: string|undefined
  content: string|undefined
  type: string|undefined
  duration: number|undefined

  /**
   * Si le composant est créé avec une durée d'affichage
   * on définit un timeout pour le cacher au moment souhaité
   */
  mounted (): void {
    setTimeout(this.show, 50)
    if (this.duration && this.duration > 0) {
      setTimeout(() => {
        this.hide()
        // setTimeout(() => {
        //   this.$el.classList.add('hidden')
        //   // this.$el.classList.remove('appear')
        //   this.$el.classList.remove('disappear')
        // }, 1000)
      }, 1000 * this.duration)
    }
  }

  show (): void {
    this.$el.classList.add('visible')
  }

  hide (): void {
    this.$el.classList.remove('visible')
  }
}

</script>

<style lang="stylus" scoped>
@import '../main.styl'

@keyframes blink {
  0% { opacity: .8 }
  70% { opacity: .9 }
}

.bubble {
  position: relative
  top: -20px
  opacity: 0
  background PRIMARY
  background #444
  border-left 5px solid GOOD
  padding 10px 10px
  font-weight bold
  border-radius 5px
  box-shadow 0 5px 10px #888 !important
  .title, .text {
    //font-family 'Schoolbell', cursive
    font-size .8em
    color LIGHT
    padding 0
    margin 0
  }
  .deco {
    font-size 5em
  }
  transition all .5s ease
}
.bubble.visible {
  top: 0
  opacity: 1
  transition all .5s ease
}
.waiting {
  animation-name blink
  animation-direction alternate
  animation-iteration-count infinite
  animation-duration: .3s
  animation-delay .5s
}
.error {
  border-left 5px solid BAD
}

.disappear {
  animation-name appear
  animation-duration 1s
  animation-iteration-count: infinite
  animation-direction reverse
}
.hidden {
  opacity 0
}

</style>
