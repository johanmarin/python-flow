import os
import yaml
import queries_db.functions as cfn
import request.functions as rfn
import API.functions as f_api
from fastapi import FastAPI



# Load config
def load_config(): 
    PATH =  os.getcwd().replace('\\', '/') 
    f = open(PATH+ '/config.yaml' )
    config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return config, PATH

config, PATH = load_config()

if __name__=='__main__':
    sql_query = cfn.read_query(PATH+config['queries_path']+config['query_prueba'])
    print(sql_query)
    sol = rfn.req(config, sql_query)
    print(sol)
    
    
app = FastAPI()

# Root route
@app.get('/')
def read_root():
    return {"Bienvenido":"La API de ####### esta en linea"}

# Get query like json
@app.get('/prueba')
def get_query_prueba():
    return 'Hola'