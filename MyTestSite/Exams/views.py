# Create your views here.
from Exams.models import *
from django.shortcuts import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import logout


def index(request):
        all_exams = Exams.objects.all()
        mod = {"all_exams" : all_exams, "u_name" : request.user.username}     
        return render_to_response("index.html", mod)
        
@login_required
def exam_details(request, exam_id):
    e = Exams.objects.get(pk=exam_id)
    q = Questions.objects.filter(exam=exam_id)
    
    model = {"exams" : e, "questions" : q}
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
        username = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = User.objects.create_user(username, email, password)
        user.is_staff = False
        user.save()
        return redirect("index")

def logout_view(request):
    logout(request)
    return redirect("index")