# Create your views here.
from Exams.models import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import logout

def index(request):
    all_exams = Exams.objects.all()

    if request.user.is_authenticated():
        u = request.user
        mod = {"all_exams" : all_exams, "u" : u, "loginout" : '/logout', "l" : "LogOut"}          
    else:
        mod = {"all_exams" : all_exams, "u" : "Oskradur notandi",  "loginout" : 'accounts/login/', "l" : "Login"}
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
