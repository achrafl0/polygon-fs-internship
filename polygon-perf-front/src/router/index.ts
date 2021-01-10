import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import PerformanceView from '../views/PerformanceView.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '*',
    name: 'Performances',
    component: PerformanceView,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
