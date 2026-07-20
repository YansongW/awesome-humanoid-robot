# Huawei

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 华为 |
| **English Name** | Huawei |
| **Headquarters** | Shenzhen, Guangdong Province, China |
| **Founded** | 1987 |
| **Official Website** | [https://www.huawei.com](https://www.huawei.com) |
| **Supply Chain Segment** | AI Computing, Ascend Chips, Pangu Large Model, Robot Cloud/Edge/End Solutions, Communications |
| **Enterprise Type** | Non-listed private enterprise, global ICT and AI infrastructure leader |
| **Parent Company/Group** | Huawei Investment & Holding Co., Ltd. |
| **Data Source** | Huawei official website, Ascend community, Pangu large model public materials, public press releases |

## Company Profile

Huawei, leveraging Ascend AI computing, the Pangu large model, HarmonyOS, and 5G/cloud collaboration, provides computing power, models, and operating system foundations for embodied intelligence and humanoid robots.

Huawei is a global leader in ICT infrastructure and smart terminals, with businesses covering carrier networks, enterprise business, terminals, and cloud computing. In the robot/embodied intelligence field, Huawei empowers robot perception, decision-making, control, and multi-robot collaboration through Ascend AI processors, the Atlas computing platform, the Pangu multimodal large model, the HarmonyOS operating system, and cloud-edge-end collaborative solutions.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| Ascend AI Computing | AI processors and computing platforms | Ascend 910 / Atlas series | Large model training/inference, robot brain |
| Pangu Large Model | Multimodal foundation model | Pangu Large Model 5.0 | Embodied intelligence, industrial quality inspection, natural language interaction |
| HarmonyOS & End-side Intelligence | Operating system and distributed soft bus | HarmonyOS / OpenHarmony | Robot terminals, smart home, industrial equipment |

## Representative Products

### Huawei Ascend / Atlas Computing Platform

> Huawei Ascend / Atlas Computing Platform: Please visit [official materials](https://www.huawei.com) for details.

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| AI Processor | Ascend 910 / 310 series | Huawei official website |
| Computing Power | Ascend 910B: FP16 approx. 320 TFLOPS / INT8 approx. 640 TOPS | Huawei public materials |
| Memory | HBM2e / LPDDR4X (varies by model) | Huawei public materials |
| Process Node | 7 nm (public reports) | Public reports |
| Atlas Form Factor | Atlas 800 training server / Atlas 300I inference card / Atlas 200I DK | Huawei official website |
| Software Stack | CANN, MindSpore, MindIE | Huawei Ascend community |
| Power Consumption | Approx. 310 W (Ascend 910 processor) | Public materials |
| Price | Not disclosed | - |

**Technical Highlights**: Domestic AI computing foundation, native support for Pangu large model, end-edge-cloud collaboration, independent software stack and ecosystem.

**Application Scenarios**: Large model training and inference, embodied intelligence brain, autonomous driving, industrial quality inspection, scientific computing.

### Huawei Pangu Large Model

> Huawei Pangu Large Model: Please visit [official materials](https://www.huawei.com) for details.

| Specification Item | Value | Remarks/Source |
|--------------------|-------|----------------|
| Model Series | NLP/CV/Scientific Computing/Multimodal/Embodied Intelligence | Huawei Cloud |
| Parameter Scale | Billions to trillions (multiple specifications) | Huawei public materials |
| Training Framework | MindSpore / PyTorch adaptation | Huawei Cloud |
| Deployment Method | Huawei Cloud / Private deployment / End-side | Huawei Cloud |
| Embodied Capabilities | Multimodal understanding, task planning, action generation | Public reports |
| Toolchain | ModelArts, MindFormers | Huawei Cloud |
| API | Huawei Cloud Pangu Large Model Service | Huawei Cloud |
| Price | Billed by call volume/instance | Huawei Cloud |

**Technical Highlights**: Full-stack independent, equal emphasis on multimodal and scientific computing, deep optimization for industry scenarios, supports robot task planning and understanding.

**Application Scenarios**: Embodied intelligence large model, industrial manufacturing, weather forecasting, drug discovery, intelligent customer service.

## Supply Chain Position

- **Upstream Key Components/Materials**: Chip manufacturing and packaging/testing (affected by international sanctions, ongoing domestic substitution), memory, optical modules, PCB, structural components.
- **Downstream Customers/Application Scenarios**: Carriers, government and enterprise customers, automotive manufacturers, robot OEMs, developers, and cloud computing users.
- **Main Competitors/Peers**: NVIDIA, Intel, AMD, Qualcomm; in the large model field, peers include OpenAI, Baidu ERNIE, Alibaba Cloud Tongyi.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_huawei`
- Product Entities: `ent_product_huawei_ascend`, `ent_product_huawei_pangu`
- Key Relationships:
  - `ent_company_huawei` -- `manufactures` --> `ent_product_huawei_ascend`
  - `ent_company_huawei` -- `manufactures` --> `ent_product_huawei_pangu`
  - `ent_product_huawei_ascend` -- `uses` --> `ent_component_huawei_ascend_chip`
  - `ent_product_huawei_pangu` -- `runs_on` --> `ent_product_huawei_ascend`

## References

1. [Official Website](https://www.huawei.com)
2. [Huawei Official Website](https://www.huawei.com)
3. [Huawei Ascend Community](https://www.hiascend.com)
