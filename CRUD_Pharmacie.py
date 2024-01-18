# Definition of the Pharmacie class

class Pharmacie:
    # Constructor method to initialize instance variables
    def __init__(self):
        # Instance variables representing Pharmacie attributes
        self.NomPharmacie = ""
        self.Adresse = ""
        self.ListeMedicaments = []

    # Method to search for a Medicament by reference code
    def RechercherMedicament(self, ref):
        for i in range(len(self.ListeMedicaments)):
            if self.ListeMedicaments[i].RefMedicament == ref:
                return i
        else:
            return -1
        

    # Method to add a new Medicament to the Pharmacy
    def AjouterMedicament(self, mec):
        if self.RechercherMedicament(mec.RefMedicament) == -1:
            self.ListeMedicaments.append(mec)
            return True
        else:

            return False
        
    # Method to remove a Medicament from the Pharmacy by reference code
    def SupprimerMedicament(self, ref):
        b=self.RechercherMedicament(ref)
        if b != -1 :
            self.ListeMedicaments.pop(b)
            return True
        else:
            return False

    # Method to modify a Medicament's information in the Pharmacy
    def ModifierMedicament(self,mec):
        i=self.RechercherMedicament(mec.RefMedicament)
        if i != -1:
            self.ListeMedicaments[i]=mec
            return True
        else:
            return False