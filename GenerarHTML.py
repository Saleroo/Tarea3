from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
#debe bytes de paridad deben ser 16 o 24 bytes
# si se usa 16 bytes -> la llave1 coincide con la llave3 pero llave2 es diferente
# si se usa 24 bytes -> la llave1,2,3 son diferenetes

# ejemplo de llave de 16 bytes :"llave secreta xd"
# ejemplo de llave de 24 bytes :"llave secreta de 3DES :o"


#  mode ECB , fill mode PKCS5Padding
BS = DES3.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)

unpad = lambda s : s[0:-ord(s[-1])]


def contenidoHTML(texto_plano,llave):
    llave=bytes(llave, 'utf-8') #la llave se codifica a bytes con utf-8

    while True:
        try:
            key = DES3.adjust_key_parity(llave)
            break
        except ValueError:
            pass


    cipher = DES3.new(key, DES3.MODE_ECB) #define tipo de cifrado 3DES modo ECB con la llave entregada

    textoPad = pad(texto_plano) #se añade el pad al string de textoplano
    text = bytes(textoPad, 'utf-8') # el textoplano con pad se codifica a bytes con utf-8

    msg_cifrado = cipher.encrypt(text) #se encripta el texto 








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

def GenerarHTML(texto_plano,llave):
    
    f= open('PagWeb.html','w')
    plantilla = contenidoHTML(texto_plano,llave)
    f.write(plantilla)
    f.close()





print("================================================")
texto_plano = input("Ingrese el texto plano: ")
print("================================================")
llave = input("Ingrese la llave (debe tener 16 o 24 bytes es decir largo 16 o 24): ")
if(len(llave) == 16):
    print("Se ingreso una llave de 16 bytes")
elif(len(llave) == 24):
    print("Se ingreso una llave de 24 bytes")
else:
    print("La llave no cumple con la condicion de ser de 16 o 24 bytes.")
    exit(1)



GenerarHTML(texto_plano,llave)

exit(0)

