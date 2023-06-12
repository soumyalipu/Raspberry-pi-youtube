import pyrebase
import random
config={
  "apiKey": "AIzaSyAUg9V_mM7rgmjBlD4iaJA8IuxkbzpTzbA",
  "authDomain": "raspberrypitest-2b725.firebaseapp.com",
  "databaseURL": "https://raspberrypitest-2b725-default-rtdb.firebaseio.com",
  "projectId": "raspberrypitest-2b725",
  "storageBucket": "raspberrypitest-2b725.appspot.com",
  "messagingSenderId": "836223957176",
  "appId": "1:836223957176:web:dd2df3ab28bc9762f99c4d",
  "measurementId": "G-CL887CY5TX"
};

firebase = pyrebase.initialize_app(config)
storage=firebase.storage()
database=firebase.database()
randomData = random.randint(0, 100)
print(randomData)
database.child("random")
data={"data":randomData}
database.set(data)