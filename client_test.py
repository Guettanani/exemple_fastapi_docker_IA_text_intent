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

# import requests

# # Base URL of the FastAPI server
# BASE_URL = "http://10.31.24.63:8002"  # Replace with your server address if different

# # Endpoint
# PREDICT_ENDPOINT = f"{BASE_URL}/predict"

# # Sample request data
# request_data = {
#     "command": "play the music",
#     "model_name": "logistic_regression_model.pkl"
# }

# def send_predict_request(data):
#     try:
#         # Sending POST request to the FastAPI server
#         response = requests.post(PREDICT_ENDPOINT, json=data)
        
#         # Checking the response status
#         if response.status_code == 200:
#             print("Prediction Response:")
#             print(response.json())
#         else:
#             print(f"Error: {response.status_code} - {response.json()}")
#     except requests.exceptions.RequestException as e:
#         print(f"Request failed: {e}")

# if __name__ == "__main__":
#     send_predict_request(request_data)

import requests

# Base URL of the FastAPI server
BASE_URL = "http://192.168.0.100:8002"  # Replace with your server address if different

# Endpoint
PREDICT_ENDPOINT = f"{BASE_URL}/predict"



def send_predict_request(data):
    # Sample request data

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

import time

if __name__ == "__main__":
    commands = [
        "turn down the sound",
        "reduce the volume",
        "lower the volume",
        "decrease the sound",
        "read playlist Disco",
        "launch playlist Disco",
        "play playlist Disco",
        "start playlist Disco",
        "open playlist Disco",
        "read playlist Classical",
        "launch playlist Classical",
        "play playlist Classical",
        "start playlist Classical",
        "open playlist Classical",
        "read playlist Electro",
        "launch playlist Electro",
        "play playlist Electro",
        "start playlist Electro",
        "open playlist Electro",
        "read playlist Hip-Hop",
        "launch playlist Hip-Hop",
        "play playlist Hip-Hop",
        "start playlist Hip-Hop",
        "open playlist Hip-Hop",
        "read playlist Jazz",
        "launch playlist Jazz",
        "play playlist Jazz",
        "start playlist Jazz",
        "open playlist Jazz",
        "read playlist Rock",
        "launch playlist Rock",
        "play playlist Rock",
        "start playlist Rock",
        "open playlist Rock",
        "launch the turbulence scenario",
        "launch the turbulence mode",
        "put yourself in turbulence mode",
        "activate turbulence mode",
        "start the turbulence scenario",
        "launch the meeting",
        "start the meeting",
        "start the video",
        "launch the video conference",
        "begin the meeting",
        "connect to videoconferencing",
        "join the video call",
        "connect to video call",
        "join the conference",
        "start video conferencing",
        "disconnect from the meeting",
        "leave the meeting",
        "exit the meeting",
        "end the call",
        "hang up the conference",
        "launch the evacuation scenario",
        "launch evacuation mode",
        "set evacuation mode",
        "activate evacuation mode",
        "initiate the evacuation process",
        "launch sky guesser",
        "start sky guesser",
        "activate sky guesser",
        "play sky guesser",
        "begin sky guesser",
        "launch the game",
        "start the game",
        "activate the game",
        "play the game",
        "begin the game",
        "answer the call",
        "pick up the phone",
        "take the call",
        "accept the call",
        "respond to the call",
        "launch podcast La french touch",
        "open podcast La french touch",
        "play podcast La french touch",
        "start podcast La french touch",
        "begin podcast La french touch",
        "put the next podcast",
        "next podcast",
        "play the next podcast",
        "switch to the next podcast",
        "move to the next podcast",
        "put on the previous podcast",
        "previous podcast",
        "play the previous podcast",
        "switch to the previous podcast",
        "move to the previous podcast",
        "put on the last podcast",
        "last podcast",
        "play the last podcast",
        "switch to the last podcast",
        "move to the last podcast",
        "put on the next song",
        "next song",
        "play the next song",
        "switch to the next song",
        "move to the next track",
        "put on the previous song",
        "previous song",
        "play the previous song",
        "switch to the previous song",
        "move to the previous track",
        "put on the last song",
        "last song",
        "play the last song",
        "switch to the last song",
        "move to the last track",
        "show me the lyrics",
        "display the lyrics",
        "give me the lyrics",
        "what are the lyrics",
        "lyrics please",
        "launch the karaoke",
        "start karaoke",
        "activate karaoke mode",
        "begin karaoke",
        "open karaoke",
        "start a blind test",
        "launch a blind test",
        "begin blind test",
        "play a blind test",
        "activate blind test mode",
        "what's the title of the track",
        "tell me the song title",
        "what song is this",
        "name of the song",
        "track title please",
        "launch intro Odyssey mode",
        "put yourself in intro Odyssey mode",
        "activate intro Odyssey scenario",
        "start intro Odyssey mode",
        "initiate intro Odyssey scenario",
        "launch take off mode",
        "put yourself in take off mode",
        "activate take off scenario",
        "start take off mode",
        "initiate take off scenario",
        "launch landing mode",
        "put yourself in landing mode",
        "activate landing scenario",
        "start landing mode",
        "initiate landing scenario",
        "launch the Interstellar film",
        "set the Interstellar film",
        "play movie Interstellar",
        "show Interstellar movie",
        "display Interstellar film",
        "launch The Dark Knight film",
        "set the The Dark Knight film",
        "play movie The Dark Knight",
        "show The Dark Knight movie",
        "display The Dark Knight film",
        "launch the Inception film",
        "set the Inception film",
        "play movie Inception",
        "show Inception movie",
        "display Inception film",
        "launch the Inglorious Bastards film",
        "set the Inglorious Bastards film",
        "play movie Inglorious Bastards",
        "show Inglorious Bastards movie",
        "display Inglorious Bastards film",
        "launch the Léon film",
        "set the Léon film",
        "play movie Léon",
        "show Léon movie",
        "display Léon film",
        "launch the Ready Player One film",
        "set the Ready Player One film",
        "play movie Ready Player One",
        "show Ready Player One movie",
        "display Ready Player One film",
        "launch the Spider Man film",
        "set the Spider Man film",
        "play movie Spider Man",
        "show Spider Man movie",
        "display Spider Man film",
        "launch the Star Wars film",
        "set the Star Wars film",
        "play movie Star Wars",
        "show Star Wars movie",
        "display Star Wars film",
        "I would like a glass of champagne",
        "can I have champagne",
        "please serve champagne",
        "bring me champagne",
        "champagne please",
        "when do we eat",
        "how soon is dinner",
        "how much longer until we eat",
        "what time is the meal",
        "when is mealtime",
        "what time will the meal be served?",
        "when does the meal start?",
        "what are we eating today",
        "today's meal",
        "what's on the menu",
        "what food is available today",
        "today's dining options",
        "what is there to drink",
        "available drinks",
        "what drinks do you have",
        "drink options",
        "beverage list please"
    ]
    
    for command in commands:
        request_data = {
            "command": command,
            "model_name": "logistic_regression_model.pkl"
        }
        send_predict_request(request_data)
        time.sleep(5)  # Délai de 5 secondes entre chaque envoi

        # cont = input("Voulez-vous continuer ? (o/n) ")

# …or create a new repository on the command line
# echo "# exemple_fastapi_docker_IA_text_intent" >> README.md
# git init
# git add README.md
# git commit -m "first commit"
# git branch -M main
# git remote add origin git@github.com:Guettanani/exemple_fastapi_docker_IA_text_intent.git
# git push -u origin main
# …or push an existing repository from the command line
# git remote add origin git@github.com:Guettanani/exemple_fastapi_docker_IA_text_intent.git
# git branch -M main
# git push -u origin main
