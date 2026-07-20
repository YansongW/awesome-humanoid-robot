# Sunrise Instruments

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 宇立仪器 |
| **English Name** | Sunrise Instruments |
| **Headquarters** | Shanghai, China |
| **Founded** | 2007 |
| **Website** | [https://www.srisensor.com.cn](https://www.srisensor.com.cn) |
| **Supply Chain Segment** | Six-axis force/torque sensors, force-controlled grinding, robot joint torque sensors |
| **Enterprise Type** | Private enterprise, National-level "Little Giant" in Specialization and Innovation |
| **Parent Company/Group** | Independent operation |
| **Data Source** | Sunrise Instruments official website, public product datasheets, industry reports |

## Company Profile

Sunrise Instruments is a globally leading supplier of force sensors and force control solutions, covering six-axis force/torque sensors, torque sensors, force-controlled grinding equipment, and automotive testing systems.

The company's team has over 30 years of experience in force sensor design and force control, with more than 1,000 product models widely used in industrial robots, collaborative robots, medical robots, automotive testing, and aerospace. Sunrise Instruments is one of the few domestic companies capable of mass-supplying miniature six-axis force sensors and entering the international robot OEM supply chain.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Six-axis Force/Torque Sensors | Multi-dimensional force measurement | M35XX / M38XX / M43XX Series | Collaborative robots, medical robots, humanoid robots |
| Force-controlled Grinding | Robot constant-force floating grinding head | iGrinder Series | Automotive, 3C, metal processing |
| Torque/Joint Sensors | Rotational joint torque measurement | Not disclosed | Humanoid robot joints, industrial servo |
| Automotive Testing | Crash and durability testing | M43XX Test Series | Automotive safety testing, wind tunnel |

## Representative Products

### Sunrise Instruments M35XX Ultra-thin Six-axis Force Sensor

> Sunrise M35XX: Please visit [official page](https://www.srisensor.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Type | Ultra-thin commercial six-axis force sensor | Official website public data |
| Thickness | As thin as 9.2 mm | Official website public data |
| Overload Capacity | 3 times rated range | Official website public data |
| Nonlinearity/Hysteresis | < 1% FS | Official website public data |
| Communication Interface | Ethernet TCP/IP, EtherCAT, RS485, RS232, USB, Analog | Official website public data |
| Protection Rating | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Ultra-thin structure suitable for space-constrained installations, can be embedded in humanoid robot wrists, ankles, or collaborative robot end-effectors for precise force control.

**Application Scenarios**: Humanoid robot wrist/ankle force control, collaborative robot end-effector, medical surgical robots, precision assembly.

### Sunrise Instruments M4313SXX Industrial-grade Six-axis Force Sensor

> Sunrise M4313SXX: Please visit [official page](https://www.srisensor.com.cn) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Accuracy | Better than 0.5% FS | Official website public data |
| Overload Capacity | Up to 5 times rated range | Official website public data |
| Zero Drift Performance | 0.05%/10℃ | Official website public data |
| Communication Interface | Ethernet TCP/IP, EtherCAT, RS485, RS232, USB, Analog | Official website public data |
| Protection Rating | Not disclosed | - |
| Dimensions | Not disclosed | - |
| Weight | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: High overload protection and excellent temperature drift performance, suitable for high-dynamic, wide-temperature-range force control needs in industrial settings.

**Application Scenarios**: Industrial robot grinding/polishing, automotive testing, collaborative robot operations, humanoid robot lower limb force control.

## Supply Chain Position

- **Upstream Key Components/Materials**: High-strength aluminum alloy, silicon strain gauges, signal conditioning circuits, precision machining, data acquisition modules
- **Downstream Customers/Application Scenarios**: Industrial robots, collaborative robots, medical robots, humanoid robots, automotive OEMs, FANUC, KUKA, etc.
- **Main Competitors/Peers**: ATI Industrial Automation, Kunwei Technology, Keli Sensing, Hypersen

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sunrise`
- Product Entity: `ent_component_sunrise_m35xx`
- Product Entity: `ent_component_sunrise_m4313sxx`
- Key Relationships:
  - `ent_company_sunrise` -- `manufactures` --> `ent_component_sunrise_m35xx`
  - `ent_company_sunrise` -- `manufactures` --> `ent_component_sunrise_m4313sxx`
  - `ent_component_sunrise_m35xx` -- `used_in` --> `ent_product_humanoid_robot_wrist`

## References

1. [Sunrise Instruments Official Website](https://www.srisensor.com.cn)
2. [Sunrise Instruments Six-axis Force Sensor Product Page](https://www.srisensor.com.cn)
3. [Industry Report – Sunrise Instruments Miniature Six-axis Force Sensor](https://www.srisensor.com.cn/1367.html)
4. [Appendix D Product Catalog](../index-products.md)
