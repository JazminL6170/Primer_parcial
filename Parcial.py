from Funciones_parcial import *
menu_opciones = '''\n\n"****   BIENVENIDO  ****
1) Cargar participantes.
2) Cargar puntuaciones.
3) Mostrar puntuaciones.
4) Participantes con promedio mayor a 4.
5) Participantes con promedio mayor a 7.
6) Promedio de cada jurado.
7) Jurado más estricto.
8) Buscar participante por nombre.
9) Mostrar los tres participantes con mayor puntaje promedio.
10) Participantes ordenados alfabéticamente.
11) Salir.

Seleccione una opcion: '''
def menu():
  participantes = crear_array(5)
  votos_jurados = crear_matriz(5, 3, 0)
  puntajes_cargados = False
  participantes_cargados = False
  eleccion_menu = None
  while eleccion_menu != "11":
    eleccion_menu = (input(menu_opciones))


    match eleccion_menu: 
        case "1":  
           bandera = cargar_participantes(participantes)
           participantes_cargados = True
           if bandera == True:
              print("\n** Participantes cargados exitosamente. **")
           else:
              print("\n** No pudo realizarse la carga, intentelo nuevamente.. **")
              participantes_cargados = False
           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()
        case "2":
           
           if participantes_cargados == False:
               print("\n** ERROR AL CARGAR LOS PUNTAJES **\n " \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
              bandera = cargar_puntuacion(participantes,votos_jurados)
              if bandera == True: 
                 print("\n** Puntuaciones cargadas exitosamente. **")
                 puntajes_cargados = True 
              else:
                 print("\n** No pudo realizarse la carga, intentelo nuevamente.. **")
              

           input("\nPresiona Enter para continuar...") 
           limpiar_pantalla() 
        case "3":
           
           if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL MOSTRAR LOS PUNTAJES **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
             mostrar_todos_los_participantes(participantes, votos_jurados)

           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()
 
        case "4":
           if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL MOSTRAR LOS PUNTAJES **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
             print("\n** PARTICIPANTES CON PROMEDIO MAYOR A 4 **\n" )
             existe = verificar_promedio(participantes,votos_jurados,4)
             if existe == False:
                print("** No hay participantes con promedio mayor a 4. **")
           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()

        case "5":
           if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL MOSTRAR LOS PUNTAJES **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
             print("\n** PARTICIPANTES CON PROMEDIO MAYOR A 7 **\n" )
             existe = verificar_promedio(participantes,votos_jurados,7)
             if existe == False:
                print("** No hay participantes con promedio mayor a 7. **")
           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()

        case "6":
           if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL MOSTRAR LAS PUNTUACIONES **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
             print("\n** PROMEDIO PUNTUACION DE LOS JURADOS **\n" )
             mostrar_jurados(votos_jurados)

           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()

        case "7":
           if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL MOSTRAR EL JURADO MAS ESTRICTO **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
             print("\n** JURADO MAS ESTRICTO **\n" )
             jurado = definir_jurado_mas_estricto(votos_jurados)
             mostrar_jurado(votos_jurados, jurado)

           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()

        case "8":
           if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL BUSCAR PARTICIPANTE **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
           else:
             nombre_buscado = input("Ingrese el nombre que desea buscar: ")
             existe = buscar_por_nombre(participantes, votos_jurados, nombre_buscado)
             if existe == False:
               print("\n** ERROR AL BUSCAR PARTICIPANTE **\n" \
              "El participante que busca no se encuentra registrado en la competencia.")
               
           input("\nPresiona Enter para continuar...")
           limpiar_pantalla()

        case "9":
          if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL MOSTRAR EL TOP 3. **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
          else:
              ordenar_participantes_por_promedio(participantes,votos_jurados)
              mostrar_matriz_top_3(votos_jurados,participantes)
          input("\nPresiona Enter para continuar...")
          limpiar_pantalla()
         
        case "10":
          if participantes_cargados == False or puntajes_cargados == False:
              print("\n** ERROR AL ORDENAR PARTICIPANTES. **\n" \
              "Recuerde ingresar los participantes y sus respectivos puntajes.")
          else:
              ordenar_participantes_alfabeticamente(participantes,votos_jurados)
              mostrar_todos_los_participantes(participantes,votos_jurados)

          input("\nPresiona Enter para continuar...")
          limpiar_pantalla()
          
        case "11": 
            print("Saliendo...")
         

        case _:
         print("Eleccion Invalida...")
         input("\nPresiona Enter para continuar...")
         limpiar_pantalla()



menu()