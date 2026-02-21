# PIZZA DELIVERY PROJECT


## USED TECHNOLOGIES 
`
Python 3.12.3
FastAPI
SQLAlchemy
PostgreSQL
Alembic
Uvicorn
`

## MAIN CHARACTERISTICS 

`
Complete Users and Orders CRUD
OAuth2/JWT Authentication
Pydantic Validation
Alembic Migration (Work in Progress)
`

## HOW TO USE 

### Clone the repository 

```
git clone https://github.com/LucasAFF1/project-fastapi.git
cd project-fastapi
```

### Create a virtual environment

```
python -m venv venv
source venv/bin/activate  # Linux
venv\Scripts\activate     # Windows
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run migrations 

```
alembic upgrade head
```

### Run the server 

```
uvicorn app.main:app --reload
```


## FUTURE IMPROVEMENTS 

`
Automated testing
Docker
CI/CD
`

## 👨‍💻 Author 

Lucas Ferreira, Computer Engineering Student. 💻




