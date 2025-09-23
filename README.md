
# MCP Server FastAPI - Servidor de Herramientas Personalizado

Un servidor MCP (Model Context Protocol) construido con FastAPI que proporciona herramientas para cálculos matemáticos, consultas de Pokémon y análisis de Google BigQuery.

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Requerimientos Previos](#requerimientos-previos)
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Uso](#uso)
- [Herramientas Disponibles](#herramientas-disponibles)
- [Integración con Claude](#integración-con-claude)
- [Solución de Problemas](#solución-de-problemas)
- [Referencias](#referencias)

## 📝 Descripción

Este proyecto implementa un servidor MCP personalizado usando FastAPI que expone múltiples herramientas:

- **Calculadora**: Operaciones matemáticas básicas
- **Pokémon API**: Búsqueda de información de Pokémon
- **BigQuery**: Estimación de costos y ejecución de queries

El servidor está diseñado para integrarse con Claude Code y otros clientes MCP.

## ⚙️ Requerimientos Previos

Antes de comenzar, asegúrate de tener instalado:

### Software Requerido

1. **Python 3.8 o superior**
   ```bash
   python3 --version
   ```

2. **pip (gestor de paquetes de Python)**
   ```bash
   pip --version
   ```

3. **Node.js y npm** (para la integración con Claude)
   ```bash
   node --version
   npm --version
   ```

### Servicios Externos (Opcionales)

- **Cuenta de Google Cloud** (solo para herramientas de BigQuery)
- **Credenciales de BigQuery** (archivo JSON de service account)

## 🚀 Instalación

### Paso 1: Clonar el Repositorio

```bash
git clone <repository-url>
cd mcp-server-fastapi
```

### Paso 2: Crear Entorno Virtual

```bash
# Crear entorno virtual
python3 -m venv mcp-fastapi-env

# Activar entorno virtual
# En macOS/Linux:
source mcp-fastapi-env/bin/activate

# En Windows:
# mcp-fastapi-env\Scripts\activate
```

### Paso 3: Instalar Dependencias

```bash
# Instalar todas las dependencias
pip install -r requirements.txt
```

### Paso 4: Verificar Instalación

```bash
# Verificar que FastAPI esté instalado
python -c "import fastapi; print('FastAPI instalado correctamente')"

# Verificar que fastapi-mcp esté instalado
python -c "import fastapi_mcp; print('FastAPI-MCP instalado correctamente')"
```

## 🔧 Configuración

### Configuración Básica

El servidor viene preconfigurado y listo para usar. No se requiere configuración adicional para las herramientas básicas.

### Configuración de BigQuery (Opcional)

Si planeas usar las herramientas de BigQuery:

1. **Crear archivo de credenciales**:
   ```bash
   # Coloca tu archivo de credenciales JSON en:
   # tools/bigquery/credentials.json
   ```

2. **Configurar variables de entorno** (opcional):
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="tools/bigquery/credentials.json"
   export GOOGLE_CLOUD_PROJECT="tu-proyecto-id"
   ```

## 🎯 Uso

### Iniciar el Servidor

```bash
# Activar entorno virtual (si no está activo)
source mcp-fastapi-env/bin/activate

# Iniciar el servidor
python main.py
```

El servidor estará disponible en:
- **API Principal**: http://localhost:8000
- **Documentación**: http://localhost:8000/docs
- **Endpoint MCP**: http://localhost:8000/mcp

### Verificar que el Servidor Funciona

```bash
# Probar endpoint de calculadora
curl "http://localhost:8000/calculator/multiply?a=5&b=4"

# Probar endpoint de Pokémon
curl "http://localhost:8000/pokemon/pikachu"
```

## 🛠️ Herramientas Disponibles

### 1. Calculadora
- **Endpoint**: `GET /calculator/multiply`
- **Parámetros**: `a` (float), `b` (float)
- **Ejemplo**: `/calculator/multiply?a=7&b=6`

### 2. Pokémon API
- **Endpoint**: `GET /pokemon/{name}`
- **Parámetros**: `name` (string) - nombre del Pokémon
- **Ejemplo**: `/pokemon/charizard`

### 3. BigQuery - Estimación de Costos
- **Endpoint**: `POST /bigquery/estimate-cost`
- **Body**: JSON con la query SQL
- **Requiere**: Credenciales de Google Cloud

### 4. BigQuery - Ejecución de Queries
- **Endpoint**: `POST /bigquery/execute-query`
- **Body**: JSON con la query SQL
- **Requiere**: Credenciales de Google Cloud

## 🔗 Integración con IDEs y Clientes MCP

### Prerequisitos para Todos los IDEs

1. **Instalar mcp-remote** (si no está instalado):
   ```bash
   npm install -g mcp-remote
   ```

2. **Asegúrate de que el servidor esté corriendo**:
   ```bash
   python main.py
   ```

### 🎯 Claude Code

**Ubicación del archivo de configuración:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**Configuración:**
```json
{
  "mcpServers": {
    "mcp_fastapi_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8000/mcp"
      ]
    }
  }
}
```

### 🌊 Windsurf

**Ubicación del archivo de configuración:**
- macOS: `~/Library/Application Support/Windsurf/User/globalStorage/codeium.codeium/mcp.json`
- Windows: `%APPDATA%\Windsurf\User\globalStorage\codeium.codeium\mcp.json`

**Configuración:**
```json
{
  "mcpServers": {
    "mcp_fastapi_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8000/mcp"
      ],
      "disabled": false
    }
  }
}
```

### 📝 VSCode (con extensión MCP)

**Ubicación del archivo de configuración:**
- macOS: `~/.vscode/mcp_servers.json`
- Windows: `%USERPROFILE%\.vscode\mcp_servers.json`

**Configuración:**
```json
{
  "mcpServers": {
    "mcp_fastapi_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8000/mcp"
      ],
      "env": {},
      "disabled": false
    }
  }
}
```

**Configuración alternativa en settings.json:**
```json
{
  "mcp.servers": {
    "mcp_fastapi_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8000/mcp"
      ]
    }
  }
}
```

### 🎯 Cursor

**Ubicación del archivo de configuración:**
- macOS: `~/Library/Application Support/Cursor/User/globalStorage/cursor.mcp/mcp_servers.json`
- Windows: `%APPDATA%\Cursor\User\globalStorage\cursor.mcp\mcp_servers.json`

**Configuración:**
```json
{
  "mcpServers": {
    "mcp_fastapi_tools": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://localhost:8000/mcp"
      ],
      "disabled": false,
      "alwaysAllow": ["*"]
    }
  }
}
```

### 🔧 Configuración Paso a Paso

#### Para Claude Code:
1. Abre el archivo de configuración en la ubicación correspondiente
2. Agrega la configuración JSON
3. Reinicia Claude Code
4. Verifica que aparezca "🔧" en la barra de estado

#### Para Windsurf:
1. Abre Windsurf
2. Ve a `Settings` > `Extensions` > `MCP`
3. Agrega el servidor manualmente o edita el archivo JSON
4. Reinicia Windsurf

#### Para VSCode:
1. Instala la extensión MCP desde el marketplace
2. Edita el archivo de configuración correspondiente
3. Recarga la ventana (`Ctrl+Shift+P` > "Developer: Reload Window")

#### Para Cursor:
1. Ve a `Settings` > `Extensions` 
2. Busca e instala la extensión MCP
3. Configura el archivo JSON
4. Reinicia Cursor

### ✅ Verificar la Conexión

Una vez configurado cualquier IDE, deberías poder usar comandos como:
- "Multiplica 5 por 8 usando la calculadora"
- "Búscame información del Pokémon Garchomp"
- "Estima el costo de esta query de BigQuery"
- "Ejecuta una multiplicación de 12 por 15"

### 🐛 Solución de Problemas por IDE

#### Claude Code:
```bash
# Verificar configuración
cat ~/Library/Application\ Support/Claude/claude_desktop_config.json

