# 🔴 PROBLÈME TROUVÉ : Home Assistant charge toujours l'ancienne version !

## ❌ Le message d'erreur révèle tout

Lors de l'ajout de l'intégration, vous voyez :
```
https://github.com/qtnlebrun/hacs-palazetti
```

Au lieu de :
```
https://github.com/WadohS/hacs-palazetti
```

**Cela prouve que Home Assistant charge l'ANCIENNE version de qtnlebrun, pas votre version WadohS !**

---

## 🔍 Pourquoi ça arrive ?

Il y a **2 installations** de l'intégration Palazzetti sur votre système :

1. ✅ **Votre version WadohS** (que vous avez modifiée) dans `/config/custom_components/palazzetti/`
2. ❌ **L'ancienne version qtnlebrun** (cachée ailleurs) que Home Assistant charge à la place

---

## ✅ SOLUTION COMPLÈTE (10 minutes)

### **Étape 1 : Désinstaller complètement via HACS**

1. **HACS** > **Intégrations**
2. Chercher **Palazzetti**
3. Cliquer sur l'intégration
4. Cliquer sur **⋮** > **Supprimer**
5. Confirmer

### **Étape 2 : Supprimer les intégrations configurées**

1. **Configuration** > **Appareils et Services** > **Intégrations**
2. Supprimer **Ginger** (⋮ > Supprimer)
3. Supprimer **Palazzetti** (⋮ > Supprimer)

### **Étape 3 : Supprimer TOUS les dossiers Palazzetti**

**Via SSH ou Terminal :**

```bash
# Supprimer le dossier principal
rm -rf /config/custom_components/palazzetti

# Supprimer les fichiers HACS (si présents)
rm -rf /config/.storage/hacs.repositories

# Vider le cache Python
rm -rf /config/__pycache__
rm -rf /config/custom_components/__pycache__
```

**Via File Editor :**
1. Supprimer le dossier `/config/custom_components/palazzetti`
2. Supprimer le dossier `/config/.storage/hacs.repositories` (si visible)

### **Étape 4 : Redémarrer Home Assistant**

1. **Configuration** > **Système** > **Redémarrer**
2. Attendre 3-5 minutes (nettoyage complet)

### **Étape 5 : Télécharger VOTRE version depuis GitHub**

**Option A - Via HACS (dépôt custom) :**

1. **HACS** > **Intégrations** > **⋮** (menu)
2. **Dépôts personnalisés**
3. Ajouter :
   - URL : `https://github.com/WadohS/hacs-palazetti`
   - Catégorie : `Integration`
4. Cliquer sur **Ajouter**
5. Chercher **Palazzetti** dans HACS
6. Installer

**Option B - Installation manuelle (RECOMMANDÉ) :**

1. Aller sur : https://github.com/WadohS/hacs-palazetti
2. Cliquer sur **Code** > **Download ZIP**
3. Extraire le ZIP
4. Copier le dossier `custom_components/palazzetti` dans `/config/custom_components/`

### **Étape 6 : Modifier les fichiers (CRUCIAL)**

#### A. Modifier `manifest.json`

**Ouvrir** `/config/custom_components/palazzetti/manifest.json`

**Remplacer TOUT le contenu par :**

```json
{
  "domain": "palazzetti",
  "name": "Palazzetti ConnBox",
  "config_flow": true,
  "version": "0.0.7",
  "requirements": [
    "palazzetti-sdk-local-api==1.0.14"
  ],
  "iot_class": "local_polling",
  "codeowners": [
    "@WadohS"
  ],
  "documentation": "https://github.com/WadohS/hacs-palazetti",
  "issue_tracker": "https://github.com/WadohS/hacs-palazetti/issues"
}
```

#### B. Modifier `__init__.py`

**Ouvrir** `/config/custom_components/palazzetti/__init__.py`

**Ligne 34, changer :**

```python
# AVANT
PLATFORMS = ["climate", "sensor"]

# APRÈS
PLATFORMS = ["climate", "sensor", "number"]
```

#### C. Vérifier `number.py`

**Vérifier que** `/config/custom_components/palazzetti/number.py` **existe**.

