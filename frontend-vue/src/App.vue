<script setup>
import HomeView from './views/HomeView.vue'

/**
 * App.vue - Componente raiz do aplicativo
 * 
 * Este é o componente principal da aplicação que contém:
 * - Layout básico (header, main, footer)
 * - Importa e renderiza diretamente o HomeView
 * 
 * Como é uma aplicação de página única, o conteúdo é renderizado diretamente
 * sem usar o RouterView
 */
</script>

<template>
  <header>
    <!-- Cabeçalho da aplicação -->
    <h1>DescomplicaCV</h1>
  </header>

  <main>
    <!-- Área principal com o HomeView renderizado diretamente -->
    <HomeView />
  </main>

  <footer>
    <!-- Rodapé da aplicação -->
    <p>&copy; 2025 DescomplicaCV</p>
  </footer>
</template>

<style scoped>
/* Estilos básicos para a estrutura da página */
header, main, footer {
  padding: 1rem;
  max-width: 1200px;
  margin: 0 auto;
}

nav {
  margin: 1rem 0;
}

nav a {
  margin-right: 1rem;
}

footer {
  margin-top: 2rem;
  text-align: center;
}
</style>
