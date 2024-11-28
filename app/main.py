# import pickle
# import os
# import numpy as np
# from typing import List, Tuple

# class TextCommandPredictor:
#     def __init__(self, model_path='/app/models/logistic_regression_model.pkl'):
#         self.model_path = model_path
#         self.model = None
#         self.load_model()
    
#     def load_model(self):
#         """Charge le modèle pickle"""
#         if not os.path.exists(self.model_path):
#             raise FileNotFoundError(f"Modèle non trouvé à {self.model_path}")
        
#         with open(self.model_path, 'rb') as f:
#             self.model = pickle.load(f)
    
#     def predict_command(self, command: List[str]) -> Tuple[str, float]:
#         """Prédit la classe d'une commande"""
#         if self.model is None:
#             raise ValueError("Le modèle n'est pas chargé")
        
#         command_text = " ".join(command)
#         prediction = self.model.predict([command_text])[0]
#         probabilities = self.model.predict_proba([command_text])[0]
#         max_probability = probabilities[list(self.model.classes_).index(prediction)]
        
#         return prediction, float(max_probability)
    
#     def batch_predict(self, commands: List[List[str]]) -> List[Tuple[str, float]]:
#         """Prédit plusieurs commandes"""
#         command_texts = [" ".join(cmd) for cmd in commands]
#         predictions = self.model.predict(command_texts)
#         probabilities = self.model.predict_proba(command_texts)
        
#         results = []
#         for pred, prob_array in zip(predictions, probabilities):
#             max_probability = prob_array.max()
#             results.append((pred, float(max_probability)))
        
#         return results


# from fastapi import FastAPI, HTTPException, Query
# from pydantic import BaseModel
# from typing import List, Optional
# from .predictor import ModelManager
# import logging
# logging.basicConfig(level=logging.INFO)

# app = FastAPI(
#     title="Command Predictor API",
#     description="API pour prédire des commandes textuelles avec plusieurs modèles",
#     version="1.1.0"
# )

# # Initialiser le gestionnaire de modèles
# model_manager = ModelManager()

# class CommandRequest(BaseModel):
#     command: List[str]
#     model: Optional[str] = None

# class BatchCommandRequest(BaseModel):
#     commands: List[List[str]]
#     model: Optional[str] = None

# class PredictionResponse(BaseModel):
#     prediction: str
#     probability: float
#     model: str

# class BatchPredictionResponse(BaseModel):
#     results: List[PredictionResponse]

# @app.post("/predict", response_model=PredictionResponse)
# async def predict_command(request: CommandRequest):
#     """
#     Prédire une commande avec un modèle spécifique
    
#     - Si aucun modèle n'est spécifié, utilise le modèle par défaut (logistic_regression_model)
#     - Supporte plusieurs modèles via le paramètre `model`
#     """
#     logging.info(f"Requête reçue : {request}")
#     try:
#         try:
#             model_name = request.model or "logistic_regression_model"
#             prediction, probability, model = model_manager.predict_command(
#                 request.command, 
#                 model_name
#             )
#             return PredictionResponse(
#                 prediction=prediction, 
#                 probability=probability,
#                 model=model
#             )
#         except FileNotFoundError as e:
#             raise HTTPException(status_code=404, detail=str(e))
#         except Exception as e:
#             raise HTTPException(status_code=500, detail=str(e))
#     except Exception as e:
#         logging.error(f"Erreur dans /predict : {e}")
#         raise HTTPException(status_code=500, detail="Erreur interne du serveur")

# @app.post("/predict", response_model=PredictionResponse)
# async def predict_command(request: CommandRequest):
#     logging.info(f"Requête reçue : {request}")
#     try:
#         model_name = request.model or "logistic_regression_model"
#         logging.info(f"Using model: {model_name}")
        
#         # Add explicit type checking and logging
#         result = model_manager.predict_command(request.command, model_name)
#         logging.info(f"Prediction result: {result}")
        
#         if result is None:
#             raise ValueError("Prediction returned None")
        
#         prediction, probability, model = result
#         return PredictionResponse(
#             prediction=prediction, 
#             probability=probability,
#             model=model
#         )
#     except Exception as e:
#         logging.error(f"Detailed error in /predict: {e}", exc_info=True)
#         raise HTTPException(status_code=500, detail=str(e))

# from typing import List, Tuple  # Add this import at the top of the file
# @app.post("/predict", response_model=PredictionResponse)
# async def predict_command(self, command: List[str], model: str = None) -> Tuple[str, float, str]:
#     print(f"Received command: {command}, model: {model}")
#     try:
#         # Default model selection
#         if not model:
#             model = self.available_models[0]
#             print(f"No model specified. Using default: {model}")

#         # Model loading with detailed logging
#         try:
#             loaded_model = self.load_model(model)
#             print(f"Model loaded: {model}, Type: {type(loaded_model)}")
#         except Exception as load_error:
#             print(f"Model loading error: {load_error}")
#             raise

#         # Command preprocessing
#         command_text = " ".join(command)
#         print(f"Processing command: {command_text}")

#         # Prediction steps with error checks
#         try:
#             prediction = loaded_model.predict([command_text])[0]
#             probabilities = loaded_model.predict_proba([command_text])[0]
            
#             # Validate prediction and probabilities
#             if prediction is None or probabilities is None:
#                 raise ValueError("Invalid prediction or probabilities")

#             max_probability = probabilities[list(loaded_model.classes_).index(prediction)]
            
#             print(f"Prediction: {prediction}, Probability: {max_probability}")
            
#             # return prediction, float(max_probability), model
#             # Modification pour retourner un dictionnaire compatible avec PredictionResponse
#             return {"prediction": prediction, "probability": float(max_probability), "model": model}

        
#         except IndexError as pred_error:
#             print(f"Prediction error: Likely issue with model classes. {pred_error}")
#             raise
#         except Exception as pred_error:
#             print(f"Unexpected prediction error: {pred_error}")
#             raise

#     except Exception as e:
#         print(f"Critical error in predict_command: {e}")
#         raise
# @app.post("/batch-predict", response_model=BatchPredictionResponse)
# async def batch_predict_commands(request: BatchCommandRequest):
#     """
#     Prédire plusieurs commandes avec un modèle spécifique
    
#     - Si aucun modèle n'est spécifié, utilise le premier modèle disponible
#     - Supporte plusieurs modèles via le paramètre `model`
#     """
#     try:
#         batch_results = model_manager.batch_predict(
#             request.commands, 
#             request.model
#         )
#         results = [
#             PredictionResponse(
#                 prediction=pred, 
#                 probability=prob, 
#                 model=model
#             ) 
#             for pred, prob, model in batch_results
#         ]
#         return BatchPredictionResponse(results=results)
#     except FileNotFoundError as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/models")
# async def list_models():
#     """
#     Liste tous les modèles disponibles
#     """
#     return {"available_models": model_manager.list_available_models()}

# @app.get("/health")
# async def health_check():
#     """Endpoint de healthcheck"""
#     return {
#         "status": "healthy", 
#         "available_models": model_manager.available_models
#     }


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from .predictor import TextCommandPredictor

app = FastAPI()

class PredictRequest(BaseModel):
    command: str
    model_name: str = 'logistic_regression_model.pkl'

@app.post("/predict")
async def predict_command(request: PredictRequest):
    model_path = os.path.join('app/models', request.model_name)
    
    try:
        predictor = TextCommandPredictor(model_path)
        prediction, probability = predictor.predict_command(request.command)
        
        return {
            "command": request.command,
            "model": request.model_name,
            "prediction": prediction,
            "probability": probability
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Model {request.model_name} not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))