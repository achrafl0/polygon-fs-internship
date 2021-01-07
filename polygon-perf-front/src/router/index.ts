import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import PerformanceView from '../views/PerformanceView.vue';
import HomeView from '../views/HomeView.vue';

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: '/performances',
    name: 'Performances',
    component: PerformanceView,
  },
  {
    path: '/home',
    name: 'Home',
    component: HomeView,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
