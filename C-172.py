class Doctor():
    
    def __init__(self):
        print("This is class doctor!")
        
    def BMI(height, weight):
        bmi = weight/(height*height)
        print("Your BMI is " + str(bmi))
        
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great your heart is normal")
        else:
            print("Your heart is experiencing difficulties. Please visit a clinic as soon as possible!")
            
class Patient():
    def __init__(self, name, height, weight, heart_rates):
        self.patient_name = name
        self.patient_height = height
        self.patient_weight = weight
        self.patient_heart_rates = heart_rates
        
    def healthCheck(self):
        print("\n Patient's name: " + self.patient_name)
        Doctor.BMI(self.patient_height, self.patient_weight)
        Doctor.heart_rate(self.patient_heart_rates)
        
patient1 = Patient("Micheal", 30, .9144, 80)
patient1.healthCheck()

patient2 = Patient("Jessica", 40, 1, 120)
patient2.healthCheck()