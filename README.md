# Proyecto de Análisis de Sentimientos

Este proyecto es una aplicación de consola que analiza el sentimiento de los comentarios de los usuarios. La aplicación puede procesar texto introducido manualmente o desde un archivo CSV. Utiliza un modelo de traducción para convertir el texto al inglés y, posteriormente, un modelo de análisis de sentimientos para clasificar cada comentario como positivo o negativo.

De este modo, es posible emplear un único modelo entrenado en inglés para detectar y clasificar emociones en más de 100 idiomas, evitando la necesidad de entrenar modelos específicos para cada lengua. Únicamente se requiere realizar fine-tuning puntual para adaptar nuevas expresiones o giros que puedan generar traducciones ambiguas o incorrectas.
<br>

## Características

- **Traducción de idiomas**: Traduce el texto de cualquier idioma a inglés antes del análisis.
- **Análisis de sentimientos**: Clasifica el sentimiento del texto en inglés.
- **Entrada dual**: Acepta texto directamente desde la consola o a través de un archivo CSV.
- **Resultados guardables**: Permite guardar los resultados del análisis en un nuevo archivo CSV.
<br>

## Modelos Utilizados

- **Traducción**: `facebook/m2m100_418M` - Un modelo de traducción de secuencia a secuencia que puede traducir 100 idiomas.
- **Análisis de Sentimientos**: `siebert/sentiment-roberta-large-english` - Un modelo afinado para el análisis de sentimientos en texto en inglés.
<br>

## Estructura del Proyecto

```
.visual studio code/
├── CSV_OPINIONES # aqui es donde se introducen los CSV con las opiniones
├── aplicacion.py # Script principal de la aplicación
├── analizador_sentimientos.py # Módulo para el análisis de sentimientos
├── traductor.py # Módulo para la traducción de texto
├── test_traductor.py # Pruebas unitarias para el traductor
└── requirements.txt # Dependencias de Python
```
***IMPORTANTE los CSV deben contenter una columna "texto" que contenga los comentarios.***

<br>

## Requisitos Previos

- Python 3.6 o superior
- `pip` para instalar paquetes de Python

## Instalación

1. **Clona el repositorio (o descarga los archivos):**

    ```bash
    git clone <url-del-repositorio>
    cd <nombre-del-directorio>
    ```

2. **Crea un entorno virtual (recomendado):**

    ***Para macos y linux***
    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

    ***Para windows***
    ```bash
    py -m venv venv
    .\venv\Scripts\activate.ps1
    ```

3. **Instala las dependencias:**

    ***Para macos y linux***
    ```bash
    pip install -r requirements.txt
    ```

***Para windows***
```bash
py pip install -r requirements.txt
```
<br>

## Uso

Para ejecutar la aplicación, navega hasta el directorio del proyecto en tu terminal y ejecuta:

```bash
python aplicacion.py
```

La aplicación te dará dos opciones:

1.  **Ingresar texto manualmente**: Escribe o pega el texto que deseas analizar directamente en la consola.
2.  **Proporcionar un archivo CSV**: Introduce la ruta a un archivo CSV. El archivo debe contener una columna llamada `texto` con los comentarios a analizar.
<br>

### Ejemplo con Archivo CSV

Si tienes un archivo `comentarios.csv` con el siguiente contenido:

```csv
texto
¡Este producto es increíble!
No me gustó nada el servicio.
El paquete llegó a tiempo.
```

La aplicación procesará cada comentario, lo traducirá al inglés, analizará su sentimiento y mostrará los resultados en una tabla. También te preguntará si deseas guardar estos resultados en un nuevo archivo CSV.
<br>

## Pruebas

Para ejecutar las pruebas unitarias para el módulo de traducción, ejecuta:

```bash
python test_traductor.py
```

Esto verificará que la función de traducción funciona como se espera para diferentes idiomas.
