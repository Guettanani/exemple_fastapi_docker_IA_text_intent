# import httpx
# from typing import List, Optional

# class CommandPredictorClient:
#     def __init__(self, base_url: str):
#         """
#         Initialise le client pour le service FastAPI.

#         :param base_url: URL de base de l'API (ex: http://localhost:8000)
#         """
#         self.base_url = base_url

#     def predict_command(self, command: List[str], model_name: Optional[str] = None):
#         """
#         Prédire une commande unique.

#         :param command: Liste de mots représentant la commande
#         :param model_name: Nom du modèle à utiliser (optionnel)
#         :return: Dictionnaire contenant la prédiction, la probabilité et le nom du modèle
#         """
#         payload = {"command": command}
#         if model_name:
#             payload["model_name"] = model_name
        
#         response = httpx.post(f"{self.base_url}/predict", json=payload)
#         response.raise_for_status()
#         return response.json()

#     def batch_predict(self, commands: List[List[str]], model_name: Optional[str] = None):
#         """
#         Prédire plusieurs commandes.

#         :param commands: Liste de listes de mots représentant les commandes
#         :param model_name: Nom du modèle à utiliser (optionnel)
#         :return: Liste de dictionnaires contenant les prédictions, probabilités et noms des modèles
#         """
#         payload = {"commands": commands}
#         if model_name:
#             payload["model_name"] = model_name
        
#         response = httpx.post(f"{self.base_url}/batch-predict", json=payload)
#         response.raise_for_status()
#         return response.json()

#     def list_models(self):
#         """
#         Obtenir la liste des modèles disponibles.

#         :return: Liste des noms de modèles disponibles
#         """
#         response = httpx.get(f"{self.base_url}/models")
#         response.raise_for_status()
#         return response.json()

#     def health_check(self):
#         """
#         Vérifier la santé du service.

#         :return: Statut et liste des modèles disponibles
#         """
#         response = httpx.get(f"{self.base_url}/health")
#         response.raise_for_status()
#         return response.json()


# # Exemple d'utilisation
# if __name__ == "__main__":
#     base_url = "http://localhost:8000"  # Remplacez par l'URL appropriée
#     client = CommandPredictorClient(base_url)

#     # Vérifier la santé du service
#     health = client.health_check()
#     print("Health Check:", health)

#     # Lister les modèles disponibles
#     models = client.list_models()
#     print("Available Models:", models)

#     # Prédire une commande unique
#     command = ["open", "file", "document.txt"]
#     prediction = client.predict_command(command, model_name="logistic_regression")
#     print("Prediction:", prediction)

#     # Prédire plusieurs commandes
#     batch_commands = [
#         ["open", "file", "document.txt"],
#         ["delete", "folder", "backup"],
#         ["copy", "image", "photo.jpg"]
#     ]
#     batch_predictions = client.batch_predict(batch_commands, model_name="logistic_regression")
#     print("Batch Predictions:", batch_predictions)


# import requests
# from typing import List, Optional

# class CommandPredictorClient:
#     def __init__(self, base_url: str):
#         """
#         Initialise le client avec l'URL de base de l'API.
        
#         :param base_url: URL de base de l'API (par exemple, "http://localhost:8002")
#         """
#         self.base_url = base_url

#     def predict_command(self, command: List[str], model_name: Optional[str] = None):
#         """
#         Prédire une commande.
        
#         :param command: Liste de mots représentant la commande.
#         :param model_name: Nom optionnel du modèle à utiliser.
#         :return: Dictionnaire contenant la prédiction, la probabilité et le modèle utilisé.
#         """
#         url = f"{self.base_url}/predict"
#         payload = {"command": command}
#         if model_name:
#             payload["model_name"] = model_name

#         response = requests.post(url, json=payload)

#         if response.status_code == 200:
#             return response.json()
#         else:
#             response.raise_for_status()