# Verificar logs
tail -f ~/Library/Logs/Claude/claude.log
```

#### Windsurf:
```bash
# Verificar si MCP está habilitado
# Ve a: Settings > Extensions > Codeium > MCP Settings
```

#### VSCode:
```bash
# Verificar extensión MCP
code --list-extensions | grep mcp

# Verificar configuración
cat ~/.vscode/mcp_servers.json
```

#### Cursor:
```bash
# Verificar configuración
cat ~/Library/Application\ Support/Cursor/User/globalStorage/cursor.mcp/mcp_servers.json
```

## 🔍 Solución de Problemas

### Problemas Comunes

#### Error: "ModuleNotFoundError"
```bash
# Asegúrate de que el entorno virtual esté activo
source mcp-fastapi-env/bin/activate

# Reinstala las dependencias
pip install -r requirements.txt
```

#### Error: "Puerto 8000 en uso"
```bash
# Encontrar proceso usando el puerto
lsof -i :8000

# Terminar el proceso (reemplaza PID con el número real)
kill -9 PID

# O usar un puerto diferente
uvicorn main:app --host 0.0.0.0 --port 8001
```

#### Error de Conexión con Claude
1. Verifica que el servidor esté corriendo en http://localhost:8000
2. Confirma que mcp-remote esté instalado: `npm list -g mcp-remote`
3. Revisa los logs de Claude para errores específicos

#### Problemas con BigQuery
```bash
# Verificar credenciales
export GOOGLE_APPLICATION_CREDENTIALS="ruta/a/credenciales.json"

# Probar conexión
python -c "from google.cloud import bigquery; client = bigquery.Client(); print('Conexión exitosa')"
```

### Logs y Debugging

Para obtener más información sobre errores:

```bash
# Ejecutar con logs detallados
uvicorn main:app --host 0.0.0.0 --port 8000 --log-level debug
```

### Verificar Instalación Completa

```bash
# Script de verificación
python -c "
import fastapi
import fastapi_mcp
import uvicorn
import google.cloud.bigquery
print('✅ Todas las dependencias están instaladas correctamente')
"
```

## 📚 Referencias

- **FastAPI MCP**: https://github.com/tadata-org/fastapi_mcp
- **Documentación MCP**: https://modelcontextprotocol.io/
- **FastAPI**: https://fastapi.tiangolo.com/
- **Google Cloud BigQuery**: https://cloud.google.com/bigquery/docs

## 📄 Estructura del Proyecto

```
mcp-server-fastapi/
├── main.py                 # Archivo principal del servidor
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Este archivo
└── tools/                 # Directorio de herramientas
    ├── calculator/        # Herramientas de calculadora
    ├── pokemon/          # Herramientas de Pokémon
    ├── bigquery/         # Herramientas de BigQuery
    └── shared/           # Modelos compartidos
```

