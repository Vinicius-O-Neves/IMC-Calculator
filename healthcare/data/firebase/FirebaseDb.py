import pyrebase

'''Objeto que com os dados para acessar o Firebase'''
class FirebaseDb:

    def __init__(self):
        self.BASE_URL = "https://imc-calculator-547f5-default-rtdb.firebaseio.com"

        self.firebaseConfig = {
            'apiKey': "AIzaSyDvcnKeN3R532FenTIpQJfEMauVmPU2rQ8",
            'authDomain': "imc-calculator-547f5.firebaseapp.com",
            'databaseURL': self.BASE_URL,
            'projectId': "imc-calculator-547f5",
            'storageBucket': "imc-calculator-547f5.appspot.com",
            'messagingSenderId': "1032231973463",
            'appId': "1:1032231973463:web:134c075f008bac31a2a912"
        }
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.auth = self.firebase.auth()
