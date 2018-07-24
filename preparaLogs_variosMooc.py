import pandas as pd

datos = pd.read_excel("proceso.xlsx")

#%%
import numpy as np

nSesion = 1
tUmbral = 60*45

sesion = np.zeros(len(datos))
sesion[0] = 1

#userID = datosWeb['ucchile_user_id']
#timestamp = datosWeb['timestamp']
#duration = datosWeb['duration']

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

#%%
import os
path = os.path.abspath(os.path.dirname('proceso.xslx'))


items_web = pd.read_csv(path+'\web_semantica\course_items.csv')
lessons_web = pd.read_csv(path+'\web_semantica\course_lessons.csv')
modules_web = pd.read_csv(path+'\web_semantica\course_modules.csv')

item2lesson_web = dict(zip(items_web['course_item_id'],items_web['course_lesson_id']))
lesson2mod_web = dict(zip(lessons_web['course_lesson_id'],lessons_web['course_module_id']))
mod2num_web =dict(zip(modules_web['course_module_id'],modules_web['course_module_order']))


items_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_items.csv')
lessons_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_lessons.csv')
modules_gestion = pd.read_csv(path+'\gestion_organizaciones_efectivas\course_modules.csv')

item2lesson_gestion = dict(zip(items_gestion['course_item_id'],items_gestion['course_lesson_id']))
lesson2mod_gestion = dict(zip(lessons_gestion['course_lesson_id'],lessons_gestion['course_module_id']))
mod2num_gestion = dict(zip(modules_gestion['course_module_id'],modules_gestion['course_module_order']))


items_elec = pd.read_csv(path+'\electrones_en_accion\course_items.csv')
lessons_elec = pd.read_csv(path+'\electrones_en_accion\course_lessons.csv')
modules_elec = pd.read_csv(path+'\electrones_en_accion\course_modules.csv')

item2lesson_elec = dict(zip(items_elec['course_item_id'],items_elec['course_lesson_id']))
lesson2mod_elec = dict(zip(lessons_elec['course_lesson_id'],lessons_elec['course_module_id']))
mod2num_elec =dict(zip(modules_elec['course_module_id'],modules_elec['course_module_order']))


items_sv = pd.read_csv(path+'\decodificando_silicon_valley\course_items.csv')
lessons_sv = pd.read_csv(path+'\decodificando_silicon_valley\course_lessons.csv')
modules_sv = pd.read_csv(path+'\decodificando_silicon_valley\course_modules.csv')

item2lesson_sv = dict(zip(items_sv['course_item_id'],items_sv['course_lesson_id']))
lesson2mod_sv = dict(zip(lessons_sv['course_lesson_id'],lessons_sv['course_module_id']))
mod2num_sv =dict(zip(modules_sv['course_module_id'],modules_sv['course_module_order']))


items_transporte = pd.read_csv('course_items_transporte.csv')
lessons_transporte = pd.read_csv('course_lessons_transporte.csv')
modules_transporte = pd.read_csv('course_modules_transporte.csv')

item2lesson_transporte = dict(zip(items_transporte['course_item_id'],items_transporte['course_lesson_id']))
lesson2mod_transporte = dict(zip(lessons_transporte['course_lesson_id'],lessons_transporte['course_module_id']))
mod2num_transporte =dict(zip(modules_transporte['course_module_id'],modules_transporte['course_module_order']))


items_aula = pd.read_csv('course_items_aula.csv')
lessons_aula = pd.read_csv('course_lessons_aula.csv')
modules_aula = pd.read_csv('course_modules_aula.csv', sep = ';')

item2lesson_aula = dict(zip(items_aula['course_item_id'],items_aula['course_lesson_id']))
lesson2mod_aula = dict(zip(lessons_aula['course_lesson_id'],lessons_aula['course_module_id']))
mod2num_aula = dict(zip(modules_aula['course_module_id'],modules_aula['course_module_order']))

#%%
datos_web = datos.loc[datos['course'] == 'web_semantica']
datos_gestion = datos.loc[datos['course'] == 'gestion_organizaciones_efectivas']
datos_aula = datos.loc[datos['course'] == 'aulaconstructivista']
datos_sv = datos.loc[datos['course'] == 'decodificando_silicon_valley']
datos_elec = datos.loc[datos['course'] == 'electrones_en_accion']
datos_transporte = datos.loc[datos['course'] == 'analisis_sistemas_de_transporte']

