import os      # Nos ayuda a listar los archivos de la carpeta y limpiar pantalla
import time    # Nos ayuda con la pantalla de carga y para medir el tiempo de inactividad


# CONFIGURACIÓN GENERAL (variables usadas en todo el programa)
ARCHIVO_REGISTROS = "registros_academia.txt"   # Archivo donde se guardan los registros del día
LIMITE_INACTIVIDAD = 600                       # 10 minutos en segundos para la inactividad (10 * 60 = 600)
SEPARADOR_REGISTRO = "-" * 42                  # Línea para separar un registro de otro en el archivo
ANCHO_ENCABEZADO = 42                          # Ancho de los encabezados con asteriscos


# LIMPIAR PANTALLA (Borra todo lo escrito anteriormente)
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


# ENCABEZADO (Muestra el titulo de cada funcion formateado)
def encabezado(texto):
    print("*" * ANCHO_ENCABEZADO)
    print(texto.center(ANCHO_ENCABEZADO))
    print("*" * ANCHO_ENCABEZADO)


# PAUSAR (Detiene el programa para que se alcance a leer antes de continuar )
def pausar():
    input("\nPresiona ENTER para volver al menú principal...")


# PANTALLA CARGA (Muestra mensaje de "cargando" antes de iniciar el programa)
def pantalla_carga():
    limpiar_pantalla()
    print("Cargando el sistema, por favor espera...")
    for segundo in range(1, 6):            # Ciclo del 1 al 5 -> máximo 5 segundos
        print(f"Cargando{'.' * segundo}")  # Va mostrando ".", "..", "...", etc.
        time.sleep(1)                      # Pausa real de 1 segundo
    print("¡Listo!\n")


# BIENVENIDA (Pide el nombre del usuario y lo registra))
def bienvenida():
    usuario = input("Escribe tu nombre: ")
    mensaje = "Bienvenido(a), " + usuario + " Comencemos con el registro de hoy ."
    print(mensaje)
    return usuario


# PEDIR FECHA (Pide día, mes y año y los guarda en una tupla)
def pedir_fecha():
    print("\nIngresa la fecha de hoy:")
    dia = input("Introduce el día: ")
    mes = input("Introduce el mes: ")
    anio = input("Introduce el año: ")
    Fecha = dia, mes, anio     # Se crea la tupla (dia, mes, anio)
    return Fecha


# MOSTRAR MENÚ (Muestra las opciones del programa como matriz y dirige a la función elegida)
def mostrar_menu():
    limpiar_pantalla()
    opciones = [
        ["1", "Registrar niño nuevo"],
        ["2", "Ver reporte del día"],
        ["3", "Ver estadísticas"],
        ["4", "Ver archivos guardados (.txt)"],
        ["5", "Salir del programa"]
    ]
    encabezado("MENÚ PRINCIPAL")
    for fila in opciones:                       
        # Recorre cada opción de la matriz
        print(fila[0] + ". " + fila[1])
    print("*" * ANCHO_ENCABEZADO)
    seleccion = input("\nElige una opción (1-5): ")
    return seleccion


