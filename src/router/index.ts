import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import AdmissionView from '@/views/AdmissionView.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Поступление',
    component: AdmissionView,
  },
  {
    path: '/transaction',
    name: 'Перевод',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '@/views/TransactionView.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
