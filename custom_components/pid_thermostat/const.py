"""Constants for the PID thermostat integration."""
from homeassistant.components.climate import ClimateEntityFeature
from homeassistant.const import Platform

from .ha_pid_shared.const import (
    ATTR_CYCLE_TIME,
    ATTR_LAST_CYCLE_START,
    ATTR_PID_ENABLE,
    ATTR_PID_ERROR,
    ATTR_PID_INPUT,
    ATTR_PID_KD,
    ATTR_PID_KI,
    ATTR_PID_KP,
    ATTR_PID_OUTPUT,
    ATTR_VALUE,
    CONF_CYCLE_TIME,
    CONF_PID_KD,
    CONF_PID_KI,
    CONF_PID_KP,
    SERVICE_ENABLE,
)


DOMAIN = "pid_thermostat"
PLATFORMS = [Platform.CLIMATE]

CONF_HEATER = "heater"
CONF_SENSOR = "target_sensor"
CONF_MIN_TEMP = "min_temp"
CONF_MAX_TEMP = "max_temp"
CONF_TARGET_TEMP = "target_temp"
CONF_AC_MODE = "ac_mode"
CONF_INITIAL_HVAC_MODE = "initial_hvac_mode"
CONF_AWAY_TEMP = "away_temp"

AC_MODE_COOL = "cool"
AC_MODE_HEAT = "heat"


DEFAULT_NAME = "PID Thermostat"
DEFAULT_CYCLE_TIME = {"seconds": 30}
DEFAULT_PID_KP = 100.0
DEFAULT_PID_KI = 0.1
DEFAULT_PID_KD = 0.0
DEFAULT_AC_MODE = AC_MODE_HEAT

SUPPORT_FLAGS = ClimateEntityFeature.TARGET_TEMPERATURE
