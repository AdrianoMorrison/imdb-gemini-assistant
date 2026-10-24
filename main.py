import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from openai import OpenAI

# 1. Carrega as variáveis de ambiente
load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
google_api_key = os.getenv("GOOGLE_API_KEY")

if not google_api_key:
    raise ValueError("A variável GOOGLE_API_KEY não foi encontrada no arquivo .env")

# 2. Inicializa o cliente OpenAI apontando para o Gemini
client = OpenAI(
    base_url=GEMINI_BASE_URL,
    api_key=google_api_key
)

def obter_dados_imdb():
    """Realiza o scraping do Top 250 do IMDb ou utiliza fallback de segurança."""
    url = "https://www.imdb.com/pt/chart/top/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            raise Exception(f"Status HTTP: {response.status_code}")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        filmes = []
        items = soup.select('li.ipc-metadata-list-summary-item')
        
        for item in items[:50]:
            titulo_elem = item.select_one('h3.ipc-title__text')
            meta_elem = item.select('span.cli-title-metadata-item')
            nota_elem = item.select_one('span.ipc-rating-score')
            
            if titulo_elem:
                titulo = titulo_elem.text.strip()
                ano = meta_elem[0].text.strip() if meta_elem else "N/A"
                nota = nota_elem.text.strip() if nota_elem else "N/A"
                filmes.append(f"- {titulo} ({ano}) | Nota: {nota}")
                
        if not filmes:
            raise Exception("Nenhum filme extraído via seletores HTML.")
            
        return "\n".join(filmes)
        
    except Exception as e:
        print(f"[Aviso] Falha no scraping ({e}). Utilizando base de dados padrão.")
        return """
        - Um Sonho de Liberdade (1994) | Nota: 9.3
        - O Poderoso Chefão (1972) | Nota: 9.2
        - Batman: O Cavaleiro das Trevas (2008) | Nota: 9.0
        - O Poderoso Chefão II (1974) | Nota: 9.0
        - 12 Homens e uma Sentença (1957) | Nota: 9.0
        - A Lista de Schindler (1993) | Nota: 9.0
        """

def iniciar_chat():
    print("🔄 Coletando dados atualizados do IMDb...")
    contexto_filmes = obter_dados_imdb()
    
    system_prompt = f"""
    Você é um crítico e assistente de cinema especialista no ranking do IMDb. 
    Responda às perguntas do usuário com base estritamente nos dados dos filmes fornecidos abaixo. 
    Se a informação não estiver na lista, seja honesto e diga que não consta no topo atualizado.

    Dados do IMDb:
    {contexto_filmes}
    """

    print("\n🎬 Assistente IMDb com Gemini Ativado!")
    print("Digite sua pergunta sobre os filmes (ou digite 'sair' para encerrar):")

    while True:
        try:
            pergunta = input("\nVocê: ").strip()
            if not pergunta:
                continue
            if pergunta.lower() in ["sair", "exit", "quit"]:
                print("Até logo!")
                break
                
            resposta = client.chat.completions.create(
                model="gemini-3.5-flash-lite",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": pergunta}
                ],
                temperature=0.3
            )
            
            print(f"\nAssistente:\n{resposta.choices[0].message.content}")
            
        except KeyboardInterrupt:
            print("\nEncerrando aplicação...")
            break

if __name__ == "__main__":
    iniciar_chat()