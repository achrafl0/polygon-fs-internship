<template>
  <div class="center align-center expand-height">
    <v-dialog v-model="dialog" width="80%" max-width="400">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="black lighten-2" dark v-bind="attrs" v-on="on">
          Performances
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="headline">
          <span>Performances</span>
          <v-spacer></v-spacer>
          <v-btn @click="dialog = false" color="white" depressed>
            <span>Close </span>
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        <v-spacer></v-spacer>
        <v-card-text>
          <div v-for="(perfdata, since) in performanceData" v-bind:key="since">
            <performance-card v-bind:since="since" v-bind:perfData="perfdata" />
          </div>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import PerformanceCard from '../components/performance-view/PerformanceCard.vue';
import { getPerformances } from '../services/ApiRequests';
import { ServerPerformanceData } from '../types';

export default Vue.extend({
  data() {
    return {
      dialog: false,
      performanceData: {} as ServerPerformanceData,
    };
  },
  components: {
    PerformanceCard,
  },
  mounted: function mounted() {
    this.fetchPerformanceData();
  },

  methods: {
    async fetchPerformanceData() {
      this.performanceData = (await getPerformances()) as ServerPerformanceData;
      console.log(this.performanceData);
    },
  },
});
</script>
