/**
 * Palazzetti Card - Version Adaptative
 * Fonctionne AVEC ou SANS l'entité number (puissance)
 * S'adapte automatiquement selon les entités disponibles
 */

class PalazzettiCard extends HTMLElement {
  set hass(hass) {
    this._hass = hass;
    
    if (!this.content) {
      const card = document.createElement('ha-card');
      this.content = document.createElement('div');
      this.content.style.padding = '16px';
      card.appendChild(this.content);
      this.appendChild(card);
    }

    const climateEntity = this._config.climate_entity;
    const powerEntity = this._config.power_entity;
    const name = this._config.name || 'Poêle';

    const climate = hass.states[climateEntity];
    
    // Vérifier si l'entité power existe
    const power = powerEntity ? hass.states[powerEntity] : null;
    const hasPowerControl = power !== null && power !== undefined;

    if (!climate) {
      this.content.innerHTML = `
        <div style="color: red; padding: 16px;">
          ⚠️ Entité introuvable : ${climateEntity}
        </div>
      `;
      return;
    }

    // Design Palazzetti officiel
    const bgColor = '#f5f5f0';
    const activeColor = '#ff6b35';
    const textColor = '#333';
    const borderColor = '#ddd';

    const currentTemp = climate.attributes.current_temperature || '—';
    const targetTemp = climate.attributes.temperature || 21;
    const fanMode = climate.attributes.fan_mode || 'auto';
    const hvacMode = climate.state || 'off';
    const isOn = hvacMode !== 'off';
    const powerValue = hasPowerControl ? (power.state || 3) : null;

    // Section puissance (conditionnelle)
    const powerSection = hasPowerControl ? `
      <div style="margin-top: 16px; padding: 12px; background: white; border: 1px solid ${borderColor}; border-radius: 8px;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
          <span style="font-weight: 500; color: ${textColor};">🔥 Puissance</span>
          <span style="font-size: 18px; font-weight: bold; color: ${activeColor};">${powerValue}</span>
        </div>
        <input 
          type="range" 
          min="1" 
          max="5" 
          step="1" 
          value="${powerValue}"
          style="width: 100%; cursor: pointer;"
          onchange="this.getRootNode().host.setPower(this.value)"
        />
        <div style="display: flex; justify-content: space-between; font-size: 12px; color: #999; margin-top: 4px;">
          <span>1</span>
          <span>2</span>
          <span>3</span>
          <span>4</span>
          <span>5</span>
        </div>
      </div>
    ` : `
      <div style="margin-top: 16px; padding: 12px; background: #fff3cd; border: 1px solid #ffc107; border-radius: 8px;">
        <div style="font-size: 14px; color: #856404;">
          ℹ️ <strong>Contrôle de puissance non disponible</strong><br/>
          <span style="font-size: 12px;">L'entité <code>number.XXX_power</code> n'existe pas. 
          Pour l'activer, modifiez <code>__init__.py</code> et ajoutez <code>"number"</code> dans PLATFORMS.</span>
        </div>
      </div>
    `;

    this.content.innerHTML = `
      <div style="background: ${bgColor}; border-radius: 12px; padding: 16px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        
        <!-- En-tête avec nom -->
        <div style="text-align: center; margin-bottom: 16px;">
          <h2 style="margin: 0; font-size: 20px; color: ${textColor};">${name}</h2>
        </div>

        <!-- Température actuelle -->
        <div style="text-align: center; margin-bottom: 20px;">
          <div style="font-size: 48px; font-weight: bold; color: ${textColor};">
            ${currentTemp}°C
          </div>
          <div style="font-size: 14px; color: #666;">Température actuelle</div>
        </div>

        <!-- Température cible -->
        <div style="background: white; border: 1px solid ${borderColor}; border-radius: 8px; padding: 12px; margin-bottom: 16px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <button 
              style="width: 40px; height: 40px; border-radius: 50%; border: 2px solid ${activeColor}; background: white; color: ${activeColor}; font-size: 24px; cursor: pointer; font-weight: bold;"
              onclick="this.getRootNode().host.adjustTemp(-1)"
            >−</button>
            
            <div style="text-align: center;">
              <div style="font-size: 28px; font-weight: bold; color: ${textColor};">${targetTemp}°C</div>
              <div style="font-size: 12px; color: #666;">Température cible</div>
            </div>
            
            <button 
              style="width: 40px; height: 40px; border-radius: 50%; border: 2px solid ${activeColor}; background: ${activeColor}; color: white; font-size: 24px; cursor: pointer; font-weight: bold;"
              onclick="this.getRootNode().host.adjustTemp(1)"
            >+</button>
          </div>
        </div>

        <!-- Ventilation -->
        <div style="background: white; border: 1px solid ${borderColor}; border-radius: 8px; padding: 12px; margin-bottom: 16px;">
          <div style="margin-bottom: 8px; font-weight: 500; color: ${textColor};">💨 Ventilation</div>
          <div style="display: grid; grid-template-columns: repeat(7, 1fr); gap: 8px;">
            ${['1', '2', '3', '4', '5', 'auto', 'high'].map(mode => `
              <button 
                style="
                  padding: 8px 4px; 
                  border-radius: 6px; 
                  border: 1px solid ${borderColor}; 
                  background: ${fanMode === mode ? activeColor : 'white'}; 
                  color: ${fanMode === mode ? 'white' : textColor}; 
                  cursor: pointer; 
                  font-size: 12px;
                  font-weight: ${fanMode === mode ? 'bold' : 'normal'};
                "
                onclick="this.getRootNode().host.setFanMode('${mode}')"
              >${mode.toUpperCase()}</button>
            `).join('')}
          </div>
        </div>

        ${powerSection}

        <!-- Marche/Arrêt -->
        <div style="margin-top: 16px; background: white; border: 1px solid ${borderColor}; border-radius: 8px; padding: 12px;">
          <div style="display: flex; justify-content: space-between; align-items: center;">
            <span style="font-weight: 500; color: ${textColor};">⏻ Marche/Arrêt</span>
            <label style="position: relative; display: inline-block; width: 60px; height: 34px;">
              <input 
                type="checkbox" 
                ${isOn ? 'checked' : ''} 
                style="opacity: 0; width: 0; height: 0;"
                onchange="this.getRootNode().host.togglePower(this.checked)"
              />
              <span style="
                position: absolute; 
                cursor: pointer; 
                top: 0; left: 0; right: 0; bottom: 0; 
                background-color: ${isOn ? activeColor : '#ccc'}; 
                transition: .4s; 
                border-radius: 34px;
              ">
                <span style="
                  position: absolute; 
                  content: ''; 
                  height: 26px; 
                  width: 26px; 
                  left: ${isOn ? '30px' : '4px'}; 
                  bottom: 4px; 
                  background-color: white; 
                  transition: .4s; 
                  border-radius: 50%;
                "></span>
              </span>
            </label>
          </div>
        </div>

      </div>
    `;
  }

