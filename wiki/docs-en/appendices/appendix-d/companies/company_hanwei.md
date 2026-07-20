# Hanwei Technology

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 汉威科技 |
| **English Name** | Hanwei Technology |
| **Headquarters** | Zhengzhou, Henan, China |
| **Founded** | 1998 |
| **Website** | [https://www.hanwei.cn](https://www.hanwei.cn) |
| **Supply Chain Segment** | Gas sensors, flexible tactile sensors, IoT solutions |
| **Enterprise Attribute** | Listed company (Shenzhen Stock Exchange ChiNext: 300007), domestic gas sensor leader |
| **Parent Company/Group** | Independently listed |
| **Data Source** | Hanwei Technology official website, annual reports, investor interaction platform |

## Company Profile

Hanwei Technology is a leading domestic enterprise in gas sensors and smart instruments, with a business scope covering sensors, smart instruments, IoT solutions, and public utility services.

The company started with gas sensors and gradually expanded to multi-physical quantity sensors such as pressure, temperature and humidity, flow, and flexible tactile sensors. It builds an IoT ecosystem centered on "sensors + monitoring terminals + data collection + cloud platform + AI." In the fields of embodied intelligence and humanoid robots, Hanwei Technology focuses on flexible tactile sensors and electronic skin, possessing four core technologies: flexible piezoresistive, piezoelectric, capacitive, and sweat sensing. Product thickness can be less than 0.3 mm, and up to 100 sensing points/cm² can be integrated.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Gas Sensors | Environmental/safety gas detection | GM-402B / ME3-NH3 | Industrial safety, smart cities, smart homes |
| Flexible Tactile Sensors | Robot electronic skin | CP101 / CP102 / CP203 | Humanoid robots, smart wearables, medical |
| Flexible Thin-Film Pressure Sensors | Pressure distribution measurement | ZNX-01 / ZNS-01 / SF45-65 | Plantar pressure, robot tactile sensing |
| IoT Solutions | Smart system integration | Smart gas/water/parks | Smart cities, industrial safety |

## Representative Products

### Hanwei Technology CP101 Flexible Micro Pressure Sensor

> Hanwei CP101: Please visit [official materials](https://www.hanwei.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Flexible micro pressure sensor | Official public materials |
| Thickness | < 0.3 mm | Public research reports |
| Sensing Point Density | Up to 100 sensing points/cm² | Public research reports |
| Response Time | < 1 ms | Public research reports |
| Bending Life | Over 1 million cycles | Public research reports |
| Detection Range | 5 mN – 10 N (varies by model) | Official/distributor materials |
| Power Supply | DC 0.1 – 4 V | Official public materials |
| Output Current | 10 μA – 30 mA | Official public materials |
| Initial Resistance | 3 – 5 kΩ | Official public materials |
| Operating Temperature | 0℃ – 55℃ | Official public materials |
| Humidity Range | < 80% RH | Official public materials |
| Stability | Fatigue test 500,000 cycles | Official public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Ultra-thin, ultra-flexible, ultra-dense, ultra-sensitive, capable of simulating human skin perception for electronic skin applications.

**Application Scenarios**: Humanoid robot electronic skin, smart gloves, medical health monitoring, wearable devices, human-machine interaction.

### Hanwei Technology ZNX-01 Insole-Type Flexible Thin-Film Pressure Sensor

> Hanwei ZNX-01: Please visit [official materials](https://www.hanwei.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Insole-type flexible thin-film pressure sensor | Official public materials |
| Thickness | ≤ 0.45 mm | Official public materials |
| Sensing Principle | Resistive piezoresistive sensing | Official public materials |
| Features | Ultra-thin and soft, fast response, high resolution, waterproof, moisture-proof, breathable | Official public materials |
| Lifespan | Over 1 million presses | Official public materials |
| Dimensions | Customizable | Official public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Capable of detecting plantar pressure distribution during standing and walking, easily integrated into insoles, prosthetics, and robot feet.

**Application Scenarios**: Plantar pressure analysis, rehabilitation medicine, sports biomechanics, robot foot force sensing.

## Supply Chain Position

- **Upstream Key Components/Materials**: Nano-sensitive materials, flexible substrates, MEMS chips, gas sensing elements, packaging materials
- **Downstream Customers/Application Scenarios**: Smart cities, industrial safety, smart homes, humanoid robots, medical and health care, automotive electronics
- **Main Competitors/Peers**: Keli Sensing, Folei New Materials, Tashan Technology, Megmeet, Huiwen Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hanwei`
- Product Entity: `ent_component_hanwei_cp101`
- Product Entity: `ent_component_hanwei_znx01`
- Key Relationships:
  - `ent_company_hanwei` -- `manufactures` --> `ent_component_hanwei_cp101`
  - `ent_company_hanwei` -- `manufactures` --> `ent_component_hanwei_znx01`
  - `ent_component_hanwei_cp101` -- `used_in` --> `ent_product_humanoid_robot_skin`

## References

1. [Hanwei Technology Official Website](https://www.hanwei.cn)
2. [Hanwei Technology CP102 Product Page](https://www.hanwei.cn/product/cp102rxcgq/)
3. [Hanwei Technology Investor Interaction Platform](https://irm.cninfo.com.cn)
4. [Appendix D Product Catalog](../index-products.md)
