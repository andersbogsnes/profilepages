import Vue from 'vue';
import Router from 'vue-router';
import Questions from './components/Questions';
import Start from './components/Start';
import Login from './components/Login';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Start',
      component: Start
    },
    {
      path: '/login',
      name: 'Login',
      component: Login
    },
    {
      path: '/questions',
      name: 'Questions',
      component: Questions
    }
  ]
})
