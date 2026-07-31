# Atividade 15 - API REST (POST, PUT, DELETE)

## PASSO 1: Inserindo 15 livros novos via POST

### Comandos utilizados:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"O Alquimista","autor":"Paulo Coelho","ano":1988}'
```

### Livros inseridos:

| ID | Titulo | Autor | Ano |
|----|--------|-------|-----|
| 4 | O Alquimista | Paulo Coelho | 1988 |
| 5 | Capitaes da Areia | Jorge Amado | 1937 |
| 6 | A Hora da Estrela | Clarice Lispector | 1977 |
| 7 | Grande Sertao: Veredas | Guimaraes Rosa | 1956 |
| 8 | Vidas Secas | Graciliano Ramos | 1938 |
| 9 | Memorias Postumas de Bras Cubas | Machado de Assis | 1881 |
| 10 | Quarto de Despejo | Carolina Maria de Jesus | 1960 |
| 11 | A Moreninha | Joaquim Manuel de Macedo | 1844 |
| 12 | Senhora | Jose de Alencar | 1875 |
| 13 | Iracema | Jose de Alencar | 1865 |
| 14 | O Guarani | Jose de Alencar | 1857 |
| 15 | A Viagem do Descobrimento | Jose Lins do Rego | 1938 |
| 16 | Fogo Morto | Jose Lins do Rego | 1943 |
| 17 | Menino de Engenho | Jose Lins do Rego | 1932 |
| 18 | O Cortico | Aluisio Azevedo | 1890 |

### Lista completa apos POST (GET /api/livros):

```json
[
  {
    "ano": 1949,
    "autor": "George Orwell",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 3,
    "titulo": "1984"
  },
  {
    "ano": 1977,
    "autor": "Clarice Lispector",
    "data_criacao": "2026-07-28 07:59:50.735613",
    "id": 6,
    "titulo": "A Hora da Estrela"
  },
  {
    "ano": 1844,
    "autor": "Joaquim Manuel de Macedo",
    "data_criacao": "2026-07-28 07:59:50.818476",
    "id": 11,
    "titulo": "A Moreninha"
  },
  {
    "ano": 1938,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.889514",
    "id": 15,
    "titulo": "A Viagem do Descobrimento"
  },
  {
    "ano": 1937,
    "autor": "Jorge Amado",
    "data_criacao": "2026-07-28 07:59:50.721347",
    "id": 5,
    "titulo": "Capitaes da Areia"
  },
  {
    "ano": 1899,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 1,
    "titulo": "Dom Casmurro"
  },
  {
    "ano": 1943,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.904382",
    "id": 16,
    "titulo": "Fogo Morto"
  },
  {
    "ano": 1956,
    "autor": "Guimaraes Rosa",
    "data_criacao": "2026-07-28 07:59:50.747057",
    "id": 7,
    "titulo": "Grande Sertao: Veredas"
  },
  {
    "ano": 1865,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.863873",
    "id": 13,
    "titulo": "Iracema"
  },
  {
    "ano": 1881,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 07:59:50.790570",
    "id": 9,
    "titulo": "Memorias Postumas de Bras Cubas"
  },
  {
    "ano": 1932,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.931718",
    "id": 17,
    "titulo": "Menino de Engenho"
  },
  {
    "ano": 1988,
    "autor": "Paulo Coelho",
    "data_criacao": "2026-07-28 07:59:50.700469",
    "id": 4,
    "titulo": "O Alquimista"
  },
  {
    "ano": 1890,
    "autor": "Aluisio Azevedo",
    "data_criacao": "2026-07-28 07:59:50.938521",
    "id": 18,
    "titulo": "O Cortico"
  },
  {
    "ano": 1890,
    "autor": "Alu\u00edsio Azevedo",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 2,
    "titulo": "O Corti\u00e7\u00e3o"
  },
  {
    "ano": 1857,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.881887",
    "id": 14,
    "titulo": "O Guarani"
  },
  {
    "ano": 1960,
    "autor": "Carolina Maria de Jesus",
    "data_criacao": "2026-07-28 07:59:50.794431",
    "id": 10,
    "titulo": "Quarto de Despejo"
  },
  {
    "ano": 1875,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.842042",
    "id": 12,
    "titulo": "Senhora"
  },
  {
    "ano": 1938,
    "autor": "Graciliano Ramos",
    "data_criacao": "2026-07-28 07:59:50.771532",
    "id": 8,
    "titulo": "Vidas Secas"
  }
]
```

---

## PASSO 2: Atualizando livros via PUT

### Comando utilizado:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros/1 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"Cotemig","autor":"3A1","ano":2026}'
```

### Resultados do PUT:

**Livro 1 atualizado:**
```json
{
  "ano": 2026,
  "autor": "3A1",
  "data_criacao": "2026-07-28 07:59:48.891105",
  "id": 1,
  "titulo": "Cotemig"
}
```

**Livro 2 atualizado:**
```json
{
  "ano": 2026,
  "autor": "Professor",
  "data_criacao": "2026-07-28 07:59:48.891105",
  "id": 2,
  "titulo": "API REST"
}
```

**Livro 3 atualizado:**
```json
{
  "ano": 2025,
  "autor": "Desenvolvedor",
  "data_criacao": "2026-07-28 07:59:48.891105",
  "id": 3,
  "titulo": "Flask Completo"
}
```

### Lista completa apos PUT (GET /api/livros):

