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
items_aula = pd.read_csv('course_items_aula.csv')
lessons_aula = pd.read_csv('course_lessons_aula.csv')
modules_aula = pd.read_csv('course_modules_aula.csv', sep = ';')

item2lesson_aula = dict(zip(items_aula['course_item_id'],items_aula['course_lesson_id']))
lesson2mod_aula = dict(zip(lessons_aula['course_lesson_id'],lessons_aula['course_module_id']))
mod2num_aula =dict(zip(modules_aula['course_module_id'],modules_aula['course_module_order']))
lesson2num_aula = dict(zip(lessons_aula['course_lesson_id'],lessons_aula['course_lesson_order']))

#%%

notas_elec = pd.read_csv(path+'\electrones_en_accion\course_grades.csv')
notas_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_grades.csv')
notas_aula = pd.read_csv('course_grades_aula.csv')

user2nota_elec = dict(zip(notas_elec['ucchile_user_id'],notas_elec['course_passing_state_id']))
user2nota_gestion = dict(zip(notas_gestion['ucchile_user_id'],notas_gestion['course_passing_state_id']))
user2nota_aula = dict(zip(notas_aula['ucchile_user_id'],notas_aula['course_passing_state_id']))
#%%
datos_elec = datos.loc[datos['course'] == 'electrones_en_accion']
datos_gestion = datos.loc[datos['course'] == 'gestion_organizaciones_efectivas']
datos_aula = datos.loc[datos['course'] == 'aulaconstructivista']

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

GoalSetting_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['GoalSetting']))
StrategicPlanning_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['StrategicPlanning']))
SelfEvaluation_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['SelfEvaluation']))
TaskStrategies_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['TaskStrategies']))
Elaboration_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['Elaboration']))
HelpSeeking_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['HelpSeeking']))
SRL_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['SRL']))
edu_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['edu']))
age_aula = dict(zip(datos_aula['ucchile_user_id'],datos_aula['age']))
isfemale_aula =dict(zip(datos_aula['ucchile_user_id'],datos_aula['isfemale']))

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

GoalSetting_median_aula = np.median(list(GoalSetting_aula.values()))
StrategicPlanning_median_aula = np.median(list(StrategicPlanning_aula.values()))
SelfEvaluation_median_aula = np.median(list(SelfEvaluation_aula.values()))
TaskStrategies_median_aula = np.median(list(TaskStrategies_aula.values()))
Elaboration_median_aula = np.median(list(Elaboration_aula.values()))
HelpSeeking_median_aula = np.median(list(HelpSeeking_aula.values()))
SRL_median_aula = np.median(list(SRL_aula.values()))

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

GoalSetting_mean_aula = np.mean(list(GoalSetting_aula.values()))
StrategicPlanning_mean_aula = np.mean(list(StrategicPlanning_aula.values()))
SelfEvaluation_mean_aula = np.mean(list(SelfEvaluation_aula.values()))
TaskStrategies_mean_aula = np.mean(list(TaskStrategies_aula.values()))
Elaboration_mean_aula = np.mean(list(Elaboration_aula.values()))
HelpSeeking_mean_aula = np.mean(list(HelpSeeking_aula.values()))
SRL_mean_aula = np.mean(list(SRL_aula.values()))

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
index_aula = 3714

range_elec = range(index_elec+1,index_elec+len(datos_elec))
range_gestion = range(index_gestion+1,index_gestion+len(datos_gestion))
range_aula = range(index_aula+1,index_aula+len(datos_aula))

dictAprobacion = {0:0, 1:1, 2:1, 3:0}

aprobacion_elec = [dictAprobacion[user2nota_elec[datos_elec['ucchile_user_id'][index_elec]]]]
aprobacion_gestion = [dictAprobacion[user2nota_gestion[datos_gestion['ucchile_user_id'][index_gestion]]]]
aprobacion_aula = [dictAprobacion[user2nota_aula[datos_aula['ucchile_user_id'][index_aula]]]]

