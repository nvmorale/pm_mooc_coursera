#load user list and fine grained activities

import pandas as pd

course_progress = pd.read_csv('course_progress.csv')
users = pd.read_csv('users.csv', usecols = ['ucchile_user_id','user_join_ts','country_cd'])

log_fg = course_progress.merge(users[['ucchile_user_id','country_cd']])

#%% convert dates to seconds since epoch

from datetime import datetime

ts_list = log_fg['course_progress_ts'].values.tolist()
ts_list_datetime = []

for i in range(len(ts_list)):
    try:
        ts_aux = datetime.strptime(ts_list[i], '%Y-%m-%d %H:%M:%S.%f')
    except:
        ts_aux = datetime.strptime(ts_list[i], '%Y-%m-%d %H:%M:%S')
    ts_list_datetime.append(int(ts_aux.timestamp()))
    
join_ts_list = users['user_join_ts'].values.tolist()
join_ts_list_datetime = []

for i in range(len(join_ts_list)):
    try:
        join_ts_aux = datetime.strptime(join_ts_list[i], '%Y-%m-%d %H:%M:%S.%f')
    except:
        join_ts_aux = datetime.strptime(join_ts_list[i], '%Y-%m-%d %H:%M:%S')
    join_ts_list_datetime.append(int(join_ts_aux.timestamp()))
    
dict_join_ts = dict(zip(users['ucchile_user_id'],join_ts_list_datetime))

#%% sort the log per user and timestamp

log_fg['course_progress_ts'] = ts_list_datetime

log_fg.sort(['ucchile_user_id','course_progress_ts'])

#%% calculate session number
import numpy as np

nSession = 1
tThreshold = 60*45

session = np.zeros(len(ts_list_datetime))
session[0] = 1

userId = log_fg['ucchile_user_id'].values.tolist()

for i in range(1,len(log_fg)):
    
    if(userId[i] == userId[i-1]):
        if(ts_list_datetime[i] - ts_list_datetime[i-1] < tThreshold):
            session[i] = nSession
        else:
            nSession += 1
            session[i] = nSession
    else:
        nSession = 1
        session[i] = nSession

log_fg['session'] = session

#%%

course_items = pd.read_csv('course_items.csv')
course_item_types = pd.read_csv('course_item_types.csv')
course_progress_state_types = pd.read_csv('course_progress_state_types.csv')


