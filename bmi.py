import pandas as pd


jdata=pd.read_json('data.json')
jdata['BMI']=''
jdata['BMI Category']=''
jdata['Health Risk']=''
metrics={'A':[0,18.4,'Underweight','Malnutrition Risk'],
         'B':[18.5,24.9,'Normal weight','Low Risk'],
         'C':[25,29.9,'Overweight','Enhanced Risk'],
         'D':[30,34.9,'Moderately Obese','Medium Risk'],
         'E':[35,39.9,'Severely obese','High Risk'],
         'F':[40,100,'Very severely obese','Very High Risk']}
for index, row in jdata.iterrows():
  height=pow((row['HeightCm']/100),2)
  row['BMI']=row['WeightKg']/height
  for key,value in metrics.items():
    if row['BMI']>=value[0] and row['BMI']<=value[1]:
      row['BMI Category']=value[2]
      row['Health Risk']=value[3]
      break






