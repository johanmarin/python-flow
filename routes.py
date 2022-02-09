import os
import yaml

from pydantic import BaseModel
from datetime import datetime
import API.functions as f_api
from starlette.responses import FileResponse

# Load config
def load_config():    
    f = open(os.getcwd().replace('\\', '/') + '/config.yaml' )
    config = yaml.load(f, Loader=yaml.FullLoader)
    f.close()
    return config

# Conexion
config = load_config()
visual_conn = f_api.connect(config)

# Query model
class Query(BaseModel):
    source: str
    sql_query: str
    date: datetime = datetime.now()
    
    
