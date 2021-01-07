<template>
  <v-app>
    <header-top-bar />
    <v-main>
      <HelloWorld />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import HelloWorld from './components/HelloWorld.vue';
import HeaderTopBar from './layout/global/HeaderTopBar.vue';

export default Vue.extend({
  name: 'App',
  components: {
    HelloWorld,
    HeaderTopBar,
  },

  data: () => ({
    //
  }),
});
</script>
