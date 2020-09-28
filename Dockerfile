FROM node:12-alpine as frontend
WORKDIR /app
COPY frontend/m-note .
RUN npm install
RUN npm run build


FROM python:3.8-slim
WORKDIR /app
COPY backend .
COPY --from=frontend /app/dist /vue
RUN pip install django
RUN pip install djangorestframework
RUN pip install django-cors-headers
RUN pip install psycopg2-binary>=2.8