# Recipe Assistant

Generador de recetas construido con [PydanticAI](https://ai.pydantic.dev/) como proyecto del curso **Pydantic-AI: Desarrollo de aplicaciones robustas con IA**.

El asistente conversa en español, consulta los ingredientes disponibles y recomienda recetas estructuradas de temporada.

## Estructura de `src/recipe_assistant/`

| Archivo | Descripción |
|---|---|
| `__init__.py` | Expone `main` como punto de entrada del comando `recipe-assistant`. |
| `main.py` | Define el agente, sus instrucciones, su herramienta y el chat interactivo con streaming. |
| `models.py` | Modelo `Recipe` (Pydantic) con la validación de la receta generada. |
| `deps.py` | Dependencias (`RecipeDeps`) con los ingredientes disponibles que se inyectan al agente. |
| `evals.py` | Evaluaciones automáticas del asistente con `pydantic-evals`. |

## Uso

```bash
uv sync
uv run recipe-assistant      # chat interactivo (escribe "salir" o "exit" para terminar)
uv run python -m recipe_assistant.evals   # ejecutar las evaluaciones
```

## Configuración de variables de entorno

El proyecto lee sus credenciales desde un archivo `.env` (cargado con `python-dotenv` en `main.py`). Este archivo contiene secretos y **no se sube al repositorio** (está en `.gitignore`); en su lugar se incluye `.env.example` como plantilla con los nombres de las variables, sin valores.

1. Copia la plantilla:
   ```bash
   cp .env.example .env
   ```
2. Completa los valores en `.env`:

| Variable | Obligatoria | Descripción |
|---|---|---|
| `GOOGLE_API_KEY` | Sí | Clave de API de Google Gemini, necesaria para el modelo del agente. Se obtiene en [Google AI Studio](https://aistudio.google.com/apikey). |
| `LOGFIRE_TOKEN` | No | Token de escritura de Logfire para enviar trazas. Alternativamente, autentícate con `uv run logfire auth`. |

Si añades una nueva variable al proyecto, agrégala también a `.env.example` (sin el valor real).

## Contenido del curso

### 1. Fundamentos y primer agente con Pydantic-AI
- Qué es PydanticAI
- Creando un agente con PydanticAI
- Instrucciones dinámicas con Pydantic-AI

**En el proyecto:** el `Agent` de `main.py` y la función `add_season`, que ajusta las instrucciones según el mes del año.

### 2. Respuestas estructuradas con PydanticAI
- Respuestas con datos ordenados
- Corrección automática de errores

**En el proyecto:** el modelo `Recipe` de `models.py` como `output_type`, con un validador que, si falla, hace que el modelo reintente (`retries=3`).

### 3. Herramientas con PydanticAI
- Acceso a información externa
- Gestión de datos internos

**En el proyecto:** la herramienta `get_available_ingredients` y `RecipeDeps` (`deps.py`), que dan al agente acceso a los ingredientes disponibles.

### 4. Conversaciones y contexto con PydanticAI
- Memoria de la conversación

**En el proyecto:** `message_history` en el bucle de chat, que conserva el contexto entre mensajes.

### 5. Ejecución asíncrona y streaming con PydanticAI
- Modos de ejecución del asistente
- Respuesta en tiempo real

**En el proyecto:** `chat_loop` usa `run_stream` de forma asíncrona para mostrar la respuesta a medida que se genera.

### 6. Validación del proyecto con PydanticAI
- Pruebas del asistente
- Observabilidad con logfire
- Más allá de PydanticAI

**En el proyecto:** `evals.py` con `pydantic-evals` para probar el asistente, y `logfire` configurado en `main.py` para observar cada ejecución.

## Autor

[Ana Maria Pinto](https://www.linkedin.com/in/ana-maria-pinto-v/)
