import requests
from .credentials import CLIENT_ID, CLIENT_SECRET  # Importez vos clés d'API depuis credentials.py
from pprint import pprint

def generate_access_token():
    auth_url = 'https://entreprise.pole-emploi.fr/connexion/oauth2/access_token?realm=%2Fpartenaire'
    scope = 'api_offresdemploiv2 o2dsoffre'

    auth_data = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': scope
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    auth_response = requests.post(auth_url, data=auth_data, headers=headers)

    if auth_response.status_code == 200:
        access_token = auth_response.json().get('access_token')
        return access_token
    else:
        # Gérer les erreurs d'appel à l'API d'authentification
        return None

def get_all_job_data():
    access_token = generate_access_token()  # Obtenez le jeton d'accès

    if access_token:
        api_url = 'https://api.pole-emploi.io/partenaire/offresdemploi/v2/offres/search'

        headers = {
            'Authorization': f'Bearer {access_token}',
        }

        params = {
            'motsCles': 'Développeur Python',
            'range': '0-1',
            # Autres paramètres requis par l'API, le cas échéant
        }

        all_job_data = []  # Initialisation pour stocker toutes les données

        while True:
            response = requests.get(api_url, headers=headers, params=params)

            if response.status_code == 200 or response.status_code == 206:
                job_data = response.json()  # Convertir la réponse en JSON
                all_job_data.extend(job_data['resultats'])

                if len(job_data['resultats']) < 150:  # Si moins de 150 résultats retournés, terminer la récupération
                    break

                # Obtenir le dernier identifiant pour la prochaine requête
                last_id = job_data['resultats'][-1]['id']
                params['range'] = f'{last_id + 1}-'  # Utiliser l'identifiant pour demander la suite des résultats
            else:
                # Gérer les erreurs d'appel à l'API
                return None

        
        return all_job_data
    else:
        # Gérer les erreurs de récupération du jeton d'accès
        return None