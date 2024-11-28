# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List
# from .predictor import TextCommandPredictor

# app = FastAPI(
#     title="Command Predictor API",
#     description="API pour prédire des commandes textuelles",
#     version="1.0.0"
# )

# # Initialiser le prédicteur une seule fois
# predictor = TextCommandPredictor()

# class CommandRequest(BaseModel):
#     command: List[str]

# class BatchCommandRequest(BaseModel):
#     commands: List[List[str]]

# class PredictionResponse(BaseModel):
#     prediction: str
#     probability: float

# class BatchPredictionResponse(BaseModel):
#     results: List[PredictionResponse]

# @app.post("/predict", response_model=PredictionResponse)
# async def predict_command(request: CommandRequest):
#     """Endpoint pour prédire une seule commande"""
#     try:
#         prediction, probability = predictor.predict_command(request.command)
#         return PredictionResponse(
#             prediction=prediction, 
#             probability=probability
#         )
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/batch-predict", response_model=BatchPredictionResponse)
# async def batch_predict_commands(request: BatchCommandRequest):
#     """Endpoint pour prédire plusieurs commandes"""
#     try:
#         batch_results = predictor.batch_predict(request.commands)
#         results = [
#             PredictionResponse(prediction=pred, probability=prob) 
#             for pred, prob in batch_results
#         ]
#         return BatchPredictionResponse(results=results)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/health")
# async def health_check():
#     """Endpoint de healthcheck"""
#     return {"status": "healthy"}



# import os
# import pickle
# import importlib
# from typing import List, Tuple, Dict
# from sklearn.pipeline import Pipeline
# import warnings
# from sklearn.exceptions import InconsistentVersionWarning
# class ModelManager:
#     def __init__(self, models_dir='/app/models'):
#         """
#         Gestionnaire de modèles avec chargement dynamique
        
#         Parameters:
#         -----------
#         models_dir : str
#             Répertoire contenant les modèles
#         """
#         self.models_dir = models_dir
#         self.loaded_models: Dict[str, Pipeline] = {}
#         self.list_available_models()
    
#     def list_available_models(self):
#         """
#         Liste tous les modèles disponibles dans le répertoire
#         """
#         self.available_models = [
#             f.replace('.pkl', '') 
#             for f in os.listdir(self.models_dir) 
#             if f.endswith('.pkl')
#         ]
#         print(f"Modèles disponibles : {self.available_models}")
#         return self.available_models
    
#     def load_model(self, model: str):
#         """
#         Charge un modèle spécifique
        
#         Parameters:
#         -----------
#         model : str
#             Nom du modèle à charger
        
#         Returns:
#         --------
#         Pipeline : Modèle chargé
#         """
#         # if model in self.loaded_models:
#         #     return self.loaded_models[model]
        
#         # model_path = os.path.join(self.models_dir, f"{model}.pkl")
        
#         # if not os.path.exists(model_path):
#         #     raise FileNotFoundError(f"Modèle {model} non trouvé")
        
#         # # with open(model_path, 'rb') as f:
#         # #     model = pickle.load(f)
#         # with open(model_path, 'rb') as f:
#         #     with warnings.catch_warnings():
#         #         warnings.filterwarnings(
#         #             'ignore', 
#         #             category=InconsistentVersionWarning
#         #         )
#         #         self.model = pickle.load(f)

#         # self.loaded_models[model] = model
#         # print(f"Modèle {model} chargé avec succès")
#         # return model

       
#         if model in self.loaded_models:
#             return self.loaded_models[model]
        
#         model_path = os.path.join(self.models_dir, f"{model}.pkl")
#         print(f"model_path: {model_path}")  # Print the model_path)
        
#         if not os.path.exists(model_path):
#             raise FileNotFoundError(f"Modèle {model} non trouvé")
        
#         with open(model_path, 'rb') as f:
#             with warnings.catch_warnings():
#                 warnings.filterwarnings(
#                     'ignore', 
#                     category=InconsistentVersionWarning
#                 )
#                 loaded_model = pickle.load(f)  # Ensure this is the model object
        
#         self.loaded_models[model] = loaded_model
#         print(f"Modèle {model} chargé avec succès")
#         return loaded_model  # Return the loaded model object
    
#     def predict_command(self, command: List[str], model: str = None) -> Tuple[str, float]:
#         """
#         Prédit la classe d'une commande avec un modèle spécifique
        
#         Parameters:
#         -----------
#         command : List[str]
#             Commande à prédire
#         model : str, optional
#             Nom du modèle à utiliser (défaut : premier modèle disponible)
        
#         Returns:
#         --------
#         Tuple[str, float] : Prédiction et probabilité
#         """
#         # if not model:
#         #     model = self.available_models[0]
        
#         # model = self.load_model(model)
        
#         # command_text = " ".join(command)
#         # prediction = model.predict([command_text])[0]
#         # probabilities = model.predict_proba([command_text])[0]
#         # max_probability = probabilities[list(model.classes_).index(prediction)]
        
#         # return prediction, float(max_probability), model
#         if not model:
#             model = self.available_models[0]
    
#             model = self.load_model(model)  # Ensure this is the model object
#             print(f"Type of model loaded: {type(model)}")
#             command_text = " ".join(command)
#             prediction = model.predict([command_text])[0]  # This should be valid if model is correct
#             probabilities = model.predict_proba([command_text])[0]
#             max_probability = probabilities[list(model.classes_).index(prediction)]
            
#             return prediction, float(max_probability)
    
#     def batch_predict(self, commands: List[List[str]], model: str = None) -> List[Tuple[str, float, str]]:
#         """
#         Prédit plusieurs commandes avec un modèle spécifique
        
#         Parameters:
#         -----------
#         commands : List[List[str]]
#             Commandes à prédire
#         model : str, optional
#             Nom du modèle à utiliser (défaut : premier modèle disponible)
        
#         Returns:
#         --------
#         List[Tuple[str, float, str]] : Liste de prédictions
#         """
#         if not model:
#             model = self.available_models[0]
        
#         model = self.load_model(model)
        
#         command_texts = [" ".join(cmd) for cmd in commands]
#         predictions = model.predict(command_texts)
#         probabilities = model.predict_proba(command_texts)
        
#         results = []
#         for pred, prob_array in zip(predictions, probabilities):
#             max_probability = prob_array.max()
#             results.append((pred, float(max_probability), model))
        
#         return results


# import pickle
# import os

# class TextCommandPredictor:
#     def __init__(self, model_path):
#         self.model_path = model_path
#         self.model = None
#         self.load_model()
    
#     def load_model(self):
#         if not os.path.exists(self.model_path):
#             raise FileNotFoundError(f"Model not found at {self.model_path}")
        
#         with open(self.model_path, 'rb') as f:
#             self.model = pickle.load(f)
    
#     def predict_command(self, command_text):
#         if self.model is None:
#             raise ValueError("Model not loaded")
        
#         prediction = self.model.predict([command_text])[0]
#         probabilities = self.model.predict_proba([command_text])[0]
#         max_probability = probabilities[list(self.model.classes_).index(prediction)]
        
#         return prediction, float(max_probability)

import pickle
import os

class TextCommandPredictor:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        self.load_model()
    
    def load_model(self):
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Model not found at {self.model_path}")
        
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
    
    def predict_command(self, command_text):
        if self.model is None:
            raise ValueError("Model not loaded")
        
        prediction = self.model.predict([command_text])[0]
        probabilities = self.model.predict_proba([command_text])[0]
        max_probability = probabilities[list(self.model.classes_).index(prediction)]
        
        return prediction, float(max_probability)