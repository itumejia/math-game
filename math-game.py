from random import randint

#Cuando el usuario gana/termina el juego, su score sera almacenado en el file con los marcadores de todos los usuarios con la siguiente función
def agregarscore (nombre, score):
    marcador=open ('marcador.txt','a')
    marcador.write('\n{} {}'.format(score,nombre))
    marcador.close() 

#Cuando el usuario elija la opción de ver el marcador, la siguiente función leerá el file con el marcador y lo ordenará para después mostrárselo al usuario
def mostrarmarcador ():
    print('\n')
    lista=[]
    lista2=[]
    f=open('marcador.txt','r')

#Este for vaciará todos los datos en una matriz y dividirá los datos en dos columnas: puntaje y nombre    
    for line in f:
        wordlist=line.split()
        lista.append(wordlist)
    f.close()
    
#En la segunda lista se generará el número de filas necesarias
    for i in range (len(lista)):
        lista2.append([])
    
#Se vaciarán los datos en la segunda lista pero esta vez convirtiendo los puntajes en números enteros
    for i in range (len(lista)):
        lista2[i].append(int(lista[i][0]))
        lista2[i].append(lista[i][1])
  
#Se ordenarán los datos de acuerdo al puntaje y se imprimirán
    lista2=sorted(lista2, key = lambda x: x[0], reverse = True)
    print ('Score\t\tNombre')
    for i in range (len(lista2)):
        for j in range (2):
            print(lista2[i][j],'\t\t',end='')
        print('\n')
    print('\n\n')


#Esta función se correrá cada vez que el juego le pida al usuario que ingrese algo.
#Revisará que no escriba letras y si lo hace, le pedirá que lo intente de nuevo
def recibirdatos (texto):
    while True:
        try:
            user=float(input(texto))
        except:
            print('***Ingresa solo números***')
        else:
            break
    return user


#Esta se función se correrá cuando se le pida al usuario su nombre
#Revisará que el usuario no ingrese solo números, si lo hace, le pedirá que lo intente de nuevo
def recibirnombre (texto):
    while True:
        user=str(input(texto))
        if user.isdecimal() == False:
            break
        else:
            print('Ingresa letras')
    return user


#Función que será llamada para ejecutar el ejercicio 1. (Primer nivel)
#Este ejercicio abarca los temas de: suma y resta de variables con los mismos exponentes, y multiplicación y división de exponentes.
def ej1 (sabiduria): #Todos los ejercicios requerirán el número de "puntos de sabiduría" previos para sumarle o restarle si el usuario acertó o no
    exp1=randint(1,10)
    exp2=randint(1,10)
    signo=['+','-','x','÷']
    xs=randint(1,4)
    
    if xs==1:
        cof1=randint(-15,15)
        cof2=randint(1,15)
        print('Calcula el coeficiente y exponente resultante para x')
        print(cof1,'x^',exp1,' ',signo[0], ' ',cof2,'x^',exp1,' =')
        rescof= cof1+cof2
        resexp=exp1
        usercof=recibirdatos('Escriba el coeficiente de su resultado: ')
        userexp=recibirdatos('Escriba el exponente de su resultado: ')
        if rescof==usercof and resexp==userexp:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',rescof,'x^',resexp)
    elif xs==2:
        cof1=randint(-15,15)
        cof2=randint(1,15)
        print('Calcula el coeficiente y exponente resultante para x')
        print(cof1,'x^',exp1,' ',signo[1], ' ',cof2,'x^',exp1,' =')
        rescof= cof1-cof2
        resexp=exp1
        usercof=recibirdatos('Escriba el coeficiente de su resultado: ')
        userexp=recibirdatos('Escriba el exponente de su resultado: ')
        if rescof==usercof and resexp==userexp:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',rescof,'x^',resexp)
    elif xs==3:
        cof1=randint(1,15)
        cof2=randint(1,15)
        print('Calcula el coeficiente y exponente resultante para x')
        print(cof1,'x^',exp1,' ',signo[2], ' ',cof2,'x^',exp2,' =')
        rescof= cof1*cof2
        resexp=exp1+exp2
        usercof=recibirdatos('Escriba el coeficiente de su resultado: ')
        userexp=recibirdatos('Escriba el exponente de su resultado: ')
        if rescof==usercof and resexp==userexp:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',rescof,'x^',resexp)

    elif xs==4:
        print('Calcula el exponente resultante para x')
        print('x^',exp1,' ',signo[3], ' x^',exp2,' =')
        resexp=exp1-exp2
        userexp=recibirdatos('Escriba el exponente de su resultado: ')
        if resexp==userexp:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era x^',resexp)
    return sabiduria


