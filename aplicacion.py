import pandas as pd
from traductor import traducir_a_ingles
from analizador_sentimientos import analizar_sentimiento
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer, pipeline

def main():
    """Función principal para ejecutar la aplicación de análisis de sentimientos."""
    # Cargar modelos
    print("Cargando modelo de traducción...")
    modelo_traductor = M2M100ForConditionalGeneration.from_pretrained("facebook/m2m100_418M")
    tokenizador_traductor = M2M100Tokenizer.from_pretrained("facebook/m2m100_418M")

    print("Cargando modelo de análisis de sentimientos...")
    pipeline_sentimientos = pipeline(task="sentiment-analysis", model="siebert/sentiment-roberta-large-english")

    print("Aplicación de Análisis de Sentimientos")
    print("1. Ingresar texto manualmente")
    print("2. Proporcionar un archivo CSV")

    opcion = input("Ingrese su opción (1 o 2): ")

    if opcion == '1':
        texto = input("Ingrese el texto a analizar: ")
        texto_traducido = traducir_a_ingles(texto, modelo_traductor, tokenizador_traductor)
        sentimiento = analizar_sentimiento(texto_traducido, pipeline_sentimientos)

        # Se corrige el problema de tipo accediendo al primer elemento de la lista.
        # Se añade una verificación para evitar errores si la lista está vacía.
        if sentimiento and isinstance(sentimiento, list) and len(sentimiento) > 0:
            print(f"\nTexto original: {texto}")
            print(f"Texto traducido: {texto_traducido}")
            print(f"Sentimiento: {sentimiento[0]['label']} (Puntuación: {sentimiento[0]['score']:.4f})")
        else:
            print("\nNo se pudo obtener el sentimiento para el texto proporcionado.")

    elif opcion == '2':
        ruta_archivo = input("Ingrese la ruta al archivo CSV: ")
        try:
            df = pd.read_csv(ruta_archivo)
            if 'texto' not in df.columns:
                print("Error: El archivo CSV debe tener una columna 'texto'.")
                return

            textos_originales = df['texto'].tolist()

            print(f"Procesando {len(textos_originales)} comentarios. Esto puede tardar unos minutos...")

            # 1. Traducir todos los textos en un solo lote
            print("Traduciendo textos...")
            textos_traducidos = traducir_a_ingles(textos_originales, modelo_traductor, tokenizador_traductor)

            # 2. Analizar todos los textos traducidos en un solo lote
            print("Analizando sentimientos...")
            sentimientos = analizar_sentimiento(textos_traducidos, pipeline_sentimientos)

            # 3. Construir el DataFrame de resultados
            # Se añade un control de tipos para evitar el error de Pylance.
            if isinstance(sentimientos, list):
                df_resultados = pd.DataFrame(sentimientos)
                df_resultados = df_resultados.rename(columns={'label': 'etiqueta_sentimiento', 'score': 'puntuacion_sentimiento'})
                df_resultados.insert(0, 'texto_traducido', textos_traducidos)
                df_resultados.insert(0, 'texto_original', textos_originales)

                print("\nAnálisis completo. Resultados:")
                print(df_resultados)

                guardar_resultados = input("¿Guardar resultados en un nuevo archivo CSV? (si/no): ")
                if guardar_resultados.lower() == 'si':
                    ruta_archivo_salida = input("Ingrese la ruta para el archivo CSV de salida: ")
                    df_resultados.to_csv(ruta_archivo_salida, index=False)
                    print(f"Resultados guardados en {ruta_archivo_salida}")
            else:
                print("Error: El resultado del análisis de sentimientos no es una lista válida.")


        except FileNotFoundError:
            print(f"Error: Archivo no encontrado en {ruta_archivo}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

    else:
        print("Opción no válida. Por favor, ingrese 1 o 2.")

if __name__ == "__main__":
    main()