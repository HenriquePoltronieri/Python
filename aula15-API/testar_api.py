import requests
import json

BASE_URL = "http://127.0.0.1:5000/api/livros"

# 15 livros novos para inserir
livros_novos = [
    {"titulo": "O Alquimista", "autor": "Paulo Coelho", "ano": 1988},
    {"titulo": "Capitaes da Areia", "autor": "Jorge Amado", "ano": 1937},
    {"titulo": "A Hora da Estrela", "autor": "Clarice Lispector", "ano": 1977},
    {"titulo": "Grande Sertao: Veredas", "autor": "Guimaraes Rosa", "ano": 1956},
    {"titulo": "Vidas Secas", "autor": "Graciliano Ramos", "ano": 1938},
    {"titulo": "Memorias Postumas de Bras Cubas", "autor": "Machado de Assis", "ano": 1881},
    {"titulo": "Quarto de Despejo", "autor": "Carolina Maria de Jesus", "ano": 1960},
    {"titulo": "A Moreninha", "autor": "Joaquim Manuel de Macedo", "ano": 1844},
    {"titulo": "Senhora", "autor": "Jose de Alencar", "ano": 1875},
    {"titulo": "Iracema", "autor": "Jose de Alencar", "ano": 1865},
    {"titulo": "O Guarani", "autor": "Jose de Alencar", "ano": 1857},
    {"titulo": "A Viagem do Descobrimento", "autor": "Jose Lins do Rego", "ano": 1938},
    {"titulo": "Fogo Morto", "autor": "Jose Lins do Rego", "ano": 1943},
    {"titulo": "Menino de Engenho", "autor": "Jose Lins do Rego", "ano": 1932},
    {"titulo": "O Cortico", "autor": "Aluisio Azevedo", "ano": 1890},
]

print("=" * 60)
print("PASSO 1: Inserindo 15 livros novos via POST")
print("=" * 60)

for livro in livros_novos:
    resp = requests.post(BASE_URL, json=livro)
    data = resp.json()
    print(f"  ID: {data['id']} | {data['titulo']} | {data['autor']} | {data['ano']}")
    print(f"    data_criacao: {data['data_criacao']}")
    print()

print()
print("Lista completa apos POST:")
resp = requests.get(BASE_URL)
print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

print()
print("=" * 60)
print("PASSO 2: Atualizando livros via PUT")
print("=" * 60)

# Atualizar livro 1
put_data_1 = {"titulo": "Cotemig", "autor": "3A1", "ano": 2026}
resp = requests.put(f"{BASE_URL}/1", json=put_data_1)
print(f"  PUT /api/livros/1 -> {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")

# Atualizar livro 2
put_data_2 = {"titulo": "API REST", "autor": "Professor", "ano": 2026}
resp = requests.put(f"{BASE_URL}/2", json=put_data_2)
print(f"  PUT /api/livros/2 -> {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")

# Atualizar livro 3
put_data_3 = {"titulo": "Flask Completo", "autor": "Desenvolvedor", "ano": 2025}
resp = requests.put(f"{BASE_URL}/3", json=put_data_3)
print(f"  PUT /api/livros/3 -> {json.dumps(resp.json(), indent=2, ensure_ascii=False)}")

print()
print("Lista completa apos PUT:")
resp = requests.get(BASE_URL)
print(json.dumps(resp.json(), indent=2, ensure_ascii=False))

print()
print("=" * 60)
print("PASSO 3: Deletando livros com indices 5, 6, 7")
print("=" * 60)

for livro_id in [5, 6, 7]:
    resp = requests.delete(f"{BASE_URL}/{livro_id}")
    if resp.status_code == 204:
        print(f"  DELETE /api/livros/{livro_id} -> 204 No Content (removido com sucesso)")
    else:
        print(f"  DELETE /api/livros/{livro_id} -> {resp.status_code}")

print()
print("Lista completa apos DELETE:")
resp = requests.get(BASE_URL)
print(json.dumps(resp.json(), indent=2, ensure_ascii=False))
