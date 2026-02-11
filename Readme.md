# Práctica 5.1 – Contenerización y Despliegue de una Aplicación Python
**Nombre:** Ismael Franco Ruiz 2ºDAW

## Descripción
Esta práctica consiste en la evolución de una API REST (de la práctica 3.2) a un entorno de despliegue profesional utilizando **Docker**, **PostgreSQL** y **Render**.

## Objetivos Cumplidos
- [x] **Contenerización:** Creación de un `Dockerfile` para la aplicación FastAPI.
- [x] **Orquestación:** Uso de `docker-compose.yml` para gestionar la API y la base de datos PostgreSQL.
- [x] **Persistencia:** Implementación de volúmenes en Docker para mantener los datos.
- [x] **Despliegue en la Nube:** Aplicación desplegada y funcionando en Render.

## Captura del Despliegue en Render
![Despliegue en Render](render_deployment.png)

## URL del Proyecto
- **API Live:** [https://five-1finalpythonismael.onrender.com](https://five-1finalpythonismael.onrender.com)
- **Documentación Swagger:** [https://five-1finalpythonismael.onrender.com/docs](https://five-1finalpythonismael.onrender.com/docs)

## Tecnologías Utilizadas
- **Backend:** FastAPI (Python 3.12)
- **Base de Datos:** PostgreSQL 15
- **Contenedores:** Docker & Docker Compose
- **Despliegue:** Render

## Cómo ejecutar en local (Docker)
1. Clonar el repositorio.
2. Asegurarse de tener Docker Desktop iniciado.
3. Ejecutar:
   ```bash
   docker compose up -d
   ```
4. Acceder en `http://localhost:8000/docs`