/**
 * API Service - Serviços para comunicação com o backend
 * 
 * Este arquivo contém:
 * - Configuração do cliente Axios
 * - Métodos para comunicação com a API do backend
 * 
 * Funcionalidades:
 * - Upload de arquivo de currículo
 * - Processamento da resposta (PDF)
 */

// Exemplo de implementação simplificada:
// import axios from 'axios'

// const apiClient = axios.create({
//   baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000',
//   headers: {
//     'Content-Type': 'multipart/form-data',
//     'Accept': 'application/json'
//   }
// })

// export const cvService = {
//   async convertCV(file) {
//     const formData = new FormData()
//     formData.append('file', file)
//     
//     const response = await apiClient.post('/convert-cv', formData, {
//       responseType: 'blob'
//     })
//     
//     return response.data
//   }
// }
