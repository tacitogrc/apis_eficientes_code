# API's Eficientes - Um Guia para Construção de APIs Escaláveis

Uma API, ou Application Programming Interface, é uma interface que permite que diferentes sistemas e aplicativos se comuniquem de forma padronizada e segura. Em outras palavras, uma API é um conjunto de protocolos e padrões que especificam como diferentes sistemas podem se comunicar uns com os outros.

As APIs são usadas para acessar recursos e dados de outras aplicações e sistemas de forma fácil e eficiente. Por exemplo, uma aplicação de previsão do tempo pode utilizar a API de uma empresa de dados meteorológicos para obter informações atualizadas e precisas sobre condições climáticas em determinada região.

# Sobre este projeto 

Este código fonte faz parte da palestra API's Eficientes. O código é livre e pode ser usado por toda a comunidade referenciando o autor sob licença MIT. 

# Documentação da API

Esta é uma API Flask que fornece funcionalidades básicas de gerenciamento de usuários com autenticação usando JSON Web Tokens (JWT).

## Endpoints

### Login

**Endpoint**: `/api/v1/login`
**Método**: POST

Este endpoint é usado para autenticação do usuário. Ele espera um payload JSON com o email do usuário. Se o usuário existir no banco de dados, um token de autenticação é gerado e retornado.

#### Corpo da Requisição

```json
{
  "email": "usuario@example.com"
}
```

#### Resposta

```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Criar Usuário

**Endpoint**: `/api/v1/users`
**Método**: POST
**Autenticação**: Necessária (token JWT no cabeçalho da requisição)

Este endpoint é usado para criar um novo usuário. Ele espera um payload JSON com o nome e email do usuário. O usuário é então adicionado ao banco de dados.

#### Corpo da Requisição

```json
{
  "name": "Fulano de Tal",
  "email": "fulano@example.com"
}
```

#### Resposta

```json
{
  "user": {
    "id": 1,
    "name": "Fulano de Tal",
    "email": "fulano@example.com"
  }
}
```

### Obter Todos os Usuários

**Endpoint**: `/api/v1/users`
**Método**: GET
**Autenticação**: Necessária (token JWT no cabeçalho da requisição)

Este endpoint recupera todos os usuários do banco de dados.

#### Resposta

```json
{
  "users": [
    {
      "id": 1,
      "name": "Fulano de Tal",
      "email": "fulano@example.com"
    },
    {
      "id": 2,
      "name": "Beltrano da Silva",
      "email": "beltrano@example.com"
    }
  ]
}
```

### Obter Usuário por ID

**Endpoint**: `/api/v1/users/<user_id>`
**Método**: GET
**Autenticação**: Necessária (token JWT no cabeçalho da requisição)

Este endpoint recupera um usuário pelo seu ID do banco de dados.

#### Resposta

```json
{
  "user": {
    "id": 1,
    "name": "Fulano de Tal",
    "email": "fulano@example.com"
  }
}
```

### Atualizar Usuário

**Endpoint**: `/api/v1/users/<user_id>`
**Método**: PUT
**Autenticação**: Necessária (token JWT no cabeçalho da requisição)

Este endpoint é usado para atualizar as informações de um usuário. Ele espera um payload JSON com o novo nome e/ou email para o usuário identificado pelo `user_id`.

#### Corpo da Requisição

```json
{
  "name": "Novo Nome",
  "email": "novoemail@example.com"
}
```

#### Resposta

```json
{
  "user": {
    "id": 1,
    "name": "Novo Nome",
    "email": "novoemail@example.com"
  }
}
```

### Excluir Usuário

**Endpoint**: `/api/v1/users/<user_id>`


**Método**: DELETE
**Autenticação**: Necessária (token JWT no cabeçalho da requisição)

Este endpoint exclui um usuário do banco de dados com base no seu ID.

#### Resposta

```json
{
  "result": "Usuário excluído"
}
```

## Autenticação

Para acessar os endpoints protegidos (`/api/v1/users`, `/api/v1/users/<user_id>`), você precisa incluir um cabeçalho `Authorization` na requisição com um token JWT válido. O token pode ser obtido chamando o endpoint de login (`/api/v1/login`) com o email de um usuário.

Exemplo:
```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

