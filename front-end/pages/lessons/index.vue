<template>
  <div>
    <h1>My Lessons</h1>
    <lesson-card v-for="lesson in lessons" :key="lesson.id" :lesson="lesson" />
  </div>
</template>

<script>
import LessonCard from '../../components/LessonCard.vue'

export default {
  name: 'LessonList', // eslint-disable-line no-eval
  components: {
    LessonCard
  },
  data () {
    return {
      lessons: this.$store.state.lessons
    }
  }
}
</script>

<style>

</style>
