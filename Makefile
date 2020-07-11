default:
	sudo docker-compose down
	sudo docker-compose build
	sudo docker-compose up

runlocal:
	cd app && python manage.py runserver

MODEL_DIR = app/image_classifier/model
servelocal:
	docker pull tensorflow/serving
	docker run -t --rm -p 8501:8501 \
	 -v "$(CURDIR)/$(MODEL_DIR)/export:/models/model" \
	  tensorflow/serving 

test:
	cd app && python manage.py test

unit_test:
	cd app && python manage.py test --pattern="tests*.py"

functional_test:
	clear && cd app && python manage.py test functional_tests