initial_distance = int(input('Enter the first distance in meters: '))
final_distance = int(input('Enter the second distance in meters: '))
time = int(input('Enter the time in seconds: '))

speed = (final_distance - initial_distance)/time  #m/s
speed_km_h = (speed*3600)/1000

print(speed_km_h)

if speed_km_h >=1 and speed_km_h <= 20:
    print('MULTA: Llamado de atencion por baja velocidad')
elif speed_km_h >20 and speed_km_h <= 60:
    print('Velocidad dentro del rango perimitio')
elif speed_km_h >60 and speed_km_h <= 80:
    print('MULTA: Llamado de atencion por alta velocidad')
elif speed_km_h >80 and speed_km_h <= 120:
    alcoholemic_test_result = float(input('Enter the results of the alcoholemic test(mg ethanol/100 ml of blood): '))
    if alcoholemic_test_result >= 20 and alcoholemic_test_result <= 39:
        print('MULTA TIPO I:\n\t- Suspensión  de  la  licencia  de  conducción  entre  seis  (6)  y  doce (12) meses. ')
    elif alcoholemic_test_result >=40 and alcoholemic_test_result <=99:
        print('MULTA TIPO I:\n\t- Suspensión  de  la  Licencia  de  Conducción  entre uno (1) y tres (3) años. ')
    elif alcoholemic_test_result >=100 and alcoholemic_test_result <=149:
        print('''MULTA TIPO I:\n\t- Suspensión de la Licencia de Conducción entre tres (3) y cinco (5) año
        - Realizar curso de   sensibilización,   conocimientos   y   consecuencias   de   la alcoholemia   y   drogadicción 
          en   centros   de   rehabilitación debidamente  autorizados,  por  un  mínimo  de  cuarenta  (40) horas.''')
    elif alcoholemic_test_result >=150:
        print('''MULTA TIPO I:\n\t- Suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción
        - Realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia
          y drogadicción en centros de rehabilitación debidamente  autorizados,  por  un  mínimo  de  ochenta  (80) horas.''')

elif speed_km_h>120:
    
    alcoholemic_test_result = float(input('Enter the results of the alcoholemic test(mg ethanol/100 ml of blood): '))
    if alcoholemic_test_result >= 20 and alcoholemic_test_result <= 39:
        print('MULTA TIPO II:\n\t- Inmovilizacion del vehiculo.\n\t- Suspensión  de  la  licencia  de  conducción  entre  seis  (6)  y  doce (12) meses. ')
    elif alcoholemic_test_result >=40 and alcoholemic_test_result <=99:
        print('MULTA TIPO II:\n\t- Inmovilizacion del vehiculo.\n\t- Suspensión  de  la  Licencia  de  Conducción  entre uno (1) y tres (3) años. ')
    elif alcoholemic_test_result >=100 and alcoholemic_test_result <=149:
        print('''MULTA TIPO II:\n\t- Inmovilizacion del vehiculo.\n\t- Suspensión de la Licencia de Conducción entre tres (3) y cinco (5) año.
        - Realizar curso de   sensibilización,   conocimientos   y   consecuencias   de   la alcoholemia   y   drogadicción 
          en   centros   de   rehabilitación debidamente  autorizados,  por  un  mínimo  de  cuarenta  (40) horas.''')
    elif alcoholemic_test_result >=150:
        print('''MULTA TIPO II:\n\t- Inmovilizacion del vehiculo.\n\t- Suspensión entre cinco (5) y diez (10) años de la Licencia de Conducción\n\t
        - Realizar curso de sensibilización, conocimientos y consecuencias de la alcoholemia y drogadicción en centros de rehabilitación debidamente  
          autorizados,  por  un  mínimo  de  ochenta  (80) horas.''')
else:
    print('Valor incorrecto')