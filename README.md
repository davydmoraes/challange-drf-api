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
- O aplicativo estará disponível em http://localhost:8000.

## End-points

`GET api/storage-station/list`

`GET, PUT api/storage-station/detail/<int:pk>`

`GET api/operation-log/list`

`GET api/operation-log/detail/<int:pk>`

`PUT api/storage-station/<int:id>/percent/`

`PUT api/pickup/<int:id>/request`

`PUT api/pickup/<int:id>/confirm`
