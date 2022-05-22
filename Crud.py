from tkinter import *
import pymysql


def createdb():
    global Id,companyName,location,datum,rocketName,rocketStatus,cost,missionStatus
    getCompanyName = companyName.get()
    getLocation = location.get()
    getdatum = datum.get()
    getrocketName = rocketName.get()
    getrocketStatus = rocketStatus.get()
    getcost = cost.get()
    getmissionStatus = missionStatus.get()
            # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sqlu = 'SELECT id FROM `space_corrected` ORDER BY id DESC LIMIT 0, 1'
            print(sqlu)
            # Exécutez la requête (Execute Query).
            cursor.execute(sqlu)
            connection.commit()
            for row in cursor:
                Id=row['id']
            id=Id + 1
    finally:
        # Closez la connexion (Close connection).      
        connection.close()

    # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    print ( "connexion réussie !")
 
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sql = 'Insert into space_corrected (id, companyName, location,datum,rocketName,rocketStatus,cost,missionStatus) values ("'+str(id)+'","'+getCompanyName+'","'+getLocation+'","'+getdatum+'","'+getrocketName+'","'+getrocketStatus+'","'+getcost+'","'+getmissionStatus+'") '
            
            # Exécutez la requête (Execute Query).
            cursor.execute(sql)
            connection.commit()
            print ("cursor.description:  ", cursor.description)
 
            print("Les données ont bien été sauvegardées !")
 
            for row in cursor:
                print(row)
             
    finally:
        # Closez la connexion (Close connection).      
        connection.close()

def supUser():
    getrocketName = rocketName.get()
    
    # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
 
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sql = 'DELETE from space_corrected where rocketName ="'+getrocketName+'"'
            
            # Exécutez la requête (Execute Query).
            cursor.execute(sql)
            connection.commit()
            print ("cursor.description:  ", cursor.description)
 
            print("Les données ont bien été sauvegardées !")
 
            for row in cursor:
                print(row)
             
    finally:
        # Closez la connexion (Close connection).      
        connection.close()


def updateDb():
    global companyName,location,datum,rocketName,rocketStatus,cost,missionStatus
    getCompanyName = companyName.get()
    getLocation = location.get()
    getdatum = datum.get()
    getrocketName = rocketName.get()
    getrocketStatus = rocketStatus.get()
    getcost = cost.get()
    getmissionStatus = missionStatus.get()
    # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    print ("connect successful!!")
 
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sql = 'update space_corrected (companyName,location,datum,rocketName,rocketStatus,cost,missionStatus) values ("'+getCompanyName+'","'+getLocation+'","'+getdatum+'","'+getrocketName+'","'+getrocketStatus+'","'+getcost+'","'+getmissionStatus+'") '
            print(sql)
            # Exécutez la requête (Execute Query).
            cursor.execute(sql)
            connection.commit()
            print ("cursor.description:  ", cursor.description)
 
            print("Les données ont bien été sauvegardées !")
 
            for row in cursor:
                print(row)
             
    finally:
        # Closez la connexion (Close connection).      
        connection.close()
def readDb() :
    # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
 
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sql = 'select * From space_corrected'
            
            # Exécutez la requête (Execute Query).
            cursor.execute(sql)
            while True:
                record=cursor.fetchone()
                if record==None:
                    break
                print (record,'\n')
             
    finally:
        # Closez la connexion (Close connection).      
        connection.close()

def readupDb1() :
    getrocketName = rocketName.get()
    # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    print ("readupDB1!!")
 
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sqlr = 'select companyName,location,datum,rocketName,rocketStatus,cost,missionStatus From space_corrected where rocketName = "'+getrocketName+'"'
            
            # Exécutez la requête (Execute Query).
            cursor.execute(sqlr)
            for row in cursor:
                print(row)
            Modifier2()
             
    finally:
        # Closez la connexion (Close connection).      
        connection.close()

def readupDb2() :
    getrocketName = rocketName.get()
    radiochange = v0.get()
    changeval = chg.get()
    # Connectez- vous à la base de données.
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='admin',                             
                             db='space',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
 
    print ("readupDB2!!")
    print(radiochange)
    try:
  
 
        with connection.cursor() as cursor:
       
            # SQL 
            sqlu = 'update space_corrected set '+radiochange +' = "'+changeval+'" where rocketName = "'+getrocketName+'" '
            print(sqlu)
            # Exécutez la requête (Execute Query).
            cursor.execute(sqlu)
            connection.commit()
            for row in cursor:
                print(row)
            
             
    finally:
        # Closez la connexion (Close connection).      
        connection.close()

