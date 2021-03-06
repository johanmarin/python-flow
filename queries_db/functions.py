# Este modulo contiene los archivos necesarios para la carga 
# y modificación de las queries queries en caso de que se requiera
# información desde una base de dat

def read_query(path: str) -> str:
    """Esta fución recibe la ubicación de una query en un archivo, lee el contenido y lo devuelve en formato string

    Args:
        path (str): ubicación del archivo

    Returns:
        str: Salida de la query como string
    """    
    with open(path) as f:
        query = f.read()
        f.close()
    print('Query leida de: %s' %path)
    return query