index_web = 78104
index_elec = 19750
index_gestion = 64786
index_sv = 14492
index_aula = 3714
index_transporte = 1

range_web = range(index_web+1,index_web+len(datos_web))
range_elec = range(index_elec+1,index_elec+len(datos_elec))
range_gestion = range(index_gestion+1,index_gestion+len(datos_gestion))
range_sv = range(index_sv+1,index_sv+len(datos_sv))
range_aula = range(index_aula+1,index_aula+len(datos_aula))
range_transporte = range(index_transporte+1,index_transporte+len(datos_transporte))

modulo_web = [mod2num_web[lesson2mod_web[item2lesson_web[datos_web['course_item_id'][index_web]]]]]

for i in range_web:    
    modulo_web.append(mod2num_web[lesson2mod_web[item2lesson_web[datos_web['course_item_id'][i]]]])


datos_web['modulo'] = modulo_web

modulo_elec = [mod2num_elec[lesson2mod_elec[item2lesson_elec[datos_elec['course_item_id'][index_elec]]]]]

for i in range_elec:    
    modulo_elec.append(mod2num_elec[lesson2mod_elec[item2lesson_elec[datos_elec['course_item_id'][i]]]])


datos_elec['modulo'] = modulo_elec

modulo_gestion = [mod2num_gestion[lesson2mod_gestion[item2lesson_gestion[datos_gestion['course_item_id'][index_gestion]]]]]

for i in range_gestion:    
    modulo_gestion.append(mod2num_gestion[lesson2mod_gestion[item2lesson_gestion[datos_gestion['course_item_id'][i]]]])


datos_gestion['modulo'] = modulo_gestion

modulo_sv = [mod2num_sv[lesson2mod_sv[item2lesson_sv[datos_sv['course_item_id'][index_sv]]]]]

for i in range_sv:    
    modulo_sv.append(mod2num_sv[lesson2mod_sv[item2lesson_sv[datos_sv['course_item_id'][i]]]])


datos_sv['modulo'] = modulo_sv

modulo_aula = [mod2num_aula[lesson2mod_aula[item2lesson_aula[datos_aula['course_item_id'][index_aula]]]]]

for i in range_aula:    
    modulo_aula.append(mod2num_aula[lesson2mod_aula[item2lesson_aula[datos_aula['course_item_id'][i]]]])


datos_aula['modulo'] = modulo_aula

modulo_transporte = [mod2num_transporte[lesson2mod_transporte[item2lesson_transporte[datos_transporte['course_item_id'][index_transporte]]]]]

for i in range_transporte:    
    modulo_transporte.append(mod2num_transporte[lesson2mod_transporte[item2lesson_transporte[datos_transporte['course_item_id'][i]]]])


datos_transporte['modulo'] = modulo_transporte

#%% generamos el log por sesiones para el curso de web semantica

userId = datos_web['ucchile_user_id'].values.tolist()
sesion = datos_web['sesion'].values.tolist()
actividad = datos_web['type_status'].values.tolist()
timestamp = datos_web['timestamp'].values.tolist()
duracion = datos_web['duration'].values.tolist()
modulo = datos_web['modulo'].values.tolist()
edu = datos_web['edu'].values.tolist()
age = datos_web['age'].values.tolist()
isfemale = datos_web['isfemale'].values.tolist()
GoalSetting = datos_web['GoalSetting'].values.tolist()
StrategicPlanning = datos_web['StrategicPlanning'].values.tolist()
SelfEvaluation = datos_web['SelfEvaluation'].values.tolist()
TaskStrategies = datos_web['TaskStrategies'].values.tolist()
Elaboration = datos_web['Elaboration'].values.tolist()
HelpSeeking = datos_web['HelpSeeking'].values.tolist()
SRL = datos_web['SRL'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
edu_log = [edu[0]]
age_log = [age[0]]
isfemale_log = [isfemale[0]]
GoalSetting_log = [GoalSetting[0]]
StrategicPlanning_log = [StrategicPlanning[0]]
SelfEvaluation_log = [SelfEvaluation[0]]
TaskStrategies_log = [TaskStrategies[0]]
Elaboration_log = [Elaboration[0]]
HelpSeeking_log = [HelpSeeking[0]]
SRL_log = [SRL[0]]



for i in range(1,len(datos_web)):
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
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
        
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    edu_log.append(edu[i])
    age_log.append(age[i])
    isfemale_log.append(isfemale[i])
    GoalSetting_log.append(GoalSetting[i])
    StrategicPlanning_log.append(StrategicPlanning[i])
    SelfEvaluation_log.append(SelfEvaluation[i])
    TaskStrategies_log.append(TaskStrategies[i])
    Elaboration_log.append(Elaboration[i])
    HelpSeeking_log.append(HelpSeeking[i])
    SRL_log.append(SRL[i])


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

logSesiones_web = pd.DataFrame(dictLogSesiones)
logSesiones_web.to_csv('procesoSesiones_web.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'])

