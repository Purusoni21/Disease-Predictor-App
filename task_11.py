#!/usr/bin/python3

print("Content-type:text/html")
print("Access-Control-Allow-Origin:*")
print()

import cgi
from keras.models import load_model
model = load_model("final.h5")
f = cgi.FieldStorage()
itching = int(f.getvalue("itching"))
skin_rash = int(f.getvalue("skin_rash"))
nodal_skin_eruptions = int(f.getvalue("nodal_skin_eruptions"))
continuous_sneezing = int(f.getvalue("continuous_sneezing"))
shivering = int(f.getvalue("shivering"))
chills = int(f.getvalue("chills"))
joint_pain = int(f.getvalue("joint_pain"))
stomach_pain = int(f.getvalue("stomach_pain"))
acidity = int(f.getvalue("acidity"))
ulcers_on_tongue = int(f.getvalue("ulcers_on_tongue"))
muscle_wasting = int(f.getvalue("muscle_wasting"))
vomiting = int(f.getvalue("vomiting"))
burning_micturition = int(f.getvalue("burning_micturition"))
spotting_ urination = int(f.getvalue("spotting_ urination"))
fatigue = int(f.getvalue("fatigue"))
weight_gain = int(f.getvalue("weight_gain"))
anxiety = int(f.getvalue("anxiety"))
cold_hands_and_feets = int(f.getvalue("cold_hands_and_feets"))
mood_swings = int(f.getvalue("mood_swings"))
weight_loss = int(f.getvalue("weight_loss"))
restlessness = int(f.getvalue("restlessness"))
lethargy = int(f.getvalue("lethargy"))
patches_in_throat = int(f.getvalue("patches_in_throat"))
irregular_sugar_level = int(f.getvalue("irregular_sugar_level"))
cough = int(f.getvalue("cough"))
high_fever = int(f.getvalue("high_fever"))
sunken_eyes = int(f.getvalue("sunken_eyes"))
breathlessness = int(f.getvalue("breathlessness"))
sweating = int(f.getvalue("sweating"))
dehydration = int(f.getvalue("dehydration"))
indigestion = int(f.getvalue("indigestion"))
headache = int(f.getvalue("headache"))
yellowish_skin = int(f.getvalue("yellowish_skin"))
dark_urine = int(f.getvalue("dark_urine"))
nausea = int(f.getvalue("nausea"))
loss_of_appetite = int(f.getvalue("loss_of_appetite"))
pain_behind_the_eyes = int(f.getvalue("pain_behind_the_eyes"))
back_pain = int(f.getvalue("back_pain"))
constipation = int(f.getvalue("constipation"))
abdominal_pain = int(f.getvalue("abdominal_pain"))
diarrhoea = int(f.getvalue("diarrhoea"))
mild_fever = int(f.getvalue("mild_fever"))
yellow_urine = int(f.getvalue("yellow_urine"))
yellowing_of_eyes = int(f.getvalue("yellowing_of_eyes"))
acute_liver_failure = int(f.getvalue("acute_liver_failure"))
fluid_overload = int(f.getvalue("fluid_overload"))
swelling_of_stomach = int(f.getvalue("swelling_of_stomach"))
swelled_lymph_nodes = int(f.getvalue("swelled_lymph_nodes"))
malaise = int(f.getvalue("malaise"))
blurred_and_distorted_vision = int(f.getvalue("blurred_and_distorted_vision"))
phlegm = int(f.getvalue("phlegm"))
throat_irritation = int(f.getvalue("throat_irritation"))
redness_of_eyes = int(f.getvalue("redness_of_eyes"))
sinus_pressure = int(f.getvalue("sinus_pressure"))
runny_nose = int(f.getvalue("runny_nose"))
congestion = int(f.getvalue("congestion"))
chest_pain = int(f.getvalue("chest_pain"))
weakness_in_limbs = int(f.getvalue("weakness_in_limbs"))
fast_heart_rate = int(f.getvalue("fast_heart_rate"))
pain_during_bowel_movements = int(f.getvalue("pain_during_bowel_movements"))
pain_in_anal_region = int(f.getvalue("pain_in_anal_region"))
bloody_stool = int(f.getvalue("bloody_stool"))
irritation_in_anus = int(f.getvalue("irritation_in_anus"))
neck_pain = int(f.getvalue("neck_pain"))
dizziness = int(f.getvalue("dizziness"))
cramps = int(f.getvalue("cramps"))
bruising = int(f.getvalue("bruising"))
obesity = int(f.getvalue("obesity"))
swollen_legs = int(f.getvalue("swollen_legs"))
swollen_blood_vessels = int(f.getvalue("swollen_blood_vessels"))
puffy_face_and_eyes = int(f.getvalue("puffy_face_and_eyes"))
enlarged_thyroid = int(f.getvalue("enlarged_thyroid"))
brittle_nails = int(f.getvalue("brittle_nails"))
swollen_extremeties = int(f.getvalue("swollen_extremeties"))
excessive_hunger = int(f.getvalue("excessive_hunger"))
extra_marital_contacts = int(f.getvalue("extra_marital_contacts"))
drying_and_tingling_lips = int(f.getvalue("drying_and_tingling_lips"))
slurred_speech = int(f.getvalue("slurred_speech"))
knee_pain = int(f.getvalue("knee_pain"))
hip_joint_pain = int(f.getvalue("hip_joint_pain'"))
muscle_weakness = int(f.getvalue("muscle_weakness"))
stiff_neck = int(f.getvalue("stiff_neck"))
swelling_joints = int(f.getvalue("swelling_joints"))
movement_stiffness = int(f.getvalue("movement_stiffness"))
spinning_movements = int(f.getvalue("spinning_movements"))
loss_of_balance = int(f.getvalue("loss_of_balance"))
unsteadiness = int(f.getvalue("unsteadiness"))
weakness_of_one_body_side = int(f.getvalue("weakness_of_one_body_side"))
loss_of_smell = int(f.getvalue("loss_of_smell"))
bladder_discomfort = int(f.getvalue("bladder_discomfort"))
foul_smell_of urine = int(f.getvalue("foul_smell_of urine"))
continuous_feel_of_urine = int(f.getvalue("continuous_feel_of_urine"))
passage_of_gases = int(f.getvalue("passage_of_gases"))
internal_itching = int(f.getvalue("internal_itching"))
toxic_look_typhos = int(f.getvalue("toxic_look_typhos"))
depression = int(f.getvalue("depression"))
irritability = int(f.getvalue("irritability"))
muscle_pain = int(f.getvalue("muscle_pain"))
altered_sensorium = int(f.getvalue("altered_sensorium"))
red_spots_over_body = int(f.getvalue("red_spots_over_body"))
belly_pain = int(f.getvalue("belly_pain"))
abnormal_menstruation = int(f.getvalue("abnormal_menstruation"))
dischromic _patches = int(f.getvalue("dischromic _patches"))
watering_from_eyes = int(f.getvalue("watering_from_eyes"))
increased_appetite = int(f.getvalue("increased_appetite"))
polyuria = int(f.getvalue("polyuria"))
family_history = int(f.getvalue("family_history"))
mucoid_sputum = int(f.getvalue("mucoid_sputum"))
rusty_sputum = int(f.getvalue("rusty_sputum"))
lack_of_concentration = int(f.getvalue("lack_of_concentration"))
visual_disturbances = int(f.getvalue("visual_disturbances"))
receiving_blood_transfusion = int(f.getvalue("receiving_blood_transfusion"))
receiving_unsterile_injections = int(f.getvalue("receiving_unsterile_injections"))
coma = int(f.getvalue("coma"))
stomach_bleeding = int(f.getvalue("stomach_bleeding"))
distention_of_abdomen = int(f.getvalue("distention_of_abdomen"))
history_of_alcohol_consumption = int(f.getvalue("history_of_alcohol_consumption"))
fluid_overload.1 = int(f.getvalue("fluid_overload.1"))
blood_in_sputum = int(f.getvalue("blood_in_sputum"))
prominent_veins_on_calf = int(f.getvalue("prominent_veins_on_calf"))
palpitations = int(f.getvalue("palpitations"))
painful_walking = int(f.getvalue("painful_walking"))
pus_filled_pimples = int(f.getvalue("pus_filled_pimples"))
blackheads = int(f.getvalue("blackheads"))
scurring = int(f.getvalue("scurring"))
skin_peeling = int(f.getvalue("skin_peeling"))
silver_like_dusting = int(f.getvalue("silver_like_dusting"))
small_dents_in_nails = int(f.getvalue("small_dents_in_nails"))
inflammatory_nails = int(f.getvalue("inflammatory_nails"))
blister = int(f.getvalue("blister"))
red_sore_around_nose = int(f.getvalue("red_sore_around_nose"))
yellow_crust_ooze = int(f.getvalue("yellow_crust_ooze"))

output = model.predict([['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 'spotting_ urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort', 'foul_smell_of urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic _patches', 'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 'history_of_alcohol_consumption', 'fluid_overload.1', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']])
print(output)
