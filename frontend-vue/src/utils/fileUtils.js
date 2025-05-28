/**
 * FileUtils - Utilitários para manipulação de arquivos
 * 
 * Este arquivo contém funções utilitárias para:
 * - Download de arquivos
 * - Validação de tipos de arquivo
 * - Formatação de tamanho de arquivo
 * 
 * Essas funções são reutilizáveis em toda a aplicação.
 */

// Exemplo de implementação simplificada:
// 
// /**
//  * Função para iniciar download de um arquivo
//  * @param {Blob} blob - O conteúdo do arquivo como Blob
//  * @param {string} fileName - Nome do arquivo para download
//  */
// export const downloadFile = (blob, fileName) => {
//   const url = window.URL.createObjectURL(blob)
//   const link = document.createElement('a')
//   link.href = url
//   link.setAttribute('download', fileName)
//   document.body.appendChild(link)
//   link.click()
//   link.remove()
//   window.URL.revokeObjectURL(url)
// }
//
// /**
//  * Valida se o tipo de arquivo é permitido
//  * @param {File} file - Arquivo para validar
//  * @param {Array} allowedTypes - Array de tipos MIME permitidos
//  * @returns {boolean} - Verdadeiro se o arquivo é válido
//  */
// export const isValidFileType = (file, allowedTypes) => {
//   return allowedTypes.includes(file.type)
// }