#%% generamos el log por sesiones para el curso de electrones en accion

userId = datos_elec['ucchile_user_id'].values.tolist()
sesion = datos_elec['sesion'].values.tolist()
actividad = datos_elec['type_status'].values.tolist()
timestamp = datos_elec['timestamp'].values.tolist()
duracion = datos_elec['duration'].values.tolist()
modulo = datos_elec['modulo'].values.tolist()
edu = datos_elec['edu'].values.tolist()
age = datos_elec['age'].values.tolist()
isfemale = datos_elec['isfemale'].values.tolist()
GoalSetting = datos_elec['GoalSetting'].values.tolist()
StrategicPlanning = datos_elec['StrategicPlanning'].values.tolist()
SelfEvaluation = datos_elec['SelfEvaluation'].values.tolist()
TaskStrategies = datos_elec['TaskStrategies'].values.tolist()
Elaboration = datos_elec['Elaboration'].values.tolist()
HelpSeeking = datos_elec['HelpSeeking'].values.tolist()
SRL = datos_elec['SRL'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
edu_log = [edu[0]]
age_log = [age[0]]
isfemale_log = [isfemale[0]]
GoalSetting_log = [GoalSetting[0]]
StrategicPlanning_log = [StrategicPlanning[0]]
SelfEvaluation_log = [SelfEvaluation[0]]
TaskStrategies_log = [TaskStrategies[0]]
Elaboration_log = [Elaboration[0]]
HelpSeeking_log = [HelpSeeking[0]]
SRL_log = [SRL[0]]



for i in range(1,len(datos_elec)):
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
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
        
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    edu_log.append(edu[i])
    age_log.append(age[i])
    isfemale_log.append(isfemale[i])
    GoalSetting_log.append(GoalSetting[i])
    StrategicPlanning_log.append(StrategicPlanning[i])
    SelfEvaluation_log.append(SelfEvaluation[i])
    TaskStrategies_log.append(TaskStrategies[i])
    Elaboration_log.append(Elaboration[i])
    HelpSeeking_log.append(HelpSeeking[i])
    SRL_log.append(SRL[i])


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

logSesiones_elec = pd.DataFrame(dictLogSesiones)
logSesiones_elec.to_csv('procesoSesiones_elec.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'])

#%% generamos el log por sesiones para el curso de gestion de organizaciones

userId = datos_gestion['ucchile_user_id'].values.tolist()
sesion = datos_gestion['sesion'].values.tolist()
actividad = datos_gestion['type_status'].values.tolist()
timestamp = datos_gestion['timestamp'].values.tolist()
duracion = datos_gestion['duration'].values.tolist()
modulo = datos_gestion['modulo'].values.tolist()
edu = datos_gestion['edu'].values.tolist()
age = datos_gestion['age'].values.tolist()
isfemale = datos_gestion['isfemale'].values.tolist()
GoalSetting = datos_gestion['GoalSetting'].values.tolist()
StrategicPlanning = datos_gestion['StrategicPlanning'].values.tolist()
SelfEvaluation = datos_gestion['SelfEvaluation'].values.tolist()
TaskStrategies = datos_gestion['TaskStrategies'].values.tolist()
Elaboration = datos_gestion['Elaboration'].values.tolist()
HelpSeeking = datos_gestion['HelpSeeking'].values.tolist()
SRL = datos_gestion['SRL'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
edu_log = [edu[0]]
age_log = [age[0]]
isfemale_log = [isfemale[0]]
GoalSetting_log = [GoalSetting[0]]
StrategicPlanning_log = [StrategicPlanning[0]]
SelfEvaluation_log = [SelfEvaluation[0]]
TaskStrategies_log = [TaskStrategies[0]]
Elaboration_log = [Elaboration[0]]
HelpSeeking_log = [HelpSeeking[0]]
SRL_log = [SRL[0]]



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
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
        
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    edu_log.append(edu[i])
    age_log.append(age[i])
    isfemale_log.append(isfemale[i])
    GoalSetting_log.append(GoalSetting[i])
    StrategicPlanning_log.append(StrategicPlanning[i])
    SelfEvaluation_log.append(SelfEvaluation[i])
    TaskStrategies_log.append(TaskStrategies[i])
    Elaboration_log.append(Elaboration[i])
    HelpSeeking_log.append(HelpSeeking[i])
    SRL_log.append(SRL[i])


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

logSesiones_gestion = pd.DataFrame(dictLogSesiones)
logSesiones_gestion.to_csv('procesoSesiones_gestion.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'])

