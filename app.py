from flask import Flask, redirect, request, jsonify, session
from authlib.integrations.flask_client import OAuth
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "supersecretkey")

# Configuração OAuth2
OAUTH_CLIENT_ID = "sua-client-id"
OAUTH_CLIENT_SECRET = "sua-client-secret"
OAUTH_AUTHORIZE_URL = "https://sso.acesso.gov.br/authorize"
OAUTH_TOKEN_URL = "https://sso.acesso.gov.br/token"
API_INSS_URL = "https://api.gov.br/inss/beneficios"

oauth = OAuth(app)
govbr = oauth.register(
    name='govbr',
    client_id=OAUTH_CLIENT_ID,
    client_secret=OAUTH_CLIENT_SECRET,
    authorize_url=OAUTH_AUTHORIZE_URL,
    authorize_params=None,
    access_token_url=OAUTH_TOKEN_URL,
    access_token_params=None,
    client_kwargs={'scope': 'openid profile email'},
)

@app.route('/')
def home():
    return "API do INSS - Autenticação Gov.br"

@app.route('/login')
def login():
    return govbr.authorize_redirect(redirect_uri="http://localhost:5000/callback")

@app.route('/callback')
def callback():
    token = govbr.authorize_access_token()
    session['token'] = token
    return redirect('/beneficios')

@app.route('/beneficios')
def beneficios():
    if 'token' not in session:
        return jsonify({"error": "Usuário não autenticado"}), 401
    
    headers = {"Authorization": f"Bearer {session['token']['access_token']}"}
    response = requests.get(API_INSS_URL, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)