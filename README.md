class Date:
    def __init__(self, jour, mois, annee):
        # Constructeur de la classe Date
        self.jour = jour
        self.mois = mois
        self.annee = annee

    def saisir_date(self, message):
        # Méthode pour saisir une date
        print(message)
        self.jour = input("Jour : ")
        self.mois = input("Mois : ")
        self.annee = input("Année : ")
        return f"{self.jour}/{self.mois}/{self.annee}"

class OffreVoyage:
    def __init__(self, ref_offre, ville_depart, ville_arrivee):
        # Constructeur de la classe OffreVoyage
        self.ref_offre = ref_offre
        self.ville_depart = ville_depart
        self.ville_arrivee = ville_arrivee

    def saisir_offre_voyage(self):
        # Méthode pour saisir les détails d'une offre de voyage
        self.ref_offre = input("Entrer la référence de l'offre : ")
        self.ville_depart = input("Entrer la ville de départ : ")
        self.ville_arrivee = input("Entrer la ville d'arrivée : ")

    def afficher_offre_voyage(self):
        # Méthode pour afficher les détails d'une offre de voyage
        print(f"Ref_Offre: {self.ref_offre}\nVille de départ: {self.ville_depart}\nVille d'arrivée: {self.ville_arrivee}")

    def __str__(self):
        return "Offre: Voyage"

    def bloquer_offre(self):
        # Méthode pour bloquer une offre
        self.etat_offre = 'Bloquée'
        print('Cette offre est Bloquée')

class Hebergement:
    def __init__(self, date_debut, nbre_de_nuit, type_hebergement, prix_nuit):
        # Constructeur de la classe Hebergement
        self.date_debut = Date(0, 0, 0)
        self.nbre_de_nuit = nbre_de_nuit
        self.type_hebergement = type_hebergement
        self.prix_nuit = prix_nuit

    def saisir_hebergement(self):
        # Méthode pour saisir les détails d'un hébergement
        self.date_debut.saisir_date("Entrer la date de début : ")
        self.nbre_de_nuit = input("Entrer le nombre de nuit : ")
        self.type_hebergement = input("Entrer le type d'hébergement (déjeuner, demi-pension, pension complète) : ")
        self.prix_nuit = input("Entrer le prix de la nuit : ")

    def afficher_hebergement(self):
        # Méthode pour afficher les détails d'un hébergement
        print(f"Date de début hébergement: {self.date_debut}\nNombre de nuit: {self.nbre_de_nuit}\nType d'hébergement: {self.type_hebergement}\nPrix de la nuit: {self.prix_nuit}")

    def bloquer_offre(self):
        # Méthode pour bloquer une offre
        self.etat_offre = 'Bloquée'
        print('Cette offre est Bloquée')

    def ligne_hebergement(self):
        return f"Date de début hébergement : {self.date_debut},\nNombre de nuit : {self.nbre_de_nuit},\nType d'hébergement : {self.type_hebergement},\nPrix de nuit : {self.prix_nuit}"

    def sauvegarder_dans_fichier(self, nom_fichier):
        with open(nom_fichier, 'a') as f:
            f.write(self.ligne_hebergement())

class OffreTransportAllerSimple(OffreVoyage):
    def __init__(self, ref_offre, ville_depart, ville_arrivee, date, prix):
        # Constructeur de la classe OffreTransportAllerSimple
        super().__init__(ref_offre, ville_depart, ville_arrivee)
        self.date = Date(0, 0, 0)
        self.prix = prix

    def saisir_aller_simple(self):
        # Méthode pour saisir les détails d'une offre de transport aller simple
        self.saisir_offre_voyage()
        self.prix = input("Entrer le prix : ")
        self.date.saisir_date("Entrer la date de départ : ")

    def update_price(self, prix):
        # Méthode pour mettre à jour le prix d'une offre de transport aller simple
        self.prix = prix

    def update_date(self):
        # Méthode pour mettre à jour la date de départ d'une offre de transport aller simple
        self.date = Date(0, 0, 0)
        self.date.saisir_date("Entrer la nouvelle date")

    def affichage_aller_simple(self):
        # Méthode pour afficher les détails d'une offre de transport aller simple
        print(f"Ville de départ: {self.ville_depart}\nVille d'arrivée: {self.ville_arrivee}\nDate de départ: {self.date}\nPrix: {self.prix}")

    def bloquer_offre(self):
        # Méthode pour bloquer une offre
        self.etat_offre = 'Bloquée'
        print('Cette offre est Bloquée')

    def ligne_transport_aller_simple(self):
        return f"Référence du offre: {self.ref_offre},\nVille de départ: {self.ville_depart},\nVille d'arrivée: {self.ville_arrivee},\nDate de départ: {self.date},\nPrix: {self.prix}"

    def sauvegarder_dans_fichier(self, nom_fichier):
        with open(nom_fichier, 'a') as f:
            f.write(self.ligne_transport_aller_simple())

