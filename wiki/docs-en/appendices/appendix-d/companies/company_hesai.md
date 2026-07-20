# Hesai Technology

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 禾赛科技 |
| **English Name** | Hesai Technology |
| **Headquarters** | Shanghai, China |
| **Founded** | 2014 |
| **Website** | [https://www.hesaitech.com](https://www.hesaitech.com) |
| **Supply Chain Role** | LiDAR, 3D Perception, Autonomous Driving & Robotics LiDAR |
| **Company Type** | Public Company (NASDAQ: HSAI / HKEX: 2525) |
| **Parent Company/Group** | Independently Listed |
| **Data Source** | Official Website, Prospectus, Public Financial Reports & News |

## Company Overview

Hesai Technology is a globally leading LiDAR company, with products covering automotive ADAS, autonomous driving, and robotics.

Hesai possesses full-stack in-house R&D capabilities in chips, optics, mechanics, and algorithms, and operates the Maxwell Smart Manufacturing Center. Its AT, ET, FT, and QT series LiDARs have been mass-produced and deployed in vehicles by multiple leading automakers, and provide 3D perception solutions for robotics and embodied intelligence.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| AT Series | Automotive-grade Ultra-high Resolution Long-range LiDAR | AT128 / AT512 / ATX | ADAS, Autonomous Driving |
| ET Series | Ultra-thin In-cabin Long-range LiDAR | ET25 | Forward Perception, Passenger Vehicles |
| FT/JT Series | All-solid-state Short-range Blind Spot/Robotics LiDAR | FT120 / JT Series | Robotics, Autonomous Driving Blind Spot |

## Representative Products

### Hesai Technology ET25

> Hesai Technology ET25: Please visit [Official Materials](https://www.hesaitech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Thickness | 25 mm | Official Press Release |
| Core Technology | 905 nm Automotive-grade LiDAR | Official Datasheet |
| FOV | 120°(H) × 25°(V) | Official Press Release |
| Detection Range | 250 m @ 10% Reflectivity (without windshield); 225 m (behind windshield) | Official Press Release |
| Point Rate | Over 3 million points/sec | Official Press Release |
| Angular Resolution | 0.05° × 0.05° | Official Press Release |
| Power Consumption | 12 W | Official Press Release |
| Noise | <25 dB (in-cabin) | Official Press Release |
| Weight | Not disclosed | Not disclosed |
| Interface | Not disclosed | Not disclosed |

**Technical Highlights**: Ultra-thin 25 mm body, can be placed behind the windshield, 250 m long-range detection, low power consumption and low noise, designed specifically for in-cabin passenger vehicle use.

**Application Scenarios**: Passenger vehicle ADAS, autonomous driving forward perception, high-end robotics long-range navigation.

### Hesai Technology AT128

> Hesai Technology AT128: Please visit [Official Materials](https://www.hesaitech.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Number of Channels | 128 | Official Datasheet |
| FOV | 120°(H) × 25.4°(V) | Official Datasheet |
| Detection Range | 200 m @ 10% Reflectivity | Official Datasheet |
| Point Rate | 1.536 million points/sec | Official Datasheet |
| Angular Resolution | 0.1° × 0.2° | Official Datasheet |
| Scanning Method | 1D Rotating Mirror + Chip-based Transceiver | Official Datasheet |
| Laser Wavelength | 905 nm | Official Datasheet |
| Price | Not disclosed | Not disclosed |

**Technical Highlights**: Semi-solid-state architecture, automotive-grade reliability, high channel density, has become the primary forward-facing LiDAR solution for multiple automakers.

**Application Scenarios**: Passenger vehicle NOA, Robotaxi, long-haul logistics, high-end mobile robots.

## Supply Chain Position

- **Upstream Key Components/Materials**: 905/1550 nm Laser Diodes, SPAD/SiPM Receiver Chips, Scanning Motors, Optical Lenses, ASIC Chips
- **Downstream Customers/Application Scenarios**: Passenger Vehicle OEMs (Li Auto, Changan, SAIC, etc.), Robotaxi, Logistics Robots, Unmanned Delivery, Humanoid Robots
- **Main Competitors/Peers**: RoboSense, Livox, Huawei, DJI Livox, Velodyne/Ouster, Luminar

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_hesai`
- Product Entity: `ent_component_hesai_et25`
- Product Entity: `ent_component_hesai_at128`
- Key Relationships:
  - `ent_company_hesai` -- `manufactures` --> `ent_component_hesai_et25`
  - `ent_company_hesai` -- `manufactures` --> `ent_component_hesai_at128`

## References

1. [Official Website](https://www.hesaitech.com)
2. [Product Materials and Public Reports](https://www.hesaitech.com)
3. [Appendix D Product Catalog](../index-products.md)
