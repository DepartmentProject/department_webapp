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
auth = fb.auth()

def tdash(request):
    return render(request, "tdash.html")

def index(request):
    return render(request, "index.html")


'''

print('Login')
    email = input('enter the email   ')
    password = input('enter the password   ')
    try:
        userlogin= auth.sign_in_with_email_and_password(email,password)
        opt2 = int(input('Do you want credentials? (1/0) '))
        if opt2==1:
            print(auth.get_account_info(userlogin['idToken']))
        
    
    

'''


def tlogin(request):
    if request.method=='POST':
        username =request.POST["tusername"]
        password =request.POST["tpassword"]
        try:
            userlogin= auth.sign_in_with_email_and_password(username,password)
            return render(request,'tdashboard.html',{'user':username})
        except:
            print('Invalid Login credentials')
    return render(request, "login.html")

def tdashboard(request):
    if request.method=='POST':
        title =request.POST["title"]
        desc =request.POST["desc"]
        date =request.POST["date"]
        file = request.FILES['files[]']
        image = store.child('Achievements/'+file.name).get_url(None)
        ach = {'title':title, 'desc':desc,'date':date,'image':image}
        db.child('Achievements').push(ach)
        return render(request,'tdashboard.html')

    return render(request,'tdashboard.html')

def cse_home(request):
    return render(request, "cse.html")
def temp(request):
    return render(request, "temp.html")

def eee_home(request):
    return render(request, "eee.html")

def cse_syllabus(request):
    return render(request, "cse_syllabus.html")

def eee_syllabus(request):
    return render(request, "eee_syllabus.html")

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
    achdic={}
    for i in ach.keys():
        achdic[i] = list(ach[i].values())
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