#%% generamos el log por sesiones para el curso de aula constructivista

userId = datos_aula['ucchile_user_id'].values.tolist()
sesion = datos_aula['sesion'].values.tolist()
actividad = datos_aula['type_status'].values.tolist()
timestamp = datos_aula['timestamp'].values.tolist()
duracion = datos_aula['duration'].values.tolist()
modulo = datos_aula['modulo'].values.tolist()
edu = datos_aula['edu'].values.tolist()
age = datos_aula['age'].values.tolist()
isfemale = datos_aula['isfemale'].values.tolist()
GoalSetting = datos_aula['GoalSetting'].values.tolist()
StrategicPlanning = datos_aula['StrategicPlanning'].values.tolist()
SelfEvaluation = datos_aula['SelfEvaluation'].values.tolist()
TaskStrategies = datos_aula['TaskStrategies'].values.tolist()
Elaboration = datos_aula['Elaboration'].values.tolist()
HelpSeeking = datos_aula['HelpSeeking'].values.tolist()
SRL = datos_aula['SRL'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
edu_log = [edu[0]]
age_log = [age[0]]
isfemale_log = [isfemale[0]]
GoalSetting_log = [GoalSetting[0]]
StrategicPlanning_log = [StrategicPlanning[0]]
SelfEvaluation_log = [SelfEvaluation[0]]
TaskStrategies_log = [TaskStrategies[0]]
Elaboration_log = [Elaboration[0]]
HelpSeeking_log = [HelpSeeking[0]]
SRL_log = [SRL[0]]



for i in range(1,len(datos_aula)):
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
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
        
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    edu_log.append(edu[i])
    age_log.append(age[i])
    isfemale_log.append(isfemale[i])
    GoalSetting_log.append(GoalSetting[i])
    StrategicPlanning_log.append(StrategicPlanning[i])
    SelfEvaluation_log.append(SelfEvaluation[i])
    TaskStrategies_log.append(TaskStrategies[i])
    Elaboration_log.append(Elaboration[i])
    HelpSeeking_log.append(HelpSeeking[i])
    SRL_log.append(SRL[i])


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

logSesiones_aula = pd.DataFrame(dictLogSesiones)
logSesiones_aula.to_csv('procesoSesiones_aula.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'])

#%% generamos el log por sesiones para el curso de silicon valley

userId = datos_sv['ucchile_user_id'].values.tolist()
sesion = datos_sv['sesion'].values.tolist()
actividad = datos_sv['type_status'].values.tolist()
timestamp = datos_sv['timestamp'].values.tolist()
duracion = datos_sv['duration'].values.tolist()
modulo = datos_sv['modulo'].values.tolist()
edu = datos_sv['edu'].values.tolist()
age = datos_sv['age'].values.tolist()
isfemale = datos_sv['isfemale'].values.tolist()
GoalSetting = datos_sv['GoalSetting'].values.tolist()
StrategicPlanning = datos_sv['StrategicPlanning'].values.tolist()
SelfEvaluation = datos_sv['SelfEvaluation'].values.tolist()
TaskStrategies = datos_sv['TaskStrategies'].values.tolist()
Elaboration = datos_sv['Elaboration'].values.tolist()
HelpSeeking = datos_sv['HelpSeeking'].values.tolist()
SRL = datos_sv['SRL'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
edu_log = [edu[0]]
age_log = [age[0]]
isfemale_log = [isfemale[0]]
GoalSetting_log = [GoalSetting[0]]
StrategicPlanning_log = [StrategicPlanning[0]]
SelfEvaluation_log = [SelfEvaluation[0]]
TaskStrategies_log = [TaskStrategies[0]]
Elaboration_log = [Elaboration[0]]
HelpSeeking_log = [HelpSeeking[0]]
SRL_log = [SRL[0]]



for i in range(1,len(datos_sv)):
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
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
        
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    edu_log.append(edu[i])
    age_log.append(age[i])
    isfemale_log.append(isfemale[i])
    GoalSetting_log.append(GoalSetting[i])
    StrategicPlanning_log.append(StrategicPlanning[i])
    SelfEvaluation_log.append(SelfEvaluation[i])
    TaskStrategies_log.append(TaskStrategies[i])
    Elaboration_log.append(Elaboration[i])
    HelpSeeking_log.append(HelpSeeking[i])
    SRL_log.append(SRL[i])


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

logSesiones_sv = pd.DataFrame(dictLogSesiones)
logSesiones_sv.to_csv('procesoSesiones_sv.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'])

