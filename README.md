# m-note
- - -
M-note is a simple markdown notebook. The main functions are now done:
Create, delete, edit notes

Authentication and user registration will be added in the future
- - -

## back
1. create venv
```
python -m venv venv
```
2. ```pip install requirements.txt```
3. Go to folder
```
cd m-note
cd backend
```
4. migrate
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## front
```
cd m-note
cd frontend
npm install
npm run build
```
