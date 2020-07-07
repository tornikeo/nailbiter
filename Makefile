default:
	sudo docker-compose down
	sudo docker-compose build
	sudo docker-compose up

runlocal:
	cd app && python manage.py runserver
	 
test:
	cd app && python manage.py test

unit_test:
	cd app && python manage.py test --pattern="tests*.py"

functional_test:
	cd app && python manage.py test functional_tests