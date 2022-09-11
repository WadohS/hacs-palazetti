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

{% if not installed %}
## Installation

1. Click install.
1. In the HA UI go to "Configuration" -> "Integrations" click "+" and search for "Blueprint".

{% endif %}


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