# Boas Práticas na Criação de API's

## API RESTful - Melhores Práticas

Uma API RESTful é uma abordagem popular para a construção de serviços web. Ela segue princípios de arquitetura que facilitam a comunicação entre cliente e servidor. Algumas melhores práticas para o desenvolvimento de APIs RESTful incluem:

- **Padrões de URL**: Utilize URLs descritivas e intuitivas que representem os recursos manipulados pela API. Evite informações sensíveis nas URLs.

- **Verbos HTTP**: Utilize os verbos HTTP adequados (GET, POST, PUT, DELETE) para operações de leitura, criação, atualização e exclusão de recursos, respectivamente.

- **Respostas HTTP**: Retorne códigos de status HTTP apropriados para indicar o sucesso ou falha de uma requisição. Utilize os códigos de status corretos para diferentes situações.

## Segurança em APIs - Autenticação Básica, API Key, JWT, OAuth 2.0

A segurança em APIs é fundamental para proteger os recursos e os dados transmitidos entre cliente e servidor. Existem diversas estratégias de autenticação e autorização disponíveis:

- **Autenticação Básica**: Consiste no envio de credenciais (usuário e senha) na requisição HTTP. É uma forma simples de autenticação, porém menos segura, pois as credenciais são enviadas sem criptografia.

- **API Key**: Uma API Key é um token único que identifica um cliente ou aplicação. É geralmente incluída no cabeçalho ou nos parâmetros da requisição para autenticar e controlar o acesso à API.

- **JWT (JSON Web Token)**: JWT é um formato de token seguro que pode ser utilizado para autenticação e troca de informações entre cliente e servidor. Ele é assinado digitalmente e pode conter informações como identidade do usuário e permissões.

- **OAuth 2.0**: O OAuth 2.0 é um protocolo de autorização amplamente utilizado. Ele permite que usuários autorizem o acesso a recursos protegidos sem compartilhar suas credenciais com a aplicação solicitante. É comumente utilizado para integração com serviços de terceiros.

## Boas Práticas em Segurança de APIs - Rate Limit, Logs, Input Validation

Além das estratégias de autenticação, existem outras boas práticas em segurança de APIs que podem ser implementadas:

- **Rate Limit**: O Rate Limit impõe limites no número de requisições que um cliente pode fazer dentro de um determinado período de tempo. Isso ajuda a evitar ataques de negação de serviço e protege a API contra uso excessivo.

- **Logs**: Registre eventos e atividades relevantes da API em logs. Isso auxilia na detecção de comportamentos suspeitos, investigação de incidentes e monitoramento da segurança.

- **Validação de Entrada**: Realize validação rigorosa nos dados de entrada recebidos pela API. Isso ajuda a prevenir ataques de injeção, como SQL injection e XSS, e garante a integridade dos dados manipulados.

## Swagger UI

O Swagger UI é uma ferramenta para documentar e testar APIs de forma interativa. Ele fornece uma interface amigável onde os desenvolvedores podem explorar e interagir com os endpoints da API. O Swagger UI exibe detalhes sobre os endpoints, parâmetros, códigos de status e exemplos de requisições e respostas. Isso facilita o entendimento e o uso correto da API pelos consumidores.

# Como rodar este projeto

````shell

    python -m venv .venv

    .venv/Scripts/Activate.ps1 

    pip install -r requirements.txt

    python run.py

````

No seu navegador acesse a URL http://127.0.0.1:5000 ou use um API Client, recomendo o ThunderClient presente no visual studio code. 

Execute o login com o json:

```json

{
  "email":"tacito.silva@fieb.org"
}

```
## Comandos Úteis

````shell

# Cria o venv
python -m venv .venv

# Instalar os pacotes na venv
pip install -r requirements.txt

# Exporta os pacotes locais em um arquivo TXT
pip freeze --local > requirements.txt

# Executar a API
python run.py

````

