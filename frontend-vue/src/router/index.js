/**
 * Router - Configuração de rotas da aplicação
 * 
 * Como agora é uma aplicação de página única:
 * - / (Home): Única página que contém toda a funcionalidade
 * - Outras rotas redirecionam para a página inicial
 */

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
      meta: { title: 'DescomplicaCV - Conversor de Currículos' }
    },
    {
      path: '/:pathMatch(.*)*',
      redirect: '/'  // Redireciona qualquer rota não encontrada para a home
    }
  ],
})

export default router