#Función que será llamada para ejecutar el ejercicio 2. (Primer nivel)
#Este ejercicio abarca los temas de: ejercicios simples de probabilidad con ilustración gráfica
def ej2(sabiduria):
    caja=[[],[],[]]
    ej=randint(1,2)
    o=0
    x=0
    for i in range(3):
        for j in range(3):
            xo=randint(1,2)
            if xo==1:
                caja[i].append('o')
                o+=1
            elif xo==2:
                caja[i].append('x')
                x+=1
                
    print('En una caja hay los siguientes elementos')
    for i in range(3):
        for j in range(3):
            print(caja[i][j],'\t', end='')
        print('\n')
    
    if ej==1:
        print('Cuál es la posibilidad de que salga una x?')
        res=x/9
        res=round(res,2)
        user=recibirdatos('Escribe tu respuesta redondeada a dos decimales: ')
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    if ej==2:
        print('Cuál es la posibilidad de que salga una o?')
        res=o/9
        res=round(res,2)
        user=recibirdatos('Escribe tu respuesta redondeada a dos decimales: ')
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    return sabiduria
    

#Función que será llamada para ejecutar el ejercicio 3. (Segundo nivel)
#Este ejercicio abarca los temas de: ecuaciones de primer grado
def ej3(sabiduria):
    numx=randint(1,2)
    print('Cuánto vale x? (Redondea a dos números decimales)')
    if numx==1:
        a=randint(-50,50)
        b=randint(0,50)
        c=randint(-50,50)
        print(a,'x+',b,'x=',c)
        res=c/(a+b)
        user=recibirdatos('x = ')
        res=round(res,2)
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    if numx==2:
        a=randint(-50,50)
        b=randint(0,50)
        c=randint(-50,50)
        d=randint(0,50)
        print(a,'x+',b,'x=',c,'+',d)
        res=(c+d)/(a+b)
        user=recibirdatos('x = ')
        res=round(res,2)
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    return sabiduria


#Función que será llamada para ejecutar el ejercicio 4. (Segundo nivel)
#Este ejercicio abarca los temas de: problemas de probabilidad avanzados
def ej4(sabiduria):
    rojo=randint(1,20)
    azul=randint(1,20)
    verde=randint(1,20)
    total=rojo+azul+verde
    x=randint(1,3)
    print('En una urna hay {} bolas rojas, {} bolas azules y {} bolas verdes'.format(rojo,azul,verde))
    if x==1:
        print('Calcula la posibilidad de que salga una bola roja. ')
        res=rojo/total
        user=recibirdatos('Escribe tu resultado redondeado a dos decimales ')
        res=round(res,2)
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    if x==2:
        print('Calcula la posibilidad de que salga una bola azul. ')
        res=azul/total
        user=recibirdatos('Escribe tu resultado redondeado a dos decimales ')
        res=round(res,2)
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    if x==3:
        print('Calcula la posibilidad de que salga una bola verde. ')
        res=verde/total
        user=recibirdatos('Escribe tu resultado redondeado a dos decimales ')
        res=round(res,2)
        user=round(user,2)
        if user==res:
            sabiduria+=1
            print('Respuesta correcta! Sigue así!')
        else:
            sabiduria-=2
            print('Respuesta incorrecta, esfuérzate más. La respuesta correcta era ',res)
    return sabiduria

