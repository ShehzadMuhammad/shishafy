run_backend:
	brew services start postgresql	
	python3 manage.py runserver

stop_sql:
	brew services stop postgresql


start_venv:
	source venv/bin/activate

makemigrations:
	python3 manage.py makemigrations core

migrate:
	python3 manage.py migrate

test:
	python3 manage.py test -p=$(PATTERN)

pyshell:
	python3 manage.py shell

sql:
	python3 manage.py dbshell
