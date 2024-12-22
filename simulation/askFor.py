# Noé Game E2

def AName(question):
    """
    Fait saisir un nom tant que l'entrée utilisateur n'est pas conforme.
    Un nom doit contenir uniquement des lettres.
    """
    while True:
        try :
            reponse = input(question)
            if not reponse.isalpha():
                raise Exception("Le nom ne doit contenir que des lettres.")
        except Exception as E:
            print(E)
        else :
            return reponse
        
def ANumber(question):
    """
    Fait saisir un nombre tant que l'entrée utilisateur n'est pas conforme.
    Un nombre doit contenir uniquement des chiffres.
    """
    while True:
        try :
            reponse = int(input(question))
        except ValueError:
            print("Vous n'avez pas entré un nombre.")
        except Exception as E:
            print(E)
        else :
            return reponse

def ABoundedNumber(question,nbMin,nbMax):
    """
    Fait saisir un nombre tant que l'entrée utilisateur n'est pas conforme.
    Un nombre doit contenir uniquement des chiffres.
    Le nombre doit être compris entre nbMin et nbMax.
    """
    while True:
        try :
            reponse = int(input(question))
            if reponse < nbMin or reponse > nbMax :
                raise Exception(f"Le nombre doit être compris entre {nbMin} et {nbMax}.")
        except ValueError:
            print("Vous n'avez pas entré un nombre.")
        except Exception as E:
            print(E)
        else :
            return reponse
        
def APositiveNumber(question):
    """
    Fait saisir un nombre tant que l'entrée utilisateur n'est pas conforme.
    Le nombre doit contenir uniquement des chiffres.
    Le nombre doit être positif.
    """
    while True:
        try :
            reponse = int(input(question))
            if reponse < 0 :
                raise Exception("Le nombre doit être positif.")
        except ValueError:
            print("Vous n'avez pas entré un nombre.")
        except Exception as E:
            print(E)
        else :
            return reponse


def ABornDate(question):
    """
    Fait saisir un date de naissance tant que l'entrée utilisateur n'est pas conforme.
    Une date de naissance doit contenir uniquement des chiffres et des '/'.
    La date de naissance doit correspondre à une personne majeure.
    """
    while True:
        try :
            date = input(f"{question} (jj/mm/aaaa) : ")
            jour,mois,annee = date.split("/")
            if int(jour) < 1 or int(jour) > 31 or int(mois) < 1 or int(mois) > 12 or int(annee) < 1930 or int(annee) > 2025:
                raise Exception("La date n'est pas valide.")
            if 2025 - int(annee) < 18:
                raise Exception("Vous devez avoir plus de 18 ans.")
        except ValueError:
            print("Vous n'avez pas entré une date.")
        except Exception as E:
            print(E)
        else :
            return date


def ADate(question):
    """
    Fait saisir un date tant que l'entrée utilisateur n'est pas conforme.
    Une date  doit contenir uniquement des chiffres et des '-'.
    La date doit être de l'année en cours (2024 ou 2025 ou 2026).
    """
    while True:
        try :
            date = input(f"{question} (jj-mm-aaaa) : ")
            jour,mois,annee = date.split("-")
            if int(jour) < 1 or int(jour) > 31 or int(mois) < 1 or int(mois) > 12 or int(annee) < 2024 or int(annee) > 2026:
                raise Exception("La date n'est pas valide.")
        except ValueError:
            print("Vous n'avez pas entré une date.")
        except Exception as E:
            print(E)
        else :
            return date

def APassword(question):
    """
    Fait saisir un mot de passe tant que l'entrée utilisateur n'est pas conforme.
    Un mot de passe doit contenir uniquement des chiffres et des lettres.
    Un mot de passe doit contenir 8 caractères.
    """
    while True:
        try :
            reponse = input(question)
            if len(reponse) < 8 :
                raise Exception("Le mot de passe doit contenir au moins 8 caractères.")
        except Exception as E:
            print(E)
        else :
            return reponse
        
def AEmail(question):
    """
    Fait saisir une adresse email tant que l'entrée utilisateur n'est pas conforme.
    Une adresse email doit contenir au minimum un '@' et un '.' après le '@'.
    """
    while True:
        try :
            reponse = input(question)
            if "@" not in reponse or "." not in reponse:
                raise Exception("L'email n'est pas valide.")
            if reponse.count("@") > 1 or reponse.count(".") > 1:
                raise Exception("L'email n'est pas valide.")
            if reponse.index("@") > reponse.index("."):
                raise Exception("L'email n'est pas valide.")
            if len(reponse) < 5:
                raise Exception("L'email n'est pas valide.")
        except Exception as E:
            print(E)
        else :
            return reponse
        
def APhoneNumber(question):
    """
    Fait saisir un numéro de téléphone tant que l'entrée utilisateur n'est pas conforme.
    Un numéro de téléphone doit être composé de 10 chiffres.
    """
    while True:
        try :
            reponse = input(question)
            if len(reponse) != 10:
                raise Exception("Le numéro de téléphone doit contenir 10 chiffres.")
            if not reponse.isdigit():
                raise Exception("Le numéro de téléphone doit contenir que des chiffres.")
            if reponse[0] != "0":
                raise Exception("Le numéro de téléphone doit commencer par 0.")
        except Exception as E:
            print(E)
        else :
            return reponse

def TypeAbonnement():
    """
    Fait saisir  tant que l'entrée utilisateur n'est pas conforme.
    Un type d'abonnement doit être uniquement P ou B.
    """
    while True : 
        try : 
            typeAbonnement = input("Saisir le type de l'abbonement : ")
            if typeAbonnement  != 'B' and typeAbonnement != 'P':
                raise Exception("Le type d'abonnement doit être P ou B")
        except Exception as E:
            print(E)
        else :
            return typeAbonnement
        
def NumeroAbonne(liste):
    """
    Fait saisir un numéro d'abonnement tant que l'entrée utilisateur n'est pas conforme.
    Un numéro d'abonnement unique ne doit pas déjà être attribué.
    Un numéro d'abonnement doit être composé uniquement de lettre et de chiffre.
    """
    while True : 
        try : 
            numero = input("Saisir le numero de l'abonne : ")
            
            if len(numero)  != 6 :
                raise Exception("Le numero d'abonnement doit contenir 6 caracteres")
            
            for dico in liste:
                if numero == dico["Numero Abonne"]:
                    raise Exception("Le numero d'abonnement existe déjà.")

            for i in range(1,6):
                if numero[i].isalpha == True or numero[i].isdigit == True:
                    raise Exception("Les caracteres doivent être des chiffres ou des lettres.")
        
        except Exception as E:
            print(E)
        else :
            return numero
