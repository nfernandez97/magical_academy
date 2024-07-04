# Etapa 1: Construir la aplicación React
FROM node:14 AS build-frontend
WORKDIR /app
COPY frontend/package*.json ./
RUN npm install
COPY frontend ./
RUN npm run build

# Etapa 2: Configurar Nginx para servir el frontend
FROM nginx:alpine AS frontend
COPY --from=build-frontend /app/build /usr/share/nginx/html
COPY frontend/nginx.conf /etc/nginx/nginx.conf

# Etapa 3: Configurar el entorno de FastAPI
FROM python:3.9-slim AS backend
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

EXPOSE 80
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]