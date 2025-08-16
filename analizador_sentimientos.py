from transformers import pipeline

def analizar_sentimiento(textos, pipeline_sentimientos):
    """
    Analiza el sentimiento de una lista de textos en inglés utilizando un pipeline de Hugging Face.

    Args:
        textos (list[str]): La lista de textos en inglés a analizar.
        pipeline_sentimientos: El pipeline de análisis de sentimientos pre-cargado.

    Returns:
        list[dict]: Una lista de diccionarios, cada uno con la etiqueta y la puntuación.
    """
    return pipeline_sentimientos(textos)