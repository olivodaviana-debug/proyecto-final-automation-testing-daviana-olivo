# Proyecto Final: Framework de Automatización (Daviana Olivo)

Este proyecto es un framework de pruebas automatizadas que combina pruebas de interfaz gráfica (UI) y de API en un único entorno modular usando Python. 

Para la parte visual (UI) aplicamos el patrón **Page Object Model (POM)** para mantener las interacciones separadas de la lógica de los tests. Para la API, usamos una estrategia de **Mocking** local; de esta forma las pruebas corren rápido y no fallan por problemas de conexión o bloqueos de red externos.

## 🛠️ Tecnologías que usamos
- **Python 3.x** como lenguaje base.
- **Pytest** para organizar y correr los casos de prueba.
- **Selenium WebDriver** para interactuar con el navegador.
- **Pytest-HTML** para armar el reporte visual al terminar.

## 📁 Cómo está organizado el código
```text
proyecto-final-automation-testing-[daviana-olivo]/
├── config/             # Configuración básica (URLs, esperas, etc.)
├── data/               # Archivos JSON con datos para las pruebas
├── pages/              # Clases de Page Object Model (BasePage, LoginPage)
├── tests/              # Los archivos de pruebas reales (UI y API)
├── utils/              # Herramientas de soporte (Logger, clientes)
├── .gitignore          # Archivos que Git no debe subir al repositorio
├── pytest.ini          # Preferencias de ejecución de Pytest
└── requirements.txt    # Lista de librerías necesarias
```

## 🚀 Instalación rápida

1. **Clonar este repositorio:**
   ```bash
   git clone https://github.com
   cd proyecto-final-automation-testing-daviana-olivo
   ```

2. **Armar y activar el entorno virtual:**
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Si usás Windows (Git Bash)
   ```

3. **Instalar los paquetes necesarios:**
   ```bash
   pip install -r requirements.txt
   ```

## 📊 Cómo correr las pruebas y ver qué pasó

Para lanzar toda la suite de pruebas al mismo tiempo en modo silencioso (sin que se abra la ventana del navegador), ejecutá:
```bash
pytest
```

### ¿Dónde ver los resultados?
Cuando las pruebas terminan, el framework arma automáticamente un archivo con el informe visual:
- Lo encontrás en la carpeta: `reports/report.html`
- Al abrirlo en tu navegador, vas a poder ver qué pruebas pasaron, cuáles fallaron, cuánto tardaron y el detalle del error en caso de que alguna falle.