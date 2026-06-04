
Minha api que permite você ultilizar uma IA em seus projetos, no caso aqui fica a Documentação

# API de IA
Esta api ultiliza GPT 5.5

# Documentação da API Redz IA

A API Redz IA permite utilizar uma inteligência artificial através de requisições HTTP.

# Aviso

O sistema de chaves ainda está em desenvolvimento e pode apresentar alguns erros ocasionais. Caso encontre algum problema, entre em contato comigo pelo WhatsApp ou Discord.

# Compra de Chaves

Para utilizar a API, primeiro é necessário adquirir uma chave de acesso.

Planos disponíveis:

- 100 mensagens = R$2,00
- 600 mensagens = R$7,00
- 1000 mensagens = R$12,00

Após a confirmação do pagamento, sua chave será criada e enviada em alguns segundos ou minutos.

URL da API

https://redz.up.railway.app/api

Autenticação

A autenticação é feita através do cabeçalho "Authorization".

Exemplo:

headers = {
    "Authorization": "sua_chave_api"
}

Exemplo de Uso (Python)

Recomendo utilizar a biblioteca "requests".
'''
import requests
import json

url = "https://redz.up.railway.app/api"

headers = {
    "Authorization": "sua_chave_api"
}

response = requests.post(
    url,
    headers=headers,
    data="oi"
).json()
'''
print(response)

# Resposta

A API retorna um JSON contendo a resposta da IA.

Exemplo:

{
    "choices": [
        {
            "message": {
                "content": "Olá!"
            }
        }
    ]
}

Para acessar o texto gerado:

print(response["choices"][0]["message"]["content"])

# Contatos

email: redandblue2235@gmail.com 
whatsapp: +55 28 99986-5324
discord: bloodofdeath
