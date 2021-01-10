<template>
  <v-container fluid class="performance-container">
    <span class="text-h6">Over the last {{ since }}</span>
    <v-divider />
    <v-col>
      <v-row class="text-subtitle-1 font-weight-bold" light>
        <v-col>
          Avg
        </v-col>
        <v-col>
          Min
        </v-col>
        <v-col>
          Max
        </v-col>
      </v-row>
      <v-row>
        <v-col>
          {{ perfData.avg_resp.toFixed(2) }}
        </v-col>
        <v-col>
          {{ perfData.min_resp.toFixed(2) }}
        </v-col>
        <v-col>
          {{ perfData.max_resp.toFixed(2) }}
        </v-col>
      </v-row>
    </v-col>
  </v-container>
</template>
<script lang="ts">
/* eslint-disable @typescript-eslint/no-unused-vars */
import Vue, { PropType } from 'vue';
import { PerformanceData } from '../../types';

export default Vue.extend({
  props: {
    since: String,
    perfData: {
      type: Object as PropType<PerformanceData>,
      required: true,
    },
  },
});
</script>
<style lang="scss">
.performance-container {
  background-color: #d5ffff;
  color: black;
  margin-top: 1em;
}
</style>
