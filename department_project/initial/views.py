from django.shortcuts import render

import pyrebase


firebaseConfig = {
    'apiKey': "AIzaSyANGBWe3WlGaVRz0AlenXeL0CVB-WrTYro",
    'authDomain': "department-webapp.firebaseapp.com",
    'databaseURL': "https://department-webapp-default-rtdb.firebaseio.com",
    'projectId': "department-webapp",
    'storageBucket': "department-webapp.appspot.com",
    'messagingSenderId': "200792524960",
    'appId': "1:200792524960:web:ed6771ec8ff2bf9e86e1c5",
    'measurementId': "G-5RV1GXRFBD"
  }


fb = pyrebase.initialize_app(firebaseConfig)
db = fb.database()

def index(request):
    return render(request, "index.html")

def cse_home(request):
    return render(request, "cse.html")

def cse_syllabus(request):
    return render(request, "cse_syllabus.html")

def cse_cgpa(request):
    sem_dict = {1:{'Communicative English':4 ,'Engineering Mathematics I':4, 'Engineering Physics':3, 'Engineering Chemistry':3, 'PSPP':3, 'Engineering Graphics':4, 'PSPP Lab':2, 'Physics and Chemistry Lab':2},2:{'Technical English':4, 'Engeneering Mathematics II':4, 'Physics for information Science':3, 'BEEE':3, 'EVS':3, 'Programming in C':3, 'Engineering Practices Lab':2, 'C Lab':2}}
    
    if request.method == "POST":
        
        if 'sem' in request.POST:
            sem = int(request.POST["sem"])
            
            print("!!!!!!!!",sem)
            return render(request, "cse_cgpa.html", {'semm':list(sem_dict[sem].keys()), 'sem_no':sem})
        else:
            sem1 = int(request.POST["semno"])
            sum_res = 0
            for i,j in sem_dict[sem1].items():
                x = int(request.POST[i])   
                sum_res = sum_res + (x*j)
            ans = sum_res/sum(sem_dict[sem1].values())
            print("zuzuzuzuzuzuzuzzuzuzuzuzuzuzu",ans)
            return render(request, "cse_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans})
    else:
        return render(request, "cse_cgpa.html", {'semm':list(sem_dict[1].keys()), 'sem_no':1})
        

    
def packages(request):
    return render(request, "packages.html")

def notes(request):
    #useropt=db.child('Semester3').shallow().get()
    x= db.child('Semester3').get().val()
    #print(x.keys())


    return render(request, "notes.html",{'key':x})
