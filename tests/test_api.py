from fastapi.testclient import TestClient
import sys
from pathlib import Path

# Add src to sys.path to resolve imports
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src.app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Music Recommender API. Use /predict to get recommendations."}

def test_health_check_no_model():
    # If model is not loaded (which might happen in test env if not trained), it should still return healthy status but model_loaded false
    # Or strict check.
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