```json
[
  {
    "ano": 1977,
    "autor": "Clarice Lispector",
    "data_criacao": "2026-07-28 07:59:50.735613",
    "id": 6,
    "titulo": "A Hora da Estrela"
  },
  {
    "ano": 1844,
    "autor": "Joaquim Manuel de Macedo",
    "data_criacao": "2026-07-28 07:59:50.818476",
    "id": 11,
    "titulo": "A Moreninha"
  },
  {
    "ano": 1938,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.889514",
    "id": 15,
    "titulo": "A Viagem do Descobrimento"
  },
  {
    "ano": 2026,
    "autor": "Professor",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 2,
    "titulo": "API REST"
  },
  {
    "ano": 1937,
    "autor": "Jorge Amado",
    "data_criacao": "2026-07-28 07:59:50.721347",
    "id": 5,
    "titulo": "Capitaes da Areia"
  },
  {
    "ano": 2026,
    "autor": "3A1",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 1,
    "titulo": "Cotemig"
  },
  {
    "ano": 2025,
    "autor": "Desenvolvedor",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 3,
    "titulo": "Flask Completo"
  },
  {
    "ano": 1943,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.904382",
    "id": 16,
    "titulo": "Fogo Morto"
  },
  {
    "ano": 1956,
    "autor": "Guimaraes Rosa",
    "data_criacao": "2026-07-28 07:59:50.747057",
    "id": 7,
    "titulo": "Grande Sertao: Veredas"
  },
  {
    "ano": 1865,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.863873",
    "id": 13,
    "titulo": "Iracema"
  },
  {
    "ano": 1881,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 07:59:50.790570",
    "id": 9,
    "titulo": "Memorias Postumas de Bras Cubas"
  },
  {
    "ano": 1932,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.931718",
    "id": 17,
    "titulo": "Menino de Engenho"
  },
  {
    "ano": 1988,
    "autor": "Paulo Coelho",
    "data_criacao": "2026-07-28 07:59:50.700469",
    "id": 4,
    "titulo": "O Alquimista"
  },
  {
    "ano": 1890,
    "autor": "Aluisio Azevedo",
    "data_criacao": "2026-07-28 07:59:50.938521",
    "id": 18,
    "titulo": "O Cortico"
  },
  {
    "ano": 1857,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.881887",
    "id": 14,
    "titulo": "O Guarani"
  },
  {
    "ano": 1960,
    "autor": "Carolina Maria de Jesus",
    "data_criacao": "2026-07-28 07:59:50.794431",
    "id": 10,
    "titulo": "Quarto de Despejo"
  },
  {
    "ano": 1875,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.842042",
    "id": 12,
    "titulo": "Senhora"
  },
  {
    "ano": 1938,
    "autor": "Graciliano Ramos",
    "data_criacao": "2026-07-28 07:59:50.771532",
    "id": 8,
    "titulo": "Vidas Secas"
  }
]
```

---

## PASSO 3: Deletando livros com indices 5, 6, 7

### Comando utilizado:

```powershell
Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE
Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE
Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE
```

### Resultados do DELETE:

- DELETE /api/livros/5 -> 204 No Content (removido com sucesso)
- DELETE /api/livros/6 -> 204 No Content (removido com sucesso)
- DELETE /api/livros/7 -> 204 No Content (removido com sucesso)

### Lista completa apos DELETE (GET /api/livros):

```json
[
  {
    "ano": 1844,
    "autor": "Joaquim Manuel de Macedo",
    "data_criacao": "2026-07-28 07:59:50.818476",
    "id": 11,
    "titulo": "A Moreninha"
  },
  {
    "ano": 1938,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.889514",
    "id": 15,
    "titulo": "A Viagem do Descobrimento"
  },
  {
    "ano": 2026,
    "autor": "Professor",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 2,
    "titulo": "API REST"
  },
  {
    "ano": 2026,
    "autor": "3A1",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 1,
    "titulo": "Cotemig"
  },
  {
    "ano": 2025,
    "autor": "Desenvolvedor",
    "data_criacao": "2026-07-28 07:59:48.891105",
    "id": 3,
    "titulo": "Flask Completo"
  },
  {
    "ano": 1943,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.904382",
    "id": 16,
    "titulo": "Fogo Morto"
  },
  {
    "ano": 1865,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.863873",
    "id": 13,
    "titulo": "Iracema"
  },
  {
    "ano": 1881,
    "autor": "Machado de Assis",
    "data_criacao": "2026-07-28 07:59:50.790570",
    "id": 9,
    "titulo": "Memorias Postumas de Bras Cubas"
  },
  {
    "ano": 1932,
    "autor": "Jose Lins do Rego",
    "data_criacao": "2026-07-28 07:59:50.931718",
    "id": 17,
    "titulo": "Menino de Engenho"
  },
  {
    "ano": 1988,
    "autor": "Paulo Coelho",
    "data_criacao": "2026-07-28 07:59:50.700469",
    "id": 4,
    "titulo": "O Alquimista"
  },
  {
    "ano": 1890,
    "autor": "Aluisio Azevedo",
    "data_criacao": "2026-07-28 07:59:50.938521",
    "id": 18,
    "titulo": "O Cortico"
  },
  {
    "ano": 1857,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.881887",
    "id": 14,
    "titulo": "O Guarani"
  },
  {
    "ano": 1960,
    "autor": "Carolina Maria de Jesus",
    "data_criacao": "2026-07-28 07:59:50.794431",
    "id": 10,
    "titulo": "Quarto de Despejo"
  },
  {
    "ano": 1875,
    "autor": "Jose de Alencar",
    "data_criacao": "2026-07-28 07:59:50.842042",
    "id": 12,
    "titulo": "Senhora"
  },
  {
    "ano": 1938,
    "autor": "Graciliano Ramos",
    "data_criacao": "2026-07-28 07:59:50.771532",
    "id": 8,
    "titulo": "Vidas Secas"
  }
]
```
