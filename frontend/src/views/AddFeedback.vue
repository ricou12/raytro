<template>
  <h1>Votre feedback de la semaine</h1>
<!--  <BubbleBox-->
<!-- content="Vous êtes invité chaque semaine à renseigner votre 'feedback' ou, en d'autres termes, les choses que vous avez aimé ou pas."/> -->

  <form class="grid" @submit.prevent="() => {}">
    <div class="s5 good">
      <h2 class="h2">&#129321; Ce que j'ai aimé</h2>
        <input
            v-for="(item, $index) in writingFeedback.liked"
            v-model="writingFeedback.liked[$index]"
            type="text"
            class="feedback-item"
            :placeholder="`${$index > 0? 'Un autre ?' :
            'Ajoutez un avis positif au moins'}`"
            :key="$index">
    </div>
    <span class="filler s1"></span>
    <div class="s5 bad">
      <h2 class="h2">&#129324; Ce que je n'ai pas aimé</h2>
        <input
            v-for="(item, $index) in writingFeedback.disliked"
            v-model="writingFeedback.disliked[$index]"
            type="text"
            class="feedback-item"
            :placeholder="`${$index > 0? 'Un autre ?' :
            'Ajoutez un avis négatif au moins'}`"
            :key="$index">
      <!-- btn demande de confirmation -->
      <button id="show-modal" @click="showModal" class="cta button">Envoyer mon feedback</button>
      <!-- Le composant modal est ajouté si la directive v-if remplit les conditions,
       ici la variable showmodal est initialisé à false, la condition n'est pas remplit le composant ne s'affiche pas.-->
      <Modal v-show="isModalVisible" @close="closeModal" @confirm="confirm" title="Feedback" textBody="Voulez-vous envoyer votre feedback ?"></Modal>
      <!-- <button @click="sendFeedback" class="cta button">Envoyer mon feedback</button> -->
      <button @click="skip" class="text button">Voir les feedback</button>
    </div>

  </form>
</template>

<script lang="ts">
import { Vue, Options, } from 'vue-class-component'
import { mapGetters, } from 'vuex'
import router from '@/router'
import Feedback from '@/models/Feedback'
import { sendFeedback, } from '@/api/feedback'
import BubbleBox from '@/components/BubbleBox.vue'
import Modal from '@/components/modal.vue'

@Options({
  computed: { ...mapGetters(['firstName', 'isLoggedIn',]), },
  components: { BubbleBox,Modal, },
})
export default class AddFeedback extends Vue {
  // showModal = false
  isModalVisible = false
  firstName: string | undefined
  isLoggedIn: string | undefined

  feedback: Feedback = new Feedback()

  get writingFeedback (): Feedback {
    const existsEmptyLike = this.feedback.liked.filter(item => item.length <= 0).length > 0
    const existsEmptyDislike = this.feedback.disliked.filter(item => item.length <= 0).length > 0
    const output = new Feedback()
    output.liked = this.feedback.liked
    output.disliked = this.feedback.disliked

    if (!existsEmptyLike) {
      output.liked.push('')
    }
    if (!existsEmptyDislike) {
      output.disliked.push('')
    }
    console.log(JSON.parse(JSON.stringify(output)))
    return output
  }

  skip () : void {
    router.push('/feedbacks')
  }

  sendFeedback (): void {
    this.feedback.clean()
    if (this.feedback.isValid()) {
      sendFeedback(this.feedback)
        .then(data => {
          console.log('GG, cest enregistré', data)
          router.push('/feedbacks')
        })
      console.log('send fiiiidback', JSON.stringify(this.feedback))
    }
    else {
      console.log('le feedback n\'est pas au top')
    }
  }

  showModal (): void {
    this.isModalVisible = true
  }

  closeModal (): void {
    this.isModalVisible = false
  }

  confirm (): void {
    this.sendFeedback()
    // this.showModal = false
  }
}
</script>

<style lang="stylus">
  @import '../main.styl'
  .feedback-item {
    display block
    width 100%
    margin-bottom 20px
  }
  .good input[type=text].feedback-item {
    color GOOD !important
  }
  .bad input[type=text].feedback-item {
    color BAD !important
  }

  .btn {
  padding: 8px 16px;
  border-radius: 5px;
  &--primary {
    background-color: green;
    color: #fff;
  }
  &--secondary {
    background-color: #dddd;
    color: #000;
  }
}

// utilities
.overflow-hidden {
  overflow: hidden;
}
.mx-auto {
  margin-left: auto;
  margin-right: auto;
}
.d-flex {
  display: flex;
}
.align-items-center {
  align-items: center;
}
.justify-content-between {
  justify-content: space-between;
}
// reset
button {
  background: none;
  border: none;
  outline: inherit;
  cursor: pointer;
}
</style>
