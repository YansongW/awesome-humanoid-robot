# T-Head Xuantie C920

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [T-Head Semiconductor / T-Head](../companies/company_t_head.md) |
| **Product Category** | RISC-V High-Performance Processor IP |
| **Release Date** | Xuantie C920 is a new generation high-performance RISC-V processor |
| **Status** | Commercial licensing |
| **Official Website/Source** | T-Head official website, Alibaba Cloud Apsara Conference materials |

## Product Overview

T-Head Xuantie C920 is a high-performance RISC-V application processor IP launched by T-Head Semiconductor, targeting scenarios such as edge AI, industrial control, robotics, and AIoT.

The Xuantie C920 is based on the RV64GC instruction set and supports the RISC-V Vector 1.0 extension. It adopts a 12-stage out-of-order superscalar pipeline, featuring high clock frequency, high computing power, and good energy efficiency. Its open RISC-V ecosystem and customizable characteristics enable chip customers to perform deep optimization for tasks such as robot control, vision processing, and AI inference.

## Product Image

> T-Head Xuantie C920: Please visit [official materials](https://www.t-head.cn) for details.

## Specification Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Processor IP | Xuantie C920 | T-Head official website |
| Instruction Set | RISC-V RV64GC + Vector 1.0 | T-Head public materials |
| Microarchitecture | 12-stage out-of-order superscalar | T-Head public materials |
| Clock Frequency | Up to 3 GHz (public reports) | Public reports |
| Computing Power | Not disclosed | - |
| Cache | Supports multi-level cache | T-Head public materials |
| Bus Interface | AXI / ACE | T-Head public materials |
| Extension Support | Can integrate AI accelerator, security extension | T-Head public materials |
| Power Consumption | Depends on specific implementation | T-Head public materials |
| Price | IP licensing, not disclosed | - |

## Supply Chain Position

- **Manufacturer**: [T-Head Semiconductor / T-Head](../companies/company_t_head.md)
- **Core Components/Technology Source**: Self-developed RISC-V core, EDA tools, licensed customer wafer foundry/packaging and testing.
- **Downstream Applications/Customers**: Chip design companies, AIoT vendors, automotive electronics, industrial control, robot chip manufacturers.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_t_head_xuantie_c920`
- Component Entity: `ent_component_t_head_xuantie_c920_ip`
- Manufacturer Entity: `ent_company_t_head`
- Key Relationships:
  - `rel_ent_company_t_head_manufactures_ent_product_t_head_xuantie_c920` (`ent_company_t_head` → `manufactures` → `ent_product_t_head_xuantie_c920`)
  - `rel_ent_company_t_head_manufactures_ent_component_t_head_xuantie_c920_ip` (`ent_company_t_head` → `manufactures` --> `ent_component_t_head_xuantie_c920_ip`)
  - `ent_product_t_head_xuantie_c920` -- `uses` --> `ent_component_t_head_xuantie_c920_ip`

## Application Scenarios

- **Robot Main Control MCU/MPU**: Serves as the core processor for robot motion control, communication, and task scheduling.
- **Edge AI Computing**: After integrating NPU, used for on-device image recognition, voice processing, and sensor fusion.
- **Industrial Control and AIoT**: Provides energy-efficient computing for smart manufacturing, smart homes, and wearable devices.

## Competitive Comparison

| Comparison Item | Xuantie C920 | ARM Cortex-A78 | SiFive P550 |
|----------------|--------------|----------------|-------------|
| Instruction Set | RISC-V | ARM | RISC-V |
| Ecosystem | T-Head/Open Source RISC-V | Mature ARM Ecosystem | SiFive Ecosystem |
| Customizability | High | Medium | High |
| Licensing Model | IP Licensing | IP Licensing | IP Licensing |

## Selection and Deployment Recommendations

- Evaluate the target software stack's support for RISC-V Vector and privileged architecture.
- Select the C920 configuration based on performance, power, and area targets, and reserve space for AI accelerator integration.
- It is recommended to obtain the IP package, reference design, and technical support through T-Head's official channels.

## Related Entries

- [Manufacturer: T-Head Semiconductor / T-Head](../companies/company_t_head.md)
- [Appendix D.4 Key Products Wiki](../index-products.md)

## References

1. [T-Head Official Website](https://www.t-head.cn)
2. [T-Head Xuantie Series](https://www.t-head.cn/product/)
3. Alibaba Cloud Apsara Conference public materials
