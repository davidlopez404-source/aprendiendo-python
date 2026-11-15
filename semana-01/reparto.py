horas_totales_proy = int(input('¿Cuántas horas tiene el proyecto? '))
consultores = int(input('¿Cuántos consultores hay? '))
horas_consultor = horas_totales_proy//consultores
horas_sin_asignar = horas_totales_proy%consultores
horas_exactas_consultor = horas_totales_proy/consultores
print('Las horas completas que le tocan a cada consultor son',horas_consultor)
print('Las horas que quedan sin asignar son',horas_sin_asignar)
print('Las horas exactas por consultor son',horas_exactas_consultor)
