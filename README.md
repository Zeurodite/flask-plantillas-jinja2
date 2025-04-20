# Actividad: Módulo 1 - Lección 2

Este repositorio contiene una aplicación Flask desarrollada como parte de la actividad sobre el uso de plantillas HTML dinámicas utilizando Jinja2. La aplicación demuestra la separación entre lógica de servidor (Back-End) y presentación (Front-End), usando herencia de plantillas y renderizado de datos dinámicos.

## 📁 Estructura del proyecto

```
flask-plantillas-jinja2/
├── app.py                     # Código principal del servidor Flask
├── requirements.txt           # Dependencias necesarias
├── DOCUMENTACION.pdf          # Documento con capturas de pantalla
├── README.md                  # Información del proyecto
├── static/
│   └── style.css              # Estilos visuales de la aplicación
└── templates/
    ├── base.html              # Plantilla base
    ├── index.html             # Página principal
    ├── pagina1.html           # Página con lista dinámica
    └── pagina2.html           # Página con tabla de usuarios
```

## 🚀 Cómo ejecutar el servidor

1. Clona este repositorio:

```bash
[git clone https://github.com/tu_usuario/flask-plantillas-jinja2.git](https://github.com/Zeurodite/flask-plantillas-jinja2.git)
cd flask-plantillas-jinja2
```

2. Crea un entorno virtual y actívalo:

```bash
python -m venv .venv
.\.venv\Scriptsctivate
```

3. Instala las dependencias:

```bash
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`

## 🌐 Rutas disponibles

### `/` Página de inicio

Muestra un mensaje de bienvenida con navegación a otras secciones.

### `/pagina1` Lista de tecnologías

Renderiza una lista dinámica con tecnologías utilizadas en el proyecto.

### `/pagina2` Tabla de usuarios

Muestra una tabla de datos dinámicos desde el Back-End.

## 🧱 Uso de Plantillas Jinja2

La aplicación utiliza `base.html` como plantilla principal y aplica la herencia para mantener la consistencia en el diseño de todas las páginas. Se hace uso de bloques `block title` y `block content`.

## 🖼️ Capturas de Pantalla

Las capturas de pantalla y explicaciones están documentadas en el archivo `DOCUMENTACION.pdf`.

## 📤 Entrega

Este repositorio debe subirse a GitHub como parte de la entrega del curso. Asegúrate de incluir:

- Código fuente y plantillas
- `requirements.txt`
- `DOCUMENTACION.pdf`
- Este archivo `README.md`

✍️ _Autor: Abdiel Rodríguez_  
📅 _Fecha: Abril 2025_
