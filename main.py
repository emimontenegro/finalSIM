import tkinter as tk
from tkinter import messagebox, ttk, font
import random
import math


def validar_numeros_coma(event):
    char = event.char
    if not (char.isdigit() or char == '.' or char == '\b'):
        return 'break'


def validar_numeros_entero(event):
    char = event.char
    if not (char.isdigit() or char == '\b'):
        return 'break'


def inicializar_pantalla():
    ventana = tk.Tk()
    ventana.geometry("520x535")
    ventana.title("TP Final - Simulación - Montenegro Emilia")
    ventana.resizable(False, False)

    variabley = 5
    variablex = 375
    incremento = 30

    etiqueta1 = tk.Label(ventana, text="Ingrese la cantidad de tiempo a simular (X)(horas): ")
    etiqueta1.place(x=5, y=5)
    text_box_tiempo = tk.Entry(ventana)
    text_box_tiempo.insert(0, "1000")
    text_box_tiempo.config(bg="lightyellow")
    text_box_tiempo.place(x=variablex, y=5)
    text_box_tiempo.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta2 = tk.Label(ventana, text="Ingrese la cantidad de iteraciones a mostrar (i): ")
    etiqueta2.place(x=5, y=variabley)
    text_box_iteraciones_mostrar = tk.Entry(ventana)
    text_box_iteraciones_mostrar.config(bg="lightyellow")
    text_box_iteraciones_mostrar.place(x=variablex, y=variabley)
    text_box_iteraciones_mostrar.bind('<Key>', validar_numeros_entero)

    variabley += incremento

    etiqueta3 = tk.Label(ventana, text="Ingrese el tiempo de iteración a partir del cual mostrar (j): ")
    etiqueta3.place(x=5, y=variabley)
    text_box_tiempo_apartir = tk.Entry(ventana)
    text_box_tiempo_apartir.config(bg="lightyellow")
    text_box_tiempo_apartir.place(x=variablex, y=variabley)
    text_box_tiempo_apartir.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta4 = tk.Label(ventana, text="Ingrese la media de llegada de autos (minutos): ")
    etiqueta4.place(x=5, y=variabley)
    text_box_llegada_autos_media = tk.Entry(ventana)
    text_box_llegada_autos_media.insert(0, "13")
    text_box_llegada_autos_media.config(bg="lavender")
    text_box_llegada_autos_media.place(x=variablex, y=variabley)
    text_box_llegada_autos_media.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta5 = tk.Label(ventana, text="Ingrese la desviación estándar de llegada de autos (minutos): ")
    etiqueta5.place(x=5, y=variabley)
    text_box_llegada_autos_desviacion = tk.Entry(ventana)
    text_box_llegada_autos_desviacion.insert(0, "1")
    text_box_llegada_autos_desviacion.config(bg="lavender")
    text_box_llegada_autos_desviacion.place(x=variablex, y=variabley)
    text_box_llegada_autos_desviacion.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta6 = tk.Label(ventana, text="Ingrese la probabilidad de que el auto sea PEQUEÑO: ")
    etiqueta6.place(x=5, y=variabley)
    text_box_prob_auto_pequeno = tk.Entry(ventana)
    text_box_prob_auto_pequeno.config(bg="lightblue")
    text_box_prob_auto_pequeno.insert(0, "0.60")
    text_box_prob_auto_pequeno.place(x=variablex, y=variabley)
    text_box_prob_auto_pequeno.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta7 = tk.Label(ventana, text="Ingrese la probabilidad de que el auto sea GRANDE: ")
    etiqueta7.place(x=5, y=variabley)
    text_box_prob_auto_grande = tk.Entry(ventana)
    text_box_prob_auto_grande.config(bg="lightblue")
    text_box_prob_auto_grande.insert(0, "0.25")
    text_box_prob_auto_grande.place(x=variablex, y=variabley)
    text_box_prob_auto_grande.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta8 = tk.Label(ventana, text="Ingrese la probabilidad de que el auto sea UTILITARIO: ")
    etiqueta8.place(x=5, y=variabley)
    text_box_prob_auto_utilitario = tk.Entry(ventana)
    text_box_prob_auto_utilitario.config(bg="lightblue")
    text_box_prob_auto_utilitario.insert(0, "0.15")
    text_box_prob_auto_utilitario.place(x=variablex, y=variabley)
    text_box_prob_auto_utilitario.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta9 = tk.Label(ventana, text="Ingrese la probabilidad de que un auto estacione durante 1 HORA: ")
    etiqueta9.place(x=5, y=variabley)
    text_box_prob_1hora = tk.Entry(ventana)
    text_box_prob_1hora.config(bg="lightgreen")
    text_box_prob_1hora.insert(0, "0.50")
    text_box_prob_1hora.place(x=variablex, y=variabley)
    text_box_prob_1hora.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta10 = tk.Label(ventana, text="Ingrese la probabilidad de que un auto estacione durante 2 HORAS: ")
    etiqueta10.place(x=5, y=variabley)
    text_box_prob_2horas = tk.Entry(ventana)
    text_box_prob_2horas.config(bg="lightgreen")
    text_box_prob_2horas.insert(0, "0.30")
    text_box_prob_2horas.place(x=variablex, y=variabley)
    text_box_prob_2horas.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta11 = tk.Label(ventana, text="Ingrese la probabilidad de que un auto estacione durante 3 HORAS: ")
    etiqueta11.place(x=5, y=variabley)
    text_box_prob_3horas = tk.Entry(ventana)
    text_box_prob_3horas.config(bg="lightgreen")
    text_box_prob_3horas.insert(0, "0.15")
    text_box_prob_3horas.place(x=variablex, y=variabley)
    text_box_prob_3horas.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta12 = tk.Label(ventana, text="Ingrese la probabilidad de que un auto estacione durante 4 HORAS: ")
    etiqueta12.place(x=5, y=variabley)
    text_box_prob_4horas = tk.Entry(ventana)
    text_box_prob_4horas.config(bg="lightgreen")
    text_box_prob_4horas.insert(0, "0.05")
    text_box_prob_4horas.place(x=variablex, y=variabley)
    text_box_prob_4horas.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    etiqueta13 = tk.Label(ventana, text="Ingrese el tiempo de cobro (minutos): ")
    etiqueta13.place(x=5, y=variabley)
    text_box_tiempo_cobro = tk.Entry(ventana)
    text_box_tiempo_cobro.insert(0, "2")
    text_box_tiempo_cobro.config(bg="lightsalmon")
    text_box_tiempo_cobro.place(x=variablex, y=variabley)
    text_box_tiempo_cobro.bind('<Key>', validar_numeros_coma)

    variabley += incremento

    boton_generar = tk.Button(ventana,
                              text="Simular",
                              command=lambda: simular(text_box_tiempo, text_box_iteraciones_mostrar,
                                                      text_box_tiempo_apartir, text_box_llegada_autos_media, text_box_llegada_autos_desviacion,
                                                      text_box_prob_auto_pequeno, text_box_prob_auto_grande,
                                                      text_box_prob_auto_utilitario, text_box_prob_1hora,
                                                      text_box_prob_2horas, text_box_prob_3horas, text_box_prob_4horas,
                                                      text_box_tiempo_cobro),
                              width=10, height=2)
    boton_generar.place(x=200, y=variabley)

    ventana.mainloop()


