import pandas as pd
import numpy as np

log = pd.read_csv('procesoSesionesSRL4.csv')

#%%

isFemale = dict(zip(log['userId'],log['isfemale']))
age = dict(zip(log['userId'],log['age']))
edu = dict(zip(log['userId'],log['edu']))
SRL = dict(zip(log['userId'],log['SRL']))
aprueba = dict(zip(log['userId'],log['aprueba']))
curso = dict(zip(log['userId'],log['curso']))

#%%
#import os
#path = os.path.abspath(os.path.dirname('proceso.xslx'))

users_gestion = pd.read_csv('users_gestion.csv')
users_elec = pd.read_csv('users_elec.csv')
users_aula = pd.read_csv('users_aula.csv')

users = pd.concat([users_gestion, users_elec, users_aula])

pais = dict(zip(users['ucchile_user_id'],users['country_cd']))

#%%

user_list = list(age.keys())
curso_list = []
aprueba_list = []
SRL_list = []
age_list = []
edu_list = []
pais_list = []
isFemale_list = []
nSesiones = []
nRepeatL = []
nRepeatA = []
nAssess = []
nLecture = []
nPerform = []

for i in range(len(user_list)):
     
    user = user_list[i]
    curso_list.append(curso[user])
    aprueba_list.append(aprueba[user])
    SRL_list.append(SRL[user])
    age_list.append(age[user])
    edu_list.append(edu[user])
    pais_list.append(pais[user])
    isFemale_list.append(isFemale[user])
    
    aux = log[log['userId'] == user]
    nSesiones.append(max(aux['sesion']))
    nRepeatL.append(sum(aux['actividad'] == 'REPEAT L'))
    nRepeatA.append(sum(aux['actividad'] == 'REPEAT A'))
    nAssess.append(sum(aux['actividad'] == 'ASSESS'))
    nLecture.append(sum(aux['actividad'] == 'LECTURE'))
    nPerform.append(sum(aux['actividad'] == 'PERFORM'))

#%%    
    
dictRegistroUsuarios = {}
dictRegistroUsuarios['userId'] = user_list
dictRegistroUsuarios['curso'] = curso_list
dictRegistroUsuarios['aprueba'] = aprueba_list
dictRegistroUsuarios['SRL'] = SRL_list 
dictRegistroUsuarios['edad'] = age_list
dictRegistroUsuarios['edu'] = edu_list
dictRegistroUsuarios['pais'] = pais_list
dictRegistroUsuarios['isF'] = isFemale_list
dictRegistroUsuarios['nSesiones'] = nSesiones
dictRegistroUsuarios['nRepeatL'] = nRepeatL
dictRegistroUsuarios['nRepeatA'] = nRepeatA
dictRegistroUsuarios['nAssess'] = nAssess
dictRegistroUsuarios['nLecture'] = nLecture
dictRegistroUsuarios['nPerform'] = nPerform

cols = ['userId','curso','aprueba','SRL','edad','edu','pais','isF','nSesiones','nRepeatL','nRepeatA','nAssess','nLecture','nPerform']
    
registroUsuarios = pd.DataFrame(dictRegistroUsuarios)
registroUsuarios.to_excel('registroEstudiantes.xlsx', index = False, columns = cols)