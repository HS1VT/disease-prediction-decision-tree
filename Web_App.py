from select import select
from flask import Flask
from pywebio.input import *
from pywebio.output import *
from pywebio.output import put_text 
from pywebio import start_server
import pandas as pd
import pickle
import numpy as np

# here we open the .pkl file that we generated in the initial step. The .pkl file conatins
# the decision tree and will help us in making our web application, and we use flask for
# the given purpose.
with open('disease_prediction.pkl','rb') as f:
    tree_files = pickle.load(f)
app = Flask(__name__)

# here we define the function that identifies all the symptoms which are listed in a list 
# format below and user sees the below functions to choose from, and the code will predict 
# the disease and the cure based on the following function.

def predict():

    # symptoms is a list that contains all the symptoms that the user will be asked to choose
    # from and based on which we will predict.

   symptom_list = ['None','itching', ' skin_rash', ' nodal_skin_eruptions',
       ' dischromic _patches', ' continuous_sneezing', ' shivering',
       ' chills', ' watering_from_eyes', ' stomach_pain', ' acidity',
       ' ulcers_on_tongue', ' vomiting', ' cough', ' chest_pain',
       ' yellowish_skin', ' nausea', ' loss_of_appetite',
       ' abdominal_pain', ' yellowing_of_eyes', ' burning_micturition',
       ' spotting_ urination', ' passage_of_gases', ' internal_itching',
       ' indigestion', ' muscle_wasting', ' patches_in_throat',
       ' high_fever', ' extra_marital_contacts', ' fatigue',
       ' weight_loss', ' restlessness', ' lethargy',
       ' irregular_sugar_level', ' blurred_and_distorted_vision',
       ' obesity', ' excessive_hunger', ' increased_appetite',
       ' polyuria', ' sunken_eyes', ' dehydration', ' diarrhoea',
       ' breathlessness', ' family_history', ' mucoid_sputum',
       ' headache', ' dizziness', ' loss_of_balance',
       ' lack_of_concentration', ' stiff_neck', ' depression',
       ' irritability', ' visual_disturbances', ' back_pain',
       ' weakness_in_limbs', ' neck_pain', ' weakness_of_one_body_side',
       ' altered_sensorium', ' dark_urine', ' sweating', ' muscle_pain',
       ' mild_fever', ' swelled_lymph_nodes', ' malaise',
       ' red_spots_over_body', ' joint_pain', ' pain_behind_the_eyes',
       ' constipation', ' toxic_look_(typhos)', ' belly_pain',
       ' yellow_urine', ' receiving_blood_transfusion',
       ' receiving_unsterile_injections', ' coma', ' stomach_bleeding',
       ' acute_liver_failure', ' swelling_of_stomach',
       ' distention_of_abdomen', ' history_of_alcohol_consumption',
       ' fluid_overload', ' phlegm', ' blood_in_sputum',
       ' throat_irritation', ' redness_of_eyes', ' sinus_pressure',
       ' runny_nose', ' congestion', ' loss_of_smell', ' fast_heart_rate',
       ' rusty_sputum', ' pain_during_bowel_movements',
       ' pain_in_anal_region', ' bloody_stool', ' irritation_in_anus',
       ' cramps', ' bruising', ' swollen_legs', ' swollen_blood_vessels',
       ' prominent_veins_on_calf', ' weight_gain',
       ' cold_hands_and_feets', ' mood_swings', ' puffy_face_and_eyes',
       ' enlarged_thyroid', ' brittle_nails', ' swollen_extremeties',
       ' abnormal_menstruation', ' muscle_weakness', ' anxiety',
       ' slurred_speech', ' palpitations', ' drying_and_tingling_lips',
       ' knee_pain', ' hip_joint_pain', ' swelling_joints',
       ' painful_walking', ' movement_stiffness', ' spinning_movements',
       ' unsteadiness', ' pus_filled_pimples', ' blackheads', ' scurring',
       ' bladder_discomfort', ' foul_smell_of urine',
       ' continuous_feel_of_urine', ' skin_peeling',
       ' silver_like_dusting', ' small_dents_in_nails',
       ' inflammatory_nails', ' blister', ' red_sore_around_nose',
       ' yellow_crust_ooze']

    # now we read the symptom_Description.csv and symptom_precaution.csv into two variables
    # and then using the same variables, we will then use the decision tree to output that
    # what are the descriptions of the disease that the patient is going through, and using 
    # the precaution scv, we will tell the user that what are the precautions that you need
    # to keep in mind that will save you from the given disease

   symptom_description = pd.read_csv('symptom_Description.csv')
   symptom_precaution = pd.read_csv('symptom_precaution.csv')

   # now we declare a list in which we'll store the expected diseases
   # in the following lines, we create a drop down menu for the user to select
   # from the 17 diseases
   symp_list=[]
   for i in range(1,18):
      first_symptom = select('Choose Symptom '+str(i),symptom_list,name = f's{i}')
      symp_list.append(first_symptom)
    # now we ask the user about what symptoms she/he is observing in her/his body 
    # and we check that if a particular disease is selected by the user, then we will
    # give that disease a number 1 and if it is not selected, then it is 0.
   symp_list = input_group('Enter The Symptoms You See In Your Body',symp_list)
   symp_list= list(symp_list.values())
   for j in range(len(symptom_list)):
       if symptom_list[j] in symp_list:
           symptom_list[j] = 1
       else: 
           symptom_list[j] = 0  
   symptom_list = pd.DataFrame(symptom_list).T  
   prediction =  tree_files.predict(symptom_list)
   
   put_html(f"<h1>{prediction[0]}</h1>")
   
   # using this line, we tell the user something about the disease that is detected in 
   # her/his body
   put_column([put_html(f"<h2>Description of The Disease Detected:</h2> "),
               put_html(list(symptom_description[symptom_description['Disease'] == prediction[0]]['Description'])[0]),
               ])
   # using this line, we tell the user that what precaution she/he can take for the 
   # prevention of the disease.
   put_html('<h3>Precautions That You Can Take:</h3>')
   # using this we tell user four precautions to take.
   put_column([
               put_text('1.'+ str(list(symptom_precaution[symptom_precaution['Disease'] == prediction[0]]['Precaution_1'])[0])),
               put_text('2.'+ str(list(symptom_precaution[symptom_precaution['Disease'] == prediction[0]]['Precaution_2'])[0])),
               put_text('3.'+ str(list(symptom_precaution[symptom_precaution['Disease'] == prediction[0]]['Precaution_3'])[0])),
               put_text('4.'+ str(list(symptom_precaution[symptom_precaution['Disease'] == prediction[0]]['Precaution_4'])[0]))])
   put_html('<a href="/" style="background-color:black;margin-left:350px;color:white;;padding :8px;border-radius:5px;font-size:30px;text-decoration:none;box-shadow:0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)">Home</a>')
  
# using following lines, we generate the localhost page on port 8000.
if __name__ == '__main__':
       start_server(predict, port=8000, debug=True)