from django.shortcuts import render, redirect

import pyrebase

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm



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

def eee_home(request):
    return render(request, "eee.html")

def cse_syllabus(request):
    return render(request, "cse_syllabus.html")

def eee_syllabus(request):
    return render(request, "eee_syllabus.html")

def contact(request):
    return render(request, "contact.html")

def cse_cgpa(request):
    sem_dict = {1:{'Communicative English':4 ,'Engineering Mathematics I':4, 'Engineering Physics':3, 'Engineering Chemistry':3, 'PSPP':3, 'Engineering Graphics':4, 'PSPP Lab':2, 'Physics and Chemistry Lab':2},
                2:{'Technical English':4, 'Engeneering Mathematics II':4, 'Physics for information Science':3, 'BEEE':3, 'EVS':3, 'Programming in C':3, 'Engineering Practices Lab':2, 'C Lab':2},
                3:{'Discrete Mathematics':4,'Digital Principles and System Design':4, 'Data Structures':3, 'Object Oriented Programming':3, 'Communication Engineering':3, 'Data Structures Laboratory':2, 'Object Oriented Programming Laboratory':2, 'Digital Systems Laboratory':2, 'Interpersonal Skills/Listening & Speaking':2},
                4:{'Probability and Queueing Theory':4,'Computer Architecture':3, 'Database Management Systems':3, 'Design and Analysis of Algorithms':3, 'Operating Systems':3, 'Software Engineering':3, 'Database Management Systems Laboratory':2, 'Operating Systems Laboratory':2, 'Advanced Reading and Writing':1},
                5:{'Algebra and Number Theory':4,'Computer Networks':3, 'Microprocessors and Microcontrollers ':3, 'Theory of Computation':3, 'Object Oriented Analysis and Design':3, 'Open Elective I ':3, 'Microprocessors and Microcontrollers Laboratory':2, 'Object Oriented Analysis and Design Laboratory':2, 'Networks Laboratory':2},
                6:{'Internet Programming':3,'Artificial Intelligence':3, 'Mobile Computing  ':3, 'Compiler Design':4, 'Distributed Systems':3, 'Professional Elective I ':3, 'Internet Programming Laboratory':2, 'Mobile Application Development Laboratory':2, 'Mini Project':1,'Professional Communication':1},
                7:{'Principles of Management':3,'Cryptography and Network Security ':3, 'Cloud Computing':3, 'Open Elective II':3, 'Professional Elective II':3, 'Professional Elective III ':3, 'Cloud Computing Laboratory':2, 'Security Laboratory ':2},
                8:{'Professional Elective IV':3, 'Professional Elective V ':3, 'Project Work':10}
                }
    if request.method == "POST":
        
        if 'sem' in request.POST:
            sem = int(request.POST["sem"])
            return render(request, "cse_cgpa.html", {'semm':list(sem_dict[sem].keys()), 'sem_no':sem})
        else:
            sem1 = int(request.POST["semno"])
            sum_res = 0
            for i,j in sem_dict[sem1].items():
                x = int(request.POST[i])   
                sum_res = sum_res + (x*j)
            ans = sum_res/sum(sem_dict[sem1].values())
            return render(request, "cse_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans})
    else:
        return render(request, "cse_cgpa.html", {'semm':list(sem_dict[1].keys()), 'sem_no':1})
        
def eee_cgpa(request):
    sem_dict = {1:{'Communicative English':4 ,'Engineering Mathematics I':4, 'Engineering Physics':3, 'Engineering Chemistry':3, 'PSPP':3, 'Engineering Graphics':4, 'PSPP Lab':2, 'Physics and Chemistry Lab':2},
                2:{'Technical English':4, 'Engeneering Mathematics II':4,'Basic Civil and Mechanical Engineering ':4, 'Physics for electronics engineering':3, 'Circuit Theory':3, 'Environmental Science and Engineering':3, 'Engineering Practices Laboratory':2, 'Electric Circuits Laboratory ':2},
                3:{'Discrete Mathematics':4,'Digital Logic Circuits':3, 'Electromagnetic Theory':3, 'Electrical Machines - I ':3, 'Electron Devices and Circuits ':3,'Power Plant Engineering':3, 'Electronics Laboratory':2, 'Electrical Machines Laboratory - I':2},
                4:{'Numerical Methods ':4,'Control Systems ':4,'Electrical Machines - II ':3, 'Transmission and Distribution ':3, 'Measurements and Instrumentation ':3, 'Linear Integrated Circuits and Applications ':3, 'Electrical Machines Laboratory - II':2, 'Linear and Digital Integrated Circuits Laboratory':2, 'Technical Seminar':1},
                5:{'Power System Analysis':3,'Microprocessors and Microcontrollers':3, 'Power Electronics  ':3, 'Digital Signal Processing ':3, 'Object Oriented Programming':3, 'Open Elective I ':3, 'Control and Instrumentation Laboratory':2, 'Object Oriented Programming Laboratory':2, 'Professional Communication':1},
                6:{'Solid State Drives ':3,'Protection and Switchgear':3, 'Embedded Systems':3,'Professional Elective I ':3, 'Professional Elective II ':3, 'Power Electronics and Drives Laboratory':2, 'Microprocessors and Microcontrollers Laboratory':2, 'Mini Project':2},
                7:{'High Voltage Engineering':3,'Power System Operation and Control  ':3, 'Renewable Energy Systems ':3, 'Open Elective II':3, 'Professional Elective III':3, 'Professional Elective IV ':3, 'Power System Simulation Laboratory':2, 'Renewable Energy Systems Laboratory':2},
                8:{'Professional Elective V':3, 'Professional Elective VI ':3, 'Project Work':10}
                }
    if request.method == "POST":
        
        if 'sem' in request.POST:
            sem = int(request.POST["sem"])
            return render(request, "cse_cgpa.html", {'semm':list(sem_dict[sem].keys()), 'sem_no':sem})
        else:
            sem1 = int(request.POST["semno"])
            sum_res = 0
            for i,j in sem_dict[sem1].items():
                x = int(request.POST[i])   
                sum_res = sum_res + (x*j)
            ans = sum_res/sum(sem_dict[sem1].values())
            return render(request, "cse_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans})
    else:
        return render(request, "eee_cgpa.html", {'semm':list(sem_dict[1].keys()), 'sem_no':1})
        


    
def packages(request):
    return render(request, "packages.html")


def achievements(request):
    ach =  db.child('Achievements').get().val()
    #print('!!!!!!!!!!!!!',ach['ach1'].values())
    #print('!!!!!!!!!!!!!',ach.keys())
    achdic={}
    for i in ach.keys():
        achdic[i] = list(ach[i].values())
        #print('!!!!!!!!!!!!!',ach[i].values())
    #print(achdic)
    return render(request, "achievements.html",{'achdic': achdic})

def notes(request):
    x= db.child('Semester3').get().val()
    return render(request, "notes.html",{'key':x})

def eee_notes(request):
    x= db.child('Semester3').get().val()
    return render(request, "eee_notes.html",{'key':x})

def contact(request):
    return render(request, "contact.html")