def tabla_tiempo_estacionamiento(rnd, probabilidades):
    if rnd < probabilidades[0]:
        return 60

    elif rnd < probabilidades[0] + probabilidades[1]:
        return 120

    elif rnd < probabilidades[0] + probabilidades[1] + probabilidades[2]:
        return 180

    else:
        return 240


def tabla_tipo_auto(rnd, probabilidades):
    if rnd < probabilidades[0]:
        return "Pequeño"

    elif rnd < probabilidades[0] + probabilidades[1]:
        return "Grande"

    else:
        return "Utilitario"


def simular(text_box_tiempo, text_box_iteraciones_mostrar, text_box_tiempo_apartir, text_box_llegada_autos_media, text_box_llegada_autos_desviacion,
            text_box_prob_auto_pequeno, text_box_prob_auto_grande, text_box_prob_auto_utilitario, text_box_prob_1hora,
            text_box_prob_2horas, text_box_prob_3horas, text_box_prob_4horas, text_box_tiempo_cobro):
    if not validar_entradas(text_box_tiempo, text_box_iteraciones_mostrar, text_box_tiempo_apartir,
                            text_box_llegada_autos_media, text_box_llegada_autos_desviacion, text_box_prob_auto_pequeno, text_box_prob_auto_grande,
                            text_box_prob_auto_utilitario, text_box_prob_1hora, text_box_prob_2horas,
                            text_box_prob_3horas, text_box_prob_4horas, text_box_tiempo_cobro):
        return

    tiempo_a_simular = float(text_box_tiempo.get())
    apartir_de_fila_j = int(text_box_tiempo_apartir.get())
    cantidad_filas_mostrar_i = int(text_box_iteraciones_mostrar.get())

    tiempo_entre_llegadas_autos_media = float(text_box_llegada_autos_media.get())
    tiempo_entre_llegadas_autos_desviacion = float(text_box_llegada_autos_desviacion.get())

    probabilidades_tiempo_estacionamiento = [float(text_box_prob_1hora.get()), float(text_box_prob_2horas.get()),
                                             float(text_box_prob_3horas.get()), float(text_box_prob_4horas.get())]

    probabilidades_tipos_autos = [float(text_box_prob_auto_pequeno.get()), float(text_box_prob_auto_grande.get()),
                                  float(text_box_prob_auto_utilitario.get())]

    tiempo_cobro = float(text_box_tiempo_cobro.get())

    generador = random.Random()

    filas = [["",  # Evento (0)
              0,  # Reloj (1)
              0,  # llegada_auto (2)
              0, "",  # RND y Tipo de auto (3, 4)
              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, # RND, Tiempo de estacionamiento y 28 eventos fin_estacionamiento (5, 34) 
              0,  # fin_cobro (35)
              0,  # fin_simulacion (36)
              "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", # 28 Estados para los 28 sectores de estacionamiento (37, 64)
              "", 0,  # Estado y cola de la zona de cobro (65, 66)
              0,  # Acumulador recaudación (67)
              ],
             ["", 0, 0, 0, "", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
             "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 0, 0]]

    objetos_autos = []

    no_se_paso_de_x = True
    iteraciones = 0
    j = 0
    cantidad_ocupados = 0
    eventos_proximos = []
    contador_filas_agregadas = 0
    ultimo_indice_simulacion = 0
    tiempo_entre_llegadas_autos = []

    root = tk.Tk()
    root.geometry("520x450")
    root.title("Tabla simulación estacionamiento")
    table = ttk.Treeview(root)
    headers = ["Evento", "Reloj(mins)", "Llegada_auto", "RND tipo auto", "Tipo auto", "RND tiempo est.", "Tiempo est.",
               "P.Fin_est1", "P.Fin_est2", "P.Fin_est3", "P.Fin_est4", "P.Fin_est5", "P.Fin_est6", "P.Fin_est7", "P.Fin_est8",
               "P.Fin_est9", "P.Fin_est10", "G.Fin_est11", "G.Fin_est12", "G.Fin_est13", "G.Fin_est14", "G.Fin_est15", "G.Fin_est16",
               "U.Fin_est17", "U.Fin_est18", "U.Fin_est19", "U.Fin_est20", "P.Fin_est21", "P.Fin_est22", "P.Fin_est23", "P.Fin_est24",
               "P.Fin_est25", "P.Fin_est26", "P.Fin_est27", "P.Fin_est28", "Fin_cobro", "Fin_simul.", 
               "P.EstadoS1", "P.EstadoS2", "P.EstadoS3", "P.EstadoS4", "P.EstadoS5", "P.EstadoS6", "P.EstadoS7", "P.EstadoS8",
               "P.EstadoS9", "P.EstadoS10", "G.EstadoS11", "G.EstadoS12", "G.EstadoS13", "G.EstadoS14", "G.EstadoS15", "G.EstadoS16",
                "U.EstadoS17", "U.EstadoS18", "U.EstadoS19", "U.EstadoS20", "P.EstadoS21", "P.EstadoS22", "P.EstadoS23", "P.EstadoS24",
                "P.EstadoS25", "P.EstadoS26", "P.EstadoS27", "P.EstadoS28","Estado ZC", "Cola ZC", "Acum. recau.",
                "EstadoA1", "TipoA1", "Fin_estA1", "Tiempo estA1", "EstadoA2", "TipoA2", "Fin_estA2", "Tiempo estA2", 
                "EstadoA3", "TipoA3", "Fin_estA3", "Tiempo estA3", "EstadoA4", "TipoA4", "Fin_estA4", "Tiempo estA4", 
                "EstadoA5", "TipoA5", "Fin_estA5", "Tiempo estA5", "EstadoA6", "TipoA6", "Fin_estA6", "Tiempo estA6", 
                "EstadoA7", "TipoA7", "Fin_estA7", "Tiempo estA7", "EstadoA8", "TipoA8", "Fin_estA8", "Tiempo estA8",
               "EstadoA9", "TipoA9", "Fin_estA9", "Tiempo estA9", "EstadoA10", "TipoA10", "Fin_estA10", "Tiempo estA10",
               "EstadoA11", "TipoA11", "Fin_estA11", "Tiempo estA11", "EstadoA12", "TipoA12", "Fin_estA12", "Tiempo estA12",
               "EstadoA13", "TipoA13", "Fin_estA13", "Tiempo estA13", "EstadoA14", "TipoA14", "Fin_estA14", "Tiempo estA14",
               "EstadoA15", "TipoA15", "Fin_estA15", "Tiempo estA15", "EstadoA16", "TipoA16", "Fin_estA16", "Tiempo estA16",
               "EstadoA17", "TipoA17", "Fin_estA17", "Tiempo estA17", "EstadoA18", "TipoA18", "Fin_estA18", "Tiempo estA18",
               "EstadoA19", "TipoA19", "Fin_estA19", "Tiempo estA19", "EstadoA20", "TipoA20", "Fin_estA20", "Tiempo estA20",
               "EstadoA21", "TipoA21", "Fin_estA21", "Tiempo estA21", "EstadoA22", "TipoA22", "Fin_estA22", "Tiempo estA22",
               "EstadoA23", "TipoA23", "Fin_estA23", "Tiempo estA23", "EstadoA24", "TipoA24", "Fin_estA24", "Tiempo estA24",
               "EstadoA25", "TipoA25", "Fin_estA25", "Tiempo estA25", "EstadoA26", "TipoA26", "Fin_estA26", "Tiempo estA26",
               "EstadoA27", "TipoA27", "Fin_estA27", "Tiempo estA27", "EstadoA28", "TipoA28", "Fin_estA28", "Tiempo estA28",
               "EstadoA29", "TipoA29", "Fin_estA29", "Tiempo estA29", "EstadoA30", "TipoA30", "Fin_estA30", "Tiempo estA30",]
    table["columns"] = headers
    table["show"] = "headings"
    for header in headers:
        table.heading(header, text=header)

    while no_se_paso_de_x and iteraciones <= 100000:  # Para recorrer cada iteración
        if j % 2 == 0:
            indice = 0
        else:
            indice = 1

        for m in range(len(filas[indice])):
            if m != len(filas[indice]) - 1:
                filas[indice][m] = "-"

        if iteraciones == 0:
            filas[indice][0] = "Inicialización"
            filas[indice][1] = 0
            tiempo_entre_llegadas_autos = calcular_tiempo_entre_llegadas_autos(tiempo_entre_llegadas_autos_media, tiempo_entre_llegadas_autos_desviacion)
            filas[indice][2] = round(tiempo_entre_llegadas_autos[0], 2)
            eventos_proximos.append((round(tiempo_entre_llegadas_autos[0], 2), "llegada_auto"))
            tiempo_entre_llegadas_autos.remove(tiempo_entre_llegadas_autos[0])
            filas[indice][36] = tiempo_a_simular * 60
            eventos_proximos.append((round(tiempo_a_simular * 60, 2), "fin_simulacion"))
            for i in range(37, 65):
                filas[indice][i] = "Libre"
            filas[indice][65] = "Libre"
            filas[indice][66] = 0
            filas[indice][67] = 0
        else:
            cantidad_ocupados = 0
            proximo_evento = seleccionar_proximo_evento(eventos_proximos)
            eventos_proximos.remove(proximo_evento)
            filas[indice][0] = proximo_evento[1]
            filas[indice][1] = proximo_evento[0]

            if proximo_evento[1] == "llegada_auto":
                for i in range(37, 65):
                    if filas[indice-1][i] == "Ocupado":
                        cantidad_ocupados += 1

                if len(tiempo_entre_llegadas_autos) == 1:
                    eventos_proximos.append((round(filas[indice][1] + tiempo_entre_llegadas_autos[0], 2), "llegada_auto"))  # Próx lleg
                    filas[indice][2] = round(filas[indice][1] + tiempo_entre_llegadas_autos[0], 2)  # Próx llegada
                    tiempo_entre_llegadas_autos.remove(tiempo_entre_llegadas_autos[0])
                    tiempo_entre_llegadas_autos = calcular_tiempo_entre_llegadas_autos(tiempo_entre_llegadas_autos_media, tiempo_entre_llegadas_autos_desviacion)
                elif len(tiempo_entre_llegadas_autos) == 2:
                    eventos_proximos.append((round(filas[indice][1] + tiempo_entre_llegadas_autos[0], 2), "llegada_auto"))  # Próx lleg
                    filas[indice][2] = round(filas[indice][1] + tiempo_entre_llegadas_autos[0], 2)  # Próx llegada
                    tiempo_entre_llegadas_autos.remove(tiempo_entre_llegadas_autos[0])

                if cantidad_ocupados < 24:
                    filas[indice][3] = round(generador.random(), 2)  # RND de tipo de auto
                    tipo_auto = tabla_tipo_auto(filas[indice][3], probabilidades_tipos_autos)  # Tipo de auto
                    filas[indice][4] = tipo_auto

                    if tipo_auto == "Pequeño":
                        se_ocupo = False
                        for i in range(7, 35):
                            filas[indice][i] = filas[indice - 1][i]

                        for i in range(7, 17):
                            filas[indice][i] = filas[indice - 1][i]
                            if filas[indice][i] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                    probabilidades_tiempo_estacionamiento)
                                filas[indice][i] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True

                                for i in range(17, 35):
                                    filas[indice][i] = filas[indice - 1][i]
                            
                        if filas[indice][23] == "-" and not se_ocupo:
                            if filas[indice][27] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][27] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True
                            if filas[indice][28] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][28] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True
                        
                        if filas[indice][24] == "-" and not se_ocupo:
                            if filas[indice][29] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][29] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True
                            if filas[indice][30] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][30] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True

                        if filas[indice][25] == "-" and not se_ocupo:
                            if filas[indice][31] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][31] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True
                            if filas[indice][32] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][32] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True

                        if filas[indice][26] == "-" and not se_ocupo:
                            if filas[indice][33] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][33] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True
                            if filas[indice][34] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                            probabilidades_tiempo_estacionamiento)
                                filas[indice][34] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True

                    if tipo_auto == "Grande":
                        se_ocupo = False
                        for i in range(17, 23):
                            filas[indice][i] = filas[indice - 1][i]
                            if filas[indice][i] == "-" and not se_ocupo:
                                filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                                filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                    probabilidades_tiempo_estacionamiento)
                                filas[indice][i] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                                eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                                se_ocupo = True

                        for i in range(7, 17):
                            filas[indice][i] = filas[indice - 1][i]

                        for i in range(23, 35):
                            filas[indice][i] = filas[indice - 1][i]
                    
                    if tipo_auto == "Utilitario":
                        se_ocupo = False

                        for i in range(7, 35):
                            filas[indice][i] = filas[indice - 1][i]

                        if filas[indice][23] == "-" and not se_ocupo and filas[indice][27] == "-" and filas[indice][28] == "-":
                            filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                            filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                    probabilidades_tiempo_estacionamiento)
                            filas[indice][23] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                            eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                            se_ocupo = True

                        if filas[indice][24] == "-" and not se_ocupo and filas[indice][29] == "-" and filas[indice][30] == "-":
                            filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                            filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                    probabilidades_tiempo_estacionamiento)
                            filas[indice][24] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                            eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                            se_ocupo = True

                        if filas[indice][25] == "-" and not se_ocupo and filas[indice][31] == "-" and filas[indice][32] == "-":
                            filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                            filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                    probabilidades_tiempo_estacionamiento)
                            filas[indice][25] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                            eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                            se_ocupo = True

                        if filas[indice][26] == "-" and not se_ocupo and filas[indice][33] == "-" and filas[indice][34] == "-":
                            filas[indice][5] = round(generador.random(), 2)  # RND Tiempo estacionamiento
                            filas[indice][6] = tabla_tiempo_estacionamiento(filas[indice][5],  # Tiempo estacionamiento
                                                                    probabilidades_tiempo_estacionamiento)
                            filas[indice][26] = round(filas[indice][1] + filas[indice][6], 2)  # Prox fin_estacionamiento
                            eventos_proximos.append((round(filas[indice][1] + filas[indice][6], 2), "fin_estacionamiento"))
                            se_ocupo = True

                filas[indice][35] = filas[indice - 1][35]  # Bajar fin_cobro anterior
                filas[indice][36] = tiempo_a_simular * 60 # Bajar fin_simulación

                for i in range(37, 65):
                    filas[indice][i] = filas[indice - 1][i]

                if cantidad_ocupados < 24 and filas[indice][6] != "-":

                    if tipo_auto == "Pequeño":
                        se_ocupo = False
                        for i in range(37, 65):
                            filas[indice][i] = filas[indice - 1][i]

                        for i in range(37, 47):
                            filas[indice][i] = filas[indice - 1][i]
                            if filas[indice][i] == "Libre" and not se_ocupo:
                                filas[indice][i] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                    filas[indice][6]])  # Agregar auto
                                for i in range(47, 65):
                                    filas[indice][i] = filas[indice - 1][i]

                        if filas[indice][53] == "Libre" and not se_ocupo:
                            if filas[indice][57] == "Libre" and not se_ocupo:
                                filas[indice][57] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto
                            if filas[indice][58] == "Libre" and not se_ocupo:
                                filas[indice][58] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto
                        
                        if filas[indice][54] == "Libre" and not se_ocupo:
                            if filas[indice][59] == "Libre" and not se_ocupo:
                                filas[indice][59] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto
                            if filas[indice][60] == "Libre" and not se_ocupo:
                                filas[indice][60] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto

                        if filas[indice][55] == "Libre" and not se_ocupo:
                            if filas[indice][61] == "Libre" and not se_ocupo:
                                filas[indice][61] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto
                            if filas[indice][62] == "Libre" and not se_ocupo:
                                filas[indice][62] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto

                        if filas[indice][56] == "Libre" and not se_ocupo:
                            if filas[indice][63] == "Libre" and not se_ocupo:
                                filas[indice][63] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto
                            if filas[indice][64] == "Libre" and not se_ocupo:
                                filas[indice][64] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                        filas[indice][6]])  # Agregar auto

                    if tipo_auto == "Grande":
                        se_ocupo = False
                        for i in range(47, 53):
                            filas[indice][i] = filas[indice - 1][i]
                            if filas[indice][i] == "Libre" and not se_ocupo:
                                filas[indice][i] = "Ocupado"
                                se_ocupo = True
                                objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                  filas[indice][6]])  # Agregar auto

                        for i in range(37, 47):
                            filas[indice][i] = filas[indice - 1][i]

                        for i in range(53, 65):
                            filas[indice][i] = filas[indice - 1][i]

                    if tipo_auto == "Utilitario":
                        se_ocupo = False

                        for i in range(37, 65):
                            filas[indice][i] = filas[indice - 1][i]

                        if filas[indice][53] == "Libre" and not se_ocupo and filas[indice][57] == "Libre" and filas[indice][58] == "Libre":
                            filas[indice][53] = "Ocupado"
                            se_ocupo = True
                            objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                filas[indice][6]])  # Agregar auto

                        if filas[indice][54] == "Libre" and not se_ocupo and filas[indice][59] == "Libre" and filas[indice][60] == "Libre":
                            filas[indice][54] = "Ocupado"
                            se_ocupo = True
                            objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                filas[indice][6]])  # Agregar auto

                        if filas[indice][55] == "Libre" and not se_ocupo and filas[indice][61] == "Libre" and filas[indice][62] == "Libre":
                            filas[indice][55] = "Ocupado"
                            se_ocupo = True
                            objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                filas[indice][6]])  # Agregar auto

                        if filas[indice][56] == "Libre" and not se_ocupo and filas[indice][63] == "Libre" and filas[indice][64] == "Libre":
                            filas[indice][56] = "Ocupado"
                            se_ocupo = True
                            objetos_autos.append(["Estacionado", filas[indice][4], round(filas[indice][1] + filas[indice][6], 2),
                                                filas[indice][6]])  # Agregar auto
                
                filas[indice][65] = filas[indice - 1][65]  # Bajar estado zona cobro
                filas[indice][66] = filas[indice - 1][66]  # Bajar cola zona cobro
                filas[indice][67] = filas[indice - 1][67]  # Bajar acumulador recaudación

            elif proximo_evento[1] == "fin_simulacion":
                ultimo_indice_simulacion = indice
                no_se_paso_de_x = False
                filas[indice][2] = filas[indice - 1][2]  # Bajar próxima llegada
                for i in range(7, 35):  # Bajar próximos fin_estacionamiento
                    filas[indice][i] = filas[indice - 1][i]
                filas[indice][35] = filas[indice - 1][35]  # Bajar próximo fin_cobro
                for i in range(37, 65):  # Bajar estados anteriores sectores
                    filas[indice][i] = filas[indice - 1][i]
                filas[indice][65] = filas[indice - 1][65]  # Bajar estado zona cobro
                filas[indice][66] = filas[indice - 1][66]  # Bajar cola zona cobro
                filas[indice][67] = filas[indice - 1][67]  # Bajar acumulador recaudación

            elif proximo_evento[1] == "fin_cobro":
                filas[indice][2] = filas[indice - 1][2]  # Bajar próxima llegada

                for i in range(7, 35):  # Bajar próximos fin_estacionamiento
                    filas[indice][i] = filas[indice - 1][i]

                filas[indice][36] = tiempo_a_simular * 60

                for i in range(37, 65):  # Bajar estados anteriores sectores
                    filas[indice][i] = filas[indice - 1][i]

                if filas[indice - 1][66] > 0:  # Hay cola?
                    eventos_proximos.append((round(filas[indice][1] + tiempo_cobro, 2), "fin_cobro"))
                    filas[indice][35] = round(filas[indice][1] + tiempo_cobro, 2)  # Generar próximo fin_cobro
                    filas[indice][66] = filas[indice - 1][66] - 1  # Restar 1 a la cola
                    filas[indice][65] = "Ocupado"  # Poner la zona de cobro en Ocupado
                    que_paso = "hay_cola"
                else:
                    filas[indice][65] = "Libre"  # Poner la zona de cobro en Libre
                    filas[indice][66] = 0
                    que_paso = "no_hay_cola"

                auto_a_cobrar = determinar_proximo_auto_cobrar(objetos_autos)
                if objetos_autos[auto_a_cobrar][0] == "Pagando":
                    filas[indice][67] = round(filas[indice - 1][67] + calcular_recaudacion(objetos_autos[auto_a_cobrar]), 2)  # Actualizar rec.
                    objetos_autos[auto_a_cobrar] = ("-", "-", "-", "-")

                if que_paso == "hay_cola":
                    auto = determinar_proximo_auto_cobrar(objetos_autos)
                    cambiar_estado_automovil(objetos_autos, filas[indice][1], que_paso, "fin_cobro", auto)


            elif proximo_evento[1] == "fin_estacionamiento":
                filas[indice][2] = filas[indice - 1][2]  # Bajar próxima llegada

                for i in range(7, 35):
                    if filas[indice-1][i] == filas[indice][1]:  # Eliminar el que acaba de ocurrir
                        filas[indice][i] = "-"
                        filas[indice][i+30] = "Libre"  # Poner libre el sector correspondiente
                    else:
                        filas[indice][i] = filas[indice-1][i]  # Bajar otros fin_estacionamiento
                        filas[indice][i+30] = filas[indice-1][i+30]  # Bajar el resto de estados de sectores

                filas[indice][36] = tiempo_a_simular * 60 # Bajar fin_simulación

                if filas[indice-1][65] == "Libre":  # Verificar si zona de cobro está libre
                    eventos_proximos.append((round(filas[indice][1] + tiempo_cobro, 2), "fin_cobro"))
                    filas[indice][35] = round(filas[indice][1] + tiempo_cobro,2)  # Generar próximo fin_cobro
                    filas[indice][65] = "Ocupado"  # Cambiar la zona de cobro a ocupado
                    filas[indice][66] = filas[indice - 1][66]  # Bajar cola zona cobro (podría poner cero tmb)
                    que_paso = "no_hay_cola"
                else:
                    filas[indice][35] = filas[indice - 1][35]  # Bajar próximo fin_cobro
                    filas[indice][65] = filas[indice - 1][65]  # Bajar estado zona cobro
                    filas[indice][66] = filas[indice - 1][66] + 1 # Actualizar cola zona cobro
                    que_paso = "hay_cola"

                filas[indice][67] = filas[indice - 1][67]  # Bajar el acum. de recaudación

                cambiar_estado_automovil(objetos_autos, filas[indice][1], que_paso, "fin_estacionamiento", 0)

        j += 1
        iteraciones += 1
        if iteraciones >= apartir_de_fila_j:
            if cantidad_filas_mostrar_i > contador_filas_agregadas:
                contador_filas_agregadas += 1
                autos_tabla = [item for sublist in objetos_autos for item in sublist]
                table.insert("", "end", values=filas[indice] + autos_tabla)

    table.insert("", "end", values=filas[ultimo_indice_simulacion])

    for header in headers:
        table.column(header, anchor="center", width=75)
    scrollbar1 = ttk.Scrollbar(table, orient="horizontal", command=table.xview)
    scrollbar2 = ttk.Scrollbar(table, orient="vertical", command=table.yview)
    table.configure(xscrollcommand=scrollbar1.set)
    table.configure(yscrollcommand=scrollbar2.set)
    table.pack(side="top", fill="both", expand=True)
    scrollbar1.pack(side="bottom", fill="x")
    scrollbar2.pack(side="right", fill="y")
    etiqueta_resultado = tk.Label(root, text="La recaudación final en la simulación fue: $" +
                                             str(filas[ultimo_indice_simulacion][67]), 
                                  font=font.Font(weight="bold", size=20))
    etiqueta_resultado.pack(side="bottom")

