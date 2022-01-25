import json, os
import random
from datetime import datetime, timedelta


def do_users():

    noms = ["valentin", "pauline", "clementine","lucas","denis","annie"]
    prenoms = ["Andersen", "Alighieri", "Austen","Beckett","Boccaccio","Borges"]
    email=["valentin.andersen@gmail.com", "pauline.alighieri@gmail.com", "clementine.austen@gmail.com","lucas.beckett@gmail.com","denis.boccaccio@gmail.com","annie.borges@gmail.com"]
    adresses=["9640 denny street","4266 cork street","4290 lovers ln","4605 st. john road","7013 36th ave","8151 necatibey cd"]
    villes=["Marseille","Rennes","Paris","Lyon","Strasbourg","Brest"]
    cp=["13000","35000","75000","69000","67000","29000"]
    roles = ["admin", "user", "user","user","user","user"]
    datas = []
   
    i = 0
    for n in noms:
        d = {}
        d['id']= i+1
        d['nom']= n
        d['prenom']= prenoms[i]
        d['email']= email[i]
        d['adresse']= adresses[i]
        d['ville']= villes[i]
        d['cp']= cp[i]
        d['role']= roles[i]

        pwd= cp[i][:2] + villes[i][:2].lower()

        d['passwd']= pwd
        datas.append(d)

        i=i+1

 
    with open( "users.json" , 'w') as outfile:
        json.dump(datas, outfile)   

def do_activities():

    activities = ["run", "bike", "swim"]
    desc =["","recuperation" ,"endurance" ,"intensif" ]
    dist={
         'bike' : ["25", "50", "75","100"],
         'run' : ["5", "10", "15","20"],
         'swim' : ["250","500", "1000", "5000"],
    }

    datas = []
   
    i = 0
    while i < 4000:
        start = datetime.now()
        end = start - timedelta(days=300)
        #random_date = start + (end - start) * random.random()
        random_date = start + timedelta(seconds= int((end - start).total_seconds() * random.random()))

        d = {}
        d['id_user']= random.randint(1,6)
        act =  activities[ random.randint(0,2) ]
        d['type']= act.upper()
        tmp = dist[act]
        d['dist']= tmp[  random.randint(0,3) ]
        d['desc']=  desc[ random.randint(0,3) ]

        d['date'] = random_date.strftime("%Y-%m-%d %H:%M:%S")

        datas.append(d)

        i=i+1

    #print( datas )
    with open('activities.json', 'w') as outfile:
        json.dump(datas, outfile) 



do_users()
do_activities()