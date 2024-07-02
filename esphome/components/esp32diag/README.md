# example configuration:

# use external components
external_components:
  - source:
      type: git
      url: https://github.com/shamasis/esphome-esp32-diagnostics.git
      ref: main
    refresh: 5s
    components: [ esp32diag]

text_sensor:
  - platform: esp32diag
    name: "Device Diagnostics"