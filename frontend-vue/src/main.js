/**
 * main.js - Ponto de entrada da aplicação Vue
 * 
 * Este arquivo é responsável por:
 * - Inicializar a instância do Vue
 * - Registrar plugins (router, pinia, etc)
 * - Montar o aplicativo no elemento DOM
 */

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import './assets/main.css'

const app = createApp(App)

app.use(createPinia())
app.use(router)

app.mount('#app')
