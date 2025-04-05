# Proyecto Integrador - Prácticas Profesionales 4
Este es el proyecto integrador de la materia de Prácticas Profesionales 4 de la carrera de Desarrollo de Software en IFTS 18.

## Integrantes del equipo
- Ulises
- Agustin
- Gabriel
- Facundo

## Instalación en PythonAnywhere

Esta es una guía para desplegar este proyecto en PythonAnywhere. La guia completa y general para realizar esto se encuentra [acá](https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/). También se puede encontrar una guía visual en Youtube en este [link](https://www.youtube.com/watch?v=xtnUwvjOThg)

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

### 5. Luego de configurar el directorio del código fuente, al realizar la creación del entorno virtual con uv, se necesitaría agregar la misma dirección de este a la configuración de la Web App en el panel de administración de PythonAnywhere, el cual típicamente es llamado .venv

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

### Requisitos
- Python 3.13 o superior
- uv (gestor de paquetes)
- Git