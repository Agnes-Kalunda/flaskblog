export SECRET_KEY=
export APP_SETTINGS="config.DevelopmentConfig"

 export DATABASE_URL=''

python3 manage.py test
# python3 manage.py db migrate -m "redo migrations"
# python manage.py db migrate -m "Deployment"
# python manage.py db upgrade

	

