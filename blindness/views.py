from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
import os

from django.urls import reverse
import requests
import time

from firebase import firebase
from operator import itemgetter 
#from . import csvjson
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
import json

def predict(request):
    
    return render(request, 'index.html')

def form(request):
    
    return render(request, 'contact.html')


def result(request):
    print(BASE_DIR)
    target = os.path.join(BASE_DIR, 'retina/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)

    if request.method == 'POST' :
        print("Here")
        x = request.POST.get('img')
        print(x)
        filename = x.split(".")
        na = filename[0]
        with open("C:/Users/srishti/Desktop/health/static/csvjson.json", "r") as read_file:
            data = json.load(read_file)
        
        #print(data[na]['diagnosis'])
        
        context={}
            
        context['value']=data[na]['diagnosis']
        if data[na]['diagnosis']==0:
            result = "No"
            summ="You are not at the risk of vision loss now. Continue your healthy lifestyle to manage blood sugar and keep your diabetes in control."
        elif data[na]['diagnosis']==1:
            result = "Mild"
            summ = "This is the mild form of diabetic retinopathy and is usually symptomless. You can reduce your risk of developing diabetic retinopathy, or help stop it getting worse, by keeping your blood sugar levels, blood pressure and cholesterol levels under control."
        elif data[na]['diagnosis']==2:
            result = "Moderate"
            summ = "This is the moderate form of diabetic retinopathy and is usually symptomless. You can reduce your risk of developing diabetic retinopathy, or help stop it getting worse, by keeping your blood sugar levels, blood pressure and cholesterol levels under control."
        elif data[na]['diagnosis']==3:
            result = "Severe"
            summ = "\
            This is the last stage non proliferative stage after this surgery is the only treatment.\
            Manage your diabetes. Make healthy eating and physical activity part of your daily routine. Try to get at least 150 minutes of moderate aerobic activity, such as walking, each week. Take oral diabetes medications or insulin as directed.\
            Monitor your blood sugar level. You may need to check and record your blood sugar level several times a day — more-frequent measurements may be required if you are ill or under stress. Ask your doctor how often you need to test your blood sugar.\
            Keep your blood pressure and cholesterol under control. Eating healthy foods, exercising regularly and losing excess weight can help. Sometimes medication is needed, too.\
            If you smoke or use other types of tobacco, ask your doctor to help you quit. Smoking increases your risk of various diabetes complications, including diabetic retinopathy.\
            Pay attention to vision changes. Contact your eye doctor right away if you experience sudden vision changes or your vision becomes blurry, spotty or hazy."
        elif data[na]['diagnosis']==4:
            result = "Proliferate"
            summ ="Proliferative diabetic retinopathy (PDR) is the more advanced form of the disease. At this stage, circulation problems deprive the retina of oxygen. As a result, new, fragile blood vessels can begin to grow in the retina and into the vitreous, the gel-like fluid that fills the back of the eye. You can consider the following treatments:\n\
            Photocoagulation. This laser treatment, also known as focal laser treatment, can stop or slow the leakage of blood and fluid in the eye. During the procedure, leaks from abnormal blood vessels are treated with laser burns.\n\
            Panretinal photocoagulation. This laser treatment, also known as scatter laser treatment, can shrink the abnormal blood vessels. During the procedure, the areas of the retina away from the macula are treated with scattered laser burns. The burns cause the abnormal new blood vessels to shrink and scar.  Your vision will be blurry for about a day after the procedure. Some loss of peripheral vision or night vision after the procedure is possible.\n\
            Vitrectomy. This procedure uses a tiny incision in your eye to remove blood from the middle of the eye (vitreous) as well as scar tissue that's tugging on the retina. It's done in a surgery center or hospital using local or general anesthesia.\n\
            Surgery often slows or stops the progression of diabetic retinopathy, but it's not a cure. Because diabetes is a lifelong condition, future retinal damage and vision loss are still possible."
        
        context['res'] = result
        context['summ']=summ
        time.sleep(2)
            
        
    return render(request,'result.html',context)       
        
        
    
    


# Create your views here.
