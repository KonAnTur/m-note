FROM node:12-alpine as frontend
WORKDIR /app
COPY frontend/m-note .
RUN npm install
RUN npm run build


FROM python:3.7-alpine
WORKDIR /app
COPY backend .
COPY --from=frontend /app/dist /vue
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers

CMD python manage.py runserver 0.0.0.0:8000