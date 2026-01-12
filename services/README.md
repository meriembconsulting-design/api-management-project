
## Technologies Utilisées
*   **API Management**: WSO2 API Manager (v4.3.0)
*   **Backend Services**: Python 3.12 (FastAPI)
*   **Containerisation & Orchestration**: Docker, Docker Compose
*   **Sécurité**: OAuth2 (client_credentials grant type)
*   **Outils de Test**: cURL, Postman

## Fonctionnalités Démontrées
*   **Gestion des APIs**: Définition, publication et versioning d'APIs (`ClientServiceAPI`, `OrderServiceAPI`) via WSO2 Publisher Portal.
*   **Sécurisation des APIs**: Implémentation d'OAuth2 pour l'authentification et l'autorisation des appels API, avec gestion des Consumer Keys/Secrets et Access Tokens.
*   **Orchestration Microservices**: Déploiement et liaison de services Python distincts via Docker Compose.
*   **Persistance des Données**: Configuration de volumes Docker pour la persistance des données de WSO2 API Manager.
*   **Health Checks**: Mise en place de vérifications d'état pour la robustesse des services Docker.
*   **Consommation d'APIs**: Abonnement et test d'APIs via WSO2 Developer Portal et outils externes (cURL, Postman).

## Guide de Démarrage Rapide
# Projet : API Management avec WSO2, Python Microservices & Docker

## Aperçu du Projet
Ce projet démontre l'implémentation d'une architecture de microservices en Python (Client et Order services) orchestrée avec Docker Compose, et sécurisée/gérée via WSO2 API Manager. L'objectif est de simuler un environnement d'entreprise où les APIs backend sont exposées de manière contrôlée, sécurisée et observable.

## Architecture
+------------------+ +------------------------+
| Client (Postman)| <-> | WSO2 API Gateway (HTTPs) |
+------------------+ +------------------------+
| |
| (Internal HTTP)
v v
+----------------+ +----------------+
| Client Service | | Order Service |
| (Python/FastAPI)| | (Python/FastAPI)|
+----------------+ +----------------+
### Prérequis
*   Docker Desktop (incluant Docker Compose) installé.

### Lancement du Projet
1.  Clonez ce dépôt : `git clone https://github.com/votre-nom-utilisateur/nom-du-repo.git`
2.  Naviguez vers le dossier du projet : `cd nom-du-repo`
3.  Lancez les services : `docker-compose up -d --build`
    *   *(Note: WSO2 prend quelques minutes pour démarrer complètement.)*
4.  Vérifiez le statut : `docker-compose ps` (tous les services doivent être 'Up (healthy)').

### Configuration et Test des APIs (WSO2)
1.  Accédez au Publisher Portal : `https://localhost:9443/publisher` (admin/admin).
    *   Configurez et publiez les `ClientServiceAPI` et `OrderServiceAPI` pointant vers `http://client-service:8000` et `http://order-service:8000` respectivement.
    *   Ajoutez des ressources (ex: `GET /users` pour Client, `GET /orders` pour Order).
    *   Activez la sécurité OAuth2 pour les deux APIs.
2.  Accédez au Developer Portal : `https://localhost:9443/devportal` (admin/admin).
    *   Créez une Application (ex: `MyPythonApp`).
    *   Abonnez `MyPythonApp` aux `ClientServiceAPI` et `OrderServiceAPI`.
    *   Générez un Access Token pour `MyPythonApp` (via Production Keys).
3.  Testez les APIs avec cURL (en remplaçant VOTRE_ACCESS_TOKEN) :
    ```bash
    # Récupération du token (si besoin, depuis le terminal)
    # curl -k -X POST \
    #   -H "Content-Type: application/x-www-form-urlencoded" \
    #   -H "Authorization: Basic VOTRE_CONSUMER_KEY_BASE64_ENCODED" \
    #   -d "grant_type=client_credentials&scope=default" \
    #   "https://localhost:9443/oauth2/token"

    # Appel ClientServiceAPI
    curl -k -X GET \
      -H "Authorization: Bearer VOTRE_ACCESS_TOKEN" \
      "https://localhost:8243/client/1.0.0/users"

    # Appel OrderServiceAPI
    curl -k -X GET \
      -H "Authorization: Bearer VOTRE_ACCESS_TOKEN" \
      "https://localhost:8243/orders/1.0.0/items"
    ```

## Améliorations Futures (Idées pour discussion en entretien)
*   Intégration d'une base de données externe pour WSO2 (ex: PostgreSQL).
*   Mise en place de CI/CD pour le déploiement automatique.
*   Ajout de politiques de Throttling et de Caching avancées dans WSO2.
*   Déploiement sur une plateforme cloud (AWS ECS/Kubernetes).
*   Implémentation de `scopes` OAuth2 pour un contrôle d'accès granulaire.

## Compétences Démontrées pour un rôle de Consultant API WSO2
Ce projet met en évidence ma capacité à :
*   Concevoir et implémenter des architectures d'APIs sécurisées et scalables.
*   Maîtriser WSO2 API Manager pour la gestion du cycle de vie des APIs, la sécurisation (OAuth2) et la publication.
*   Utiliser Docker et Docker Compose pour la containerisation et l'orchestration de microservices.
*   Résoudre des problèmes complexes d'intégration et de déploiement (troubleshooting).
*   Comprendre et appliquer les meilleures pratiques en matière d'API Management.