class Date():
    def __init__(self,jour,mois,annee):
        self.jour=jour
        self.mois=mois
        self.annee=annee
    def Saisir_Date(self , msg=""):
            print(msg)
            self.jour= input("Day: ")
            self.mois= input("Month: ")
            self.annee= input("Year: ")
            return str(self.jour)+ "/" + str(self.mois) + "/"+ str(self.annee)
    def __str__(self):
            return str(self.jour)+ "/" + str(self.mois) + "/"+ str(self.annee)
class Offre_voyage():
    def __init__(self,Ref_offre,Ville_depart,Ville_arrivee):
        self.Ref_offre=Ref_offre
        self.Ville_depart=Ville_depart
        self.Ville_arrivee=Ville_arrivee
    def Saisir_Offre_Voyage(self):
        self.Ref_offre=(input("Entrer le referance du offre : "))
        self.Ville_depart=input("Entrer la ville de depart : ")
        self.Ville_arrivee=input("Entrer la ville d arrivee: ")
    def Afficher_Offre_Voyage(self):
        print(' Ref_Offre:',self.Ref_offre,'\n','la ville de depart :',self.Ville_depart,'\n','la ville d arrivee:',self.Ville_arrive)
    def __str__(self) :
        return "Offre: Voyage"
    def Bloquer_Offre(self):
        self.etat_offre='Bloquee'
        print('Ce offre est Bloquee')
class Hebergement():
    def __init__(self,Date_debut,Nbre_de_nuit,Type,Prix_nuit):
        self.Date_debut=Date(0, 0,0)
        self.Nbre_de_nuit=Nbre_de_nuit
        self.Type=Type
        self.Prix_nuit=Prix_nuit
    def Saisir_Hebergement(self):
        self.Date_debut=self.Date_debut.Saisir_Date("Entrer la date du debut : ")
        self.Nbre_de_nuit=input("Entrer le nombre de nuit  : ")
        self.Type=input("Entrer le type : (déjeuner, demi-pension, pension complète)  ")
        self.Prix_nuit=input("Entrer le prix de nuit : ")
    def Afficher_Hebergement(self):
        print(' Date_debut:',self.Date_debut,'\n','Le Nombre de nuit :',self.Nbre_de_nuit,'\n','Type:',self.Type,'\n','Le prix de la nuit :',self.Prix_nuit)
    def Bloquer_Offre(self):
        self.etat_offre='Bloquee'
        print('Ce offre est Bloquee')
    def ligneHebergement(self):
            return (
                f"Date de debut hebergement : {self.Date_debut}, \n"
                f"Nombre de nuit : {self.Nbre_de_nuit},\n "
                f"Type d hebergement: {self.Type},\n "
                f"Prix de nuit : {self.Prix_nuit} ")
    def SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.ligneHebergement())
class Offre_Transport_Aller_Simple(Offre_voyage):
    def __init__(self,Ref_offre,Ville_depart, Ville_arrivee ,date , Prix ):
        Offre_voyage.__init__(self, Ref_offre, Ville_depart, Ville_arrivee)
        self.date=Date(0,0,0)
        self.Prix=Prix
    def Saisir_Aller_simple(self):
        self.Saisir_Offre_Voyage()
        self.Prix=input("Entrer le prix: ")
        self.date=self.date.Saisir_Date("Entrer la date de depart : ")
    def UpdatePrice(self , Prix):
        self.Prix=Prix
    def UpdateDate(self):
        self.date=Date(0,0,0)
        self.date.Saisir_Date("Entrer la nouvelle date")
    def Affichage_Aller_simple(self):
        print('la ville de depart :',self.Ville_depart,'\n','la ville d arrivee:',self.Ville_arrivee,'\n','la date de depart:',self.date,'\n','prix :',self.Prix,'\n','la date de depart:',self.date)
    def Bloquer_Offre(self):
        self.etat_offre='Bloquee'
        print('Ce offre est Bloquee')
    def ligneTransportA(self):
            return (
                f"Reference du offre  : {self.Ref_offre}, \n"
                f"Ville de depart : {self.Ville_depart},\n "
                f"Ville d arrivee: {self.Ville_arrivee},\n "
                f"Date de depart : {self.date},\n "
                f"Prix :{self.Prix},\n  ")
    def SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.LigneTransportA())
class Offre_Transport_Aller_Retour(Offre_Transport_Aller_Simple):
    def __init__(self,Ref_offre,Ville_depart, Ville_arrivee ,date ,date_arrivee, Prix ):
        super().__init__(Ref_offre,Ville_depart, Ville_arrivee ,date,Prix)
        self.date_arrivee=Date(0,0,0)
    def Saisir_Aller_Retour(self):
        self.Saisir_Aller_simple()
        self.date_arrivee=self.date_arrivee.Saisir_Date("Entrer la date d arrivee : ")
        
    def Affichage_Aller_Retour(self):
        self.Affichage_Aller_simple()
        print('la date d arrivee :',self.date_arrivee)
    def Bloquer_Offre(self):
        self.etat_offre='Bloquee'
        print('Ce offre est Bloquee')
    def ligneTransportAR(self):
            return (
                f"Reference du offre  : {self.Ref_offre}, \n"
                f"Ville de depart : {self.Ville_depart},\n "
                f"Ville d arrivee: {self.Ville_arrivee},\n "
                f"Date de depart : {self.date},\n "
                f"Date d arrivee : {self.date_arrivee}"
                f"Prix :{self.Prix},\n  "
                )
    def SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.ligneTransportAR())
