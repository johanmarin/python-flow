import os
import json
import requests
import pandas as pd


def get_json(config: dict) -> dict:
    """esta función permite obtener los datos desde la API y convertirlos a formato dataframe

    Args:
        config (dict): diccionario con los datos para realizar la consulta
                        {
                            'server': {
                                'url': 'dirección del host', 
                                'routes': {
                                    'data': 'query', 
                                    'file': 'csv'
                                    }
                                },
                            
                            'downloads': './downloads/data.csv', 
                            'query': {
                                'source': 'nombre del programa', 
                                'sql_query': 'codigo sql de la consulta'
                                }
                        }

    Returns:
        dict: datos obtenidos por la consulta
    """    
    url = config['DB_server']['url'] + config['DB_server']['routes']['data']
    response = requests.get(url, json=config['query']) 
    resp = response.text
    if 'Error' in resp:
        return resp
    else:
        return {'type': 'csv', 'data': json.loads(resp)}

def get_csv(config: dict) -> str:
    """esta función permite obtener los datos desde la API y almacenarlos en un archivo csv en la carpeta downloads

    Args:
        config (dict): diccionario con los datos para realizar la consulta
                        {
                            'server': {
                                'url': 'dirección del host', 
                                'routes': {
                                    'data': 'query', 
                                    'file': 'csv'
                                    }
                                },
                            
                            'downloads': './downloads/data.csv', 
                            'query': {
                                'source': 'postman', 
                                'sql_query': 'SELECT TOP(10) * FROM dbo.creCreditos;'
                                }
                        }

    Returns:
        str: Retorna la ruta del archivo descargado
    """     
    filename = config['downloads']
    # Remove old files
    if os.path.exists(filename):
        os.remove(filename)
        print('El archivo ya exitia y fue necesario reemplazarlo')
        
    url = config['DB_server']['url'] + config['DB_server']['routes']['file']
    r = requests.get(url, allow_redirects=True, json=config['query'])
    
    if 'Error' in r.text:
        return json.loads(r.text)
    else:
        open(filename, 'wb').write(r.content)
        return {'type': 'csv', 'path': filename}
    

def req(config: dict, sql_query: str) -> dict:
    """esta función permite obteenr datos por medio de la API de la base de datos, se debe ingresar la query

    Args:
        config (dict): diccionario con los datos de configuración
        sql_query (str): Query sql

    Returns:
        [type]: puede devolver un dicconario
    """    
    
    config['query'] = {'source': config['name'], 'sql_query': sql_query}
    
    if config['type'] == 'json':
        return get_json(config)
    elif config['type'] == 'csv':
        return get_csv(config)
    else:
        return {'Error': 'No se han devuelto datos'} 