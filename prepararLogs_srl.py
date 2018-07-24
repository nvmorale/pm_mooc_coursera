import pandas as pd

datos = pd.read_excel("proceso.xlsx")

#%% incorporamos info de sesiones
import numpy as np

nSesion = 1
tUmbral = 60*45

sesion = np.zeros(len(datos))
sesion[0] = 1

userId = datos['ucchile_user_id'].values.tolist()
actividad = datos['type_status'].values.tolist()
timestamp = datos['timestamp'].values.tolist()
duracion = datos['duration'].values.tolist()

for i in range(1,len(datos)):
    
    if(userId[i] == userId[i-1]):
        if(timestamp[i] - timestamp[i-1] < duracion[i] + tUmbral):
            sesion[i] = nSesion
        else:
            nSesion += 1
            sesion[i] = nSesion
    else:
        nSesion = 1
        sesion[i] = nSesion

datos['sesion'] = sesion

# Incorporamos info de semanas

nSemana = 1
tSemana = 60*60*24*7

semana = np.zeros(len(datos))
semana[0] = 1

tInicial = timestamp[0]

for i in range(1,len(datos)):
    
    if(userId[i] == userId[i-1]):
        if(timestamp[i] - timestamp[i-1] < nSemana*tSemana):
            semana[i] = nSemana
        else:
            nSemana += 1
            semana[i] = nSemana
    else:
        nSemana = 1
        semana[i] = nSemana

datos['semana'] = semana


#%%
import os
path = os.path.abspath(os.path.dirname('proceso.xslx'))

items_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_items.csv')
lessons_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_lessons.csv')
modules_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_modules.csv')

item2lesson_gestion = dict(zip(items_gestion['course_item_id'],items_gestion['course_lesson_id']))
lesson2mod_gestion = dict(zip(lessons_gestion['course_lesson_id'],lessons_gestion['course_module_id']))
mod2num_gestion = dict(zip(modules_gestion['course_module_id'],modules_gestion['course_module_order']))
lesson2num_gestion = dict(zip(lessons_gestion['course_lesson_id'],lessons_gestion['course_lesson_order']))


items_elec = pd.read_csv(path+'\electrones_en_accion\course_items.csv')
lessons_elec = pd.read_csv(path+'\electrones_en_accion\course_lessons.csv')
modules_elec = pd.read_csv(path+'\electrones_en_accion\course_modules.csv')

item2lesson_elec = dict(zip(items_elec['course_item_id'],items_elec['course_lesson_id']))
lesson2mod_elec = dict(zip(lessons_elec['course_lesson_id'],lessons_elec['course_module_id']))
mod2num_elec =dict(zip(modules_elec['course_module_id'],modules_elec['course_module_order']))
lesson2num_elec = dict(zip(lessons_elec['course_lesson_id'],lessons_elec['course_lesson_order']))

#%%

notas_elec = pd.read_csv(path+'\electrones_en_accion\course_grades.csv')
notas_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_grades.csv')

user2nota_elec = dict(zip(notas_elec['ucchile_user_id'],notas_elec['course_passing_state_id']))
user2nota_gestion = dict(zip(notas_gestion['ucchile_user_id'],notas_gestion['course_passing_state_id']))
#%%
datos_elec = datos.loc[datos['course'] == 'electrones_en_accion']
datos_gestion = datos.loc[datos['course'] == 'gestion_organizaciones_efectivas']

#%% Extraemos los valores de SRl por usuario

GoalSetting_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['GoalSetting']))
StrategicPlanning_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['StrategicPlanning']))
SelfEvaluation_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['SelfEvaluation']))
TaskStrategies_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['TaskStrategies']))
Elaboration_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['Elaboration']))
HelpSeeking_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['HelpSeeking']))
SRL_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['SRL']))
edu_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['edu']))
age_gestion = dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['age']))
isfemale_gestion =dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['isfemale']))

GoalSetting_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['GoalSetting']))
StrategicPlanning_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['StrategicPlanning']))
SelfEvaluation_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['SelfEvaluation']))
TaskStrategies_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['TaskStrategies']))
Elaboration_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['Elaboration']))
HelpSeeking_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['HelpSeeking']))
SRL_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['SRL']))
edu_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['edu']))
age_elec = dict(zip(datos_elec['ucchile_user_id'],datos_elec['age']))
isfemale_elec =dict(zip(datos_elec['ucchile_user_id'],datos_elec['isfemale']))


#%% Calculamos las medias, medianas y desviaciones de las estrategias de srl en cada curso
GoalSetting_median_gestion = np.median(list(GoalSetting_gestion.values()))
StrategicPlanning_median_gestion = np.median(list(StrategicPlanning_gestion.values()))
SelfEvaluation_median_gestion = np.median(list(SelfEvaluation_gestion.values()))
TaskStrategies_median_gestion = np.median(list(TaskStrategies_gestion.values()))
Elaboration_median_gestion = np.median(list(Elaboration_gestion.values()))
HelpSeeking_median_gestion = np.median(list(HelpSeeking_gestion.values()))
SRL_median_gestion = np.median(list(SRL_gestion.values()))