  setConfig(config) {
    if (!config.climate_entity) {
      throw new Error('Vous devez définir climate_entity');
    }
    this._config = config;
  }

  adjustTemp(delta) {
    const climateEntity = this._config.climate_entity;
    const climate = this._hass.states[climateEntity];
    const currentTarget = climate.attributes.temperature;
    const newTarget = Math.max(10, Math.min(30, currentTarget + delta));

    this._hass.callService('climate', 'set_temperature', {
      entity_id: climateEntity,
      temperature: newTarget,
    });
  }

  setFanMode(mode) {
    const climateEntity = this._config.climate_entity;
    this._hass.callService('climate', 'set_fan_mode', {
      entity_id: climateEntity,
      fan_mode: mode,
    });
  }

  setPower(value) {
    const powerEntity = this._config.power_entity;
    if (!powerEntity) return;

    this._hass.callService('number', 'set_value', {
      entity_id: powerEntity,
      value: parseInt(value),
    });
  }

  togglePower(turnOn) {
    const climateEntity = this._config.climate_entity;
    this._hass.callService('climate', 'set_hvac_mode', {
      entity_id: climateEntity,
      hvac_mode: turnOn ? 'heat' : 'off',
    });
  }

  getCardSize() {
    return 5;
  }
}

customElements.define('palazzetti-card', PalazzettiCard);
