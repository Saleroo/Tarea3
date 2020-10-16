import base64
import camellia






def contenidoHTML(texto_plano,llave,variable_inicial):
    c1 = camellia.CamelliaCipher(key=llave, IV=variable_inicial, mode=camellia.MODE_CBC)
    encrypted = c1.encrypt(texto_plano)
    msg_cifrado=base64.standard_b64encode(encrypted)



    return f"""
        <!DOCTYPE html>
    <html lang="es">
    <head>

    </head>
        <body>

            <p>Este sitio contiene un mensaje secreto</p>
            <div class="algorithm" id="{msg_cifrado}"></div>
        </body>

    </html>
    """

def GenerarHTML(texto_plano,llave,variable_inicial):
    
    f= open('PagWeb.html','w')
    plantilla = contenidoHTML(texto_plano,llave,variable_inicial)
    f.write(plantilla)
    f.close()







print("la llave,IV y texto plano deben ser de 16 caracteres" )

texto_plano = input("Ingrese el texto plano: ")
if(len(texto_plano)!= 16):
    print("no ingreso 16 caracteres de texto plano")
    exit(1)

texto_plano = bytes(texto_plano, 'utf-8')

llave = input("Ingrese la llave: ")
if(len(llave)!= 16):
    print("no ingreso 16 caracteres de llave")
    exit(1)

llave = bytes(llave, 'utf-8')

variable_inicial = input("Ingrese la vector de inicializacion(IV): ")
if(len(variable_inicial)!= 16):
    print("no ingreso 16 caracteres de IV")
    exit(1)

variable_inicial = bytes(variable_inicial, 'utf-8')

GenerarHTML(texto_plano,llave,variable_inicial)

exit(0)

