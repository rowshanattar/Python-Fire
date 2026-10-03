import main

def test_summarize_endpoint():
    from fastapi.testclient import TestClient

    client = TestClient(main.app)

    # Test with valid input
    response = client.post("/summarize", json={"topic": "Facebook", "sentences": 1})
    assert response.status_code == 200

    # Test with invalid input (missing topic)
    response = client.post("/summarize", json={"sentences": 3})
    assert response.status_code == 422  # Unprocessable Entity

    # Test with invalid input (negative sentences)
    response = client.post("/summarize", json={"topic": "Artificial Intelligence", "sentences": -1})
    assert response.status_code == 422  # Unprocessable Entity