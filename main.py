"""
Esqueleto de funciones principales de la aplicación movil para el proyecto final del curso IISyC 2021-01.
"""
#Librerias
import time

# Variables
registrado = False
fecha = time.strftime("%x")
usuario = {"nombre":"", "edad":"", "genero":""}
que_hizo = ""
dicc_sentimiento = {}
dicc_actividades = {}
dicc_respuesta = {}
#variables de pregunta_orientadora()
pregunta_del_dia=''
# Funciones



def registro():
  """
  Los datos del usuario se almacenan en un diccionario. Por cada llave (dato) del diccionario se le pide al usuario que ingrese su valor.
  """
  for i in usuario:
    #Este segmento del código obliga a que el usuario ingrese un número entero para la edad.
    if i == "edad":
      edad = input("Ingresa tu {}: ".format(i))
      while type(edad) != int:
        try: 
          edad = int(edad)
        except:
          print("Por favor ingresa un número.")
          edad = input("Ingresa tu {}: ".format(i))
      usuario[i] = edad
      continue
    #Define con que genero gramatical se tratará al usuario.
    if i == "genero":
      print("¿Como quieres que te tratemos? \nEn femenino (1), masculino (2) o neutro (3).")
      usuario[i] = input("Elige una opción: ")
      while usuario[i]!="1" and  usuario[i]!="2" and usuario[i]!="3":
        usuario[i] = input("Elige una opción valida: ")
      continue
    #Ingresa un valor a su correspondiente llave.        
    usuario[i] = input("Ingresa tu {}: ".format(i))
  # Establece que el registro del usuario ya se realizo.
  usuario["nombre"] = usuario["nombre"].lower().capitalize()
  registrado = True
  

def sentimiento_dia(): #Felipe
  """
  Registra como se siente el usuario el día en el que usa la aplicación.
  """
  estado_animo = ""
  print("\n")
  print("Hola",usuario["nombre"],"¿Cómo te encunetras?")
  opciones = ["muy mal","mal","neutral","bien","muy bien"]
  print("| "+" | ".join(opciones).capitalize()+" |")
# El usuario dice como se siente según las opciones dadas.
  estado_animo = input("Me encuentro: ")
  estado_animo = estado_animo.lower()
# Se valida el input según la opciones determinadas.
  while estado_animo not in opciones:
      estado_animo = input("Escribe una opción valida: ")
      estado_animo = estado_animo.lower()
# Se agrega a un diccionario la fecha actual junto con como se siente el usuario.
  dicc_sentimiento[fecha] = estado_animo


def que_hiciste_hoy(): #Daniel
  """
  Registra que ha hecho el usuario en el día que usa la aplicación.
  """

  print("\n")
  print("Hey "+usuario["nombre"]+'! '+"¿Qué hiciste el día de hoy?")
  opciones2 = ["Estudiar", "Leer", "Hacer ejercicio", "Cocinar", "Bailar", "Otra"]
  print("| "+" | ".join(opciones2) + " |")

  que_hizo = input("Lo que hice hoy fué: ").capitalize()

  if que_hizo == "Otra":
      nueva_opcion = input("Ingrese la núeva opción: ").capitalize()
      opciones2.append(nueva_opcion)
      print("| "+" | ".join(opciones2) + " |")
      que_hizo = input("Lo que hice hoy fué: ").capitalize()

  while que_hizo not in opciones2:
    print("Ingrese una opción válida: ")
    que_hizo = input("Lo que hice hoy fué: ")
    que_hizo = que_hizo.capitalize()
    
    if que_hizo == "Otra":
        nueva_opcion = input("Ingrese la núeva opción: ").capitalize()
        opciones2.append(nueva_opcion)
        print("| "+" | ".join(opciones2) + " |")
        que_hizo = input("Lo que hice hoy fué: ").capitalize()
  dicc_actividades[time.strftime("%x")] = que_hizo
  

def pintura():
  pass


