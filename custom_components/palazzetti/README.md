# Palazzetti ConnBox - Intégration Home Assistant

[![GitHub Release](https://img.shields.io/github/release/WadohS/hacs-palazetti.svg?style=for-the-badge)](https://github.com/WadohS/hacs-palazetti/releases)
[![GitHub Activity](https://img.shields.io/github/commit-activity/y/WadohS/hacs-palazetti.svg?style=for-the-badge)](https://github.com/WadohS/hacs-palazetti/commits/master)
[![License](https://img.shields.io/github/license/WadohS/hacs-palazetti.svg?style=for-the-badge)](LICENSE)

[![hacs](https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge)](https://github.com/custom-components/hacs)
[![Project Maintenance](https://img.shields.io/badge/maintainer-WadohS-blue.svg?style=for-the-badge)](https://github.com/WadohS)

[![Community Forum](https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge)](https://community.home-assistant.io/)

_Intégration pour contrôler votre poêle Palazzetti via le ConnBox dans Home Assistant._

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-palazetti&category=integration)

## 🌟 Fonctionnalités

**Cette intégration créera les plateformes suivantes.**

| Plateforme | Description |
| --- | --- |
| `climate` | Contrôle du poêle Palazzetti via ConnBox (On/Off, température cible et vitesse ventilateur) |
| `number` | Contrôle de la puissance du poêle |

## 📦 Installation

### Via HACS (Recommandé)

#### Installation en 1 clic 🚀

[![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-palazetti&category=integration)

**Cliquez sur le bouton ci-dessus** pour ajouter automatiquement l'intégration Palazzetti à votre Home Assistant !

#### Installation manuelle via HACS

Si le bouton ne fonctionne pas :

1. Ouvrez HACS dans votre interface Home Assistant
2. Allez dans "Intégrations"
3. Cliquez sur les 3 points en haut à droite ⋮
4. Sélectionnez "Dépôts personnalisés"
5. Ajoutez l'URL : `https://github.com/WadohS/hacs-palazetti`
6. Catégorie : "Integration"
7. Recherchez "Palazzetti" et installez-le
8. Redémarrez Home Assistant

### Installation manuelle

1. Utilisez votre outil préféré pour ouvrir le répertoire de configuration de Home Assistant (où se trouve `configuration.yaml`)
2. Si vous n'avez pas de répertoire `custom_components`, créez-le
3. Dans le répertoire `custom_components`, créez un nouveau dossier appelé `palazzetti`
4. Téléchargez **tous** les fichiers depuis le répertoire `custom_components/palazzetti/` de ce dépôt
5. Placez-les dans le nouveau répertoire que vous venez de créer
6. Redémarrez Home Assistant

Votre structure de répertoire devrait ressembler à ceci :

```
custom_components/palazzetti/translations/en.json
custom_components/palazzetti/translations/fr.json
custom_components/palazzetti/__init__.py
custom_components/palazzetti/climate.py
custom_components/palazzetti/config_flow.py
custom_components/palazzetti/const.py
custom_components/palazzetti/manifest.json
custom_components/palazzetti/number.py
```

## ⚙️ Configuration

La configuration se fait entièrement via l'interface utilisateur :

### Configuration en 1 clic ⚡

[![Ajouter l'intégration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=palazzetti)

**Cliquez sur le bouton ci-dessus** pour configurer automatiquement l'intégration !

### Configuration manuelle

1. Allez dans **Configuration** → **Intégrations**
2. Cliquez sur **+ Ajouter une intégration**
3. Recherchez **Palazzetti**
4. Entrez l'adresse IP de votre ConnBox
5. Cliquez sur **Soumettre**

## 🎨 Exemples d'utilisation

### Carte Thermostat simple

```yaml
type: thermostat
entity: climate.palazzetti_poele
```

### Carte avec contrôle de puissance

```yaml
type: entities
entities:
  - entity: climate.palazzetti_poele
  - entity: number.palazzetti_puissance
```

### Automatisation - Allumage programmé

```yaml
automation:
  - alias: "Allumer le poêle le matin"
    trigger:
      - platform: time
        at: "06:30:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.temperature_salon
        below: 18
    action:
      - service: climate.turn_on
        target:
          entity_id: climate.palazzetti_poele
      - service: climate.set_temperature
        target:
          entity_id: climate.palazzetti_poele
        data:
          temperature: 21
```

### Automatisation - Extinction automatique

```yaml
automation:
  - alias: "Éteindre le poêle la nuit"
    trigger:
      - platform: time
        at: "22:00:00"
    action:
      - service: climate.turn_off
        target:
          entity_id: climate.palazzetti_poele
```

## 🐛 Signaler un problème

Si vous rencontrez un bug ou avez une suggestion :

1. Vérifiez que vous utilisez la dernière version
2. Consultez les [issues existantes](https://github.com/WadohS/hacs-palazetti/issues)
3. Créez une nouvelle issue avec :
   - Version de Home Assistant
   - Version de l'intégration
   - Modèle de votre poêle Palazzetti
   - Description détaillée du problème
   - Logs pertinents

## 🤝 Contribuer

Les contributions sont les bienvenues ! Veuillez consulter notre [Guide de contribution](CONTRIBUTING.md).

## 📝 Changelog

### Version 0.0.1 (2026-01-05)
- 🎉 Mise à jour initiale de la version
- ✨ Ajout du bouton d'installation en 1 clic
- 📚 Documentation améliorée avec exemples
- 🔄 Migration vers le nouveau format HACS

### Versions précédentes
- Support des plateformes climate et number
- Contrôle local via ConnBox
- Configuration via interface utilisateur

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- [@qtnlebrun](https://github.com/qtnlebrun) pour le développement initial
- Communauté Home Assistant pour leur support
- Tous les utilisateurs qui signalent des problèmes et suggèrent des améliorations

---

**Compatible avec** : Home Assistant 0.118.0 et versions ultérieures

**Classe IoT** : Interrogation locale (local_polling)