GoalSetting_median_elec = np.median(list(GoalSetting_elec.values()))
StrategicPlanning_median_elec = np.median(list(StrategicPlanning_elec.values()))
SelfEvaluation_median_elec = np.median(list(SelfEvaluation_elec.values()))
TaskStrategies_median_elec = np.median(list(TaskStrategies_elec.values()))
Elaboration_median_elec = np.median(list(Elaboration_elec.values()))
HelpSeeking_median_elec = np.median(list(HelpSeeking_elec.values()))
SRL_median_elec = np.median(list(SRL_elec.values()))

GoalSetting_mean_gestion = np.mean(list(GoalSetting_gestion.values()))
StrategicPlanning_mean_gestion = np.mean(list(StrategicPlanning_gestion.values()))
SelfEvaluation_mean_gestion = np.mean(list(SelfEvaluation_gestion.values()))
TaskStrategies_mean_gestion = np.mean(list(TaskStrategies_gestion.values()))
Elaboration_mean_gestion = np.mean(list(Elaboration_gestion.values()))
HelpSeeking_mean_gestion = np.mean(list(HelpSeeking_gestion.values()))
SRL_mean_gestion = np.mean(list(SRL_gestion.values()))

GoalSetting_mean_elec = np.mean(list(GoalSetting_elec.values()))
StrategicPlanning_mean_elec = np.mean(list(StrategicPlanning_elec.values()))
SelfEvaluation_mean_elec = np.mean(list(SelfEvaluation_elec.values()))
TaskStrategies_mean_elec = np.mean(list(TaskStrategies_elec.values()))
Elaboration_mean_elec = np.mean(list(Elaboration_elec.values()))
HelpSeeking_mean_elec = np.mean(list(HelpSeeking_elec.values()))
SRL_mean_elec = np.mean(list(SRL_elec.values()))

GoalSetting_std_gestion = np.std(list(GoalSetting_gestion.values()))
StrategicPlanning_std_gestion = np.std(list(StrategicPlanning_gestion.values()))
SelfEvaluation_std_gestion = np.std(list(SelfEvaluation_gestion.values()))
TaskStrategies_std_gestion = np.std(list(TaskStrategies_gestion.values()))
Elaboration_std_gestion = np.std(list(Elaboration_gestion.values()))
HelpSeeking_std_gestion = np.std(list(HelpSeeking_gestion.values()))
SRL_std_gestion = np.std(list(SRL_gestion.values()))

GoalSetting_std_elec = np.std(list(GoalSetting_elec.values()))
StrategicPlanning_std_elec = np.std(list(StrategicPlanning_elec.values()))
SelfEvaluation_std_elec = np.std(list(SelfEvaluation_elec.values()))
TaskStrategies_std_elec = np.std(list(TaskStrategies_elec.values()))
Elaboration_std_elec = np.std(list(Elaboration_elec.values()))
HelpSeeking_std_elec = np.std(list(HelpSeeking_elec.values()))
SRL_std_elec = np.std(list(SRL_elec.values()))


#%% Agregamos información de modulo y lesson a los datos

index_elec = 19750
index_gestion = 64786

range_elec = range(index_elec+1,index_elec+len(datos_elec))
range_gestion = range(index_gestion+1,index_gestion+len(datos_gestion))

modulo_elec = [mod2num_elec[lesson2mod_elec[item2lesson_elec[datos_elec['course_item_id'][index_elec]]]]]
lesson_elec = [lesson2num_elec[item2lesson_elec[datos_elec['course_item_id'][index_elec]]]]

dictAprobacion = {0:0, 1:1, 2:1, 3:0}

aprobacion_elec = [dictAprobacion[user2nota_elec[datos_elec['ucchile_user_id'][index_elec]]]]
aprobacion_gestion = [dictAprobacion[user2nota_gestion[datos_gestion['ucchile_user_id'][index_gestion]]]]

for i in range_elec:    
    modulo_elec.append(mod2num_elec[lesson2mod_elec[item2lesson_elec[datos_elec['course_item_id'][i]]]]+1)
    lesson_elec.append(lesson2num_elec[item2lesson_elec[datos_elec['course_item_id'][i]]]+1)
    aprobacion_elec.append(dictAprobacion[user2nota_elec[datos_elec['ucchile_user_id'][i]]])

datos_elec['modulo'] = modulo_elec
datos_elec['lesson'] = lesson_elec
datos_elec['aprueba'] = aprobacion_elec