modulo_elec = [mod2num_elec[lesson2mod_elec[item2lesson_elec[datos_elec['course_item_id'][index_elec]]]]]
lesson_elec = [lesson2num_elec[item2lesson_elec[datos_elec['course_item_id'][index_elec]]]]

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



modulo_aula = [mod2num_aula[lesson2mod_aula[item2lesson_aula[datos_aula['course_item_id'][index_aula]]]]]
lesson_aula = [lesson2num_aula[item2lesson_aula[datos_aula['course_item_id'][index_aula]]]]

for i in range_aula:    
    modulo_aula.append(mod2num_aula[lesson2mod_aula[item2lesson_aula[datos_aula['course_item_id'][i]]]]+1)
    lesson_aula.append(lesson2num_aula[item2lesson_aula[datos_aula['course_item_id'][i]]]+1)
    aprobacion_aula.append(dictAprobacion[user2nota_aula[datos_aula['ucchile_user_id'][i]]])

datos_aula['modulo'] = modulo_aula
datos_aula['lesson'] = lesson_aula
datos_aula['aprueba'] = aprobacion_aula

aprueba_elec =dict(zip(datos_elec['ucchile_user_id'],datos_elec['aprueba']))
aprueba_gestion =dict(zip(datos_gestion['ucchile_user_id'],datos_gestion['aprueba']))
aprueba_aula =dict(zip(datos_aula['ucchile_user_id'],datos_aula['aprueba']))


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
actividad_log = ['begin session']
timestamp_log = [timestamp[0]-1]

contador_elec[itemId[0]] = 1

