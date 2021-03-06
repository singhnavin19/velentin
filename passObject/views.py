from passObject.models import Student
from django.shortcuts import render

def passObject(request):
   student1=Student()
   student1.id=1
   student1.name='amit'
   student1.knowDjango=True
   
   student2=Student()
   student2.id=2
   student2.name='lokesh'
   student2.knowDjango=False

   
   students=[student1,student2];
   for s in students:
       print(s.name)   
   return render(request,"passObject.html",{'students':students});