modulo_gestion = [mod2num_gestion[lesson2mod_gestion[item2lesson_gestion[datos_gestion['course_item_id'][index_gestion]]]]]
lesson_gestion = [lesson2num_gestion[item2lesson_gestion[datos_gestion['course_item_id'][index_gestion]]]]

for i in range_gestion:    
    modulo_gestion.append(mod2num_gestion[lesson2mod_gestion[item2lesson_gestion[datos_gestion['course_item_id'][i]]]]+1)
    lesson_gestion.append(lesson2num_gestion[item2lesson_gestion[datos_gestion['course_item_id'][i]]]+1)
    aprobacion_gestion.append(dictAprobacion[user2nota_gestion[datos_gestion['ucchile_user_id'][i]]])
    
datos_gestion['modulo'] = modulo_gestion
datos_gestion['lesson'] = lesson_gestion
datos_gestion['aprueba'] = aprobacion_gestion

aprueba_elec =dict(zip(datos_elec['ucchile_user_id'],datos_elec['aprueba']))
aprueba_gestion =dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['aprueba']))

#%% generamos el log por sesiones para el curso de electrones en accion

userId = datos_elec['ucchile_user_id'].values.tolist()
sesion = datos_elec['sesion'].values.tolist()
actividad = datos_elec['type_status'].values.tolist()
timestamp = datos_elec['timestamp'].values.tolist()
modulo = datos_elec['modulo'].values.tolist()
lesion = datos_elec['lesson'].values.tolist()

