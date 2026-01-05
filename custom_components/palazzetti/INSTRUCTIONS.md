# 📦 Guide d'installation - Mise à jour Palazzetti v0.0.6

## 🎯 Fichiers inclus dans cette mise à jour

Ce package contient **3 fichiers** à remplacer dans votre dépôt GitHub :

### 1️⃣ hacs.json
📍 **Emplacement** : À la racine de votre dépôt
```
/hacs.json
```

### 2️⃣ manifest.json  
📍 **Emplacement** : Dans le dossier de l'intégration
```
/custom_components/palazzetti/manifest.json
```

### 3️⃣ README.md
📍 **Emplacement** : À la racine de votre dépôt
```
/README.md
```

## 📝 Modifications apportées

### ✅ hacs.json
- Simplifié au format moderne HACS
- Ajout de `render_readme: true` pour afficher le README dans HACS

### ✅ manifest.json
- Version mise à jour : **0.0.6**
- Codeowner changé : `@qtnlebrun` → `@WadohS`
- URLs mises à jour vers votre dépôt

### ✅ README.md
- ✨ Ajout du bouton d'installation en 1 clic HACS
- ✨ Ajout du bouton de configuration en 1 clic
- 📚 Documentation complète en français
- 🎨 Exemples d'automatisations
- 📝 Section Changelog ajoutée avec version 0.0.6
- 🔗 Tous les liens mis à jour vers votre dépôt

## 🚀 Instructions d'installation

### Méthode 1 : Via GitHub Web (Recommandé)

1. **Allez sur votre dépôt** : https://github.com/WadohS/hacs-palazetti

2. **Pour hacs.json** :
   - Cliquez sur `hacs.json` à la racine
   - Cliquez sur l'icône ✏️ (Edit)
   - Supprimez tout le contenu
   - Copiez le contenu du fichier `hacs.json` fourni
   - Cliquez sur "Commit changes"

3. **Pour manifest.json** :
   - Naviguez vers `custom_components/palazzetti/`
   - Cliquez sur `manifest.json`
   - Cliquez sur l'icône ✏️ (Edit)
   - Supprimez tout le contenu
   - Copiez le contenu du fichier `manifest.json` fourni
   - **VÉRIFIEZ que la version indique "0.0.6"**
   - Cliquez sur "Commit changes"

4. **Pour README.md** :
   - Cliquez sur `README.md` à la racine
   - Cliquez sur l'icône ✏️ (Edit)
   - Supprimez tout le contenu
   - Copiez le contenu du fichier `README.md` fourni
   - Cliquez sur "Commit changes"

5. **IMPORTANT - Créer un nouveau tag (release)** :
   - Allez dans l'onglet "Releases"
   - Cliquez sur "Create a new release"
   - **Tag version** : `v0.0.6` (IMPORTANT : avec le "v" devant)
   - **Release title** : `Version 0.0.6`
   - Description : 
     ```
     ## Version 0.0.6
     
     - 🎉 Mise à jour de la version vers 0.0.6
     - ✨ Ajout du bouton d'installation en 1 clic
     - 📚 Documentation améliorée avec exemples
     - 🔄 Migration vers le nouveau format HACS
     - 🔧 Correction du codeowner (@WadohS)
     - 🔗 Mise à jour de tous les liens vers le bon dépôt
     ```
   - Cliquez sur "Publish release"

### Méthode 2 : Via Git en ligne de commande

```bash
# Cloner votre dépôt
git clone https://github.com/WadohS/hacs-palazetti.git
cd hacs-palazetti

# Remplacer les fichiers
# (copiez manuellement les 3 fichiers aux bons emplacements)

# Commit les changements
git add hacs.json custom_components/palazzetti/manifest.json README.md
git commit -m "Update to version 0.0.6 - Add installation buttons"
git push

# Créer un tag v0.0.6 (IMPORTANT : avec le "v")
git tag v0.0.6
git push --tags
```

## ⚠️ IMPORTANT : Pourquoi la version ne s'affichait pas

La version sur GitHub s'affiche via les **Releases** (tags). Pour que la version apparaisse :

1. **Le fichier `manifest.json` doit contenir** : `"version": "0.0.6"`
2. **Un tag GitHub doit être créé** : `v0.0.6`
3. **Le badge dans README.md** affichera automatiquement la dernière release

### Vérification du badge de version

Le badge en haut du README :
```markdown
[![GitHub Release](https://img.shields.io/github/release/WadohS/hacs-palazetti.svg?style=for-the-badge)](https://github.com/WadohS/hacs-palazetti/releases)
```

Ce badge récupère automatiquement la dernière release/tag de votre dépôt GitHub.

## 🎉 Après l'installation

Une fois les fichiers mis à jour et le tag `v0.0.6` créé :

1. ✅ Le badge affichera "release v0.0.6" en haut du README
2. ✅ HACS détectera la version 0.0.6
3. ✅ Les utilisateurs verront la version 0.0.6 dans HACS
4. ✅ L'intégration affichera la version 0.0.6 dans Home Assistant

### Les utilisateurs pourront :

1. ✅ Installer en 1 clic via ce bouton :
   
   [![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-palazetti&category=integration)

2. ✅ La configuration sera simplifiée avec ce bouton :
   
   [![Ajouter l'intégration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=palazzetti)

3. ✅ HACS affichera automatiquement votre README formaté

## 🔍 Vérification

Après la mise à jour, vérifiez que :
- [ ] Le README s'affiche correctement sur GitHub
- [ ] Le tag `v0.0.6` apparaît dans les Releases
- [ ] Le badge "release v0.0.6" s'affiche en haut du README
- [ ] Les boutons d'installation sont visibles dans le README
- [ ] HACS détecte la version 0.0.6 (peut prendre 5-10 minutes)

## 📞 Dépannage

### La version ne s'affiche toujours pas ?

1. **Vérifiez que le tag existe** : 
   - Allez sur https://github.com/WadohS/hacs-palazetti/tags
   - Vous devez voir `v0.0.6`

2. **Vérifiez le manifest.json** :
   - Le fichier doit contenir `"version": "0.0.6"`

3. **Actualisez le cache du badge** :
   - Attendez 5-10 minutes
   - Actualisez la page GitHub (Ctrl+F5)
   - Le badge peut mettre quelques minutes à se mettre à jour

4. **Format du tag** :
   - Le tag doit commencer par `v` : `v0.0.6` (pas `0.0.6`)

## 🎯 Prochaines étapes recommandées

1. Testez l'installation en 1 clic sur une instance de test
2. Partagez le lien d'installation avec vos utilisateurs
3. Mettez à jour votre documentation si nécessaire
4. Pour les futures versions, créez toujours un tag (v0.0.7, v0.0.8, etc.)

---

**Version du guide** : 1.1  
**Date** : 5 janvier 2026  
**Version de l'addon** : 0.0.6  
**Créé par** : Assistant IA Genspark
