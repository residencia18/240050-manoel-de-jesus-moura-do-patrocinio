  . criar página sobre
  . check responsividade 


#criar ambiente virtual
  python -m venv virtual
#ativar ambiente virtual
  source virtual/bin/activate

#Instalar Django
  pip install Django

#criar migrações de banco de dados
  python manage.py makemigrations
#criar banco de dados
  python3 manage.py migrate
#executar servidor
  python3 manage.py runserver