duracion = datos_elec['duration'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
lesion_log = [lesion[0]]

for i in range(1,len(datos_elec)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    if(mismoUser & mismaSesion):
        avanzaModulo = modulo[i] > modulo[i-1]
        retrocedeModulo = modulo[i] < modulo[i-1]
        avanzaLesion = lesion[i] > lesion[i-1]
        retrocedeLesion = lesion[i] < lesion[i-1]
        
        if(avanzaModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            lesion_log.append(lesion[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('avanzaModulo')
                    
        elif(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            lesion_log.append(lesion[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
                    
        else:
            if(avanzaLesion):
                userId_log.append(userId[i])
                sesion_log.append(sesion[i])
                modulo_log.append(modulo[i])
                lesion_log.append(lesion[i])
                timestamp_log.append(timestamp[i]-1)
                actividad_log.append('avanzaLesion')
                                
            elif(retrocedeLesion):
                userId_log.append(userId[i])
                sesion_log.append(sesion[i])
                modulo_log.append(modulo[i])
                lesion_log.append(lesion[i])
                timestamp_log.append(timestamp[i]-1)
                actividad_log.append('retrocedeLesion')
                    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    lesion_log.append(lesion[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    
edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_elec[userId_log[i]])
    age_log.append(age_elec[userId_log[i]])
    isfemale_log.append(isfemale_elec[userId_log[i]])
    GoalSetting_log.append(GoalSetting_elec[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_elec[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_elec[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_elec[userId_log[i]])
    Elaboration_log.append(Elaboration_elec[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_elec[userId_log[i]])
    SRL_log.append(SRL_elec[userId_log[i]])
    aprueba_log.append(aprueba_elec[userId_log[i]])
    

dictLogSesiones = {}
dictLogSesiones['userId'] = userId_log
dictLogSesiones['sesion'] = sesion_log
dictLogSesiones['timestamp'] = timestamp_log
dictLogSesiones['actividad'] = actividad_log
dictLogSesiones['modulo'] = modulo_log
dictLogSesiones['lesson'] = lesion_log
dictLogSesiones['edu'] = edu_log
dictLogSesiones['age'] = age_log
dictLogSesiones['isfemale'] = isfemale_log
dictLogSesiones['GoalSetting'] = GoalSetting_log
dictLogSesiones['StrategicPlanning'] = StrategicPlanning_log
dictLogSesiones['SelfEvaluation'] = SelfEvaluation_log
dictLogSesiones['TaskStrategies']=TaskStrategies_log
dictLogSesiones['Elaboration']= Elaboration_log
dictLogSesiones['HelpSeeking']= HelpSeeking_log
dictLogSesiones['SRL'] =SRL_log
dictLogSesiones['aprueba'] = aprueba_log

logSesiones_elec = pd.DataFrame(dictLogSesiones)
logSesiones_elec.to_csv('procesoSesiones_elec.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo', 'lesson','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])

#%% generamos el log por sesiones para el curso de gestion de organizaciones

userId = datos_gestion['ucchile_user_id'].values.tolist()
sesion = datos_gestion['sesion'].values.tolist()
actividad = datos_gestion['type_status'].values.tolist()
timestamp = datos_gestion['timestamp'].values.tolist()
duracion = datos_gestion['duration'].values.tolist()
modulo = datos_gestion['modulo'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]

for i in range(1,len(datos_gestion)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    if(mismoUser & mismaSesion):
        avanzaModulo = modulo[i] > modulo[i-1]
        retrocedeModulo = modulo[i] < modulo[i-1]
        
        if(avanzaModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('avanzaModulo')
                    
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
                
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])

edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_gestion[userId_log[i]])
    age_log.append(age_gestion[userId_log[i]])
    isfemale_log.append(isfemale_gestion[userId_log[i]])
    GoalSetting_log.append(GoalSetting_gestion[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_gestion[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_gestion[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_gestion[userId_log[i]])
    Elaboration_log.append(Elaboration_gestion[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_gestion[userId_log[i]])
    SRL_log.append(SRL_gestion[userId_log[i]])
    aprueba_log.append(aprueba_gestion[userId_log[i]])

    

dictLogSesiones = {}
dictLogSesiones['userId'] = userId_log
dictLogSesiones['sesion'] = sesion_log
dictLogSesiones['timestamp'] = timestamp_log
dictLogSesiones['actividad'] = actividad_log
dictLogSesiones['modulo'] = modulo_log
dictLogSesiones['edu'] = edu_log
dictLogSesiones['age'] = age_log
dictLogSesiones['isfemale'] = isfemale_log
dictLogSesiones['GoalSetting'] = GoalSetting_log
dictLogSesiones['StrategicPlanning'] = StrategicPlanning_log
dictLogSesiones['SelfEvaluation'] = SelfEvaluation_log
dictLogSesiones['TaskStrategies']=TaskStrategies_log
dictLogSesiones['Elaboration']= Elaboration_log
dictLogSesiones['HelpSeeking']= HelpSeeking_log
dictLogSesiones['SRL'] =SRL_log
dictLogSesiones['aprueba'] =aprueba_log

logSesiones_gestion = pd.DataFrame(dictLogSesiones)
logSesiones_gestion.to_csv('procesoSesiones_gestion.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])

#%% generamos el log por semanas para el curso de electrones en accion

userId = datos_elec['ucchile_user_id'].values.tolist()
semana = datos_elec['semana'].values.tolist()
actividad = datos_elec['type_status'].values.tolist()
timestamp = datos_elec['timestamp'].values.tolist()
duracion = datos_elec['duration'].values.tolist()
modulo = datos_elec['modulo'].values.tolist()
lesion = datos_elec['lesson'].values.tolist()

userId_log = [userId[0]]
semana_log = [semana[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
lesion_log = [lesion[0]]

for i in range(1,len(datos_elec)):
    mismoUser = userId[i-1] == userId[i]
    mismaSemana = semana[i-1] == semana[i]
    
    if(mismoUser):
        avanzaModulo = modulo[i] > modulo[i-1]
        retrocedeModulo = modulo[i] < modulo[i-1]
        avanzaLesion = lesion[i] > lesion[i-1]
        retrocedeLesion = lesion[i] < lesion[i-1]
        
        if(avanzaModulo):
            userId_log.append(userId[i])
            semana_log.append(semana[i])
            modulo_log.append(modulo[i])
            lesion_log.append(lesion[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('avanzaModulo')
                    
        elif(retrocedeModulo):
            userId_log.append(userId[i])
            semana_log.append(semana[i])
            modulo_log.append(modulo[i])
            lesion_log.append(lesion[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
                    
        else:
            if(avanzaLesion):
                userId_log.append(userId[i])
                semana_log.append(semana[i])
                modulo_log.append(modulo[i])
                lesion_log.append(lesion[i])
                timestamp_log.append(timestamp[i]-1)
                actividad_log.append('avanzaLesion')
                                
            elif(retrocedeLesion):
                userId_log.append(userId[i])
                semana_log.append(semana[i])
                modulo_log.append(modulo[i])
                lesion_log.append(lesion[i])
                timestamp_log.append(timestamp[i]-1)
                actividad_log.append('retrocedeLesion')
                    
    userId_log.append(userId[i])
    semana_log.append(semana[i])
    modulo_log.append(modulo[i]) 
    lesion_log.append(lesion[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])

edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_elec[userId_log[i]])
    age_log.append(age_elec[userId_log[i]])
    isfemale_log.append(isfemale_elec[userId_log[i]])
    GoalSetting_log.append(GoalSetting_elec[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_elec[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_elec[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_elec[userId_log[i]])
    Elaboration_log.append(Elaboration_elec[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_elec[userId_log[i]])
    SRL_log.append(SRL_elec[userId_log[i]])
    aprueba_log.append(aprueba_elec[userId_log[i]])  


dictLogSemanas = {}
dictLogSemanas['userId'] = userId_log
dictLogSemanas['semana'] = semana_log
dictLogSemanas['timestamp'] = timestamp_log
dictLogSemanas['actividad'] = actividad_log
dictLogSemanas['modulo'] = modulo_log
dictLogSemanas['lesson'] = lesion_log
dictLogSemanas['edu'] = edu_log
dictLogSemanas['age'] = age_log
dictLogSemanas['isfemale'] = isfemale_log
dictLogSemanas['GoalSetting'] = GoalSetting_log
dictLogSemanas['StrategicPlanning'] = StrategicPlanning_log
dictLogSemanas['SelfEvaluation'] = SelfEvaluation_log
dictLogSemanas['TaskStrategies']=TaskStrategies_log
dictLogSemanas['Elaboration']= Elaboration_log
dictLogSemanas['HelpSeeking']= HelpSeeking_log
dictLogSemanas['SRL'] =SRL_log
dictLogSemanas['aprueba'] = aprueba_log

logSemanas_elec = pd.DataFrame(dictLogSemanas)
logSemanas_elec.to_csv('procesoSemanas_elec.csv', index = False, columns = ['userId', 'semana', 'timestamp', 'actividad', 'modulo', 'lesson','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL', 'aprueba'])

#%% generamos el log por semanas para el curso de gestion de organizaciones

userId = datos_gestion['ucchile_user_id'].values.tolist()
semana = datos_gestion['semana'].values.tolist()
actividad = datos_gestion['type_status'].values.tolist()
timestamp = datos_gestion['timestamp'].values.tolist()
duracion = datos_gestion['duration'].values.tolist()
modulo = datos_gestion['modulo'].values.tolist()

userId_log = [userId[0]]
semana_log = [semana[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]

for i in range(1,len(datos_gestion)):
    mismoUser = userId[i-1] == userId[i]
    mismaSemana = semana[i-1] == semana[i]
    
    if(mismoUser):
        avanzaModulo = modulo[i] > modulo[i-1]
        retrocedeModulo = modulo[i] < modulo[i-1]
        
        if(avanzaModulo):
            userId_log.append(userId[i])
            semana_log.append(semana[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('avanzaModulo')
                    
        if(retrocedeModulo):
            userId_log.append(userId[i])
            semana_log.append(semana[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
                
    userId_log.append(userId[i])
    semana_log.append(semana[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    
edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_gestion[userId_log[i]])
    age_log.append(age_gestion[userId_log[i]])
    isfemale_log.append(isfemale_gestion[userId_log[i]])
    GoalSetting_log.append(GoalSetting_gestion[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_gestion[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_gestion[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_gestion[userId_log[i]])
    Elaboration_log.append(Elaboration_gestion[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_gestion[userId_log[i]])
    SRL_log.append(SRL_gestion[userId_log[i]])
    aprueba_log.append(aprueba_gestion[userId_log[i]])


dictLogSemanas = {}
dictLogSemanas['userId'] = userId_log
dictLogSemanas['semana'] = semana_log
dictLogSemanas['timestamp'] = timestamp_log
dictLogSemanas['actividad'] = actividad_log
dictLogSemanas['modulo'] = modulo_log
dictLogSemanas['edu'] = edu_log
dictLogSemanas['age'] = age_log
dictLogSemanas['isfemale'] = isfemale_log
dictLogSemanas['GoalSetting'] = GoalSetting_log
dictLogSemanas['StrategicPlanning'] = StrategicPlanning_log
dictLogSemanas['SelfEvaluation'] = SelfEvaluation_log
dictLogSemanas['TaskStrategies']=TaskStrategies_log
dictLogSemanas['Elaboration']= Elaboration_log
dictLogSemanas['HelpSeeking']= HelpSeeking_log
dictLogSemanas['SRL'] =SRL_log
dictLogSemanas['aprueba'] = aprueba_log

logSemanas_gestion = pd.DataFrame(dictLogSemanas)
logSemanas_gestion.to_csv('procesoSemanas_gestion.csv', index = False, columns = ['userId', 'semana', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])


#%% procesamos la actividad del usuario por curso a nivel de modulos para el mooc de gestion

userId = datos_gestion['ucchile_user_id'].values.tolist()
actividad = datos_gestion['type_status'].values.tolist()
timestamp = datos_gestion['timestamp'].values.tolist()
duracion = datos_gestion['duration'].values.tolist()
modulo = datos_gestion['modulo'].values.tolist()

userId_log = [userId[0], userId[0]]
actividad_log = ['inicia curso', 'modulo '+str(modulo[0])]
timestamp_log = [timestamp[0]-3, timestamp[0]-2]

completaMod = [False, False, False, False, False, False, False]

for i in range(1,len(datos_gestion)):
    
    mismoUser = userId[i-1] == userId[i]
    
    if(not mismoUser):
        
        completaMod = [False, False, False, False, False, False, False]
        
        userId_log.append(userId[i-1])
        timestamp_log.append(timestamp[i-1]+1)
        actividad_log.append('termina curso')
                
        userId_log.append(userId[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('inicia curso')
                
        userId_log.append(userId[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('modulo ' + str(modulo[i]))
                
        if(actividad[i] == 'assessment.complete'):
            
            userId_log.append(userId[i])
            timestamp_log.append(timestamp[i])
            actividad_log.append('modulo ' + str(modulo[i]) + ' completo')            
        
    else:
        
        mismoModulo = modulo[i-1] == modulo[i]
        completaModulo = actividad[i-1] == 'assessment.complete'
        
        if(not mismoModulo):
            if(completaModulo):
                userId_log.append(userId[i])
                timestamp_log.append(timestamp[i-1]-1)
                actividad_log.append('modulo '+str(modulo[i-1]) + ' completo')
                
            userId_log.append(userId[i-1])
            timestamp_log.append(timestamp[i-1]+1)
            actividad_log.append('modulo '+str(modulo[i])) 
    
userId_log.append(userId[i])
timestamp_log.append(timestamp[i]+1)
actividad_log.append('termina curso')
   
edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_gestion[userId_log[i]])
    age_log.append(age_gestion[userId_log[i]])
    isfemale_log.append(isfemale_gestion[userId_log[i]])
    GoalSetting_log.append(GoalSetting_gestion[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_gestion[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_gestion[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_gestion[userId_log[i]])
    Elaboration_log.append(Elaboration_gestion[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_gestion[userId_log[i]])
    SRL_log.append(SRL_gestion[userId_log[i]])
    aprueba_log.append(aprueba_gestion[userId_log[i]])


dictLogModulos = {}
dictLogModulos['userId'] = userId_log
dictLogModulos['timestamp'] = timestamp_log
dictLogModulos['actividad'] = actividad_log
dictLogModulos['edu'] = edu_log
dictLogModulos['age'] = age_log
dictLogModulos['isfemale'] = isfemale_log
dictLogModulos['GoalSetting'] = GoalSetting_log
dictLogModulos['StrategicPlanning'] = StrategicPlanning_log
dictLogModulos['SelfEvaluation'] = SelfEvaluation_log
dictLogModulos['TaskStrategies']=TaskStrategies_log
dictLogModulos['Elaboration']= Elaboration_log
dictLogModulos['HelpSeeking']= HelpSeeking_log
dictLogModulos['SRL'] =SRL_log
dictLogModulos['aprueba'] = aprueba_log

logModulos_gestion = pd.DataFrame(dictLogModulos)
logModulos_gestion.to_csv('procesoModulos_gestion.csv', index = False, columns = ['userId', 'timestamp', 'actividad','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])

    
#%% procesamos la actividad del usuario por curso a nivel de modulos para el mooc de electrones en accion

userId = datos_elec['ucchile_user_id'].values.tolist()
actividad = datos_elec['type_status'].values.tolist()
timestamp = datos_elec['timestamp'].values.tolist()
duracion = datos_elec['duration'].values.tolist()
modulo = datos_elec['modulo'].values.tolist()
lesion = datos_elec['lesson'].values.tolist()

userId_log = [userId[0], userId[0]]
actividad_log = ['inicia curso', 'modulo '+str(modulo[0])]
timestamp_log = [timestamp[0]-3, timestamp[0]-2]

completaMod = [False, False, False, False, False, False, False]

for i in range(1,len(datos_gestion)):
    
    mismoUser = userId[i-1] == userId[i]
    
    if(not mismoUser):
        
        completaMod = [False, False, False, False, False, False, False]
        
        userId_log.append(userId[i-1])
        timestamp_log.append(timestamp[i-1]+1)
        actividad_log.append('termina curso')
                
        userId_log.append(userId[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('inicia curso')
         
        userId_log.append(userId[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('lesion' + str(modulo[i]) +'.' + str(lesion[i]))
                
        if(actividad[i] == 'assessment.complete'):
            
            userId_log.append(userId[i])
            timestamp_log.append(timestamp[i])
            actividad_log.append('lesion' + str(modulo[i]) +'.' + str(lesion[i]) + ' completo')            
        
    else:
        
        mismoModulo = modulo[i-1] == modulo[i]
        mismaLesion = lesion[i-1] == lesion[i]
        completaModulo = actividad[i-1] == 'assessment.complete'
        
        if(not (mismoModulo & mismaLesion)):
            if(completaModulo):
                userId_log.append(userId[i])
                timestamp_log.append(timestamp[i-1]-1)
                actividad_log.append('lesion' + str(modulo[i-1]) +'.' + str(lesion[i-1]) + ' completo')
                
            userId_log.append(userId[i-1])
            timestamp_log.append(timestamp[i-1]+1)
            actividad_log.append('lesion' + str(modulo[i]) +'.' + str(lesion[i]))
    
userId_log.append(userId[i])
timestamp_log.append(timestamp[i]+1)
actividad_log.append('termina curso')
   
edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_elec[userId_log[i]])
    age_log.append(age_elec[userId_log[i]])
    isfemale_log.append(isfemale_elec[userId_log[i]])
    GoalSetting_log.append(GoalSetting_elec[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_elec[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_elec[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_elec[userId_log[i]])
    Elaboration_log.append(Elaboration_elec[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_elec[userId_log[i]])
    SRL_log.append(SRL_elec[userId_log[i]])
    aprueba_log.append(aprueba_elec[userId_log[i]])

dictLogModulos = {}
dictLogModulos['userId'] = userId_log
dictLogModulos['timestamp'] = timestamp_log
dictLogModulos['actividad'] = actividad_log
dictLogModulos['edu'] = edu_log
dictLogModulos['age'] = age_log
dictLogModulos['isfemale'] = isfemale_log
dictLogModulos['GoalSetting'] = GoalSetting_log
dictLogModulos['StrategicPlanning'] = StrategicPlanning_log
dictLogModulos['SelfEvaluation'] = SelfEvaluation_log
dictLogModulos['TaskStrategies']=TaskStrategies_log
dictLogModulos['Elaboration']= Elaboration_log
dictLogModulos['HelpSeeking']= HelpSeeking_log
dictLogModulos['SRL'] =SRL_log
dictLogModulos['aprueba'] = aprueba_log

logModulos_elec = pd.DataFrame(dictLogModulos)
logModulos_elec.to_csv('procesoModulos_elec.csv', index = False, columns = ['userId', 'timestamp', 'actividad','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])
    
#%% generamos el log con transiciones de SRL para el curso de electrones en accion

userId = datos_elec['ucchile_user_id'].values.tolist()
sesion = datos_elec['sesion'].values.tolist()
actividad = datos_elec['type_status'].values.tolist()
timestamp = datos_elec['timestamp'].values.tolist()
duracion = datos_elec['duration'].values.tolist()
tipo = datos_elec['type'].values.tolist()
itemId = datos_elec['course_item_id'].values.tolist()

contador_elec = dict(zip(items_elec['course_item_id'].values.tolist(),list(np.zeros(len(items_elec)))))

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = ['iniciaSesion']
timestamp_log = [timestamp[0]-1]

contador_elec[itemId[0]] = 1

for i in range(1,len(datos_elec)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    aux = contador_elec[itemId[i]]
    contador_elec[itemId[i]] = aux + 1
    
    rehearsal = contador_elec[itemId[i]] > 2
    organization = (tipo[i-1] == 'lecture') & (tipo[i] == 'assessment')
    elaboration = actividad[i] == 'assessment.complete'
    
    
    if(mismoUser & mismaSesion):
        if(rehearsal):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('rehearsal')
            timestamp_log.append(timestamp[i]+1)
        if(organization):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('organization')
            timestamp_log.append(timestamp[i]+2)
        if(elaboration):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('elaboration')
            timestamp_log.append(timestamp[i]+3)
    else:       
        userId_log.append(userId[i-1])
        sesion_log.append(sesion[i-1])
        timestamp_log.append(timestamp[i-1]+4)
        actividad_log.append('terminaSesion')
        
        userId_log.append(userId[i])
        sesion_log.append(sesion[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('iniciaSesion')
    
    if(not mismoUser):
        contador_elec = dict(zip(items_elec['course_item_id'].values.tolist(),list(np.zeros(len(items_elec)))))
    
userId_log.append(userId[i])
sesion_log.append(sesion[i])
timestamp_log.append(timestamp[i]+4)
actividad_log.append('terminaSesion')
    
edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_elec[userId_log[i]])
    age_log.append(age_elec[userId_log[i]])
    isfemale_log.append(isfemale_elec[userId_log[i]])
    GoalSetting_log.append(GoalSetting_elec[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_elec[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_elec[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_elec[userId_log[i]])
    Elaboration_log.append(Elaboration_elec[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_elec[userId_log[i]])
    SRL_log.append(SRL_elec[userId_log[i]])
    aprueba_log.append(aprueba_elec[userId_log[i]])
    

dictLogSesionesSRL = {}
dictLogSesionesSRL['userId'] = userId_log
dictLogSesionesSRL['sesion'] = sesion_log
dictLogSesionesSRL['timestamp'] = timestamp_log
dictLogSesionesSRL['actividad'] = actividad_log
dictLogSesionesSRL['edu'] = edu_log
dictLogSesionesSRL['age'] = age_log
dictLogSesionesSRL['isfemale'] = isfemale_log
dictLogSesionesSRL['GoalSetting'] = GoalSetting_log
dictLogSesionesSRL['StrategicPlanning'] = StrategicPlanning_log
dictLogSesionesSRL['SelfEvaluation'] = SelfEvaluation_log
dictLogSesionesSRL['TaskStrategies']=TaskStrategies_log
dictLogSesionesSRL['Elaboration']= Elaboration_log
dictLogSesionesSRL['HelpSeeking']= HelpSeeking_log
dictLogSesionesSRL['SRL'] =SRL_log
dictLogSesionesSRL['aprueba'] =aprueba_log

logSesionesSRL_elec = pd.DataFrame(dictLogSesionesSRL)
logSesionesSRL_elec.to_csv('procesoSesionesSRL_elec.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])

#%% generamos el log con transiciones de SRL para el curso de gestion

userId = datos_gestion['ucchile_user_id'].values.tolist()
sesion = datos_gestion['sesion'].values.tolist()
actividad = datos_gestion['type_status'].values.tolist()
timestamp = datos_gestion['timestamp'].values.tolist()
duracion = datos_gestion['duration'].values.tolist()
tipo = datos_gestion['type'].values.tolist()
itemId = datos_gestion['course_item_id'].values.tolist()

contador_gestion = dict(zip(items_gestion['course_item_id'].values.tolist(),list(np.zeros(len(items_gestion)))))

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = ['iniciaSesion']
timestamp_log = [timestamp[0]-1]

contador_gestion[itemId[0]] = 1

for i in range(1,len(datos_gestion)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    aux = contador_gestion[itemId[i]]
    contador_gestion[itemId[i]] = aux + 1
    
    rehearsal = contador_gestion[itemId[i]] > 2
    organization = (tipo[i-1] == 'lecture') & (tipo[i] == 'assessment')
    elaboration = actividad[i] == 'assessment.complete'
    
    
    if(mismoUser & mismaSesion):
        if(rehearsal):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('rehearsal')
            timestamp_log.append(timestamp[i]+1)
        if(organization):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('organization')
            timestamp_log.append(timestamp[i]+2)
        if(elaboration):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('elaboration')
            timestamp_log.append(timestamp[i]+3)
    else:       
        userId_log.append(userId[i-1])
        sesion_log.append(sesion[i-1])
        timestamp_log.append(timestamp[i-1]+4)
        actividad_log.append('terminaSesion')
        
        userId_log.append(userId[i])
        sesion_log.append(sesion[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('iniciaSesion')
    
    if(not mismoUser):
        contador_gestion = dict(zip(items_gestion['course_item_id'].values.tolist(),list(np.zeros(len(items_gestion)))))
    
userId_log.append(userId[i])
sesion_log.append(sesion[i])
timestamp_log.append(timestamp[i]+4)
actividad_log.append('terminaSesion')
    
edu_log = []
age_log = []
isfemale_log = []
GoalSetting_log = []
StrategicPlanning_log = []
SelfEvaluation_log = []
TaskStrategies_log = []
Elaboration_log = []
HelpSeeking_log = []
SRL_log = []
aprueba_log = []

for i in range(0,len(userId_log)):
    edu_log.append(edu_gestion[userId_log[i]])
    age_log.append(age_gestion[userId_log[i]])
    isfemale_log.append(isfemale_gestion[userId_log[i]])
    GoalSetting_log.append(GoalSetting_gestion[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_gestion[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_gestion[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_gestion[userId_log[i]])
    Elaboration_log.append(Elaboration_gestion[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_gestion[userId_log[i]])
    SRL_log.append(SRL_gestion[userId_log[i]])
    aprueba_log.append(aprueba_gestion[userId_log[i]])

    

dictLogSesionesSRL = {}
dictLogSesionesSRL['userId'] = userId_log
dictLogSesionesSRL['sesion'] = sesion_log
dictLogSesionesSRL['timestamp'] = timestamp_log
dictLogSesionesSRL['actividad'] = actividad_log
dictLogSesionesSRL['edu'] = edu_log
dictLogSesionesSRL['age'] = age_log
dictLogSesionesSRL['isfemale'] = isfemale_log
dictLogSesionesSRL['GoalSetting'] = GoalSetting_log
dictLogSesionesSRL['StrategicPlanning'] = StrategicPlanning_log
dictLogSesionesSRL['SelfEvaluation'] = SelfEvaluation_log
dictLogSesionesSRL['TaskStrategies']=TaskStrategies_log
dictLogSesionesSRL['Elaboration']= Elaboration_log
dictLogSesionesSRL['HelpSeeking']= HelpSeeking_log
dictLogSesionesSRL['SRL'] =SRL_log
dictLogSesionesSRL['aprueba'] =aprueba_log

logSesionesSRL_gestion = pd.DataFrame(dictLogSesionesSRL)
logSesionesSRL_gestion.to_csv('procesoSesionesSRL_gestion.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL','aprueba'])
