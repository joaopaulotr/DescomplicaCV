/**
 * Store de demonstração que pode ser excluído
 * 
 * Este arquivo é um exemplo e pode ser substituído pelo cvStore
 * para gerenciar o estado do aplicativo.
 */

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {
  const count = ref(0)
  const doubleCount = computed(() => count.value * 2)
  function increment() {
    count.value++
  }

  return { count, doubleCount, increment }
})
