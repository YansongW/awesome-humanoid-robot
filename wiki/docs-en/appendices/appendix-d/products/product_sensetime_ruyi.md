# SenseTime SenseNova / Embodied Multimodal Model

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [SenseTime / SenseTime](../companies/company_sensetime.md) |
| **Product Category** | Multimodal Large Model / Embodied Intelligence Model |
| **Release Date** | SenseNova released in 2023, continuously iterated |
| **Status** | Commercial / API Service |
| **Official Website/Source** | See references in the main text |

## Product Overview

SenseTime SenseNova (SenseNova) is a multimodal large model system developed by SenseTime, covering natural language, image, video, speech, and code generation. Leveraging the SenseCore large-scale computing infrastructure and computer vision advantages, SenseNova provides visual language understanding, task planning, and action generation capabilities for embodied intelligence, deployable in the cloud or adapted to robot edge devices.

## Product Image

> SenseTime SenseNova / Embodied Multimodal Model: Please visit [official materials](https://www.sensetime.com) for details.

## Specification Parameters Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Model Series | SenseNova (Language/Vision/Multimodal/Embodied) | SenseTime official website |
| Parameter Scale | Tens of billions to hundreds of billions (multiple specifications) | SenseTime public materials |
| Capabilities | Image understanding, video analysis, natural language interaction, task planning | SenseTime public materials |
| Embodied Capabilities | Visual language action support, environment understanding, instruction following | Public reports |
| Deployment | Cloud API / Private deployment / Edge adaptation | SenseTime official website |
| Training Compute | SenseCore large-scale computing infrastructure | SenseTime official website |
| Interface | SenseTime API / Enterprise customization | SenseTime official website |
| Pricing | Billed by call volume / private deployment | SenseTime official website |

## Supply Chain Position

- **Manufacturer**: [SenseTime / SenseTime](../companies/company_sensetime.md)
- **Core Components/Technology Sources**: GPU/AI chip clusters, data annotation, open-source frameworks, computing power partners.
- **Downstream Applications/Customers**: Automotive companies, robot manufacturers, internet platforms, financial/medical/education clients.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_sensetime_ruyi`
- Manufacturer Entity: `ent_company_sensetime`
- Key Relationships:
  - `rel_ent_company_sensetime_manufactures_ent_product_sensetime_ruyi` (`ent_company_sensetime` → `manufactures` → `ent_product_sensetime_ruyi`)
  - `ent_product_sensetime_ruyi` -- `runs_on` --> `ent_product_sensetime_sensecore`
  - `ent_product_sensetime_ruyi` -- `generates` --> `ent_data_robot_task_plan`

## Application Scenarios

- **Humanoid Robot Brain**: Understand natural language instructions and plan action sequences.
- **Visual Navigation**: Combine visual SLAM with semantic understanding for environmental interaction.
- **Industrial Quality Inspection**: Multimodal defect detection and report generation.

## Competitive Comparison

| Comparison Item | SenseNova | GPT-4V | Huawei Pangu |
|----------------|-----------|--------|--------------|
| Visual Understanding | Strong in Chinese scenarios | Strong in general English | Industry/embodied optimized |
| Deployment | Cloud + Edge + Private | Cloud API | Cloud + Edge + Private |
| Compute Power | SenseCore | Azure/OpenAI | Ascend |

## Selection and Deployment Recommendations

- Select the corresponding model based on computing power/accuracy/scenario requirements, prioritizing the official toolchain and ecosystem compatibility.
- Before deployment, confirm that power supply, heat dissipation, mechanical interfaces, and communication protocols meet the overall system requirements.
- It is recommended to obtain the latest firmware, SDK, and technical support through official channels or authorized distributors.

## Related Entries

- [Manufacturer: SenseTime / SenseTime](../companies/company_sensetime.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [SenseTime / SenseTime Official Product/Company Page](https://www.sensetime.com)
2. [SenseTime Official Website](https://www.sensetime.com)
3. SenseTime SenseNova Launch Event Materials
