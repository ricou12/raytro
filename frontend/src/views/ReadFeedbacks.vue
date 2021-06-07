<template>
  <h1>Feedbacks de la semaine #{{ week.value }}</h1>
  <div class="toolbox">
    <button @click="goToWeek(week.value - 1)" class="mini button control">&#8249;</button>
    <button @click="goToWeek(currentWeek)" class="mini button control">Semaine en cours</button>
    <button @click="goToWeek(week.value + 1)" class="mini button control">&#8250;</button>
  </div>
  <ul class="feedbacks">
    <li
      v-for="(feedbackItem, $index) in feedbacks"
      :key="$index"
      :class="`post-it ${feedbackItem.type}`">{{ feedbackItem.comment }}</li>
  </ul>

</template>

<script lang="ts">
import { Vue, Options, } from 'vue-class-component'
import { ref, } from 'vue'
import FeedbackItem from '@/models/FeedbackItem'
import { getFeedbacks, } from '@/api/feedback'

@Options({
  name: 'Feedbacks',
})
export default class ReadFeedbacks extends Vue {
  feedbacks: Array<FeedbackItem> | undefined
  currentWeek: number | undefined
  year: number | undefined
  week: any

  created (): void {
    const now = new Date()
    this.feedbacks = []
    this.year = now.getFullYear()
    this.currentWeek = this.getWeekNumber(now) - 2
    this.week = ref(this.currentWeek)
    this.fetchFeedBacks()

    this.$watch('week.value', (value: number) => {
      console.log('new week', value)
    })
  }

  fetchFeedBacks (): void {
    getFeedbacks(this.year, this.week.value)
      .then(data => {
        this.feedbacks = []
        for (const item of data) {
          this.feedbacks.push(new FeedbackItem(item[4],item[3],item[1],item[2]))
        }
        this.$forceUpdate()
      })
  }

  goToWeek (weekNumber: number): void {
    this.week.value = weekNumber
    this.fetchFeedBacks()
  }

  getWeekNumber (date: Date): number {
    const firstDayOfYear = new Date(date.getFullYear(), 0, 1)
    const pastDaysOfYear = (date.getTime() - firstDayOfYear.getTime()) / 86400000
    return Math.ceil((pastDaysOfYear + firstDayOfYear.getDay() + 1) / 7)
  }
}

</script>

<style lang="stylus">
@import url('https://fonts.googleapis.com/css2?family=Schoolbell&display=swap');

.feedbacks {
  display flex
  flex-wrap wrap
  margin 0
  padding 0
}
.post-it {
  font-family: 'Schoolbell', cursive;
  display block
  background #d9ce95
  padding 5px 20px 20px 10px
  min-width 180px
  max-width 260px
  min-height 80px
  margin 0 20px 20px 0
  color #0d4458
  box-shadow 3px 5px 8px #ccc
}
.liked.post-it {
  border-top 20px solid #a6d4c3
  background #AFDBCB
}
.disliked.post-it {
  border-top 20px solid #d6a9c1
  background #DBAFC7
}
  .toolbox {
    position absolute
    top 0
    right 0
  }
</style>
