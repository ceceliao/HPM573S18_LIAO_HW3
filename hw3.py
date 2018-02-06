class patient:
    def __init__(self, name):
        self.name=name

    def discharge(self):
        raise NotImplementedError('This is an abstracted method and need to be implemented in derived classes')

class EmergencyPatient(patient):
    def __init__(self, name):
        patient.__init__ (self,name)
        self.ecost=1000

    def discharge(self):
        print (self.name, 'EmergencyPetient')

#same for hospitalized, but 2000
class HospitalizedPatient(patient):
    def __init__(self, name):
        patient.__init__(self, name)
        self.ecost=2000

    def discharge(self):
        print(self.name, 'Hospitalized Patient')

class hospital:
    def __init__(self):
        self.cost = 0
        self.patients = []

    def admit(self, patients):
        self.patients.append(patients)

    def dischargeAll(self):
        for patients in self.patients:

            patients.discharge()
            self.cost += patients.ecost

    def get_total_cost(self):
        return self.cost




P1 = HospitalizedPatient('P1')
P2 = EmergencyPatient('P2')
P3 = EmergencyPatient('P3')
P4 = EmergencyPatient('P4')
P5 = HospitalizedPatient('P5')



YNHH = hospital()
YNHH.admit(P1)
YNHH.admit(P2)
YNHH.admit(P3)
YNHH.admit(P4)
YNHH.admit(P5)
YNHH.dischargeAll()
print(YNHH.get_total_cost())

