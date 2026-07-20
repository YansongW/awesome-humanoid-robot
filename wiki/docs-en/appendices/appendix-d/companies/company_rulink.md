# Rulink / Flexolink

> This entry belongs to [Appendix D Company/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 柔灵科技 |
| **English Name** | Rulink / Flexolink AI |
| **Headquarters** | Hangzhou, Zhejiang, China (Offices in Shenzhen and Atlanta, USA) |
| **Founded** | 2020 |
| **Website** | [https://www.flexolinkai.com](https://www.flexolinkai.com) |
| **Supply Chain Segment** | Flexible Sensors, Electronic Skin, Non-invasive Brain-Computer Interface, Neural Interaction Wristband |
| **Company Type** | Private Enterprise, High-Tech Enterprise |
| **Parent Company/Group** | Independent Operation |
| **Data Sources** | 36Kr PitchHub, Rulink Public Reports, China Daily |

## Company Profile

Rulink (Flexolink AI), founded in 2020, is an innovative enterprise focusing on non-invasive brain-computer interfaces and flexible electronic technologies. The company's team consists of materials scientists, neuroscientists, and human-computer interaction engineers from universities such as MIT, New York University, Carnegie Mellon, and UC Berkeley, with offices in Hangzhou and Shenzhen, China, and Atlanta, USA.

With "materials + algorithms" as its core, Rulink has developed a series of products including flexible electrode materials based on novel nano-metal particles, the forehead-patch EEG sleep monitoring device Airdream, and the 3D interactive EMG wristband. Its flexible electronic skin and EMG/neural signal sensing technologies can be widely applied in humanoid robot electronic skin, smart wearables, medical health, and AR/VR human-computer interaction.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|---|---|---|---|
| Flexible Neural Sensors | High-precision, low-impedance flexible electrodes | Nano-metal particle flexible electrodes | Brain-computer interface, electronic skin |
| Sleep Monitoring Device | Medical-grade forehead-patch EEG monitoring | Airdream | Smart healthcare, wellness |
| EMG Interaction Wristband | Gesture recognition and virtual interaction | 3D interactive EMG wristband | AR/VR, robot teleoperation |
| Electronic Skin Solution | Robot tactile sensing and perception | Flexible electronic skin module | Humanoid robots, smart wearables |

## Representative Products

### Rulink 3D Interactive EMG Wristband

> Rulink EMG Wristband: Please visit [official materials](https://www.flexolinkai.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Sensing Type | Flexible surface EMG (sEMG) + Flexible electronic skin | Public reports |
| Electrode Material | Novel nano-metal particle flexible electrodes | Public reports |
| Number of Channels | Not disclosed | - |
| Sampling Rate | Not disclosed | - |
| Signal Type | EMG signals, gesture movement intention | Public reports |
| Interaction Method | Gesture recognition, 3D virtual object manipulation | Public reports |
| Weight | Not disclosed | - |
| Battery Life | Not disclosed | - |
| Communication Interface | Not disclosed | - |
| Price | Not disclosed | - |

**Technical Highlights**: Uses flexible nanomaterials for conformal skin contact, combined with AI algorithms for gesture and movement intention decoding, enabling controller-free interaction when paired with AR glasses.

**Application Scenarios**: AR/VR gesture interaction, robot teleoperation, prosthetic control, humanoid robot end-effector perception.

### Rulink Airdream Forehead-Patch EEG Sleep Aid Device

> Rulink Airdream: Please visit [official materials](https://www.flexolinkai.com) for details.

| Specification | Value | Notes/Source |
|---|---|---|
| Product Form | Forehead-patch EEG monitoring device | Public reports |
| Weight | 4 g (single-channel miniaturized device) | 36Kr report |
| Monitoring Accuracy | Medical-grade 93% / Home-grade 86–87% | Public reports |
| Interaction Function | Closed-loop acoustic modulation based on deep sleep EEG waves | Public reports |
| Communication Interface | Not disclosed | - |
| Certification Status | Has obtained China NMPA medical device registration certificate | Public reports |
| Price | Not disclosed | - |

**Technical Highlights**: A miniaturized, wearable EEG monitoring solution that reduces wearing burden through nano-flexible electronic technology, enabling continuous sleep quality monitoring and closed-loop intervention.

**Application Scenarios**: Smart healthcare, wellness institutions, home sleep management, brain-computer interface research.

## Supply Chain Position

- **Upstream Key Components/Materials**: Nano-metal particle electrode materials, flexible polymer substrates, low-noise bioelectric front-end chips, AI algorithm frameworks
- **Downstream Customers/Application Scenarios**: AR/VR device manufacturers, robot manufacturers, medical health, wellness, consumer electronics
- **Main Competitors/Peers**: Neuralink (invasive), Meta neural wristband, Interlink Electronics, Nengsida

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_rulink`
- Product Entity: `ent_product_rulink_tactile_sensor`
- Component Entity: `ent_component_rulink_flexible_electrode`
- Key Relationships:
  - `ent_company_rulink` -- `manufactures` --> `ent_product_rulink_tactile_sensor`
  - `ent_company_rulink` -- `manufactures` --> `ent_component_rulink_flexible_electrode`
  - `ent_product_rulink_tactile_sensor` -- `uses` --> `ent_component_rulink_flexible_electrode`

## References

1. [36Kr PitchHub – Rulink Project Information](https://pitchhub.36kr.com/project/1678511003644934)
2. [China Daily – Rulink at Yunqi Conference Report](http://ex.chinadaily.com.cn/exchange/partners/82/rss/channel/cn/columns/snl9a7/stories/WS6164f759a3107be4979f1f3e.html)
3. [OFweek – Rulink Interview](https://mp.ofweek.com/znyj/a756714302187)
4. [HKTDC – Startup Express International Edition](https://hkmb.hktdc.com/sc/d7eKi5jx/article/"Startup Express: International Edition" – Medical Health)
5. [Appendix D Product Catalog](../index-products.md)
