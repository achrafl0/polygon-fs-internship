<template>
  <div id="app">
    <v-app>
      <header-top-bar />
      <v-main>
        <v-content class="expand-height">
          <!-- Transitions to add a bit more style -->
          <transition name="fade" mode="out-in">
            <router-view />
          </transition>
        </v-content>
      </v-main>
    </v-app>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import HeaderTopBar from './layout/global/HeaderTopBar.vue';

export default Vue.extend({
  name: 'App',
  components: {
    HeaderTopBar,
  },

  data: () => ({
    //
  }),
});
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.center {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.align-center {
  text-align: center;
}

.fade-enter-active,
.fade-leave-active {
  transition-duration: 0.2s;
  transition-property: opacity;
  transition-timing-function: ease;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
.expand-height {
  height: 100%;
}
</style>
