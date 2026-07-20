# Shenyuansheng Technology / Shenyuansheng

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 神源生科技 |
| **English Name** | Shenyuansheng |
| **Headquarters** | Nanjing, Jiangsu, China |
| **Founded** | 2012 |
| **Official Website** | [https://www.shenyuansheng.com / http://www.nbit6d.com](https://www.shenyuansheng.com) |
| **Supply Chain Role** | Six-axis force/torque sensors, multi-dimensional force measurement and control equipment, force control solutions |
| **Enterprise Attribute** | National High-Tech Enterprise, affiliated with Nanjing University of Aeronautics and Astronautics |
| **Parent Company/Group** | Independent operation |
| **Data Source** | Shenyuansheng official website, public product materials, academic papers |

## Company Profile

Nanjing Shenyuansheng Intelligent Technology Co., Ltd. (NBIT), relying on the Institute of Bionic Structure and Material Protection of Nanjing University of Aeronautics and Astronautics, focuses on the R&D and industrialization of multi-dimensional force sensors, force measurement and control technology, and scientific instruments. The company's products are widely used in aerospace, robotics, industrial automation, medical surgery, and university research.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Six-axis Force Sensors | Robot end-effector force sensing | MLL / Octagonal Ring / Ring-type Digital Series | Collaborative/Humanoid Robots |
| Joint Torque Sensors | Rotary joint torque | Custom Series | Industrial Robots, Humanoid Robots |
| Force Measurement Platforms & Data Acquisition | Force measurement & scientific instruments | NST Series Collectors, Force Measurement Platforms | Research, Testing |
| Force Control Specialized Equipment | Grinding/Assembly | Polishing & Grinding Specialized Machine | Industrial Automation |

## Representative Products

### Shenyuansheng MLL Series Six-axis Force Sensor

> Shenyuansheng MLL Series Six-axis Force Sensor: Please visit [Official Materials](https://www.shenyuansheng.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Aluminum alloy analog six-axis force sensor | Shenyuansheng official website |
| Force Measurement Range (Fx/Fy/Fz) | 50 / 50 / 100 N (typical model) | Shenyuansheng official website |
| Torque Measurement Range (Mx/My/Mz) | 2 / 2 / 4 Nm (typical model) | Shenyuansheng official website |
| Accuracy | ≤ 0.5% FS | Shenyuansheng official website |
| Resolution | 24 bit (with collector) | Shenyuansheng official website |
| Overload Capacity | ≥ 300% FS | Shenyuansheng official website |
| Crosstalk Error | ≤ 2% FS | Shenyuansheng official website |
| Power Supply | 5 – 24 VDC | Shenyuansheng official website |
| Output | Analog / USB / RS485 (with collector) | Shenyuansheng official website |
| Sampling Frequency | Up to 1000 Hz | Shenyuansheng official website |
| Operating Temperature | 0℃ – +60℃ | Shenyuansheng official website |
| Weight | Approx. 200 g (varies by model) | Shenyuansheng official website |
| Price | Not disclosed | - |

**Technical Highlights**: High-stiffness aluminum alloy structure, low crosstalk error, supports analog and digital acquisition, suitable for precision force control and research testing.

**Application Scenarios**: Collaborative robot drag teaching, humanoid robot wrist/ankle force control, medical surgery force feedback, 3C assembly, scientific experiments.

### Shenyuansheng Ring-type Digital Six-axis Force Sensor

> Shenyuansheng Ring-type Digital Six-axis Force Sensor: Please visit [Official Materials](https://www.shenyuansheng.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Type | Titanium alloy ring-type digital six-axis force sensor | Shenyuansheng official website |
| Features | High stiffness, high resolution, low crosstalk | Shenyuansheng official website |
| Application | Robot force control grinding, assembly | Shenyuansheng official website |
| Price | Not disclosed | - |

**Technical Highlights**: Titanium alloy ring structure, built-in digital acquisition, suitable for high-load industrial force control.

**Application Scenarios**: Robot grinding and polishing, precision assembly, drag teaching.

## Supply Chain Position

- **Upstream Key Components/Materials**: Aerospace aluminum alloy, strain gauges, signal conditioning chips, cables and connectors
- **Downstream Customers/Application Scenarios**: Collaborative robots, humanoid robots, medical robots, aerospace testing, university research
- **Main Competitors/Peers**: Kunwei Technology, Yuli Instrument, Keli Sensing, ATI Industrial Automation

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_shenyuan`
- Product Entity: `ent_product_shenyuan_mll_6axis_sensor`
- Component Entity: `ent_component_shenyuan_mll_sensor_core`
- Key Relationships:
  - `ent_company_shenyuan` -- `manufactures` --> `ent_product_shenyuan_mll_6axis_sensor`
  - `ent_company_shenyuan` -- `manufactures` --> `ent_component_shenyuan_mll_sensor_core`
  - `ent_product_shenyuan_mll_6axis_sensor` -- `uses` --> `ent_component_shenyuan_mll_sensor_core`

## References

1. [Shenyuansheng Technology Official Website](https://www.shenyuansheng.com)
2. [Shenyuansheng MLL Series Six-axis Force Sensor Product/Materials Page](http://www.nbit6d.com/product/687.html)
3. Company annual reports, product datasheets, and public press releases
4. [Appendix D Product Catalog](../index-products.md)
