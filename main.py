import requests as rq
import datetime as dt
import os
excercise_url="https://trackapi.nutritionix.com/v2/natural/exercise"
key=os.getenv['KEY']
sheety_url="https://api.sheety.co/e0e8bdef3f93c4de3912230aebc3dc04/newWorkout/workouts"
header={
    "x-app-id": os.getenv['X-APP-ID'],
    "x-app-key":os.getenv['X-APP-KEY']
    }

input1=input("what did you do today: ")
excercise_req={
    "query":input1,
    "gender":"male",
    "weight_kg":59,
    "age":23
}
responce=rq.post(url=excercise_url,json=excercise_req,headers=header)
result=responce.json()
# pip=result["exercises"][0]["user_input"].title()
print(result)

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for n in result["exercises"]:
    sheet_inputs={
        "workout":{
            "date":today_date,
            "time":now_time,
            "exercise":n["name"].title(),
            "duration":n["duration_min"],
            "calories":n["nf_calories"]
        }
    }
    sheety=rq.post(
        sheety_url,
        json=sheet_inputs,
        auth=(
            os.getenv['USENAME'],
            os.getenv['PASSWORD']
        )
    )

    print(sheety.text)
