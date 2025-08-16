from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

def traducir_a_ingles(textos, modelo, tokenizador):
    """
    Traduce una lista de textos a inglés usando el modelo M2M100.

    Args:
        textos (list[str]): La lista de textos a traducir.
        modelo: El modelo M2M100 pre-entrenado.
        tokenizador: El tokenizador M2M100 pre-entrenado.

    Returns:
        list[str]: La lista de textos traducidos en inglés.
    """
    # El tokenizador necesita ser configurado con el idioma de origen,
    # pero M2M100 a menudo puede detectar el idioma de origen automáticamente.
    # Para este proyecto dejaremos que el modelo lo maneje.
    entradas = tokenizador(textos, return_tensors="pt", padding=True, truncation=True)
    tokens_generados = modelo.generate(**entradas, forced_bos_token_id=tokenizador.get_lang_id("en"))
    textos_traducidos = tokenizador.batch_decode(tokens_generados, skip_special_tokens=True)
    return textos_traducidos