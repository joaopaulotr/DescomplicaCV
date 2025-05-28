<script setup>
/**
 * HomeView.vue - Página única da aplicação
 * 
 * Esta é a página principal que contém toda a funcionalidade:
 * - Título e descrição breve da aplicação
 * - Formulário para upload do currículo
 * - Lógica de processamento e download do PDF
 * - Feedback para o usuário
 */
import { ref } from 'vue';

// Refs para gerenciar estado
const selectedFile = ref(null);
const isProcessing = ref(false);
const message = ref({ show: false, type: '', text: '' });

// Função para lidar com a seleção de arquivo
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    selectedFile.value = file;
  }
};

// Função para remover o arquivo selecionado
const removeFile = () => {
  selectedFile.value = null;
  // Reset do input file
  const fileInput = document.getElementById('cv-file');
  if (fileInput) fileInput.value = '';
};

// Função para processar o arquivo
const processFile = async () => {
  if (!selectedFile.value) return;
  
  isProcessing.value = true;
  message.value = { show: true, type: 'info', text: 'Processando seu currículo...' };
  
  try {
    // Em um app real, aqui você faria uma chamada à API
    // const formData = new FormData();
    // formData.append('file', selectedFile.value);
    // const response = await fetch('http://localhost:8000/convert-cv', {
    //   method: 'POST',
    //   body: formData
    // });
    
    // Simulando um delay de processamento
    await new Promise(resolve => setTimeout(resolve, 2000));
    
    // Simulação de sucesso
    message.value = { show: true, type: 'success', text: 'CV processado com sucesso! O download começará automaticamente.' };
    
    // Em uma aplicação real:
    // const blob = await response.blob();
    // const url = window.URL.createObjectURL(blob);
    // const a = document.createElement('a');
    // a.href = url;
    // a.download = 'curriculo-convertido.pdf';
    // document.body.appendChild(a);
    // a.click();
    // document.body.removeChild(a);
    
    // Resetando o arquivo após processamento
    setTimeout(() => {
      removeFile();
      isProcessing.value = false;
    }, 3000);
    
  } catch (error) {
    message.value = { show: true, type: 'error', text: 'Erro ao processar o arquivo. Tente novamente.' };
    isProcessing.value = false;
  }
};
</script>

<template>
  <div class="home">
    <h1>DescomplicaCV</h1>
    <p>Converta seu currículo para um template profissional em segundos</p>
    
    <!-- Upload Form -->
    <div class="upload-container">
      <form @submit.prevent="processFile" class="upload-form">
        <div class="file-input-container">
          <input
            type="file"
            id="cv-file"
            @change="handleFileChange"
            accept=".pdf,.docx,.doc,.txt"
            class="file-input"
          />
          <label for="cv-file" class="file-label">
            <div v-if="!selectedFile">
              <span class="upload-icon">📄</span>
              <p>Clique para selecionar seu currículo</p>
              <small>Formatos aceitos: PDF, DOCX, TXT</small>
            </div>
            <div v-else class="file-selected">
              <p class="file-name">{{ selectedFile.name }}</p>
              <button type="button" class="remove-file-btn" @click="removeFile">×</button>
            </div>
          </label>
        </div>
        
        <button type="submit" class="submit-btn" :disabled="!selectedFile || isProcessing">
          {{ isProcessing ? 'Processando...' : 'Converter Currículo' }}
        </button>
      </form>
      
      <!-- Message Area -->
      <div v-if="message.show" :class="['message', message.type]">
        {{ message.text }}
      </div>
    </div>
  </div>
</template>

<style scoped>
.home {
  text-align: center;
  padding: 2rem 0;
  max-width: 600px;
  margin: 0 auto;
}

.upload-container {
  margin-top: 2rem;
}

.upload-form {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.file-input-container {
  position: relative;
}

.file-input {
  opacity: 0;
  position: absolute;
  z-index: -1;
}

.file-label {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 2px dashed #ccc;
  border-radius: 8px;
  padding: 2rem;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  min-height: 150px;
}

.file-label:hover {
  border-color: #4f46e5;
  background-color: rgba(79, 70, 229, 0.05);
}

.upload-icon {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.file-selected {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.file-name {
  font-weight: 500;
  word-break: break-all;
}

.remove-file-btn {
  background: none;
  border: none;
  color: #ef4444;
  font-size: 1.5rem;
  cursor: pointer;
  padding: 0;
}

.submit-btn {
  background-color: #4f46e5;
  color: white;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 0.375rem;
  border: none;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.2s;
}

.submit-btn:hover {
  background-color: #4338ca;
}

.submit-btn:disabled {
  background-color: #9ca3af;
  cursor: not-allowed;
}

.message {
  margin-top: 1.5rem;
  padding: 1rem;
  border-radius: 0.375rem;
}

.info {
  background-color: #e0f2fe;
  color: #0369a1;
}

.success {
  background-color: #dcfce7;
  color: #15803d;
}

.error {
  background-color: #fee2e2;
  color: #b91c1c;
}
</style>
