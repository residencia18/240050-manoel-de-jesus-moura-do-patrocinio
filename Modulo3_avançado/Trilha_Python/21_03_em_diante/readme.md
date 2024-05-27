
  . Verificar como delimitar os produtos no cadastro de influencers
  . Transformar card produto em componente
  . Implementar input de busca


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

#instalar o Django REST