def pregunta_orientadora():
  """
  realiza una pregunta al usuario basado en su estado de animo para que este despeje un poco su mente
  """
  print("\n")
  #define que decir en caso que el usuario se sienta mal o muy mal
  if dicc_sentimiento[fecha]=="muy mal" or dicc_sentimiento[fecha]=="mal":
    print('es normal no sentirse bien a veces, sin embargo, guardarlo en nuestro interior no genera nada bueno, asi que, cuentame ¿que te esta haciendo sentir mal?')
    pregunta_del_dia=input()
    dicc_respuesta[fecha] = pregunta_del_dia

  #define que decir en caso que el usuario se sienta neutral
  if dicc_sentimiento[fecha]=='neutral':
    print('sentirse neutral es algo natural, no podemos tener la mente en algo todo el tiempo, sin embargo, siempre es bueno expresar lo que sientes, ¿podrias contarnos un poco mas?')
    pregunta_del_dia=input()
    dicc_respuesta[fecha] = pregunta_del_dia

  #define que decir en caso que el usuario se sienta bien o muy bien
  if dicc_sentimiento[fecha]=="bien":
    print('¡siempre es genial saber que te sientes bien {}!, cuentamos un poco mas sobre ese sentimiento, ¡es bueno tener claro de donde viene tu felicidad!'.format(usuario["nombre"]))
    pregunta_del_dia=input()
    dicc_respuesta[fecha] = pregunta_del_dia  



  pass



def retroalimentacion(): #Diego
    opcion_r = str()
    print('\n'+' RETROALIMENTACIÓN '.center(50, " "), '\n')
    print(('¡Hola ' + usuario['nombre'] + '!').center(50, " "))
    print(
        '\n' +
        'Mediante este menú podrás acceder a la retroalimentación de las actividades que has hecho y los sentimientos diarios que has experimentado desde que empezaste a usar la app'
    )
    #Opciones de retroalimentacion: Sentimientos o actividades
    print(
        '\n¿Cuál retroalimentación deseas ver?\n1. Sentimientos\n2. Actividades'
    )
    #Solicita una opción y no continua con el programa hasta que se ingrese una opción válida
    while opcion_r != '1' and opcion_r != '2':
        opcion_r = input('\nDigita el número de opción que desees: ')
        if opcion_r != '1' and opcion_r != '2':
            print('Digitaste un valor erróneo')

    print()
    #Le recuerda al usuario la opción escogida
    if opcion_r == '1':
        print('¡Bien! Has elegido la retroalimentación de Sentimientos')
    else:
        print('¡Bien! Has elegido la retroalimentación de Actividades')
    #Imprime la retroalimentacion
    print('\nEsta es tu retroalimentación')
    #Si la opción elegida es Sentimiento
    if opcion_r == '1':
        print()
        #Imprime el sentimiento y el día
        for dia, sentimiento in dicc_sentimiento.items():
            print(f'Te sentiste {sentimiento} el {dia} '.center(40, ' '))
            #Si el sentimiento es negativo, da una frase alientadora
            if sentimiento == 'mal' or sentimiento == 'muy mal':
              print('\n¡Vaya! Al parecer no te has sentido de la mejor manera últimamente, pero no te preocupes, sabes que aquí estoy disponible para cuando necesites desahogarte. Puedes contar conmigo :)')
            elif sentimiento == 'bien' or sentimiento == 'muy bien':
              print('\n¡Excelente! Estoy muy feliz de que estés bien :)')
            else:
              print(f'Vas por buen camino pero puedes mejorar')
    #retroalimentacion de actividades si la opcion_r fue 2
    else:
        print(
            f'Las actividades que has hecho últimamente son las siguientes:\n'
        )
        for dia, actividad in dicc_actividades.items():
            print((f'{actividad}'.capitalize()+  f' el {dia} ').center(40, ' '))
        print(f'\nVas por buen camino pero puedes mejorar aún más')


def run():
  if not registrado:
    registro()
    sentimiento_dia()
    que_hiciste_hoy()
    pregunta_orientadora()
    retroalimentacion()

if __name__ == "__main__":
  run()