def validar_entradas(text_box_tiempo, text_box_iteraciones_mostrar, text_box_tiempo_apartir, text_box_llegada_autos_media, 
                     text_box_llegada_autos_desviacion, text_box_prob_auto_pequeno, text_box_prob_auto_grande, text_box_prob_auto_utilitario,
                     text_box_prob_1hora, text_box_prob_2horas, text_box_prob_3horas, text_box_prob_4horas, text_box_tiempo_cobro):
    mensaje_error = "Por favor, ingrese números válidos en los campos."
    res = True

    try:
        tiempo_simular = int(text_box_tiempo.get())
        param_i = int(text_box_iteraciones_mostrar.get())
        param_j = int(text_box_tiempo_apartir.get())

        tiempo_llegada_autos_media = float(text_box_llegada_autos_media.get())
        tiempo_llegada_autos_desviacion = float(text_box_llegada_autos_desviacion.get())

        prob_auto_pequeno = float(text_box_prob_auto_pequeno.get())
        prob_auto_grande = float(text_box_prob_auto_grande.get())
        prob_auto_utilitario = float(text_box_prob_auto_utilitario.get())

        prob_1hora = float(text_box_prob_1hora.get())
        prob_2horas = float(text_box_prob_2horas.get())
        prob_3horas = float(text_box_prob_3horas.get())
        prob_4horas = float(text_box_prob_4horas.get())

        tiempo_cobro = float(text_box_tiempo_cobro.get())

        if param_j < 0 or param_j > 100000:
            mensaje_error = "Se puede mostrar a partir de la iteración 0, hasta la iteración 100000."
            raise ValueError()

        if param_i <= 0:
            mensaje_error = "i debe ser mayor o igual a 1."
            raise ValueError()

        if prob_auto_pequeno + prob_auto_grande + prob_auto_utilitario != 1:
            mensaje_error = "Error con probabilidades de tipo de auto."
            raise ValueError()

        if prob_1hora + prob_2horas + prob_3horas + prob_4horas != 1:
            mensaje_error = "Error con probabilidades de tiempo de estacionamiento."
            raise ValueError()

        if tiempo_simular <= 0 or tiempo_llegada_autos_media <= 0 or tiempo_llegada_autos_desviacion <= 0:
            mensaje_error = "No pueden ser negativos o 0 tiempo a simular y tiempos de llegada."
            raise ValueError()

        if tiempo_cobro < 0:
            mensaje_error = "No puede ser negativo el tiempo de cobro"

        return res

    except ValueError:
        messagebox.showerror("Error", mensaje_error)
        res = False
        return res

