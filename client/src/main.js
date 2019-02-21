import Vue from 'vue'
import App from './App.vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Project from '@/components/Project'
import Space from '@/components/Space'

import './../node_modules/bulma/css/bulma.css';
Vue.config.productionTip = false
Vue.use(Router)


const router = new Router({
	mode: 'history',
  routes: [
    { path: '/', name: 'Main', component: Main },
    { path: '/project/:id', name: 'Project', component: Project },
    { path: '/space/:id', name: 'Space', component: Space },

  ],
});

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
