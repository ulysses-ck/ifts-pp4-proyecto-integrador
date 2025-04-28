# Proyecto Integrador - Prácticas Profesionales 4
Este es el proyecto integrador de la materia de Prácticas Profesionales 4 de la carrera de Desarrollo de Software en IFTS 18.

## Integrantes del equipo
- Ulises
- Agustin
- Gabriel
- Facundo

## Instalación en PythonAnywhere

Esta es una guía para desplegar este proyecto en PythonAnywhere. Las guías que se siguieron para realizarlo son las siguientes:
- [PythonAnywhere](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/)
- [Deploy a Django web app to Python Anywhere [FREE]](https://www.youtube.com/watch?v=xtnUwvjOThg)
- [MDN Article](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Deployment#example_hosting_on_pythonanywhere)

### 1. Instalar uv
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Configurar PATH
Agregar la siguiente línea a tu `~/.bashrc`:
```bash
export PATH="$HOME/.local/bin:$PATH"
```

### 3. Recargar configuración
```bash
source ~/.bashrc
```

### 4. Instalar dependencias
Navegar al directorio del proyecto e instalar las dependencias:
```bash
cd your-project-directory
uv sync --no-dev --locked
```

### 5. Configuración Panel
Luego de configurar el directorio del código fuente, al realizar la creación del entorno virtual con uv, se necesitaría agregar la misma dirección de este a la configuración de la Web App en el panel de administración de PythonAnywhere, el cual típicamente es llamado .venv. Asegurarse también de haber realizado la configuración del dominio en `settings.py` en `ALLOWED_HOSTS` y `CSRF_TRUSTED_ORIGINS`

## Instalación Local

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd ifts-pp4-proyecto-integrador
```

### 2. Instalar uv (si no está instalado)
#### Windows (PowerShell):
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### Linux/macOS:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Crear entorno virtual `.venv`
```bash
uv venv
```

### 3. Instalar dependencias
```bash
uv sync
```

## Instalación Tradicional (venv + pip)

### 1. Clonar el repositorio
```bash
git clone <url-del-repositorio>
cd ifts-pp4-proyecto-integrador
```

### 2. Crear entorno virtual
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
# Instalar dependencias principales
pip install -r requirements.txt

# Instalar dependencias de desarrollo (opcional)
pip install -r requirements-dev.txt
```

### Requisitos
- Python 3.13 o superior
- uv (gestor de paquetes) - opcional
- Git

## Scripts Disponibles

### Generar DBML
Para generar el archivo DBML del modelo de datos:
```bash
# Usando Python directamente
python manage.py dbml > db.dbml

# Usando uv
uv run manage.py dbml > db.dbml
```

> **Nota**: El archivo DBML generado puede ser visualizado en [dbdiagram.io](https://dbdiagram.io/d). Simplemente copia el contenido del archivo `db.dbml` y pégalo en el editor de dbdiagram.io para ver una representación visual del modelo de datos.

### Ejecutar Seed
Para poblar la base de datos con datos iniciales:
```bash
# Usando Python directamente
python manage.py runscript seed

# Usando uv
uv run manage.py runscript seed
```

> **Nota**: Asegúrate de tener el entorno virtual activado antes de ejecutar cualquiera de estos comandos.

## Configuración de Tailwind CSS

### Instalación de Volta y Node.js
Primero, instala Volta, el gestor de herramientas JavaScript:

#### Windows
```powershell
# Usando winget
winget install Volta.Volta

# O descarga el instalador desde https://volta.sh
```

#### Linux/macOS
```bash
curl https://get.volta.sh | bash
```

Después de instalar Volta, instala Node.js:
```bash
volta install node
```

### Instalación de pnpm
Con Volta y node instalado, ahora instala pnpm:
```bash
volta install pnpm
```

### Instalación de dependencias de Tailwind
```bash
# Instalar dependencias usando pnpm
pnpm install
```

### Configuración de Tailwind CSS
El proyecto ya viene configurado con Tailwind CSS. Los archivos principales son:

- `static/src/styles.css`: Archivo fuente de estilos
- `static/dist/output.css`: Archivo compilado de estilos (generado automáticamente)
- `package.json`: Configuración de dependencias y scripts
- `tailwind.config.js`: Configuración de Tailwind CSS

### Compilar estilos
Para compilar los estilos de Tailwind CSS, ejecuta:
```bash
# Modo desarrollo (watch)
pnpm watch:css
```

Este comando vigilará los cambios en tus archivos HTML y CSS, y recompilará automáticamente los estilos.

### Estructura de archivos
```
├── static/
│   ├── src/
│   │   └── styles.css    # Archivo fuente de Tailwind
│   └── dist/
│       └── output.css    # Archivo compilado
├── templates/
│   └── base.html         # Template base con la referencia al CSS
├── package.json          # Configuración de pnpm y scripts
└── tailwind.config.js    # Configuración de Tailwind
```

### Uso en templates
Los estilos de Tailwind ya están configurados en el template base (`templates/base.html`). Para usar Tailwind CSS en tus templates, simplemente extiende de base.html y utiliza las clases de Tailwind:

```html
{% extends 'base.html' %}

{% block content %}
<div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold text-gray-800">Mi Página</h1>
</div>
{% endblock %}
```

> **Nota**: Asegúrate de tener el comando `pnpm watch:css` ejecutándose mientras desarrollas para que los cambios en los estilos se compilen automáticamente.

## Configuración de Email

### Configuración con Gmail
Para configurar el envío de emails con Gmail, sigue estos pasos:

1. Activa la verificación en dos pasos en tu cuenta de Google:
   - Ve a [Google Account Security](https://myaccount.google.com/security)
   - Activa "2-Step Verification"

2. Genera una contraseña de aplicación:
   - Ve a [App Passwords](https://myaccount.google.com/apppasswords)
   - Selecciona "App" y "Other (Custom name)"
   - Ingresa un nombre (ej: "Django App")
   - Copia la contraseña generada de 16 dígitos

3. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu.email@gmail.com
EMAIL_HOST_PASSWORD=tu-contraseña-de-16-dígitos
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=tu.email@gmail.com
```

### Otros Servicios SMTP
El proyecto soporta cualquier servicio SMTP. Aquí hay algunas opciones populares:

1. **SendGrid** (Gratis hasta 100 emails/día):
```env
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=tu-api-key
```

2. **Amazon SES** (Muy económico para producción):
```env
EMAIL_HOST=email-smtp.us-east-1.amazonaws.com
EMAIL_PORT=587
EMAIL_HOST_USER=tu-access-key
EMAIL_HOST_PASSWORD=tu-secret-key
```

3. **Mailgun** (Gratis hasta 100 emails/día):
```env
EMAIL_HOST=smtp.mailgun.org
EMAIL_PORT=587
EMAIL_HOST_USER=tu-usuario
EMAIL_HOST_PASSWORD=tu-contraseña
```

### Modo Desarrollo
Durante el desarrollo, los emails se imprimen en la consola en lugar de ser enviados. Esto se configura automáticamente cuando `DEBUG=True` en `settings.py`.

Para probar el envío de emails en desarrollo, puedes:
1. Desactivar el modo debug en `settings.py`
2. Usar un servicio de prueba como [Mailtrap](https://mailtrap.io/)
3. Usar un servidor SMTP local como [MailHog](https://github.com/mailhog/MailHog)

### Seguridad
- Nunca commits el archivo `.env` a tu repositorio
- Asegúrate de que `.env` esté en tu `.gitignore`
- Usa diferentes credenciales para desarrollo y producción
- Considera usar variables de entorno en tu plataforma de hosting en lugar de archivos `.env` en producción

## URLs Disponibles

### Core
- `/` - Página de inicio

### Barberos
- `/barber/` - Lista de barberos
- `/barber/create/` - Crear barbero
- `/barber/<int:pk>/detail/` - Detalle del barbero
- `/barber/<int:pk>/update/` - Actualizar barbero
- `/barber/<int:pk>/delete/` - Eliminar barbero

### Clientes
- `/client/` - Página principal de clientes
- `/client/create/` - Crear cliente
- `/client/list/` - Lista de clientes
- `/client/update/<int:pk>/` - Actualizar cliente
- `/client/delete/<int:pk>/` - Eliminar cliente

### Turnos
- `/turn/` - Página principal de turnos
- `/turn/create/` - Crear turno
- `/turn/available/` - Turnos disponibles
- `/turn/<int:pk>/detail/` - Detalle del turno
- `/turn/<int:pk>/update/` - Actualizar turno
- `/turn/<int:pk>/delete/` - Eliminar turno

> **Nota**: Todas las URLs de administración (`/admin/`) están disponibles para usuarios con permisos de administrador.