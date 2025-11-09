# 🥗 Daily Diet API

API RESTful desenvolvida com **Flask** e **SQLAlchemy** para gerenciar um diário de refeições, permitindo o registro e acompanhamento de itens dentro ou fora da dieta.

---

## 🚀 Funcionalidades

- **CRUD Completo:** Crie, liste, busque, atualize e delete refeições.  
- **Banco de Dados:** Utiliza **MySQL** (configurado com Docker) para persistência dos dados.  
- **Validação:** Tratamento de erros para dados ausentes ou inválidos.  
- **Testes:** Suíte de testes de integração com **Pytest** para garantir a estabilidade dos endpoints.

---

## ⚙️ Tecnologias Utilizadas

- **Backend:** Flask, Flask-SQLAlchemy  
- **Banco de Dados:** MySQL  
- **Driver DB:** PyMySQL  
- **Testes:** Pytest, Requests

---

## 🏁 Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente.

### 1. Pré-requisitos

- Python 3.10+  
- Docker e Docker Compose  
- pip (gerenciador de pacotes do Python)

### 2. Configuração do Banco de Dados

O banco de dados MySQL é gerenciado pelo Docker Compose.

```bash
# Inicie o container do MySQL em segundo plano
docker compose up -d
```

Isso irá iniciar um servidor MySQL na porta **3306** com as credenciais e o banco de dados definidos no `docker-compose.yml`.

### 3. Configuração da Aplicação Flask

```bash
# 1. Clone o repositório (se ainda não o fez)
# git clone ...

# 2. Navegue até a pasta do projeto
cd daily-diet-api

# 3. Crie um ambiente virtual
python -m venv .venv

# 4. Ative o ambiente virtual
# No Windows:
# .\.venv\Scripts\activate
# No macOS/Linux:
source .venv/bin/activate

# 5. Instale as dependências
pip install -r requirements.txt

# 6. Inicie a aplicação Flask
python app.py
```

Ao iniciar, o `app.py` irá automaticamente executar `db.create_all()`, criando a tabela `meal` no seu banco de dados MySQL.  
O servidor estará rodando em **http://127.0.0.1:5000**.

---

## 🧪 Como Rodar os Testes

Com o ambiente virtual ativado e o servidor Flask (`app.py`) rodando em um terminal, abra outro terminal e execute:

```bash
pytest
```

Os testes de integração irão rodar, validando cada endpoint da API em tempo real.

---

## 📖 Documentação da API

A URL base para todos os endpoints é:

```
http://127.0.0.1:5000/api
```

### Modelo de Dados: `Meal`

| Campo       | Tipo     | Descrição                                      | Obrigatório |
|--------------|----------|-----------------------------------------------|--------------|
| id           | Integer  | Identificador único                            | ❌           |
| name         | String   | Nome da refeição                               | ✅           |
| description  | String   | Descrição detalhada                            | ❌           |
| datetime     | DateTime | Data e hora da refeição (formato ISO)          | ✅           |
| is_diet      | Boolean  | Indica se a refeição está dentro da dieta      | ✅           |

---

### 1️⃣ Listar todas as Refeições

**Endpoint:** `GET /api/meals`  
**Descrição:** Retorna uma lista de todas as refeições cadastradas.

**Resposta (200 OK):**
```json
[
  {
    "datetime": "2025-11-08T20:30:00",
    "description": "Pão Integral",
    "id": 1,
    "is_diet": true,
    "name": "Pão"
  }
]
```

---

### 2️⃣ Buscar Refeição por ID

**Endpoint:** `GET /api/meals/<int:meal_id>`

**Resposta (200 OK):**
```json
{
  "datetime": "2025-11-08T20:30:00",
  "description": "Pão Integral",
  "id": 1,
  "is_diet": true,
  "name": "Pão"
}
```

**Erro (404 Not Found):**
```json
{ "message": "Refeição não encontrada" }
```

---

### 3️⃣ Criar nova Refeição

**Endpoint:** `POST /api/meals`

**Body:**
```json
{
  "name": "Lanche da tarde",
  "description": "Iogurte e frutas",
  "datetime": "2025-11-09T15:00:00",
  "is_diet": true
}
```

**Resposta (201 Created):**
```json
{
  "datetime": "2025-11-09T15:00:00",
  "description": "Iogurte e frutas",
  "id": 3,
  "is_diet": true,
  "name": "Lanche da tarde"
}
```

**Erros:**
```json
{ "message": "Dados inválidos ou faltando" }
{ "message": "Formato de 'datetime' inválido. Use ISO format (YYYY-MM-DDTHH:MM:SS)" }
```

---

### 4️⃣ Atualizar uma Refeição

**Endpoint:** `PUT /api/meals/<int:meal_id>`

**Body:**
```json
{
  "name": "Lanche Atualizado",
  "description": "Iogurte desnatado e morangos",
  "datetime": "2025-11-09T15:05:00",
  "is_diet": false
}
```

**Resposta (200 OK):**
```json
{ "message": "Refeição atualizada com sucesso!" }
```

**Erros:**
```json
{ "message": "Refeição não encontrada!" }
{ "message": "Corpo da requisição inválido ou ausente" }
{ "message": "Campo obrigatório ausente: 'name'" }
```

---

### 5️⃣ Deletar uma Refeição

**Endpoint:** `DELETE /api/meals/<int:meal_id>`

**Resposta (204 No Content):** Nenhum conteúdo retornado.

**Erro (404 Not Found):**
```json
{ "message": "Refeição não encontrada!" }
```

---

## 🧑‍💻 Autor

Desenvolvido com ❤️ por **Bruno Godoy**