#Funcion que contiene el primer nivel del juego, será llamada cuando el usuario elija lo opción de iniciar el juego
def nivel1(sabiduria):
    print ('Este es el primer nivel. \nAcumula 10 puntos de sabiduría para llegar al segundo nivel! \nTus respuestas correctas te darán un punto de sabiduría y las incorrectas te quitarán 2\nTen pocas respuestas incorrectas para tener un Score más alto!')     
    intentos=0 #Se contarán el número de ejercicios que el usuario realiza para después sacar el score
    while True:
        if sabiduria <=0:
            sabiduria=0
        
        if sabiduria <10:
            intentos+=1
            print('\nTienes ',sabiduria,' puntos de sabiduría. Suma otros ',10-sabiduria,' para avanzar al siguiente nivel')
            ejercicio=randint(1,2)
            if ejercicio==1:
                sabiduria=ej1(sabiduria)
            if ejercicio==2:
                sabiduria=ej2(sabiduria)
        else:
            break
    print('''
░░░░░░░░░░░░░░░░░░░░░░█████████
░░███████░░░░░░░░░░███▒▒▒▒▒▒▒▒███
░░█▒▒▒▒▒▒█░░░░░░░███▒▒▒▒▒▒▒▒▒▒▒▒▒███
░░░█▒▒▒▒▒▒█░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░░█▒▒▒▒▒█░░░██▒▒▒▒▒██▒▒▒▒▒▒██▒▒▒▒▒███
░░░░░█▒▒▒█░░░█▒▒▒▒▒▒████▒▒▒▒████▒▒▒▒▒▒██
░░░█████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░░░█▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒██
██▒▒▒███████████▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒▒██
█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒████████▒▒▒▒▒▒▒██
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░█▒▒▒███████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██
░██▒▒▒▒▒▒▒▒▒▒████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█
░░████████████░░░█████████████████ ''')

         
    print('\nFelicidades! Has llegado al segundo nivel')
    score = nivel2(intentos)
    return score
        
#Función que contiene el segundo nivel del juego, será llamada inmediatamente después de terminar el primer nivel
def nivel2(intentos):
    sabiduria=0
    print('Tus puntos de sabiduría se han reiniciado a 0! \nConsigue 10 puntos de sabiduría más para ganar el juego!!!')
    while True:
        if sabiduria <=0:
            sabiduria=0
        print('\nTienes ',sabiduria,' puntos de sabiduría. Suma otros ',10-sabiduria,' para ganar el juego!')
        
        if sabiduria <10:
            intentos+=1
            ejercicio=randint(1,2)
            if ejercicio==1:
                sabiduria=ej3(sabiduria)
            elif ejercicio==2:
                sabiduria=ej4(sabiduria)
        else:
            break
    score = 120-intentos #Después de ganar el juego se calculará el score. Se calcula de esta manera porque el puntaje máximo (100) se logra cuando el usuario termina el juego en tan solo 20 intentos
    if score <=0:
        score=0
    print('''                                 .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~''')
    print ('Felicidades!!! Has ganado! Tu score ha sido de ',score)
    return score

sabiduria=0
cont=-1
nombre=recibirnombre('Cuál es tu nombre? ')
marcador = []


#Menú. Se continuará mostrando hasta que el usuario decida salir
while True:
    print('Bienvenid@ ',nombre,'!')
    print('''
    1: Comenzar el juego.
    2: Mostrar marcador global.
    3: Salir.''')

    menu=recibirdatos('Selecciona una opción: ')

    if menu==1:
        score=nivel1(sabiduria)
        agregarscore(nombre,score)
    elif menu==2:
        mostrarmarcador()
    elif menu==3:
        break
    else:
        print('Opción no válida')
    
