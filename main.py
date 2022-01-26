import os
import yaml
import conexion_db.functions as cfn
import request.functions as rfn



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