def calcular_tiempo_entre_llegadas_autos(tiempo_entre_llegadas_autos_media, tiempo_entre_llegadas_autos_desviacion):
    numeros = []
    aleatorio1 = random.random()
    aleatorio2 = random.random()
    
    n1 = (math.sqrt(-2 * math.log(aleatorio1)) * math.cos(2 * math.pi * aleatorio2)) * tiempo_entre_llegadas_autos_desviacion + tiempo_entre_llegadas_autos_media
    n2 = (math.sqrt(-2 * math.log(aleatorio1)) * math.sin(2 * math.pi * aleatorio2)) * tiempo_entre_llegadas_autos_desviacion + tiempo_entre_llegadas_autos_media
    
    numeros.append(n1)
    numeros.append(n2)
    
    return numeros
    

def seleccionar_proximo_evento(proximos_eventos):
    j = 0
    prox = ()
    for i in proximos_eventos:
        if j == 0:
            prox = i
        else:
            if prox[0] >= i[0]:
                prox = i
        j += 1
    return prox


def determinar_proximo_auto_cobrar(automoviles):
    indice = 0
    indiceb = 0
    prox = ("", "", 10000000, 0)
    for i in automoviles:  # Busca el auto con menor fin_estacionamiento para cobrarle
        if i[2] != "-":
            if float(prox[2]) >= float(i[2]):
                prox = i
                indiceb = indice
        indice += 1
    return indiceb

def calcular_recaudacion(auto_a_cobrar):
    if auto_a_cobrar[1] == "Pequeño":
        return round((auto_a_cobrar[3] / 60) * 1, 2)
    elif auto_a_cobrar[1] == "Grande":
        return round((auto_a_cobrar[3] / 60) * 1.2, 2)
    else:
        return round((auto_a_cobrar[3] / 60) * 1.5, 2)


def cambiar_estado_automovil(automoviles, reloj_actual, que_paso, evento, auto):
    if evento == "fin_estacionamiento":
        for i in automoviles:  # Busca el auto con menor fin_estacionamiento para cobrarle
            if i[2] == reloj_actual:
                if que_paso == "hay_cola":
                    i[0] = "EC"
                elif que_paso == "no_hay_cola":
                    i[0] = "Pagando"

    elif evento == "fin_cobro":
        indice = determinar_proximo_auto_cobrar(automoviles)
        prox = automoviles[indice]

        if prox[2] != "-":
            if reloj_actual > prox[2]:
                    prox[0] = "Pagando"

if __name__ == '__main__':
    inicializar_pantalla()