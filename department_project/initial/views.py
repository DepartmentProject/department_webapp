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
store = fb.storage()

def index(request):
    return render(request, "index.html")

def cse_home(request):
    return render(request, "cse.html")

def cse_syllabus(request):
    return render(request, "cse_syllabus.html")

def contact(request):
    return render(request, "contact.html")

def cse_cgpa(request):
    sem_dict = {1:{'Communicative English':4 ,'Engineering Mathematics I':4, 'Engineering Physics':3, 'Engineering Chemistry':3, 'Problem Solving and Python Programming':3, 'Engineering Graphics':4, 'Problem Solving and Python Programming Laboratory':2, 'Physics and Chemistry Laboratory':2},
                2:{'Technical English':4, 'Engeneering Mathematics II':4, 'Physics for information Science':3, 'BEEE':3, 'EVS':3, 'Programming in C':3, 'Engineering Practices Lab':2, 'C Lab':2},
                3:{'Discrete Mathematics':4,'Digital Principles and System Design':4, 'Data Structures':3, 'Object Oriented Programming':3, 'Communication Engineering':3, 'Data Structures Laboratory':2, 'Object Oriented Programming Laboratory':2, 'Digital Systems Laboratory':2, 'Interpersonal Skills/Listening & Speaking':1},
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
        

    
def packages(request):
    return render(request, "packages.html")


def achievements(request):
    ach =  db.child('Achievements').get().val()
    achdic={}
    for i in ach.keys():
        achdic[i] = list(ach[i].values())
        
    return render(request, "achievements.html",{'achdic': achdic})

def notes(request):
    x= db.child('Semester3').get().val()
    return render(request, "notes.html",{'key':x})

def contact(request):
    return render(request, "contact.html")

def ece_home(request):
    return render(request, "ece.html")

def ece_syllabus(request):
    return render(request, "ece_syllabus.html")

def ece_cgpa(request):
    sem_dict = {1:{'Communicative English':4 ,'Engineering Mathematics I':4, 'Engineering Physics':3, 'Engineering Chemistry':3, 'Problem Solving and Python Programming':3, 'Engineering Graphics':4, 'Problem Solving and Python Programming Laboratory':2, 'Physics and Chemistry Laboratory':2},
                2:{'Technical English':4, 'Engeneering Mathematics II':4, 'Physics for Electronics Engineering':3, 'Basic Electrical and Instrumentation Engineerong':3, 'Circuit Analysis':4, 'Electronic Devices':3, 'Engineering Practices Laboratory':2, 'Circuits and Devices Laboratory':2},
                3:{'Linear Algebra and Partial Differential Equations':4,'Fundamentals of Data Structures in C':3, 'Electronic Ciruits I':3, 'Signals and Systems':4, 'Digital Electronics':3, 'Control Systems Engineering':3, 'Fundamentals of Data Structures in C laboratory':2, 'Analog and Digital Ciruits Laboratory':2, 'Interpersonal Skills/Listening & Speaking':1},
                4:{'Probability and Random Processes':4,'Electronic Circuits II':3, 'Communication Theory':3, 'Electromagnetic Fields':4, 'Linear Integrated Circuits':3, 'Environmental Science and Engineering':3, 'Circuits Design and Simulation Laboratory':2, 'Linear Integrated circuits Laboratory':2},
                5:{'Digital Communication':3,'Discrete-Time Signal Processing':4, 'Computer Architecture and Organization':3, 'Communication Networks':3, 'Professional Elective I':3, 'Open Elective I ':3, 'Digital Signal Processing Laboratory':2, 'Communication Systems Laboratory':2, 'Communication Networks Laboratory':2},
                6:{'Microprocessors and Microcontrollers':3,'VLSI Design':3, 'Wireless Communication':3, 'Principles of Management':3, 'Transmission Lines and RF Systems':3, 'Professional Elective II ':3, 'Microprocessors and Microcontrollers Laboratory':2, 'VLSI Design Laboratory':2, 'Technical Seminar':1,'Professional Communication':1},
                7:{'Antennas and Microwave Engineering':3,'Optical Communication':3, 'Embedded and Real Time Systems':3, 'Ad hoc and Wireless Sensor Networks':3, 'Professional Elective III':3, 'Open Elective II ':3, 'Embedded Laboratory':2, 'Advanced Communication Laboratory':2},
                8:{'Professional Elective IV':3, 'Professional Elective V':3, 'Project Work':10}
                }
    if request.method == "POST":
        
        if 'sem' in request.POST:
            sem = int(request.POST["sem"])
            return render(request, "ece_cgpa.html", {'semm':list(sem_dict[sem].keys()), 'sem_no':sem})
        else:
            sem1 = int(request.POST["semno"])
            sum_res = 0
            for i,j in sem_dict[sem1].items():
                x = int(request.POST[i])   
                sum_res = sum_res + (x*j)
            ans = sum_res/sum(sem_dict[sem1].values())
            if ans>9:
                msg = "You are doing great, Keep it up"
                return render(request, "ece_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans, 'msg':msg})
            elif ans>8:
                msg = "Keep it up"
                return render(request, "ece_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans, 'msg':msg})
            elif ans>7:
                msg = "Not bad , Keep Trying"
                return render(request, "ece_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans, 'msg':msg})
            else:
                msg = "Work hard"
                return render(request, "ece_cgpa.html", {'semm':list(sem_dict[sem1].keys()), 'sem_no':sem1, 'ans':ans, 'msg':msg})
    else:
        return render(request, "ece_cgpa.html", {'semm':list(sem_dict[1].keys()), 'sem_no':1})

def ece_notes(request):
    x= db.child('Semester3').get().val()
    prp = db.child('ECE').child('Sem 4').child('PRP').get().val()
    evs = db.child('ECE').child('Sem 4').child('EVS').get().val()
    lic = db.child('ECE').child('Sem 4').child('LIC').get().val()
    ct = db.child('ECE').child('Sem 4').child('CT').get().val()
    ec2 = db.child('ECE').child('Sem 4').child('EC2').get().val()
    emf = db.child('ECE').child('Sem 4').child('EC2').get().val()
    return render(request, "ece_notes.html",{'key':x, 'sem4prp':prp, 'sem4evs':evs, 'sem4lic':lic, 'sem4ct':ct, 'sem4ec2':ec2, 'sem4emf':emf})