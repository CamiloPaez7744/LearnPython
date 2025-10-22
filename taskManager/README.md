# Task Manager 📋

An intelligent task management system in Python with AI integration via OpenAI for automatic decomposition of complex tasks.

## 📖 Description

Task Manager is a command-line application that allows you to manage tasks efficiently. The application includes traditional task management functionalities and advanced AI-powered features to help you break down complex tasks into more manageable subtasks.

### Key Features

- ✅ **Basic task management**: Create, list, complete, and delete tasks
- 🤖 **AI assistance**: Automatic decomposition of complex tasks using GPT-4
- 💾 **Data persistence**: Automatic storage in JSON format
- 🎯 **Priority system**: Organize your tasks by priority (Low, Medium, High)
- ✨ **Intuitive interface**: Easy-to-use interactive menu
- 🧪 **Fully tested**: Complete unit test suite with pytest

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- OpenAI account with API key (for AI functionalities)

### Installation Steps

1. **Clone the repository:**
```bash
git clone https://github.com/CamiloPaez7744/LearnPython.git
cd taskManager
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**

Create a `.env` file in the project root with your OpenAI API key:
```env
OPENAI_API_KEY=your_api_key_here
```

## 📋 Usage

### Run the application

```bash
python main.py
```

### Main Menu

When you run the application, you'll see the following menu:

```
--- Intelligent Task Manager ---
1. Add Task
2. Add Task with AI Assistance
3. List Tasks
4. Complete Task
5. Delete Task
6. Exit
```

### Funcionalidades

#### 1️⃣ Agregar Tarea Manual
Permite agregar una tarea especificando manualmente la descripción y prioridad.

```
Opción: 1
Enter task description: Completar informe mensual
Enter task priority (Low, Medium, High): High
```

#### 2️⃣ Agregar Tarea con Asistencia de IA
La IA descompone automáticamente una tarea compleja en subtareas más pequeñas.

```
Opción: 2
Enter task description: Desarrollar una aplicación web completa
```

La IA generará subtareas como:
- Diseñar la arquitectura del sistema
- Crear la base de datos
- Desarrollar el backend
- Implementar el frontend
- Realizar pruebas
- Desplegar la aplicación

#### 3️⃣ Listar Tareas
Muestra todas las tareas con su estado, ID, descripción y prioridad.

```
[ ] (ID: 1) Completar informe mensual - Priority: High
[✓] (ID: 2) Revisar correos - Priority: Medium
```

#### 4️⃣ Completar Tarea
Marca una tarea como completada usando su ID.

```
Opción: 4
Enter task ID to complete: 1
Task completed: [✓] (ID: 1) Completar informe mensual - Priority: High
```

#### 5️⃣ Eliminar Tarea
Elimina permanentemente una tarea del sistema.

```
Opción: 5
Enter task ID to delete: 1
```

## 🏗️ Estructura del Proyecto

```
taskManager/
├── main.py                 # Punto de entrada de la aplicación
├── task_manager.py         # Lógica principal de gestión de tareas
├── ai_service.py          # Integración con OpenAI API
├── tasks.json             # Archivo de persistencia de datos
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Documentación del proyecto
├── .env                   # Variables de entorno (no incluido en git)
└── tests/
    └── test_task_manager.py  # Pruebas unitarias
```

## 🧪 Pruebas

El proyecto incluye una suite completa de pruebas unitarias usando pytest.

### Ejecutar las pruebas

```bash
pytest tests/
```

### Ejecutar con cobertura

```bash
pytest --cov=. tests/
```

### Casos de prueba incluidos

- ✅ Agregar y obtener tareas
- ✅ Completar tareas y verificar persistencia
- ✅ Eliminar tareas
- ✅ Incremento automático de IDs
- ✅ Manejo de archivos corruptos o faltantes
- ✅ Formato correcto de archivos JSON

## 📦 Dependencias Principales

- **openai** (2.6.0): Cliente oficial de OpenAI para integración con GPT-4
- **python-dotenv** (1.1.1): Gestión de variables de entorno
- **pytest** (implícito): Framework de pruebas
- **pydantic** (2.12.3): Validación de datos
- **requests** (2.32.5): Cliente HTTP

Ver `requirements.txt` para la lista completa de dependencias.

## 🔧 Componentes del Sistema

### TaskManager
Clase principal que gestiona todas las operaciones CRUD de tareas:
- `add_task(description, priority)`: Crea una nueva tarea
- `list_tasks()`: Muestra todas las tareas
- `complete_task(task_id)`: Marca una tarea como completada
- `delete_task(task_id)`: Elimina una tarea
- `save_tasks()`: Guarda tareas en JSON
- `load_tasks()`: Carga tareas desde JSON

### Task
Clase que representa una tarea individual:
- `id`: Identificador único
- `description`: Descripción de la tarea
- `priority`: Prioridad (Low, Medium, High)
- `completed`: Estado de completado (booleano)

### AI Service
Servicio de integración con OpenAI:
- `suggest_task_decomposition(task)`: Descompone tareas complejas
- `create_simple_tasks(task)`: Simplifica tareas
- `prioritize_tasks(tasks)`: Sugiere priorización
- `generate_task_summary(task)`: Genera resúmenes

## 🔐 Seguridad

- Las API keys se almacenan en variables de entorno (archivo `.env`)
- El archivo `.env` debe incluirse en `.gitignore`
- Nunca compartas tu API key de OpenAI públicamente

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Notas Importantes

- Asegúrate de tener créditos suficientes en tu cuenta de OpenAI
- El modelo GPT-4 tiene costos asociados por uso
- Las tareas se guardan automáticamente en `tasks.json`
- La aplicación maneja errores de archivos corruptos automáticamente

## 🐛 Solución de Problemas

### Error: "OpenAI API key is not set"
**Solución:** Verifica que tu archivo `.env` existe y contiene tu API key correctamente:
```env
OPENAI_API_KEY=tu_api_key_aqui
```

### Error: "No module named 'openai'"
**Solución:** Instala las dependencias:
```bash
pip install -r requirements.txt
```

### Las tareas no persisten entre ejecuciones
**Solución:** Verifica que el archivo `tasks.json` existe y tiene permisos de escritura.

## 📄 Licencia

Este proyecto es parte del repositorio de aprendizaje [LearnPython](https://github.com/CamiloPaez7744/LearnPython).

## 👤 Autor

**Camilo Paez**
- GitHub: [@CamiloPaez7744](https://github.com/CamiloPaez7744)

## 🙏 Agradecimientos

- OpenAI por proporcionar la API de GPT-4
- La comunidad de Python por las excelentes bibliotecas

---

⭐ Si este proyecto te resultó útil, considera darle una estrella en GitHub!