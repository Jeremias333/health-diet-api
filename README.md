# health-diet
APP feito para gerir a parte lógica do sistema de dietas saudáveis utilizando Docker e Docker Compose para entrega da aplicação.

## Instalação
*Necessário possuir Docker e Docker Composer instalados.*

1. Clone o repositório
1.1. Crie um arquivo .env na pasta raiz do projeto com as seguintes variáveis:
```
    HOST_DB=????
    USER_DB=????
    PASSWORD_DB=????
    DATABASE_DB=????
```
2. Execute o comando `docker compose down` na pasta raiz do projeto
3. Execute o comando `docker compose up -d` na pasta raiz do projeto
4. Execute o comando `docker compose exec python bash` na pasta raiz do projeto
5. Execute o comando `python start.py` 

