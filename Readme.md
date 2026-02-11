# Práctica 3.2 – API REST con FastAPI y Base de Datos Persistente
**Nombre:** Ismael Franco Ruiz 2ºDAW

## Descripción
Esta API gestiona un sistema de biblioteca con dos entidades principales: **Autores** y **Libros**. Permite realizar operaciones CRUD completas sobre ambos recursos, almacenando la información en una base de datos SQLite persistente.

## Entidades
### Autores
- **id**: Identificador único (autogenerado).
- **name**: Nombre del autor.
- **bio**: Biografía breve.
- **birth_date**: Fecha de nacimiento.
- **nationality**: Nacionalidad.

### Libros
- **id**: Identificador único (autogenerado).
- **title**: Título del libro.
- **description**: Descripción o sinopsis.
- **publish_year**: Año de publicación.
- **pages**: Número de páginas.
- **author_id**: ID del autor (Clave foránea).

## Estructura del Proyecto
```
app/
├── main.py             # Punto de entrada de la aplicación
├── database/
│   └── database.py     # Configuración de la base de datos
├── models/
│   └── models.py       # Modelos SQLAlchemy
├── schemas/
│   └── schemas.py      # Esquemas Pydantic
└── routes/
    ├── authors.py      # Rutas para Autores
    └── books.py        # Rutas para Libros
```

## Cómo ejecutar el proyecto

1. Instalar las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar el servidor:
   ```bash
   fastapi dev app/main.py
   ```

3. Acceder a la documentación interactiva:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)