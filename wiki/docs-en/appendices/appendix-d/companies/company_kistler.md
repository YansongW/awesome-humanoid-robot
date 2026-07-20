# Kistler

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 奇石乐 (Kistler) |
| **English Name** | Kistler |
| **Headquarters** | Winterthur, Switzerland |
| **Founded** | 1950 |
| **Website** | [https://www.kistler.com](https://www.kistler.com) |
| **Supply Chain Role** | Force/Pressure/Acceleration/Torque Sensors, Piezoelectric Measurement & Test Systems |
| **Company Type** | Global leader in piezoelectric measurement technology, family-owned |
| **Parent Company/Group** | Kistler Holding AG |
| **Data Source** | Kistler official website, product datasheets, annual reports |

## Company Profile

Kistler is a global leader in piezoelectric force, pressure, and acceleration measurement technology, with products widely used in automotive testing, machining, robotics, and industrial automation.

Kistler started with piezoelectric measurement technology and provides complete solutions from sensors and measurement chains to test systems. Its force sensors cover single-axis, three-axis, and six-component measurements, maintaining high precision and low crosstalk under high-frequency dynamic loads. In recent years, Kistler has introduced miniaturized and highly integrated sensors into collaborative robots and precision assembly, providing key sensing units for humanoid robot joint force control, foot-end force feedback, and production line testing.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Piezoelectric Force Sensors | Dynamic force / multi-axis force measurement | 9107B / 9129AA / 9311B | Machining, automotive testing, robotics |
| Strain Gauge Force Sensors | Static / quasi-static force measurement | 9247B Series | Weighing, assembly, press-fitting |
| Pressure/Acceleration Sensors | Combustion / crash / vibration testing | 6041A / 8762A | Automotive, aerospace |
| Measurement Systems | Data acquisition & analysis | KiDAq / LabAmp | Test benches, R&D |

## Representative Products

### Kistler 9107B Three-Component Force Sensor

> Kistler 9107B Three-Component Force Sensor: Please visit [official documentation](https://www.kistler.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Piezoelectric three-component force sensor | Official website |
| Measurement Directions | Fx / Fy / Fz | Official website/datasheet |
| Force Measurement Range (Fx/Fy) | Not disclosed | - |
| Force Measurement Range (Fz) | Not disclosed | - |
| Sensitivity | Not disclosed | - |
| Stiffness | High stiffness design | Official website/datasheet |
| Natural Frequency | Not disclosed | - |
| Crosstalk | < ±1% (typical) | Official website/datasheet |
| Operating Temperature | Not disclosed | - |
| Protection Rating | Not disclosed | - |
| Output Interface | Piezoelectric charge output + compatible charge amplifier | Official website/datasheet |
| Dimensions | Compact flange mount | Official website/datasheet |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Piezoelectric quartz crystal sensing element, simultaneous three-axis dynamic force measurement, high stiffness and high natural frequency, suitable for high-frequency cutting force and robot dynamic force control.

**Application Scenarios**: Machining cutting force monitoring, robot end-effector force control, structural dynamic testing, automotive chassis and suspension testing, humanoid robot foot-end force feedback.

### Kistler 6041A Piezoelectric Pressure Sensor

> Kistler 6041A Piezoelectric Pressure Sensor: Please visit [official documentation](https://www.kistler.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Piezoelectric pressure sensor | Official website |
| Range | Not disclosed | - |
| Application | Combustion analysis, dynamic pressure testing | Official website |
| Price | Not disclosed | - |

**Technical Highlights**: Piezoelectric sensor suitable for internal combustion engine combustion analysis and high-frequency dynamic pressure measurement.

**Application Scenarios**: Automotive engine testing, aerospace propulsion systems, industrial process monitoring.

## Supply Chain Position

- **Upstream Key Components/Materials**: Piezoelectric quartz crystals, high-strength alloys, precision machining, electronic measurement instruments, shielded cables and connectors
- **Downstream Customers/Application Scenarios**: Automotive testing, machine tools and cutting tools, aerospace, robot OEMs, industrial automation
- **Main Competitors/Peers**: ATI Industrial Automation, HBM (Hottinger Brüel & Kjær), PCB Piezotronics, Kistler Group brands, domestic Kunwei Technology

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_kistler`
- Product Entity: `ent_product_kistler_9107b`
- Component Entity: `ent_component_kistler_9107b_sensor`
- Key Relationships:
  - `ent_company_kistler` -- `manufactures` --> `ent_product_kistler_9107b`
  - `ent_company_kistler` -- `manufactures` --> `ent_component_kistler_9107b_sensor`
  - `ent_product_kistler_9107b` -- `uses` --> `ent_component_kistler_9107b_sensor`

## References

1. [Kistler Official Website](https://www.kistler.com)
2. [Kistler 9107B Three-Component Force Sensor Product/Data Page](https://www.kistler.com/en/products/force-sensors/9107b)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
