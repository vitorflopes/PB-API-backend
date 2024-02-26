from app.routes import obter_usuarios
from run import app

HTTP_OK = 200
HTTP_CREATED = 201
HTTP_NOT_FOUND = 404
HTTP_BAD_REQUEST = 400
HTTP_UNAUTHORIZED = 401
HTTP_SERVER_ERROR = 500


def test_obter_usuarios():
    # Crie um cliente de teste
    client = app.test_client()
    
    # Faça uma solicitação GET à rota /usuarios
    resposta = client.get('/usuarios')
    
    # Verifique se a resposta tem o código de status HTTP_OK
    assert resposta.status_code == HTTP_OK