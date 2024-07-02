import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import text_sensor

esp32diag_ns = cg.esphome_ns.namespace("esp32diag")
ESP32Diag = esp32diag_ns.class_(
    "ESP32Diag", text_sensor.TextSensor, cg.Component
)

CONFIG_SCHEMA = text_sensor.text_sensor_schema(ESP32Diag).extend(
    cv.COMPONENT_SCHEMA
)


async def to_code(config):
    var = await text_sensor.new_text_sensor(config)
    await cg.register_component(var, config)