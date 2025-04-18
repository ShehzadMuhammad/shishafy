run_backend:
	brew services start postgresql
	python3 manage.py runserver

stop_psql:
	brew services stop postgresql

makemigrations:
	python3 manage.py makemigrations core

migrate:
	python3 manage.py migrate

test:
	python3 manage.py test -p=$(PATTERN)

pyshell:
	python3 manage.py shell

psql:
	python3 manage.py dbshell