def Creer() :
    
    global companyName,location,datum,rocketName,rocketStatus,cost,missionStatus

    window=Tk()
    
    
    lblID=Label(window, text="ID", fg='black', font=("Helvetica", 12))
    lblID.place(x=60, y=40)
    ID = str(id)


    lblnom=Label(window, text="companyName", fg='black', font=("Helvetica", 12))
    lblnom.place(x=60, y=40)
    companyName = Entry(window, text="Saisissez votre companyName", bd=5)
    companyName.place(x=150, y=40)

    lbllocation=Label(window, text="location", fg='black', font=("Helvetica", 12))
    lbllocation.place(x=60, y=80)
    location=Entry(window, text="Saisissez votre location", bd=5)
    location.place(x=150, y=80)

    lbldatum=Label(window, text="datum", fg='black', font=("Helvetica", 12))
    lbldatum.place(x=60, y=120)
    datum=Entry(window, text="Saisissez votre datum", bd=5)
    datum.place(x=150, y=120)

    lblrocketName=Label(window, text="rocketName", fg='black', font=("Helvetica", 12))
    lblrocketName.place(x=60, y=160)
    rocketName=Entry(window, text="Saisissez votre rocketName", bd=5)
    rocketName.place(x=150, y=160)

    lblrocketStatus=Label(window, text="rocketStatus", fg='black', font=("Helvetica", 12))
    lblrocketStatus.place(x=60, y=200)
    rocketStatus=Entry(window, text="Saisissez votre rocketStatus", bd=5)
    rocketStatus.place(x=150, y=200)

    lblcost=Label(window, text="cost", fg='black', font=("Helvetica", 12))
    lblcost.place(x=60, y=240)
    cost=Entry(window, text="Saisissez votre cost", bd=5)
    cost.place(x=150, y=240)

    lblmissionStatus=Label(window, text="missionStatus", fg='black', font=("Helvetica", 12))
    lblmissionStatus.place(x=60, y=280)
    missionStatus=Entry(window, text="Saisissez votre missionStatus", bd=5)
    missionStatus.place(x=150, y=280)


    btn=Button(window, text="Envoyer", fg='black',command=createdb)
    btn.place(x=60, y=300)
                    
    window.title('Vos Informations')
    window.geometry("500x400+10+10")
    window.mainloop()
    
def Modifier() :
    global companyName,location,datum,rocketName,rocketStatus,cost,missionStatus
    verifName = Tk()
    lblerocketName=Label(verifName, text="rocketName", fg='black', font=("Helvetica", 12))
    lblerocketName.place(x=60, y=120)
    rocketName=Entry(verifName, text="Saisissez votre rocketName", bd=5)
    rocketName.place(x=150, y=120)
    btn=Button(verifName, text="Envoyer", fg='black',command=readupDb1)
    btn.place(x=60, y=200)
    verifName.geometry("500x400+10+10")
    verifName.mainloop()
    
def Modifier2() :
    
    global  chg, rocketName,v0
    window=Tk()

    lbl=Label(window, text="Veuillez saisir ce que vous voulez modifier :", fg='black', font=("Helvetica", 12))
    lbl.place(x=60, y=40)
    lbl=Label(window, text="Options disponibles :", fg='black', font=("Helvetica", 12))
    lbl.place(x=80, y=80)
    lbl=Label(window, text="companyName,location,datum,rocketName,rocketStatus,cost,missionStatus", fg='black', font=("Helvetica", 12))
    lbl.place(x=60, y=120)
    v0=Entry(window, text="Saisissez votre choix", bd=5)
    v0.place(x=150, y=160)
    

    lblchg=Label(window, text="Valeur de remplacement : ", fg='black', font=("Helvetica", 12))
    lblchg.place(x=60, y=220)
    chg = Entry(window, text="Saisissez la nouvelle valeur", bd=5)
    chg.place(x=150, y=260)
    btn=Button(window, text="Envoyer", fg='black',command=readupDb2)
    btn.place(x=60, y=300)
    window.title('Vos Informations')
    window.geometry("500x400+10+10")
    window.mainloop()

def Supprimer() :

    global rocketName
    verifrocketName = Tk()
    lbl=Label(verifrocketName, text="Veuillez saisir le rocketName de la rocket a supprimer :", fg='black', font=("Helvetica", 12))
    lbl.place(x=60, y=40)
    lblrocketName=Label(verifrocketName, text="rocketName", fg='black', font=("Helvetica", 12))
    lblrocketName.place(x=60, y=120)
    rocketName=Entry(verifrocketName, text="Saisissez l'rocketName", bd=5)
    rocketName.place(x=150, y=120)
    btn=Button(verifrocketName, text="Envoyer", fg='black',command=Supprimer2)
    btn.place(x=60, y=200)
    verifrocketName.geometry("500x400+10+10")
    verifrocketName.mainloop()
    
def Supprimer2() :
    verifrocketName = Tk()
    lbl=Label(verifrocketName, text="Etes vous sur de vouloir supprimer ce rocket ?", fg='black', font=("Helvetica", 12))
    lbl.place(x=60, y=40)
    
    btn=Button(verifrocketName, text="OUI", fg='black',command=supUser)
    btn.place(x=60, y=200)
    btn=Button(verifrocketName, text="NON(Retour au menu principal)", fg='black',command=choix)
    btn.place(x=160, y=200)
    verifrocketName.geometry("500x400+10+10")
    verifrocketName.mainloop()

def choix() :
    choixdb = Tk()
    Lbl=Label(choixdb)
    choixdb.geometry("200x100")  
    b1 = Button(choixdb,text = "Creer",command=Creer,activeforeground = "red",activebackground = "pink",pady=10)  
      
    b2 = Button(choixdb, text = "Modifier",command=Modifier ,activeforeground = "blue",activebackground = "pink",pady=10)  
      
    b3 = Button(choixdb, text = "Lire",command=readDb,activeforeground = "green",activebackground = "pink",pady = 10)  
      
    b4 = Button(choixdb, text = "Supprimer",command=Supprimer,activeforeground = "yellow",activebackground = "pink",pady = 10)  
      
    b1.pack(side = LEFT)  
      
    b2.pack(side = RIGHT)  
      
    b3.pack(side = TOP)  
      
    b4.pack(side = BOTTOM)
    choixdb.mainloop()
choix();
