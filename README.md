# 🎬 IMDb Gemini Assistant

> Um assistente inteligente de cinema desenvolvido em Python que combina **Web Scraping do IMDb** com a inteligência generativa da **API Google Gemini**, utilizando o endpoint de compatibilidade da OpenAI para criar uma experiência interativa de recomendações, análises e consultas sobre os melhores filmes da história.

---

## 🚀 Sobre o Projeto

O **IMDb Gemini Assistant** foi criado com o objetivo de explorar a integração entre **coleta automatizada de dados da web** e **Inteligência Artificial Generativa**.

A aplicação realiza a extração dos filmes presentes no ranking **IMDb Top 250**, coletando informações como:

- 🎬 Título do filme
- 📅 Ano de lançamento
- ⭐ Nota no IMDb
- 🏆 Posição no ranking

Esses dados são utilizados como contexto para um modelo **Gemini**, permitindo que o usuário faça perguntas em linguagem natural sobre os filmes mais bem avaliados do mundo.

Além disso, o projeto utiliza uma estratégia de **programação defensiva**, garantindo maior robustez e confiabilidade.

Caso a coleta automática dos dados falhe devido a:

- Proteções anti-bot do IMDb
- Rate limits
- Mudanças na estrutura da página
- Problemas de conectividade

A aplicação ativa automaticamente uma base local de *fallback*, assegurando que o assistente continue funcionando normalmente.

---

## ✨ Funcionalidades

✅ Extração automática dos filmes do IMDb Top 250

✅ Integração com a API Google Gemini

✅ Compatibilidade via SDK OpenAI

✅ Consulta em linguagem natural

✅ Respostas como crítico de cinema

✅ Base de dados local de fallback

✅ Tratamento de erros e falhas de scraping

✅ Configuração simples através de variáveis de ambiente

✅ Ambiente virtual isolado para execução

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **Google Gemini API**
  - Modelo: `gemini-3.5-flash-lite`
- **OpenAI SDK**
  - Utilizado para comunicação com o endpoint compatível do Gemini
- **BeautifulSoup4**
  - Web Scraping
- **Requests**
  - Requisições HTTP
- **Python-Dotenv**
  - Gerenciamento de variáveis de ambiente

---

## 📂 Estrutura do Projeto

```text
imdb-gemini-assistant/
│
├── .env.example          # Exemplo de variáveis de ambiente
├── .gitignore            # Arquivos ignorados pelo Git
├── requirements.txt      # Dependências do projeto
├── main.py               # Aplicação principal
└── README.md             # Documentação do projeto
```

---

## ⚙️ Como Executar Localmente

### Pré-requisitos

Antes de começar, você precisará ter instalado:

- Python 3.10 ou superior
- Git
- Uma chave gratuita da API Google AI Studio

---

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/AdrianoMorrison/imdb-gemini-assistant.git

cd imdb-gemini-assistant
```

---

### 2️⃣ Crie um ambiente virtual

#### Linux / Mac / Git Bash

```bash
python -m venv .venv

source .venv/Scripts/activate
```

#### Windows (CMD)

```cmd
python -m venv .venv

.venv\Scripts\activate.bat
```

#### Windows (PowerShell)

```powershell
python -m venv .venv

.venv\Scripts\Activate.ps1
```

---

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure a chave da API

Crie um arquivo `.env` na raiz do projeto:

```env
GOOGLE_API_KEY=sua_chave_aqui
```

Ou renomeie o arquivo:

```text
.env.example
```

para:

```text
.env
```

e substitua a chave de exemplo pela sua.

---

### 5️⃣ Execute a aplicação

```bash
python main.py
```

---

## 💡 Exemplo de Execução

```text
🔄 Coletando dados atualizados do IMDb...

[Aviso] Falha no scraping (Status HTTP: 202).
Utilizando base de dados padrão.

🎬 Assistente IMDb com Gemini Ativado!

Digite sua pergunta sobre os filmes
(ou digite 'sair' para encerrar):

Você:
Qual é o filme mais bem avaliado e qual o ano dele?

Assistente:
O filme mais bem avaliado da lista é
Um Sonho de Liberdade (1994),
com nota 9.3 no IMDb.
```

---

## 💬 Exemplos de Perguntas

Você pode perguntar:

```text
Quais são os 10 filmes mais bem avaliados da história?

Qual é o melhor filme de crime da lista?

Liste os filmes lançados antes de 1980.

Qual diretor aparece mais vezes no Top 250?

Me recomende três filmes parecidos com O Poderoso Chefão.

Quais são os filmes mais bem avaliados da década de 1990?

Por que Um Sonho de Liberdade é tão bem avaliado?
```

---

## 🔒 Segurança

A chave da API não deve ser enviada para o GitHub.

Certifique-se de incluir o arquivo `.env` no `.gitignore`.

Exemplo:

```gitignore
.env
.venv/
__pycache__/
```

---

## 🧠 Arquitetura da Solução

```text
IMDb Top 250
       │
       ▼
Web Scraping (Requests + BeautifulSoup)
       │
       ├── Sucesso
       │       ▼
       │   Dados Atualizados
       │
       └── Falha
               ▼
      Base Local de Fallback
               │
               ▼
         Contexto dos Filmes
               │
               ▼
        Google Gemini API
               │
               ▼
     Resposta ao Usuário
```

---

## 🎯 Objetivos de Aprendizado

Este projeto foi desenvolvido para praticar:

- Consumo de APIs de IA Generativa
- Integração do Google Gemini
- Web Scraping com BeautifulSoup
- Tratamento de exceções
- Programação defensiva
- Gerenciamento de variáveis de ambiente
- Arquitetura resiliente em aplicações Python

---

## 🚀 Melhorias Futuras

- [ ] Interface Web com Streamlit
- [ ] Histórico de conversas
- [ ] Suporte a múltiplos ranking de filmes
- [ ] Busca por gênero
- [ ] Busca por diretor
- [ ] Banco de dados SQLite
- [ ] Cache automático dos dados do IMDb
- [ ] Deploy em nuvem

---

## 🤝 Contribuições

Contribuições são sempre bem-vindas!

Caso tenha sugestões de melhorias, novas funcionalidades ou correções de bugs:

1. Faça um Fork do projeto
2. Crie uma nova branch

```bash
git checkout -b feature/minha-feature
```

3. Realize suas alterações

4. Faça commit

```bash
git commit -m "feat: adiciona nova funcionalidade"
```

5. Envie para seu fork

```bash
git push origin feature/minha-feature
```

6. Abra um Pull Request

---

## 📜 Licença

Este projeto está distribuído sob a licença MIT.

Sinta-se livre para estudar, modificar e compartilhar.

---

## 👨‍💻 Autor

**Adriano Soares**

Analista de Logística | Power BI | SQL Server | Python | IA Generativa

🔗 GitHub: https://github.com/AdrianoMorrison

---

## ⭐ Gostou do projeto?

Se este projeto ajudou você ou serviu como inspiração para seus estudos, considere deixar uma estrela no repositório.

⭐ **Star no GitHub ajuda bastante na divulgação do projeto!**
