# 📦 Guide d'installation - Mise à jour Palazzetti v0.0.1

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
- Version mise à jour : `0.0.0` → `0.0.1`
- Codeowner changé : `@qtnlebrun` → `@WadohS`
- URLs mises à jour vers votre dépôt

### ✅ README.md
- ✨ Ajout du bouton d'installation en 1 clic HACS
- ✨ Ajout du bouton de configuration en 1 clic
- 📚 Documentation complète en français
- 🎨 Exemples d'automatisations
- 📝 Section Changelog ajoutée
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
   - Cliquez sur "Commit changes"

4. **Pour README.md** :
   - Cliquez sur `README.md` à la racine
   - Cliquez sur l'icône ✏️ (Edit)
   - Supprimez tout le contenu
   - Copiez le contenu du fichier `README.md` fourni
   - Cliquez sur "Commit changes"

5. **Créer un nouveau tag (release)** :
   - Allez dans l'onglet "Releases"
   - Cliquez sur "Create a new release"
   - Tag version : `v0.0.1`
   - Release title : `Version 0.0.1`
   - Description : Copiez la section Changelog du README
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
git commit -m "Update to version 0.0.1 - Add installation buttons"
git push

# Créer un tag
git tag v0.0.1
git push --tags
```

## 🎉 Après l'installation

Une fois les fichiers mis à jour et le tag créé :

1. ✅ Les utilisateurs pourront installer en 1 clic via ce bouton :
   
   [![Ouvrir dans HACS](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=WadohS&repository=hacs-palazetti&category=integration)

2. ✅ La configuration sera simplifiée avec ce bouton :
   
   [![Ajouter l'intégration](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=palazzetti)

3. ✅ HACS affichera automatiquement votre README formaté

## 🔍 Vérification

Après la mise à jour, vérifiez que :
- [ ] Le README s'affiche correctement sur GitHub
- [ ] Le tag `v0.0.1` apparaît dans les Releases
- [ ] Les boutons d'installation sont visibles dans le README
- [ ] HACS détecte la nouvelle version

## 📞 Support

Si vous rencontrez des problèmes :
- Vérifiez que tous les fichiers sont bien remplacés
- Assurez-vous d'avoir créé le tag `v0.0.1`
- Attendez quelques minutes que HACS détecte la mise à jour

## 🎯 Prochaines étapes recommandées

1. Testez l'installation en 1 clic sur une instance de test
2. Partagez le lien d'installation avec vos utilisateurs
3. Mettez à jour votre documentation si nécessaire

---

**Version du guide** : 1.0  
**Date** : 5 janvier 2026  
**Créé par** : Assistant IA Genspark