class Formule_complet(Offre_Transport_Aller_Retour,Hebergement):
    def __init__(self,Ref_offre='',Ville_depart='', Ville_arrivee='' ,date=Date(0,0,0), Prix=0,date_depart=Date(0,0,0),Type='' ,date_arrivee=Date(0,0,0), Date_debut=Date(0,0,0),Nbre_de_nuit=0,Prix_nuit=0):
        Offre_Transport_Aller_Retour.__init__(self,Ref_offre,Ville_depart, Ville_arrivee ,date,date_depart ,date_arrivee, Prix)
        Hebergement.__init__(self,Date_debut,Nbre_de_nuit,Type,Prix_nuit)
    def Saisir_Complet(self):
        self.Saisir_Aller_Retour()
        self.Saisir_Hebergement()
    def Affichage_Complet(self):
        self.Affichage_Aller_Retour()
        self.Afficher_Hebergement()
    def SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.ligneTransportAR())
             F.write(self.ligneHebergement())
    def Bloquer_Offre(self):
        self.etat_offre='Bloquee'
        print('Ce offre est Bloquee')
class Reservation:
    def __init__(self ):
        self.Ref_réservation=''
        self.Type_Offre=""
        self.Ref_Offre=""
        self.Date_départ=Date(0,0,0)
        self.Date_de_retour=Date(0,0,0)
        self.Genre=''
        self.Nom=''
        self.prenom=''
        self.Pays=''
        self.n_passport=''
        self.Etat_Reservation="en cours"
        self.prix_hebergement=0
        self.prix_voyage_simple=0
        self.prix_voyage_AR=0
        self.Total_A_Payer=0
    def CreateReservation(self):
        self.Ref_réservation=(input("Entrer le referance de reservation : "))
        print("List des offres : ")
        print("1 - Voyage A")
        print("2 - Voyage A/R")
        print("3 - Accommodation")
        print("4 - Formule complet")
        choice=int(input("Choix:"))
        self.Type_Offre=choice
        self.Ref_Offre=input("Entrer le reference du offre : ")
        self.Date_départ=self.Date_départ.Saisir_Date('Entrer la date de depart')
        if choice==2 or choice ==4:
            self.Date_de_retour=self.Date_de_retour.Saisir_Date('Entrer la date de retour')
        self.Genre=input("Entrer le genre: ")
        self.Nom=input("Entrer le Nom: ")
        self.Prenom=input("Entrer le Prenom: ")
        self.Pays=input("Entrer la nationalite : ")
        self.n_passport=input("Entrer le Numero de passport : ")
        if choice==1:
            self.prix_voyage_simple=input("Entrer le prix du voyage simple : ")
            self.Total_A_Payer=self.prix_voyage_simple
        elif choice==2:
            self.prix_voyage_AR=input("Entrer le prix du voyage Aller-Retour : ")
            self.Total_A_Payer=self.prix_voyage_AR
        elif choice==3:
            self.prix_hebergement=input("Entrer le prix d hebergement : ")
            self.Total_A_Payer=self.prix_hebergement
        elif choice ==4:
            self.prix_voyage_AR=input("Entrer le prix du voyage Aller-Retour : ")
            self.prix_hebergement=input("Entrer le prix d hebergement : ")
            self.Total_A_Payer=self.prix_voyage_AR+self.prix_hebergement
    def Confirmer_reservation(self):
        self.Etat_Reservation="Confirmee"
    def Annuler_reservation(self):
        self.Etat_Reservation="Annulee"
    def LigneReservation(self):
        return (
            f"Reference de reservation : {self.Ref_réservation}, \n"
            f"Type d offre : {self.Type_Offre},\n"
            f"Referene du offre : {self.Ref_Offre},\n"
            f"Date de depart : {self.Date_départ},\n"
            f"Date de retour : {self.Date_de_retour},\n"
            f"Le genre : {self.Genre},\n"
            f"Le nom : {self.Nom},\n"
            f"Le prenom : {self.prenom},\n"
            f"Le pays : {self.Pays},\n"
            f"N_Passport : {self.n_passport},\n"
            f"Etat de reservation : {self.Etat_Reservation},\n"
            )
    def  SauvegarderDansFichier(self, NomFichier):
         with open(NomFichier, 'a') as F:
             F.write(self.ligneReservation())
        
        
        
    
        
        
        
        
        
        
        
#aa=Formule_complet()
#aa.Saisir_Complet()
#aa.Affichage_Complet()
#aa.SauvegarderDansFichier('Voyagedb.json')      
#ss=Offre_voyage('','', '')
#ss.Saisir_Offre_Voyage()
#ss.Afficher_Offre_Voyage()
dd=Hebergement('', 0, '', 0)
dd.Saisir_Hebergement()
dd.Afficher_Hebergement()
dd.SauvegarderDansFichier('Voyagedb.json')   
#ee=Offre_Transport_Aller_Simple('','','', '',0)
#ee.Saisir_Aller_simple()
#ee.Affichage_Aller_simple()
#ee.UpdateDate()
#ee.UpdatePrice(2000)
#ee.Affichage_Aller_simple()

#hh=Offre_Transport_Aller_Retour('','','','','','', 0)
#hh.Saisir_Aller_Retour()
#hh.Affichage_Aller_Retour()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        