# CONTROL INACTIVIDAD (Revisa si el usuario estuvo inactivo por 10 minutos o más y pregunta si quiere seguir o se regresa al inicio))
def control_inactividad(tiempo_inicio):
    tiempo_transcurrido = time.time() - tiempo_inicio   
    # los segundos que pasaron

    if tiempo_transcurrido >= LIMITE_INACTIVIDAD:
        minutos_pasados = int(tiempo_transcurrido // 60)
        print(f"\n Llevas {minutos_pasados} minutos sin actividad.")

        # Ciclo que marca cada minuto de inactividad detectado
        for minuto in range(minutos_pasados):
            print(f"  Minuto {minuto + 1} de inactividad registrado...")

        respuesta = input("¿Deseas continuar en el menú? (si/no): ").lower()
        if respuesta == "no":
            return False    # se regresa al inicio
    return True


# ELEGIR CARRETA (Muestra las opciones en manera de matriz y se guarda la elegida)
def elegir_carreta():
    carretas = [
        ["1", "Ardillas"],
        ["2", "Belugas"],
        ["3", "Gacelas"],
        ["4", "Monos"],
        ["5", "Cocos"],
        ["6", "Cobras"],
        ["7", "Águilas"]
    ]
    print("\nCarretas disponibles:")
    for fila in carretas:              # ciclo recorre las 7 filas completas
        print(fila[0] + ". " + fila[1])

    numero = input("Selecciona el número de la carreta: ")
    for fila in carretas:
        if fila[0] == numero:
            return fila[1]
    return "Sin carreta"      # Si el usuario escribe un número que no existe


# PREGUNTAR PAGO CUOTA (Pregunta si el niño pago la cuota, con qué metodo y si se le debe cambio y se registgran los datos)
def preguntar_pago_cuota():
    pago = input("\n¿Pagó las cuotas? (si/no): ").lower()
    metodo = "-"
    cambio = "0"
    if pago == "si":
        metodo = input("  ¿Método de pago? (efectivo/transferencia): ").lower()
        cambio = input("  ¿Se le debe cambio? Escribe el monto (0 si no se le debe): ")
    return pago, metodo, cambio


# PREGUNTAR PAGO COMIDA (preguntar si el niño pago la comida, con qué metodo, si se le debe cambio y se registran los datos)
def preguntar_pago_comida():
    pago = input("\n¿Pagó la comida? (si/no): ").lower()
    metodo = "-"
    monto = "0"
    cambio = "0"
    if pago == "si":
        metodo = input("  ¿Método de pago? (efectivo/transferencia): ").lower()
        monto = input("  ¿Cuánto pagó por la comida? $")
        cambio = input("  ¿Se le debe cambio? Escribe el monto (0 si no se le debe): ")
    return pago, metodo, monto, cambio


# FORMATEAR REGISTRO (Arma el bloque de texto del registro hecho para guardarlo en el archivo)
def formatear_registro(Fecha, nombre, carreta, pago_cuota, metodo_cuota, cambio_cuota,
                        pago_comida, metodo_comida, monto_comida, cambio_comida, comentario):
    texto_cuota = "Sí" if pago_cuota == "si" else "No"
    texto_comida = "Sí" if pago_comida == "si" else "No"

    bloque = (
        f"{SEPARADOR_REGISTRO}\n"
        f"Nombre:      {nombre}\n"
        f"Carreta:     {carreta}\n"
        f"Fecha:       {Fecha[0]}/{Fecha[1]}/{Fecha[2]}\n"
        f"Cuota:       {texto_cuota} ({metodo_cuota}) - Cambio: ${cambio_cuota}\n"
        f"Comida:      {texto_comida} ({metodo_comida}) - Monto: ${monto_comida} - Cambio: ${cambio_comida}\n"
        f"Comentarios: {comentario if comentario else '(sin comentarios)'}\n"
        f"{SEPARADOR_REGISTRO}\n"
    )
    return bloque


# REGISTRAR NIÑO (Junta los datos del niño y los guarda en el archivo de registros que no se elimina))
def registrar_nino(Fecha):
    limpiar_pantalla()
    encabezado("NUEVO REGISTRO")

    nombre = input("\nNombre del niño: ")
    carreta = elegir_carreta()

    pago_cuota, metodo_cuota, cambio_cuota = preguntar_pago_cuota()
    pago_comida, metodo_comida, monto_comida, cambio_comida = preguntar_pago_comida()

    comentario = input("\nComentarios extra (opcional, Enter para dejar vacío): ")

    bloque = formatear_registro(Fecha, nombre, carreta, pago_cuota, metodo_cuota, cambio_cuota,
                                 pago_comida, metodo_comida, monto_comida, cambio_comida, comentario)

    # try-except controla errores al escribir el archivo 
    try:
        with open(ARCHIVO_REGISTROS, "a") as archivo:   # "a" = anexar (para agregar sin borrar)
            archivo.write(bloque)
        print("\n Registro guardado correctamente:\n")
        print(bloque)
    except PermissionError:
        print("\n Error: no se tienen permisos para escribir en el archivo.")
    except Exception as error:
        print(f"\n Ocurrió un error inesperado al guardar: {error}")


# VER REPORTE DEL DIA (Muestra lo registrado en el dia de manera ordenada)
def ver_reporte_dia():
    limpiar_pantalla()
    encabezado("REPORTE DEL DÍA")

    try:
        with open(ARCHIVO_REGISTROS, "r") as archivo:
            lineas = archivo.readlines()     # Regresa una lista con cada línea del archivo
    except FileNotFoundError:
        print("\n Todavía no existe el archivo de registros. Registra al primer niño primero.")
        return

    if not lineas:
        print("\nAún no hay registros el día de hoy.")
        return

    print()
    for linea in lineas:
        print(linea, end="")     


# VER ARCHIVOS DISPONIBLES (muestra los archivos que hay en la carpeta y permite abrirlos)
def ver_archivos_disponibles():
    limpiar_pantalla()
    encabezado("ARCHIVOS GUARDADOS (.TXT)")

    archivos_txt = [f for f in os.listdir(".") if f.endswith(".txt")] # verifica lista de archivos .txt en la carpeta

    if not archivos_txt:
        print("\nNo hay archivos .txt disponibles en esta carpeta.")
        return

    print("\nArchivos disponibles:")
    diccionario_archivos = {}
    for i, nombre_archivo in enumerate(archivos_txt, start=1):
        diccionario_archivos[str(i)] = nombre_archivo
        print(f"{i}. {nombre_archivo}")

    eleccion = input("\nEscribe el número del archivo que quieres abrir: ")

    if eleccion in diccionario_archivos:
        nombre_elegido = diccionario_archivos[eleccion]
        try:
            with open(nombre_elegido, "r") as archivo:
                contenido = archivo.read()          # Enseña todo el contenido del archivo 
                print(f"\n--- Contenido de {nombre_elegido} ---\n")
                print(contenido)
        except FileNotFoundError:
            print(" Error: el archivo no fue encontrado.")
        except PermissionError:
            print(" Error: no tienes permiso para abrir ese archivo.")
    else:
        print("Esa opción no es válida.")


# VER ESTADISTICAS (Muestra las estadisticas del día)
# separa el archivo en bloques y revisa cada bloque por separado.
def ver_estadisticas():
    limpiar_pantalla()
    encabezado("ESTADÍSTICAS DEL DÍA")

    try:
        with open(ARCHIVO_REGISTROS, "r") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print("\nTodavía no hay registros para mostrar estadísticas.")
        return

    # Se divide el archivo completo en bloques
    bloques = [b.strip() for b in contenido.split(SEPARADOR_REGISTRO) if b.strip()]

    if not bloques:
        print("\nTodavía no hay registros para mostrar estadísticas.")
        return

    total_ninos = 0
    pagaron_cuota = 0
    pagaron_comida = 0
    deben_cambio = 0
    dinero_comida = 0.0
    dinero_cuotas = 0

    for bloque in bloques:
        pago_cuota_si = False
        pago_comida_si = False
        cambio_del_nino = 0.0   # suma del cambio de cuota + comida para cada niño

        for linea in bloque.split("\n"):
            linea = linea.strip()

            if linea.startswith("Nombre:"):
                total_ninos += 1

            elif linea.startswith("Cuota:"):
                datos_cuota = linea.split("Cuota:")[1].strip()   
                if datos_cuota.startswith("Sí"):
                    pago_cuota_si = True
                try:
                    cambio_del_nino += float(datos_cuota.split("Cambio: $")[1].strip())
                except (IndexError, ValueError):
                    pass   # si el dato no es un número válido, se ignora y no suma nadda

            elif linea.startswith("Comida:"):
                datos_comida = linea.split("Comida:")[1].strip()  
                if datos_comida.startswith("Sí"):
                    pago_comida_si = True
                    try:
                        monto_texto = datos_comida.split("Monto: $")[1].split(" - ")[0].strip()
                        dinero_comida += float(monto_texto)
                    except (IndexError, ValueError):
                        pass
                try:
                    cambio_del_nino += float(datos_comida.split("Cambio: $")[1].strip())
                except (IndexError, ValueError):
                    pass

        if pago_cuota_si:
            pagaron_cuota += 1
            dinero_cuotas += 25          # cada cuota cuesta siempre $25
        if pago_comida_si:
            pagaron_comida += 1
        if cambio_del_nino > 0:
            deben_cambio += 1

    print(f"\nNiños registrados hoy: {total_ninos}")
    print(f"Niños que pagaron cuotas: {pagaron_cuota}")
    print(f"Niños que pagaron comida: {pagaron_comida}")
    print(f"Niños a los que se les debe cambio: {deben_cambio}")
    print(f"Dinero total recaudado de comida: ${dinero_comida:.2f}")
    print(f"Dinero total recaudado de cuotas: ${dinero_cuotas}")


# MAIN (Une la pantalla de carga, bienvenida, fecha, y control de inactividad)
def main():
    while True:   # Ciclo externo: si hay inactividad, regresamos a la pantalla de inicio
        pantalla_carga()
        usuario = bienvenida()
        Fecha = pedir_fecha()

        continuar_en_menu = True
        while continuar_en_menu:                 # Ciclo del menú principal
            tiempo_inicio = time.time()           # Marca el momento en que se mostró el menú
            seleccion = mostrar_menu()

            continuar_en_menu = control_inactividad(tiempo_inicio)
            if not continuar_en_menu:
                print("\nRegresando a la pantalla de inicio...\n")
                time.sleep(2)
                break

            if seleccion == "1":
                registrar_nino(Fecha)
                pausar()
            elif seleccion == "2":
                ver_reporte_dia()
                pausar()
            elif seleccion == "3":
                ver_estadisticas()
                pausar()
            elif seleccion == "4":
                ver_archivos_disponibles()
                pausar()
            elif seleccion == "5":
                limpiar_pantalla()
                print(f"¡Byeee, {usuario}! Nos vemos el proximo sabado .")
                return          # Termina el programa 
            else:
                print("Opción no válida, intenta de nuevo.")
                pausar()


#  hace que main() solo se ejecute si corremos este archivo 
if __name__ == "__main__":
    main()
