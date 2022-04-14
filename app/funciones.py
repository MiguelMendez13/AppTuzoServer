import string
def palabrasAceptadas(datos):
    letras = []
    todos = []
    numeros = []
    for x in string.ascii_lowercase:
        letras.append(x)
        todos.append(str(x))

    for x in range(0,10):
        numeros.append(x)
        todos.append(str(x))

    grupos={
        "ISC":[
            "1S11","2S11","2S12","2S21","3S11","4S11",
            "4S11","4S21","5S11","6S11","6S12","6S21",
            "7S11","8S11","8S12","8S21","9S21"
         ],
        "TIC":[]
    }



    """Matricula
    Nombre
    ApPaterno
    ApMaterno
    Carrera
    Grupo
    Correo
    Telefono
    Contrasenia
    ConfContra"""
    errores=""

    for x in datos:
        if errores == "":
            if x =="Nombre" or x == "ApPaterno" or x == "ApMaterno":
                if len(datos[x])>20:
                    errores+="Solo se permiten maximo 20 letras en el campo: "+x+"\n"
                    break
                for x2 in datos[x]:
                    if x2.lower() in letras:
                        pass
                    else:
                        errores+="Solo se permiten letras en el campo: "+x+"\n"
                        break

            elif x == "Matricula" or x == "Telefono":
                if (len(datos[x])!=10 and x == "Telefono"):
                    errores+="Solo se permiten 10 numeros en el campo: "+x+"\n"
                    break
                elif (len(datos[x])!=9 and x == "Matricula"):
                    errores+="Solo se permiten 9 numeros en el campo: "+x+"\n"
                    break
                for x2 in datos[x]:
                    try:
                        if int(x2) in numeros:
                            pass
                    except:
                        errores+="Solo se permiten numeros en el campo: "+x+"\n"
                        break

            elif x == "Carrera":
                if datos[x]=="ISC" or datos[x]=="TIC":
                    if datos["Grupo"] in grupos[datos[x]]:
                        pass
                    else:
                        errores+="Error en el campo: Grupo\n"
                        break
                else:
                    errores+="Error en el campo: "+x+"\n"
                    break
            elif x == "Contrasenia":
                if len(datos[x])>20:
                    errores+="Solo se permiten maximo 20 caracteres(numeros,letras) en el campo: "+x+"\n"
                    break
                for x2 in datos[x]:
                    # print(x2)
                    if x2.lower() in todos:
                        pass
                    else:
                        errores+="Solo se permiten caracteres(numeros,letras) en el campo: "+x+"\n"
                        break
            elif x == "ConfContra":
                if datos[x]==datos["Contrasenia"]:
                    pass
                else:
                    errores+="La contrasenia y la confirmacion de contrasenia no son iguales"
            
            elif x == "Grupo":
                pass
            
            elif x=="Correo":
                pass
            else:
                print(x)
                errores+="ERROR intenta mas tarde"
        else:
             break

    return(errores)