for i in range(1,len(datos_elec)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    aux = contador_elec[itemId[i]]
    contador_elec[itemId[i]] = aux + 1
    
    repeating = (contador_elec[itemId[i]] > 2) & (tipo[i] == 'lecture')
    studyingTactics = ((tipo[i-1] == 'lecture') & (tipo[i] == 'assessment'))|((tipo[i] == 'lecture') & (tipo[i-1] == 'assessment'))
    evaluation = actividad[i] == 'assessment.complete'
    reading = actividad[i] == 'lecture.complete'
    
    
    if(mismoUser & mismaSesion):
        if(repeating):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('repeating')
            timestamp_log.append(timestamp[i]+1)
        if(evaluation):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('evaluation')
            timestamp_log.append(timestamp[i])
        if(reading):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('reading')
            timestamp_log.append(timestamp[i])
        if(studyingTactics):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('studying tacticts')
            timestamp_log.append(timestamp[i]-1)
    else:       
        userId_log.append(userId[i-1])
        sesion_log.append(sesion[i-1])
        timestamp_log.append(timestamp[i-1]+duracion[i-1])
        actividad_log.append('end session')
        
        userId_log.append(userId[i])
        sesion_log.append(sesion[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('begin session')
    
    if(not mismoUser):
        contador_elec = dict(zip(items_elec['course_item_id'].values.tolist(),list(np.zeros(len(items_elec)))))
    
userId_log.append(userId[i])
sesion_log.append(sesion[i])
timestamp_log.append(timestamp[i]+duracion[i])
actividad_log.append('end session')
    
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

logSesionesSRL_elec['HighGoalSetting'] = logSesionesSRL_elec['GoalSetting'] >= GoalSetting_median_elec
logSesionesSRL_elec['HighStrategicPlanning'] = logSesionesSRL_elec['StrategicPlanning'] >= StrategicPlanning_median_elec
logSesionesSRL_elec['HighSelfEvaluation'] = logSesionesSRL_elec['SelfEvaluation'] >= SelfEvaluation_median_elec
logSesionesSRL_elec['HighTaskStrategies'] = logSesionesSRL_elec['TaskStrategies'] >= TaskStrategies_median_elec
logSesionesSRL_elec['HighElaboration'] = logSesionesSRL_elec['Elaboration'] >= Elaboration_median_elec
logSesionesSRL_elec['HighHelpSeeking'] = logSesionesSRL_elec['HelpSeeking'] >= HelpSeeking_median_elec
logSesionesSRL_elec['HighSRL'] = logSesionesSRL_elec['SRL'] >= SRL_median_elec

logSesionesSRL_elec.to_csv('procesoSesionesSRL_elec.csv', index = False)

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
actividad_log = ['begin session']
timestamp_log = [timestamp[0]-1]

contador_gestion[itemId[0]] = 1

for i in range(1,len(datos_gestion)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    aux = contador_gestion[itemId[i]]
    contador_gestion[itemId[i]] = aux + 1
    
    repeating = (contador_gestion[itemId[i]] > 2) & (tipo[i] == 'lecture')
    studyingTactics = ((tipo[i-1] == 'lecture') & (tipo[i] == 'assessment'))|((tipo[i] == 'lecture') & (tipo[i-1] == 'assessment'))
    evaluation = actividad[i] == 'assessment.complete'
    reading = actividad[i] == 'lecture.complete'
    
    
    if(mismoUser & mismaSesion):
        if(repeating):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('repeating')
            timestamp_log.append(timestamp[i]+1)
        if(evaluation):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('evaluation')
            timestamp_log.append(timestamp[i])
        if(reading):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('reading')
            timestamp_log.append(timestamp[i])
        if(studyingTactics):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('studying tacticts')
            timestamp_log.append(timestamp[i]-1)
    else:       
        userId_log.append(userId[i-1])
        sesion_log.append(sesion[i-1])
        timestamp_log.append(timestamp[i-1]+duracion[i-1])
        actividad_log.append('end session')
        
        userId_log.append(userId[i])
        sesion_log.append(sesion[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('begin session')
    
    if(not mismoUser):
        contador_gestion = dict(zip(items_gestion['course_item_id'].values.tolist(),list(np.zeros(len(items_gestion)))))
    
userId_log.append(userId[i])
sesion_log.append(sesion[i])
timestamp_log.append(timestamp[i]+duracion[i])
actividad_log.append('end session')
    
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

logSesionesSRL_gestion['HighGoalSetting'] = logSesionesSRL_gestion['GoalSetting'] >= GoalSetting_median_gestion
logSesionesSRL_gestion['HighStrategicPlanning'] = logSesionesSRL_gestion['StrategicPlanning'] >= StrategicPlanning_median_gestion
logSesionesSRL_gestion['HighSelfEvaluation'] = logSesionesSRL_gestion['SelfEvaluation'] >= SelfEvaluation_median_gestion
logSesionesSRL_gestion['HighTaskStrategies'] = logSesionesSRL_gestion['TaskStrategies'] >= TaskStrategies_median_gestion
logSesionesSRL_gestion['HighElaboration'] = logSesionesSRL_gestion['Elaboration'] >= Elaboration_median_gestion
logSesionesSRL_gestion['HighHelpSeeking'] = logSesionesSRL_gestion['HelpSeeking'] >= HelpSeeking_median_gestion
logSesionesSRL_gestion['HighSRL'] = logSesionesSRL_gestion['SRL'] >= SRL_median_gestion

logSesionesSRL_gestion.to_csv('procesoSesionesSRL_gestion.csv', index = False)


#%% generamos el log con transiciones de SRL para el curso de aula constructivista

userId = datos_aula['ucchile_user_id'].values.tolist()
sesion = datos_aula['sesion'].values.tolist()
actividad = datos_aula['type_status'].values.tolist()
timestamp = datos_aula['timestamp'].values.tolist()
duracion = datos_aula['duration'].values.tolist()
tipo = datos_aula['type'].values.tolist()
itemId = datos_aula['course_item_id'].values.tolist()

contador_aula = dict(zip(items_aula['course_item_id'].values.tolist(),list(np.zeros(len(items_aula)))))

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = ['begin session']
timestamp_log = [timestamp[0]-1]

contador_aula[itemId[0]] = 1

for i in range(1,len(datos_aula)):
    mismoUser = userId[i-1] == userId[i]
    mismaSesion = sesion[i-1] == sesion[i]
    
    aux = contador_aula[itemId[i]]
    contador_aula[itemId[i]] = aux + 1
    
    repeating = (contador_aula[itemId[i]] > 2) & (tipo[i] == 'lecture')
    studyingTactics = ((tipo[i-1] == 'lecture') & (tipo[i] == 'assessment'))|((tipo[i] == 'lecture') & (tipo[i-1] == 'assessment'))
    evaluation = actividad[i] == 'assessment.complete'
    reading = actividad[i] == 'lecture.complete'
    
    
    if(mismoUser & mismaSesion):
        if(repeating):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('repeating')
            timestamp_log.append(timestamp[i]+1)
        if(evaluation):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('evaluation')
            timestamp_log.append(timestamp[i])
        if(reading):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('reading')
            timestamp_log.append(timestamp[i])
        if(studyingTactics):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            actividad_log.append('studying tacticts')
            timestamp_log.append(timestamp[i]-1)
    else:       
        userId_log.append(userId[i-1])
        sesion_log.append(sesion[i-1])
        timestamp_log.append(timestamp[i-1]+duracion[i-1])
        actividad_log.append('end session')
        
        userId_log.append(userId[i])
        sesion_log.append(sesion[i])
        timestamp_log.append(timestamp[i])
        actividad_log.append('begin session')
    
    if(not mismoUser):
        contador_aula = dict(zip(items_aula['course_item_id'].values.tolist(),list(np.zeros(len(items_aula)))))
    
userId_log.append(userId[i])
sesion_log.append(sesion[i])
timestamp_log.append(timestamp[i]+duracion[i])
actividad_log.append('end session')
    
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
    edu_log.append(edu_aula[userId_log[i]])
    age_log.append(age_aula[userId_log[i]])
    isfemale_log.append(isfemale_aula[userId_log[i]])
    GoalSetting_log.append(GoalSetting_aula[userId_log[i]])
    StrategicPlanning_log.append(StrategicPlanning_aula[userId_log[i]])
    SelfEvaluation_log.append(SelfEvaluation_aula[userId_log[i]])
    TaskStrategies_log.append(TaskStrategies_aula[userId_log[i]])
    Elaboration_log.append(Elaboration_aula[userId_log[i]])
    HelpSeeking_log.append(HelpSeeking_aula[userId_log[i]])
    SRL_log.append(SRL_aula[userId_log[i]])
    aprueba_log.append(aprueba_aula[userId_log[i]])
    

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

logSesionesSRL_aula = pd.DataFrame(dictLogSesionesSRL)

logSesionesSRL_aula['HighGoalSetting'] = logSesionesSRL_aula['GoalSetting'] >= GoalSetting_median_aula
logSesionesSRL_aula['HighStrategicPlanning'] = logSesionesSRL_aula['StrategicPlanning'] >= StrategicPlanning_median_aula
logSesionesSRL_aula['HighSelfEvaluation'] = logSesionesSRL_aula['SelfEvaluation'] >= SelfEvaluation_median_aula
logSesionesSRL_aula['HighTaskStrategies'] = logSesionesSRL_aula['TaskStrategies'] >= TaskStrategies_median_aula
logSesionesSRL_aula['HighElaboration'] = logSesionesSRL_aula['Elaboration'] >= Elaboration_median_aula
logSesionesSRL_aula['HighHelpSeeking'] = logSesionesSRL_aula['HelpSeeking'] >= HelpSeeking_median_aula
logSesionesSRL_aula['HighSRL'] = logSesionesSRL_aula['SRL'] >= SRL_median_aula

logSesionesSRL_aula.to_csv('procesoSesionesSRL_aula.csv', index = False)



#%%

logSesionesSRL_todo = pd.concat([logSesionesSRL_aula,logSesionesSRL_gestion,logSesionesSRL_elec], ignore_index = True)

logSesionesSRL_todo.to_csv('procesoSesionesSRL.csv', index = False)