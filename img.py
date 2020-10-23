import  os 
from  flask  import  Flask , jsonify , request
from  math  import  sqrt

app  =  Flask(__name__)

@.route( '/' )
def  nao_entre_em_panico ():
    proximo  =  1
    anterior  =  0
    limite  =  98
    encontrado  =  0
    resposta  =  "1, \ n "
    while ( found  <  limite ):
        tmp  =  proximo
        proximo  =  proximo  +  anterior
        anterior  =  tmp
        encontrado  =  encontrado + 1
        resposta + =  str ( proximo ) +  ", \ n "
        
     return resposta

if  __name__  ==  "__main__" :
    port  =  int(os.environ.get("PORT" , 5000 )
    app.run(host = '0.0.0.0' , port=port)

