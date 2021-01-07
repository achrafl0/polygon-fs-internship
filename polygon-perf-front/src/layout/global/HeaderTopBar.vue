<template>
  <v-app-bar app color="white">
    <div class="d-flex align-center">
      <v-img
        alt="Polygon Logo"
        contain
        :src="require('../../assets/logo.svg')"
        transition="scale-transition"
        width="20"
      />

      <v-img
        alt="Polygon Name"
        class="shrink mt-1 hidden-sm-and-down"
        contain
        min-width="100"
        :src="require('../../assets/logo.png')"
        width="100"
      />
    </div>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue';

export default Vue.extend({
  name: 'HeaderTopBar',
});
</script>

<style></style>
