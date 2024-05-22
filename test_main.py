from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_predict_positive_negative():
    response = client.post('/predict/',
                           json={'text':
                                 'I love you, but I hate you, but I love you'
                                })
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative_a_lot():
    response = client.post('/predict/',
                           json={'text':
                                 f"I love you, but I hate you, but I hate you,
                                 but I hate you, but I hate you, but I hate you"
                                 })
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_predict_5050_firs_negative():
    response = client.post('/predict/',
                           json={'text': 'I hate you, but I love you'})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'