Si manquant, créer le fichier avec ce contenu :

```python
"""Support for Palazzetti power."""
from __future__ import annotations

import logging

from homeassistant.components.number import NumberEntity, NumberMode

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .const import DOMAIN, ICON_FIRE

from .entity import PalazzettiEntity

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Setup number platform"""

    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([PalazzettiPower(coordinator, entry)])


class PalazzettiPower(PalazzettiEntity, NumberEntity):
    """Palazetti stove power entity"""

    _attr_has_entity_name = True
    _attr_name = None
    _attr_icon = ICON_FIRE
    _attr_mode = NumberMode.SLIDER
    _attr_native_min_value = 1
    _attr_native_max_value = 5
    _attr_native_step = 1

    def __init__(self, coordinator: DataUpdateCoordinator, config_entry: ConfigEntry):
        PalazzettiEntity.__init__(self, coordinator, config_entry, "power")

    async def async_set_native_value(self, value: float) -> None:
        """Update the current value."""
        await self.coordinator.hub.product.async_set_power(int(value))
        await self.coordinator.async_request_refresh()

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = self.coordinator.data.get("PWR")

        self.async_write_ha_state()
```

### **Étape 7 : Redémarrer Home Assistant**

1. **Configuration** > **Système** > **Redémarrer**
2. Attendre 2-3 minutes

### **Étape 8 : Ajouter les intégrations**

1. **Configuration** > **Appareils et Services** > **Intégrations**
2. **+ AJOUTER UNE INTÉGRATION**
3. Chercher **Palazzetti**

**VÉRIFIER LE MESSAGE :**
- ✅ Doit afficher : `https://github.com/WadohS/hacs-palazetti`
- ❌ Si affiche encore `qtnlebrun` → Recommencer depuis l'étape 3

4. Configurer le premier poêle (Palazzetti)
5. Configurer le deuxième poêle (Ginger)

### **Étape 9 : Vérifier les entités**

1. **Outils développeur** > **États**
2. Chercher **"power"**
3. Vous devriez voir :
   - ✅ `number.palazzetti_power`
   - ✅ `number.ginger_power`

---

## 🔍 Vérifications importantes

### Vérification 1 : Bon manifest.json

```bash
cat /config/custom_components/palazzetti/manifest.json | grep codeowners
```

Doit afficher :
```
"codeowners": ["@WadohS"],
```

Si affiche `@qtnlebrun` → mauvais fichier !

### Vérification 2 : PLATFORMS contient "number"

```bash
cat /config/custom_components/palazzetti/__init__.py | grep PLATFORMS
```

Doit afficher :
```python
PLATFORMS = ["climate", "sensor", "number"]
```

### Vérification 3 : number.py existe

```bash
ls -la /config/custom_components/palazzetti/number.py
```

Doit afficher :
```
-rw-r--r-- 1 root root 1847 Jan 5 23:00 number.py
```

---

## 📦 Package prêt à installer

Je vous prépare un **package complet** avec :
- ✅ Tous les fichiers corrects (WadohS, version 0.0.7)
- ✅ Script d'installation automatique
- ✅ Vérifications intégrées

**Contenu du package :**
1. `manifest.json` (version 0.0.7, URLs WadohS)
2. `__init__.py` (avec "number")
3. `number.py` (complet)
4. `install.sh` (installation automatique)
5. Guide complet

---

## 🎯 Résumé

**Le problème :**
- Vous avez modifié VOS fichiers ✅
- MAIS Home Assistant charge une AUTRE copie de l'intégration (qtnlebrun) ❌

**La solution :**
1. Supprimer TOUTES les installations
2. Nettoyer complètement
3. Réinstaller VOTRE version
4. Vérifier que le message affiche WadohS
5. Ajouter les intégrations

---

## ⚠️ Point CRITIQUE

Avant d'ajouter les intégrations à l'étape 8, **vérifiez absolument** que le message d'aide pointe vers **WadohS** et non **qtnlebrun**.

Si ça pointe encore vers qtnlebrun, c'est qu'il reste une copie cachée quelque part.

---

Je prépare maintenant le package complet avec tous les fichiers corrects ! 🚀
