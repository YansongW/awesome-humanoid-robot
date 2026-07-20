# Analog Devices / Analog Devices

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Analog Devices |
| **English Name** | Analog Devices |
| **Headquarters** | Norwood, Massachusetts, USA |
| **Founded** | 1965 |
| **Website** | [https://www.analog.com](https://www.analog.com) |
| **Supply Chain Role** | Analog/Mixed-Signal IC, Inertial Measurement Unit (IMU), Sensor Interface |
| **Enterprise Attribute** | Public Company (NASDAQ: ADI), Global Leading Semiconductor Company |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | Official website, product datasheets, public financial reports |

## Company Profile

Analog Devices is a global leader in analog, mixed-signal, and digital signal processing semiconductor companies. Its iSensor MEMS IMU is widely used in robotics, aerospace, and industrial automation.

ADI provides high-performance inertial measurement units (IMUs), accelerometers, gyroscopes, and signal conditioning chips. The ADIS16495 is a tactical-grade 6-axis IMU featuring low drift, high shock resistance, and wide temperature operation, suitable for humanoid robot attitude estimation, navigation, and motion control.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| iSensor IMU | Tactical/Industrial Grade IMU | ADIS16495 / ADIS16475 / ADIS16465 | Robotics, Drones, Autonomous Driving, Industrial Control |
| MEMS Accelerometer/Gyroscope | General Motion Sensing | ADXL Series / ADIS Series | Consumer Electronics, Automotive, Industrial |
| Signal Chain & Power | Analog Front End & Conversion | ADC/DAC / Amplifiers / Power Management | Sensor Interface, Control Systems |

## Representative Products

### Analog Devices ADIS16495

> Analog Devices ADIS16495: Please visit [Official Documentation](https://www.analog.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Package | 24-pin Module (with connector interface) | Official datasheet |
| Sensor Type | 6-axis IMU (3-axis gyroscope + 3-axis accelerometer) | Official datasheet |
| Accelerometer Range | ±8 g | Official datasheet |
| Gyroscope Range | ±125°/s / ±450°/s / ±2000°/s (selectable) | Official datasheet |
| In-Run Bias Stability | 0.8°/hr (typical) | Official datasheet |
| Angular Random Walk | 0.09°/√hr | Official datasheet |
| Interface | SPI | Official datasheet |
| Supply Voltage | 3.0 V – 3.6 V | Official datasheet |
| Operating Current | 89 mA | Official datasheet |
| Operating Temperature | -40°C ~ +105°C | Official datasheet |
| Shock Resistance | 2000 g | Official datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Tactical-grade accuracy, full temperature range calibration, high shock resistance, SPI digital output, suitable for high-dynamic robot attitude estimation.

**Application Scenarios**: Humanoid robot IMU, drone flight control, autonomous driving, industrial stabilization platforms, precision instruments.

### Analog Devices ADIS16475

> Analog Devices ADIS16475: Please visit [Official Documentation](https://www.analog.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Sensor Type | 6-axis IMU | Official datasheet |
| Package | 14-pin Module | Official datasheet |
| Gyroscope Range | ±125°/s / ±500°/s (selectable) | Official datasheet |
| Accelerometer Range | ±8 g | Official datasheet |
| Operating Temperature | -40°C ~ +105°C | Official datasheet |
| Interface | SPI | Official datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Small form factor tactical-grade IMU, suitable for space-constrained robot platforms with high precision requirements.

**Application Scenarios**: Small humanoid robots, exoskeletons, drones, AGVs.

## Supply Chain Position

- **Upstream Key Components/Materials**: MEMS wafers, ASIC foundry, packaging materials, precision resistors and capacitors
- **Downstream Customers/Application Scenarios**: Robot OEMs, drones, autonomous driving, aerospace, industrial automation, medical devices
- **Main Competitors/Peers**: Bosch Sensortec, STMicroelectronics, TDK InvenSense, Honeywell, NovAtel

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_analog_devices`
- Product Entity: `ent_component_analog_devices_adis16495`
- Product Entity: `ent_component_analog_devices_adis16475`
- Key Relationships:
  - `ent_company_analog_devices` -- `manufactures` --> `ent_component_analog_devices_adis16495`
  - `ent_company_analog_devices` -- `manufactures` --> `ent_component_analog_devices_adis16475`

## References

1. [Official Website](https://www.analog.com)
2. [Product Documentation and Public Reports](https://www.analog.com)
3. [Appendix D Product Catalog](../index-products.md)
