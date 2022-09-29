<template>
  <div>
    <login v-if="!getUser"/>
  </div>
</template>

<script>
import login from '../components/login.vue';
export default {
  components: { 
    login 
  },
  name: 'IndexPage',
  computed: {
    getUser() {
      console.log(this.$store.state);
      return this.$store.state.user;
    },
  }
}
</script>
