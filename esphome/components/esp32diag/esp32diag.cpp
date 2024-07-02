#include "esphome/core/log.h"
#include "esp32diag.h"

namespace esphome {
namespace esp32diag {

static const char *TAG = "esp32diag.text_sensor";

void ESP32Diag::setup() {
  
}

void ESP32Diag::dump_config() { 
    ESP_LOGCONFIG(TAG, "Empty text sensor");
}

}  // namespace esp32diag
}  // namespace esphome