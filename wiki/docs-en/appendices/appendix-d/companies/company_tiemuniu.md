# Tiemuniu / Iron Bull

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Tiemuniu (Beijing Tiemuniu Intelligent Machine Technology Co., Ltd.) |
| **English Name** | Tiemuniu / Iron Bull |
| **Headquarters** | Beijing, China |
| **Founded** | 2008 |
| **Official Website** | [https://www.mybull.com](https://www.mybull.com) |
| **Supply Chain Role** | Complete Machine OEM / Autonomous Mobile Robot (AMR) |
| **Enterprise Type** | Autonomous Mobile Robot Products and Solutions Provider |
| **Parent Company/Group** | Leador Spatial Information Technology Co., Ltd. |
| **Data Sources** | Tiemuniu Official Website, OFweek, EV Look, New Strategy Robot Network |

## Company Profile

Tiemuniu Robot is a leading provider of autonomous mobile robot (AMR) products and solutions. Leveraging technical support from the Wuhan University Key Laboratory of Surveying, Mapping and Remote Sensing and expert teams including Academician Li Deren, it has formed an innovation system integrating industry, academia, and research. The company focuses on L4-level unmanned logistics solutions, offering customers a "Cloud-Pipe-Device" unmanned logistics transportation solution to help achieve integrated indoor-outdoor unmanned logistics transport.

The company's product line covers unmanned tow tractors, unmanned forklifts, unmanned flatbed vehicles, as well as the "Road King" Robot Positioning and Navigation System (PNS) and the TS-R Robot Management and Control Platform. Tiemuniu products are widely used in automotive, logistics, new energy batteries, photovoltaics, 3C electronics, petroleum, chemical, light industry, security, and other industries, with offices established in the United States, Japan, Saudi Arabia, and other countries.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| Unmanned Tow Tractor | Indoor-outdoor heavy material towing | 2T/4T/6T/10T/15T/40T Tow Tractor | Automotive, airports, ports |
| Unmanned Forklift | Rack access and pallet handling | Indoor-outdoor integrated unmanned logistics forklift | Warehouses, factories, docks |
| Unmanned Flatbed Vehicle | Roller docking flexible conveying | Indoor-outdoor integrated unmanned logistics flatbed vehicle | Factories, chemical fiber, ports |
| Navigation and Dispatching System | Positioning, navigation, and cluster management | PNS System / TS-R Platform / RMMS | AMR OEM, system integration |

## Representative Products

### Tiemuniu Unmanned Tow Tractor

> Tiemuniu Unmanned Tow Tractor: Please visit [Official Materials](https://www.mybull.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Dimensions | Varies by load capacity model | Official Website |
| Weight | Varies by load capacity model | Official Website |
| Load Capacity | 2T / 4T / 6T / 10T / 15T / 40T | OFweek / Official Website |
| Speed/RPM | Not disclosed | - |
| Endurance | Not disclosed | - |
| Navigation Method | GNSS + IMU + 3D SLAM Multi-source Fusion | EV Look |
| Interface/Communication | TS-R Dispatching System | Official Website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Capable of towing multiple material carts at once, supports automatic coupling/decoupling and customized trailers, enabling all-weather, indoor-outdoor complex scenario unmanned driving.

**Application Scenarios**: Automotive OEM factories, airport luggage transfer, port container short-haul transport, factory production line material distribution.

### Tiemuniu Unmanned Forklift

> Tiemuniu Unmanned Forklift: Please visit [Official Materials](https://www.mybull.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Dimensions | Varies by model | Official Website |
| Weight | Varies by model | Official Website |
| Load Capacity/Lifting | Not disclosed | - |
| Fork Positioning Accuracy | High repeatability | Official Website |
| Protection | Optional explosion-proof version (Ex ⅡBT4Gb / Ex ⅢC135°Db) | OFweek |
| Interface/Communication | TS-R Dispatching System | Official Website |
| Price | Not disclosed | Requires inquiry |

**Technical Highlights**: Indoor-outdoor integrated automatic cargo transfer, rack access, pallet stacking, supports all-weather operation and explosion-proof customization.

**Application Scenarios**: Warehouses, factories, logistics parks, airports, docks, petrochemical and other flammable/explosive environments.

## Supply Chain Position

- **Upstream Key Components/Materials**: Self-developed PNS positioning and navigation system; externally purchased LiDAR, GNSS/IMU, motors, drives, batteries, vehicle body structural parts.
- **Downstream Customers/Application Scenarios**: Automotive OEM factories, airports, ports, logistics parks, new energy and chemical enterprises.
- **Main Competitors/Benchmarks**: Standard Robots, Xian AI, Hikrobot, Geek+.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_tiemuniu`
- Product Entities: `ent_product_tiemuniu_tugger`, `ent_product_tiemuniu_forklift`
- Key Relationships:
  - `ent_company_tiemuniu` -- `manufactures` --> `ent_product_tiemuniu_tugger`
  - `ent_company_tiemuniu` -- `manufactures` --> `ent_product_tiemuniu_forklift`

## References

1. [Tiemuniu Official Website](https://www.mybull.com)
2. [OFweek – Tiemuniu Unmanned Logistics Solution](https://robot.ofweek.com/2024-09/ART-8321202-8110-30646164.html)
3. [EV Look – Tiemuniu CeMAT ASIA Debut](https://www.evlook.com/news-54750.html)
4. [New Strategy Robot Network – Tiemuniu Drives Digital and Intelligent Transformation with Robot Products](http://www.xzlrobot.com/c14043.html)
