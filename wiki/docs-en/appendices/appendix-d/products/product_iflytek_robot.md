# iFlytek Robot

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [iFlytek / iFlytek](../companies/company_iflytek.md) |
| **Product Category** | Embodied Intelligent Robot / Service Robot |
| **Release Date** | Related solutions gradually released from 2023 to 2024 |
| **Status** | Solution / Co-development in progress |
| **Official Website/Source** | See references in the main text |

## Product Overview

The iFlytek robot solution is centered on the iFlytek Spark Large Model and the Robot Super Brain, combining leading voice interaction, natural language understanding, and multimodal perception capabilities. It provides an intelligent agent brain for scenarios such as service robots, elderly care, education, and guided tours. The company often collaborates with partners for motion control and complete machines, emphasizing the empowerment of the "brain" and interaction capabilities.

## Product Images

> iFlytek Robot: Please visit [Official Materials](https://www.iflytek.com) for details.

## Specification Parameters Table

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Core Capabilities | Speech recognition, natural language understanding, multimodal interaction, task planning | iFlytek official website |
| Brain Platform | iFlytek Spark Large Model + Robot Super Brain | iFlytek public information |
| Voice Interaction | Far-field sound pickup, dialect recognition, multi-turn dialogue | iFlytek public information |
| Visual Understanding | Combined with iFlytek Spark multimodal capabilities | Public reports |
| Motion Control | Joint development with complete machine partners | Not disclosed |
| Deployment Method | Cloud + Edge | iFlytek official website |
| Typical Scenarios | Guided tours, companionship, education, healthcare | Public reports |
| Price | Not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [iFlytek / iFlytek](../companies/company_iflytek.md)
- **Core Components/Technology Sources**: AI chips/servers, microphone arrays, camera modules, complete machine partners.
- **Downstream Applications/Customers**: Service robot OEMs, elderly care institutions, educational institutions, medical institutions, exhibition halls/government affairs.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_iflytek_robot`
- Manufacturer Entity: `ent_company_iflytek`
- Key Relationships:
  - `rel_ent_company_iflytek_manufactures_ent_product_iflytek_robot` (`ent_company_iflytek` → `manufactures` → `ent_product_iflytek_robot`)
  - `ent_product_iflytek_robot` -- `uses` --> `ent_product_iflytek_xinghuo`
  - `ent_product_iflytek_robot` -- `uses` --> `ent_component_voice_array`

## Application Scenarios

- **Exhibition Hall Guided Tours**: Greeting, explanation, and Q&A based on voice and vision.
- **Elderly Care Companionship**: Emotional companionship, health reminders, emergency call linkage.
- **Educational Interaction**: AI teachers, programming education, children's companionship.

## Competitive Comparison

| Comparison Item | iFlytek Robot | SenseTime Embodied Solution | UBTECH Walker |
|-----------------|---------------|-----------------------------|---------------|
| Core Advantage | Voice interaction and Chinese large model | Vision and multimodal | Complete machine and motion control |
| Model | Brain + ecosystem collaboration | Model + perception solution | Self-developed complete machine |
| Scenarios | Service/elderly care/education | Industrial/service | Education/commercial |

## Purchase and Deployment Recommendations

- Select the corresponding model based on computing power, accuracy, and scenario requirements, prioritizing official toolchain support and ecosystem compatibility.
- Before deployment, confirm that power supply, heat dissipation, mechanical interfaces, and communication protocols meet the complete machine requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: iFlytek / iFlytek](../companies/company_iflytek.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [iFlytek / iFlytek Official Product/Company Page](https://www.iflytek.com)
2. [iFlytek Official Website](https://www.iflytek.com)
3. iFlytek Spark Large Model Launch Event
