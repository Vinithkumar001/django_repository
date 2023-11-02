from django.db import models
from django.db.models import CharField,ForeignKey,AutoField,CASCADE
class survey_question(models.Model):
    survey_id=AutoField(primary_key=True)
    title=CharField(max_length=255)
    question=CharField(max_length=255)
class survey_answer(models.Model):
    surveyid=ForeignKey(survey_question,on_delete=CASCADE)
    answer=CharField(max_length=255)