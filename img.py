importar  os 
from  flask  import  Flask , jsonify , request
from  math  import  sqrt

app  =  Flask ( _name_ )

@ app . rota ( '/' )
def  nao_entre_em_panico ():
    proximo  =  1
    anterior  =  0
    limite  =  98
    encontrado  =  0
    resposta  =  "1, \ n "
    while ( encontrado  <  limite ):
        tmp  =  proximo
        proximo  =  proximo  +  anterior
        anterior  =  tmp
        encontrado  =  encontrado + 1
        resposta + =  str ( proximo ) +  ", \ n "
        
     resposta de retorno

if  _name_  ==  "_main_" :
    porta  =  int ( os . amb . get ( "PORT" , 5000 ))
    app . executar ( host = '0.0.0.0' , porta = porta )
