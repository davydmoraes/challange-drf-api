# Challenge Server Side

API responsável pelas requisições solicidatas no desafio de gerenciamento de estações de armazenamento.

- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [End-points](#end-points)

  
## Instalação

- Clone o repositório:

```bash
git clone https://github.com/davydmoraes/challange-drf-api.git
cd challange-drf-api
```

- Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate      # Windows
```

- Instale as dependências:
```bash
pip install -r requirements.txt
```

- Configure o banco de dados:
```bash
python manage.py migrate
```

## Como Usar
```bash
python manage.py runserver
```
- O aplicativo estará disponível em http://localhost:8000/api

## End-points

`GET api/storage-station/list`

`GET, PUT api/storage-station/detail/<pk>`

`GET api/operation-log/list`

`GET api/operation-log/detail/<pk>`

`PUT api/storage-station/<id>/percent/`

`PUT api/pickup/<id>/request`

`PUT api/pickup/<id>/confirm`

- OBS: acessando as rotas pelo navegador, é possível realizar os teste via interface gráfica do Django REST Framework
