import os
import json
import requests
import pandas as pd


def get_data(config: dict) -> pd.DataFrame:
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
        pd.DataFrame: datos obtenidos por la consulta
    """    
    url = config['server']['url'] + config['server']['routes']['data']
    response = requests.get(url, json=config['query']) 
    resp = response.text
    if 'Error' in resp:
        return resp
    else:
        df = pd.DataFrame.from_dict(json.loads(resp))
        return df

def get_file(config: dict):
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
    """  
    filename = config['downloads']
    # Remove old files
    if os.path.exists(filename):
        os.remove(filename)
        
    url = config['server']['url'] + config['server']['routes']['file']
    r = requests.get(url, allow_redirects=True, json=config['query'])
    
    if 'Error' in r.text:
        return json.loads(r.text)
    else:
        open(filename, 'wb').write(r.content)
        if os.path.exists(filename):
            df = pd.read_csv(filename)
            os.remove(filename)
            return df
    

def req(config: dict, sql_query: str) -> pd.DataFrame:
    """esta función permite obteenr datos por medio de la API de la base de datos, se debe ingresar la query

    Args:
        config (dict): diccionario con los datos de configuración
        sql_query (str): Query sql

    Returns:
        [type]: pd.
    """    
    
    config['query'] = {'source': config['name'], 'sql_query': sql_query}
    
    if config['type'] == 'json':
        return get_data(config)
    elif config['type'] == 'csv':
        return get_file(config)
    else:
        return {'Error': 'No se han devuelto datos'} 