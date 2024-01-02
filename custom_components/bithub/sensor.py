import requests
from homeassistant.helpers.entity import Entity
from homeassistant.const import TEMP_CELSIUS

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([ASICModelSensor(), HashRateSensor(),PowerSensor(), TempSensor(), BestDiffSensor()])

class PowerSensor(Entity):
    """Watt representation"""

    def __init__(self):
        """Initialize the Watt sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Power'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get('http://YOURBITAXEIP/api/system/info', timeout=10)
            response.raise_for_status()
            data = response.json()
            self._state = data.get('power', 'Unknown')
        except requests.exceptions.RequestException:
            self._state = 'Error'

class BestDiffSensor(Entity):
    """Diff representation"""

    def __init__(self):
        """Initialize the Diff sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'BestDiff'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get('http://YOURBITAXEIP/api/system/info', timeout=10)
            response.raise_for_status()
            data = response.json()
            self._state = data.get('bestDiff', 'Unknown')
        except requests.exceptions.RequestException:
            self._state = 'Error'

class TempSensor(Entity):
    """TempSensor representation"""

    def __init__(self):
        """Initialize the Temp sensor."""
        self._state = None
        self._unit_of_measurement = TEMP_CELSIUS

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Temperature'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get('http://YOURBITAXEIP/api/system/info', timeout=10)
            response.raise_for_status()
            data = response.json()
            self._state = data.get('temp', 'Unknown')
        except requests.exceptions.RequestException:
            self._state = 'Error'

class ASICModelSensor(Entity):
    """Representation of a Sensor for the ASIC Model."""

    def __init__(self):
        """Initialize the ASIC Model sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'ASIC Model'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get('http://YOURBITAXEIP/api/system/info', timeout=10)
            response.raise_for_status()
            data = response.json()
            self._state = data.get('ASICModel', 'Unknown')
        except requests.exceptions.RequestException:
            self._state = 'Error'

class HashRateSensor(Entity):
    """Representation of a Sensor for the Hash Rate."""

    def __init__(self):
        """Initialize the Hash Rate sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Hash Rate in GH/s'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor."""
        try:
            response = requests.get('http://YOURBITAXEIP/api/system/info', timeout=10)
            response.raise_for_status()
            data = response.json()
            self._state = data.get('hashRate', 'Unknown')
        except requests.exceptions.RequestException:
            self._state = 'Error'
