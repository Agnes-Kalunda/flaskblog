export SECRET_KEY=
export APP_SETTINGS="config.DevelopmentConfig"
export DATABASE_URL=''
python3 manage.py server
# python manage.py db migrate -m "Add column to post_img"
# python manage.py db upgrade