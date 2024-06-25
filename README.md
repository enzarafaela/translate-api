# Translation API

Esta é uma API de tradução simples construída com FastAPI, Uvicorn e Deep_Translator. A API permite traduzir textos entre diferentes idiomas usando diversos provedores de tradução.

## Funcionalidades

Tradução de texto entre diferentes idiomas.
Suporte para múltiplos provedores de tradução (Google, Yandex, etc.).

## Tecnologias Utilizadas

FastAPI
Uvicorn
Deep_Translator
Requisitos
Python 3.7+
FastAPI
Uvicorn
Deep_Translator

## How to Use

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/translation-api.git
cd translation-api
```

Crie um ambiente virtual e ative-o:

```bash
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o servidor Uvicorn:

```bash
uvicorn main:app --reload
```

Acesse os endpoints da API em http://127.0.0.1:8000/

## Endpoints

``POST /translate``
Traduz um texto de um idioma para outro.

Parâmetros:

``text`` (str): O texto a ser traduzido.
``target_language`` (str): O idioma para o qual o texto deve ser traduzido.

Exemplo de Requisição:

```javascript
// Define a URL da API
const API_URL = 'https://translate-api-trybe.up.railway.app/translate/';

type DataParams = {
  text: string;
  target_language: string;
};

type TranslatedData = {
  translated_text: string;
}

async function translateText(data: DataParams) {
  try {
    // Fetch busca os dados da API
    // O metodo POST é utilizado para enviar dados para a API
    // O headers é utilizado para definir o tipo de conteúdo que será enviado
    // O body é onde os dados são enviados, e é convertido para JSON
    // Neste caso, o body é um objeto com duas propriedades: text e target_language que são os dados que serão requeridos pela a API. São obrigatórios, se não forem enviados, a API retornará um erro.
    const response = await fetch(API_URL, {
      method: 'POST', 
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    
    // Converte os dados recebidos em JSON
    const returnedData = await response.json() as TranslatedData;

    // Testando se deu tudo certo, imrpimindo o texto traduzido
    console.log('Translated Text:', returnedData.translated_text);
  } catch (error) {
    // Mas caso de erro, imprime o erro no console
    console.error('Error:', error);
  }
}

// Define dados que serão enviados como parametro para a API
const data = {
  text: 'Hey guys, subscribe to the YouTube channel to learn more about programming in JavaScript and other programming languages', // Aqui você insere o SEU texto, que será capturado do retorno da API de receitas
  target_language: 'pt', // qual idioma você quer traduzir o texto
};

translateText(data);
```