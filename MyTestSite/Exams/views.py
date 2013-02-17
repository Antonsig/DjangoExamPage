# Create your views here.
from Exams.models import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import *
from datetime import datetime
from django.contrib.auth import logout
from decimal import Decimal

def index(request):
    all_exams = Exams.objects.all()
    currentuser = request.user
    mod = {"all_exams" : all_exams, "u" : currentuser, "loginout" : '/logout', "l" : "LogOut"}    
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

def about(request):
    all_exams = Exams.objects.all()
    currentuser = request.user
    mod = {"all_exams" : all_exams, "u" : currentuser, "loginout" : '/logout', "l" : "LogOut"}  
    return render_to_response("about.html", mod)
        
def useranswers(request):
    if request.method == 'POST':
        us = request.user
        u = us.id
        e = request.POST['eid']
        q = request.POST['qid']
        a = request.POST['val']
        iq = int(q)
        ie = int(e)
        i = Decimal(u*100000) + Decimal(ie*100) + Decimal(iq)
        answ_obj = Answers(i,u,e,q,a)
        answ_obj.save()
        ex = Exams.objects.get(pk=e)
        qu = Questions.objects.filter(exam=e)
        model = {"exams" : ex, "questions" : qu, "user" : us}
        return render_to_response("exam.html", model)
        
@login_required
def results (request):
    u = request.user.id
    all_results = Answers.objects.filter(userID=u)
    all_exams = Exams.objects.all()
    all_questions = Questions.objects.all()
    model = {"resul" : all_results, "exams" : all_exams, "questions" : all_questions}
    return render_to_response("results.html",model)
        
def home(request):
    return redirect("index")

def createxam(request):
    if request.method == 'GET':
        return render_to_response("createxam.html", request)
    else:
        e_name = request.POST["profnafn"]
        n_date = "2013-02-17"
        o_date = request.POST["p_byr"]
        c_date = request.POST["p_lok"]
        new_exam = Exams(name=e_name, date_created=n_date, date_opened=o_date, date_closed=c_date )
        new_exam.save()
        model = {"e_name" : e_name, "e_num" : new_exam.id }
        return render_to_response("createxamquestions.html", model)

def createxamquestion(request):
    if request.method == 'POST':
        e_name = request.POST["prof_n"]
        e = request.POST["prof_id"]
        q = request.POST["question"]
        aa = request.POST["answerA"]
        ab = request.POST["answerB"]
        ac = request.POST["answerC"]
        ad = request.POST["answerD"]
        a = request.POST['val']
        quest_obj = Questions(exam_id=e, question=q, answerA=aa, answerB=ab, answerC=ac, answerD=ad, correct_answer=a)
        quest_obj.save()
        model = {"e_name" : e_name, "e_num" : e }
        return render_to_response("createxamquestions.html", model)
