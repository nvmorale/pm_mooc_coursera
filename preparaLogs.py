#%% cargamos los datos y segmentamos los del curso de interes

import pandas as pd

datos = pd.read_excel("proceso.xlsx")

datosWeb = datos.loc[datos['course'] == 'web_semantica']
#datosGestion = datos.loc[datos['course'] == 'gestion_organizaciones_efectivas']
#datosAula = datos.loc[datos['course'] == 'aulaconstructivista']
#datosSV = datos.loc[datos['course'] == 'decodificando_silicon_valley']
#datosElec = datos.loc[datos['course'] == 'electrones_en_accion']
#datosTransporte = datos.loc[datos['course'] == 'analisis_sistemas_de_transporte']

#%% agrupamos las sesiones de trabajo en el mooc

import numpy as np

nSesion = 1
tUmbral = 60*45

indexWeb = 78104

sesion = np.zeros(len(datosWeb))
sesion[0] = 1

#userID = datosWeb['ucchile_user_id']
#timestamp = datosWeb['timestamp']
#duration = datosWeb['duration']

userId = datosWeb['ucchile_user_id'].values.tolist()
actividad = datosWeb['type_status'].values.tolist()
timestamp = datosWeb['timestamp'].values.tolist()
duracion = datosWeb['duration'].values.tolist()

rangeWeb = range(indexWeb+1,indexWeb+len(datosWeb))

for i in range(1,len(datosWeb)):

    if(userId[i] == userId[i-1]):
        if(timestamp[i] - timestamp[i-1] < duracion[i] + tUmbral):
            sesion[i] = nSesion
        else:
            nSesion += 1
            sesion[i] = nSesion
    else:
        nSesion = 1
        sesion[i] = nSesion
            
    
datosWeb['sesion'] = sesion

#%% Procesamos los modulos en el curso y exportamos a listas los datos
import os
path = os.path.abspath(os.path.dirname('proceso.xslx'))

items_web = pd.read_csv(path+'\web_semantica\course_items.csv')
lessons_web = pd.read_csv(path+'\web_semantica\course_lessons.csv')
modules_web = pd.read_csv(path+'\web_semantica\course_modules.csv')

item2lesson_web = dict(zip(items_web['course_item_id'],items_web['course_lesson_id']))
lesson2mod_web = dict(zip(lessons_web['course_lesson_id'],lessons_web['course_module_id']))
mod2num_web =dict(zip(modules_web['course_module_id'],modules_web['course_module_order']))

index_web = 78104

range_web = range(index_web+1,index_web+len(datosWeb))

modulo_web = [mod2num_web[lesson2mod_web[item2lesson_web[datosWeb['course_item_id'][index_web]]]]]

for i in range_web:    
    modulo_web.append([mod2num_web[lesson2mod_web[item2lesson_web[datosWeb['course_item_id'][i]]]]])

datosWeb['modulo'] = modulo_web

datosWebLimpios = datosWeb.loc[datosWeb['modulo'] != 0]

userId = datosWebLimpios['ucchile_user_id'].values.tolist()
sesion = datosWebLimpios['sesion'].values.tolist()
actividad = datosWebLimpios['type_status'].values.tolist()
timestamp = datosWebLimpios['timestamp'].values.tolist()
duracion = datosWebLimpios['duration'].values.tolist()
modulo2 = datosWebLimpios['modulo'].values.tolist()

#%% Procesamos el log de proceso por sesiones

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo2[0]]

for i in range(1,len(datosWebLimpios)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    if(mismoUser & mismaSesion):
        avanzaModulo = modulo2[i] > modulo2[i-1]
        retrocedeModulo = modulo2[i] < modulo2[i-1]
        
        if(avanzaModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo2[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('avanzaModulo')
            
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo2[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')

    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo2[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
            
logSesiones = {'userId': userId_log, 'sesion': sesion_log, 'timestamp': timestamp_log, 'actividad': actividad_log}
logSesionesDF = pd.DataFrame(logSesiones)


#%% insertamos datos de SRL y demograficos 

datosClasificacion_web = datosWeb[['ucchile_user_id','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'
]]

datosClasificacion_web.set_index('ucchile_user_id', inplace = True)

#%% exportamos el log

logSesionesDF.to_csv('procesoWebSesiones.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad'])            
            
#%% procesamos la actividad del usuario por curso a nivel de modulos

userId_log = [userId[0], userId[0]]
actividad_log = ['inicia curso', 'modulo '+str(modulo2[0])]
timestamp_log = [timestamp[0]-3, timestamp[0]-2]

cMod1 = [False, False, False, False, False, False, False]
cursoCompleto = False

for i in range(1,len(datosWebLimpios)):
    
    mismoUser = userId[i-1] == userId[i]

#cuando se cambia de usuario, este pudo haber completado o abandonado el curso
#luego para el siguiente usuario se agrega que inicia curso y el primer módulo    
    
    if(not mismoUser):
        
        cMod1 = [False, False, False, False, False, False, False]
        userId_log.append(userId[i-1])
        timestamp_log.append(timestamp[i-1]+1)
        
        if(cursoCompleto):            
            actividad_log.append('completa curso')
            cursoCompleto = False
        else:
            actividad_log.append('termina curso')
        
        userId_log.append(userId[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('inicia curso')
        
        userId_log.append(userId[i])
        timestamp_log.append(timestamp[i]+1)
        actividad_log.append('modulo '+str(modulo2[i]))
             
        if(actividad[i] == 'assessment.complete'):
            userId_log.append(userId[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('modulo '+str(modulo2[i]) + ' completo')
    else:
        mismoModulo = modulo2[i-1] == modulo2[i]
        completaModulo = actividad[i-1] == 'assessment.complete'
                
        if(not mismoModulo):
            if(completaModulo):
                userId_log.append(userId[i])
                timestamp_log.append(timestamp[i-1]-1)
                actividad_log.append('modulo '+str(modulo2[i-1]) + ' completo')
                
            userId_log.append(userId[i-1])
            timestamp_log.append(timestamp[i-1]+1)
            actividad_log.append('modulo '+str(modulo2[i]))              
    
    cMod1[modulo2[i]-1] = actividad[i-1] == 'assessment.complete'
    cursoCompleto = min(cMod1[0:6])

userId_log.append(userId[i])
timestamp_log.append(timestamp[i]+1)
        
if(cursoCompleto): 
    actividad_log.append('completa curso')
else:
    actividad_log.append('termina curso')

logModulos = {'userId': userId_log, 'timestamp': timestamp_log, 'actividad': actividad_log}
logModulosDF = pd.DataFrame(logModulos)

logModulosDF.to_csv('procesoWebModulos.csv', index = False, columns = ['userId', 'timestamp', 'actividad'])            
                 
 
#%% exportamos datos del curso por sesiones sin procesar

datosWebLimpios[['ucchile_user_id','timestamp','type_status','sesion']].to_csv('procesoWeb.csv')