# palazzetti

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)

[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

[![Community Forum][forum-shield]][forum]

_Component to integrate with [integration_blueprint][integration_blueprint]._

**This component will set up the following platforms.**

Platform | Description
-- | --
`climate` | Control a Palazzetti stove via the ConnBox (On/Off, target temperature and fan speed)
`number` | Control the stove power

## Installation

1. Using the tool of choice open the directory (folder) for your HA configuration (where you find `configuration.yaml`).
2. If you do not have a `custom_components` directory (folder) there, you need to create it.
3. In the `custom_components` directory (folder) create a new folder called `palazzetti`.
4. Download _all_ the files from the `custom_components/palazzetti/` directory (folder) in this repository.
5. Place the files you downloaded in the new directory (folder) you created.
6. Restart Home Assistant
7. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Palazzetti"

Using your HA configuration directory (folder) as a starting point you should now also have this:

```text
custom_components/palazzetti/translations/en.json
custom_components/palazzetti/translations/fr.json
custom_components/palazzetti/__init__.py
custom_components/palazzetti/climate.py
custom_components/palazzetti/config_flow.py
custom_components/palazzetti/const.py
custom_components/palazzetti/manifest.json
custom_components/palazzetti/number.py
```

## Configuration is done in the UI

<!---->

## Contributions are welcome!

If you want to contribute to this please read the [Contribution guidelines](CONTRIBUTING.md)

***

[integration_blueprint]: https://github.com/qtnlebrun/hacs-palazetti
[commits-shield]: https://img.shields.io/github/commit-activity/y/qtnlebrun/hacs-palazetti.svg?style=for-the-badge
[commits]: https://github.com/qtnlebrun/hacs-palazetti/commits/master
[hacs]: https://github.com/custom-components/hacs
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[forum-shield]: https://img.shields.io/badge/community-forum-brightgreen.svg?style=for-the-badge
[forum]: https://community.home-assistant.io/
[license-shield]: https://img.shields.io/github/license/qtnlebrun/hacs-palazetti.svg?style=for-the-badge
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40qtnlebrun-blue.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/qtnlebrun/hacs-palazetti.svg?style=for-the-badge
[releases]: https://github.com/qtnlebrun/hacs-palazetti/releases
