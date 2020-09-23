# m-note
- - -
M-note is a minimalistic notebook based on <a href="https://github.com/codex-team/editor.js">Editor.js</a>.

Frontend made on: Vue, vue-router, vuex, vue-resourse

Backend made on: Django, DRF

DEMO: https://m-note-mark.herokuapp.com
- - -

## Starting
### Backend
First you need to make a virtual environment and install the necessary Python libraries there.
```
python -m venv venv
venv\Script\activate
cd backend
pip install requirements.txt
```
Then you can start the server
```
python manage.py runserver
```
### Frontend
```
cd frontend
cd m-note
npm install
npm run serve
```
### docker run
```
docker-compose build
docker-compose up
```