#     def batch_predict(self, commands: List[List[str]], model_name: Optional[str] = None):
#         """
#         Prédire plusieurs commandes en batch.
        
#         :param commands: Liste de commandes (chaque commande est une liste de mots).
#         :param model_name: Nom optionnel du modèle à utiliser.
#         :return: Liste de dictionnaires contenant les prédictions, probabilités et modèles utilisés.
#         """
#         url = f"{self.base_url}/batch-predict"
#         payload = {"commands": commands}
#         if model_name:
#             payload["model_name"] = model_name

#         response = requests.post(url, json=payload)

#         if response.status_code == 200:
#             return response.json()
#         else:
#             response.raise_for_status()

#     def list_models(self):
#         """
#         Lister les modèles disponibles.
        
#         :return: Liste des modèles disponibles.
#         """
#         url = f"{self.base_url}/models"
#         response = requests.get(url)

#         if response.status_code == 200:
#             return response.json()
#         else:
#             response.raise_for_status()

#     def health_check(self):
#         """
#         Vérifier la santé de l'API.
        
#         :return: Dictionnaire indiquant l'état de santé de l'API.
#         """
#         url = f"{self.base_url}/health"
#         response = requests.get(url)

#         if response.status_code == 200:
#             return response.json()
#         else:
#             response.raise_for_status()


# # Exemple d'utilisation
# if __name__ == "__main__":
#     client = CommandPredictorClient(base_url="http://localhost:8002")

#     # Prédire une commande
#     try:
#         prediction = client.predict_command(command=["open", "file", "document.txt"])
#         print("Prédiction unique:", prediction)
#     except Exception as e:
#         print("Erreur lors de la prédiction unique:", e)

#     # Prédire plusieurs commandes en batch
#     try:
#         batch_prediction = client.batch_predict(commands=[
#             ["open", "file", "document.txt"],
#             ["delete", "folder", "backup"]
#         ])
#         print("Prédictions batch:", batch_prediction)
#     except Exception as e:
#         print("Erreur lors de la prédiction batch:", e)

#     # Lister les modèles disponibles
#     try:
#         models = client.list_models()
#         print("Modèles disponibles:", models)
#     except Exception as e:
#         print("Erreur lors de la récupération des modèles:", e)

#    # Demander à l'utilisateur de saisir le nom du modèle
#     model_name = input("Veuillez entrer le nom du modèle à utiliser (ou appuyez sur Entrée pour utiliser le modèle par défaut) : ").strip()

#     # Définir des commandes pour la prédiction
#     commands = [
#         ["open", "file", "document.txt"],
#         ["delete", "folder", "backup"]
#     ]

#     try:
#         # Appeler la prédiction en batch avec le modèle spécifié
#         batch_prediction = client.batch_predict(
#             commands=commands,
#             model_name=model_name if model_name else None  # Utiliser None si l'utilisateur n'entre rien
#         )
#         print("Prédictions batch avec modèle spécifié:", batch_prediction)
#     except Exception as e:
#         print("Erreur lors de la prédiction batch avec un modèle spécifique:", e)


#     # Vérifier la santé de l'API
#     try:
#         health = client.health_check()
#         print("État de santé de l'API:", health)
#     except Exception as e:
#         print("Erreur lors du health check:", e)

import requests

# Base URL of the FastAPI server
BASE_URL = "http://10.31.24.63:8002"  # Replace with your server address if different

# Endpoint
PREDICT_ENDPOINT = f"{BASE_URL}/predict"

# Sample request data
request_data = {
    "command": "play the music",
    "model_name": "logistic_regression_model.pkl"
}

def send_predict_request(data):
    try:
        # Sending POST request to the FastAPI server
        response = requests.post(PREDICT_ENDPOINT, json=data)
        
        # Checking the response status
        if response.status_code == 200:
            print("Prediction Response:")
            print(response.json())
        else:
            print(f"Error: {response.status_code} - {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

if __name__ == "__main__":
    send_predict_request(request_data)
