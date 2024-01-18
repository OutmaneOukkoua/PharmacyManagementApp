# Definition of the Medicament class
class Medicament:
    # Constructor method to initialize instance variables
    def __init__(self):
        # Instance variables representing Medicament attributes
        self.RefMedicament=""
        self.Description=""
        self.FormeMedicament=""
        self.Prix=0.0
        self.Quantite=0

    # String representation of the Medicament object
    def __str__(self):
        # Format the Medicament information as a string
        pharmacie = f"Reference : {self.RefMedicament} | Description : {self.Description} | Forme : {self.FormeMedicament} | Prix : {self.Prix} | Quantite : {self.Quantite}"
        return pharmacie