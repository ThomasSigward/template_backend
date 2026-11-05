# Django Backend Template

## Stack
- Python 3.12
- Django 5.2 LTS
- Django REST Framework
- PostgreSQL
- Gunicorn
- Docker

## Architecture
- config/settings/base.py: configuration commune
- config/settings/development.py: développement
- config/settings/production.py: production
- apps/: applications métier
- tests/: tests automatisés

## Conventions
- Une application Django par domaine métier.
- Utiliser les serializers DRF.
- Séparer les vues, serializers, services et modèles.
- Ne jamais stocker de secrets dans Git.
- Utiliser les variables d'environnement.
- Écrire des tests pour les fonctionnalités.
- Documenter les endpoints API.

## Règles
- Ne pas modifier les paramètres de production sans justification.
- Ne pas ajouter de dépendance sans nécessité.
- Ne pas introduire de logique métier dans l'application core.
- Toujours vérifier les migrations.
- Toujours exécuter les tests avant de terminer une fonctionnalité.