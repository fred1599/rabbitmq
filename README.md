# My Messaging System

Ce projet est un système de messagerie utilisant RabbitMQ pour la gestion des messages et FastAPI pour l'API web. Il suit les principes de la Clean Architecture.

## Table des matières

- [Installation](#installation)
- [Configuration](#configuration)
- [Lancer l'application](#lancer-lapplication)
- [Utilisation de l'API](#utilisation-de-lapi)

## Installation

1. Clonez le dépôt :

    ```bash
    git clone https://github.com/votre-utilisateur/my_messaging_system.git
    cd my_messaging_system
    ```

2. Créez un environnement virtuel et activez-le :

    ```bash
    python -m venv env_messaging
    source env_messaging/bin/activate
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

4. Installez RabbitMQ :

    - Sur Ubuntu :

        ```bash
        sudo apt-get install rabbitmq-server
        sudo systemctl enable rabbitmq-server
        sudo systemctl start rabbitmq-server
        ```

## Configuration

1. Assurez-vous que RabbitMQ est en cours d'exécution :

    ```bash
    sudo systemctl status rabbitmq-server
    ```

2. Vérifiez la configuration de RabbitMQ dans `app/core/config.py` :

    ```python
    from pydantic_settings import BaseSettings

    class Settings(BaseSettings):
        API_V1_STR: str = "/api/v1"
        PROJECT_NAME: str = "My Messaging System"
        VERSION: str = "1.0.0"
        RABBITMQ_URL: str = "amqp://guest:guest@localhost/"

    settings = Settings()
    ```

## Lancer l'application

1. Démarrez le serveur FastAPI avec Uvicorn :

    ```bash
    uvicorn app.main:app --reload --port 8000
    ```

2. Démarrez le consommateur de messages dans un autre terminal :

    ```bash
    python app/workers/message_consumer.py
    ```

## Utilisation de l'API

### Créer et envoyer un message

Envoyez une requête POST à l'endpoint `/api/v1/messages` avec le paramètre de requête `content` :

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/message/?content=coucou"
