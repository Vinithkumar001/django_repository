
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import survey_answer,survey_question
# Create your views here.
#def home(request):
    #return render(request,"home.html")
def create_survey(request):
    if request.method== "POST":
        title=request.POST.get("title")
        question=request.POST.get("question")
        survey=survey_question(title=title,question=question)
        survey.save() 
    return render(request,"create.html")
def get_survey(request):
    if request.method== "GET":
        all_survey=survey_question.objects.all()
    return render(request,"home.html",{"all_survey":all_survey})
def get_survey_by_id(request):
    if request.method== "GET":
        survey_by_id=survey_question.objects.get("survey_id")
    return render(request,"get_by_id.html",survey_by_id)
def update_survey(request,survey_id):
    survey=survey_question.objects.get(survey_id=survey_id)
    if request.method== "POST":
        title=request.POST.get("title")
        question=request.POST.get("question")
        survey.title=title
        survey.question=question
        survey.save()
    return render(request,'updatefile.html',{"survey":survey})
    
    survey_ques=survey_question.objects.all()
    survey_ans=survey_answer.objects.all()
    for ques in survey_ques,survey_ans:
        result=ques(survey_id=survey_id)
        result.delete()
def delete_survey(request,survey_id):

    survey=survey_question.objects.get(survey_id=survey_id)
    survey.delete()
    return render(request,"deletefile.html") 
def create_survey_answer(request,survey_id):
    survey=survey_question.objects.get(survey_id=survey_id)
    if request.method== "POST":
        survey_ans=request.POST.get("answer")
        survey_answer_obj=survey_answer(surveyid=survey,answer=survey_ans)
        survey_answer_obj.save()

        return render(request,"sucess.html")
    return render(request,"answercreate.html",{"survey_id": survey_id})

    

def update_answer(request,surveyid):
    survey=survey_answer.objects.get(surveyid=surveyid)
    if request.method== "POST":
        survey_ans=request.POST.get("answer")
        survey.answer=survey_ans
        survey.save()
    return render(request,"updateanswer.html",{"surveyid":surveyid})

def delete_answer(request,surveyid):
    survey=survey_answer.objects.get(surveyid=surveyid)
    survey.delete()
    return render(request,"deletefile.html")
        