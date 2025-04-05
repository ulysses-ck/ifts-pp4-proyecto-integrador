# Proyecto Integrador - Prácticas Profesionales 4
Este es el proyecto integrador de la materia de Prácticas Profesionales 4 de la carrera de Desarrollo de Software en IFTS 18.

## Integrantes del equipo
- Ulises
- Agustin
- Gabriel
- Facundo

## Instalación en PythonAnywhere

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
uv pip install -e .
```

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

### 3. Instalar dependencias
```bash
uv pip install -e .
```

### Requisitos
- Python 3.13 o superior
- uv (gestor de paquetes)
- Git