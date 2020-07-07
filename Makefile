default:
	sudo docker-compose down
	sudo docker-compose build
	sudo docker-compose up

runlocal:
	cd app && python manage.py runserver
	 
test:
	cd app && python manage.py test