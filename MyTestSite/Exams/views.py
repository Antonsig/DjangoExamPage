# Create your views here.
from Exams.models import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import logout

def index(request):
    all_exams = Exams.objects.all()
    currentuser = request.user

    if currentuser.is_superuser:
        mod = {"all_exams" : all_exams, "u" : currentuser, "loginout" : '/logout', "l" : "LogOut", "hideNyrNotandi" : "display:none;"}
        print ("superuser")        
    elif currentuser.is_authenticated():
        mod = {"all_exams" : all_exams, "u" : currentuser, "loginout" : '/logout', "l" : "LogOut", "hideNyttProf" : "display:none;", "hideNyrNotandi" : "display:none;"}    
        print ("user")    
    else:
        mod = {"all_exams" : all_exams, "u" : "Oskradur notandi",  "loginout" : 'accounts/login/', "l" : "Login", "hideNyttProf" : "display:none;"}
        
    return render_to_response("index.html", mod)
        
@login_required
def exam_details(request, exam_id):
    e = Exams.objects.get(pk=exam_id)
    q = Questions.objects.filter(exam=exam_id)
    u = request.user
    
    model = {"exams" : e, "questions" : q, "user" : u}
    return render_to_response("exam.html", model)
    
def questions(request):
    first_question = Questions.objects.get(pk=1)
    all_questions = Questions.objects.all()
    # print first_question.question
    mod = {"all_questions" : all_questions}
    model = {"first_question" : first_question}
    return render_to_response("index.html", mod)
    return render_to_response("index.html", model)

def register(request):
    if request.method == 'GET':
        return render_to_response("register.html")
    else:
        uname = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(uname, email, password)
        user.first_name = request.POST["firstname"]
        user.last_name = request.POST["lastname"]
        user.is_staff = False
        user.save()
        return redirect("index")

def logout_view(request):
    logout(request)
    return redirect("index")

def about():
    abouttext = "<p>We are the best of the best of the best</p><p>Anton Sigurdsson</p><p>Sigurdur Jonsson</p>"
    return render_to_response("about.html", abouttext)

def answers(request, offset):
   if request.method == 'POST':
        u = request.POST.get('user.id')
        e = request.POST.get('exams.id')
        q = request.POST.get('questions.id')
        a = request.POST.get('val')
        answ_obj = Answer(userID=u, exam=e, qustionID=q,user_answer = a)
        answ_obj.save()
def home(request):
    return redirect("index")

def createxam(request):
    if request.method == 'GET':
        return render_to_response("createxam.html", request)
    else:
        e_name = request.POST["profnafn"]
        q_num = request.POST["f_spurn"]
        n_date = request.POST["p_byr"]
        o_date = request.POST["p_byr"]
        c_date = request.POST["p_lok"]
        #n_date = "2013-02-17"
        #o_date = "2013-02-17"
        #c_date = "2013-02-17"
        new_exam = Exams(name=e_name, date_created=n_date, date_opened=o_date, date_closed=c_date )
        new_exam.save()
        model = {"e_name" : e_name, "e_num" : new_exam.id }
        return render_to_response("createxamquestions.html", model)