#%% generamos el log por sesiones para el curso de transporte

userId = datos_transporte['ucchile_user_id'].values.tolist()
sesion = datos_transporte['sesion'].values.tolist()
actividad = datos_transporte['type_status'].values.tolist()
timestamp = datos_transporte['timestamp'].values.tolist()
duracion = datos_transporte['duration'].values.tolist()
modulo = datos_transporte['modulo'].values.tolist()
edu = datos_transporte['edu'].values.tolist()
age = datos_transporte['age'].values.tolist()
isfemale = datos_transporte['isfemale'].values.tolist()
GoalSetting = datos_transporte['GoalSetting'].values.tolist()
StrategicPlanning = datos_transporte['StrategicPlanning'].values.tolist()
SelfEvaluation = datos_transporte['SelfEvaluation'].values.tolist()
TaskStrategies = datos_transporte['TaskStrategies'].values.tolist()
Elaboration = datos_transporte['Elaboration'].values.tolist()
HelpSeeking = datos_transporte['HelpSeeking'].values.tolist()
SRL = datos_transporte['SRL'].values.tolist()

userId_log = [userId[0]]
sesion_log = [sesion[0]]
actividad_log = [actividad[0]]
timestamp_log = [timestamp[0]]
modulo_log = [modulo[0]]
edu_log = [edu[0]]
age_log = [age[0]]
isfemale_log = [isfemale[0]]
GoalSetting_log = [GoalSetting[0]]
StrategicPlanning_log = [StrategicPlanning[0]]
SelfEvaluation_log = [SelfEvaluation[0]]
TaskStrategies_log = [TaskStrategies[0]]
Elaboration_log = [Elaboration[0]]
HelpSeeking_log = [HelpSeeking[0]]
SRL_log = [SRL[0]]



for i in range(1,len(datos_transporte)):
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
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
        
        if(retrocedeModulo):
            userId_log.append(userId[i])
            sesion_log.append(sesion[i])
            modulo_log.append(modulo[i])
            timestamp_log.append(timestamp[i]-1)
            actividad_log.append('retrocedeModulo')
            edu_log.append(edu[i])
            age_log.append(age[i])
            isfemale_log.append(isfemale[i])
            GoalSetting_log.append(GoalSetting[i])
            StrategicPlanning_log.append(StrategicPlanning[i])
            SelfEvaluation_log.append(SelfEvaluation[i])
            TaskStrategies_log.append(TaskStrategies[i])
            Elaboration_log.append(Elaboration[i])
            HelpSeeking_log.append(HelpSeeking[i])
            SRL_log.append(SRL[i])
    
    userId_log.append(userId[i])
    sesion_log.append(sesion[i])
    modulo_log.append(modulo[i])
    timestamp_log.append(timestamp[i])
    actividad_log.append(actividad[i])
    edu_log.append(edu[i])
    age_log.append(age[i])
    isfemale_log.append(isfemale[i])
    GoalSetting_log.append(GoalSetting[i])
    StrategicPlanning_log.append(StrategicPlanning[i])
    SelfEvaluation_log.append(SelfEvaluation[i])
    TaskStrategies_log.append(TaskStrategies[i])
    Elaboration_log.append(Elaboration[i])
    HelpSeeking_log.append(HelpSeeking[i])
    SRL_log.append(SRL[i])


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

logSesiones_transporte = pd.DataFrame(dictLogSesiones)
logSesiones_transporte.to_csv('procesoSesiones_transporte.csv', index = False, columns = ['userId', 'sesion', 'timestamp', 'actividad', 'modulo','edu','age','isfemale','GoalSetting','StrategicPlanning','SelfEvaluation','TaskStrategies','Elaboration','HelpSeeking','SRL'])

#%%