# SenseTime

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 商汤科技 |
| **English Name** | SenseTime |
| **Headquarters** | Hong Kong, China / Shanghai |
| **Founded** | 2014 |
| **Website** | [https://www.sensetime.com](https://www.sensetime.com) |
| **Supply Chain Role** | Computer Vision, Multimodal Large Models, AI Computing, Embodied Intelligence, Autonomous Driving |
| **Enterprise Attribute** | Listed Company (HKEX: 0020), one of the largest AI software companies in Asia |
| **Parent Company/Group** | None (Independent listed entity) |
| **Data Source** | SenseTime official website, annual reports, public press releases, industry research reports |

## Company Overview

SenseTime focuses on computer vision and multimodal large models, leveraging the SenseCore large-scale AI infrastructure and the SenseNova large model series to provide perception, understanding, and decision-making capabilities for embodied intelligence and robotics.

SenseTime is a leading AI software company in China, with businesses covering smart commerce, smart cities, smart living, and intelligent vehicles. The SenseCore large-scale AI infrastructure provides a closed loop of computing power, algorithms, and data; the SenseNova large model system covers language, vision, multimodal, and code generation; SenseTime also offers perception and interaction solutions for robotics/embodied intelligence.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|-------------------------|-------------------|
| SenseNova Large Models | Multimodal Foundation Models | SenseNova 5.0 / 5.5 | Embodied Intelligence, Content Generation, Smart Customer Service |
| SenseCore AI Infrastructure | Computing Power & MaaS Platform | Lingang AIDC | Large Model Training, Scientific Research, Industry AI |
| Intelligent Vehicles & Robotics | Visual Perception & Decision Solutions | SenseAuto / Embodied Intelligence Solutions | Autonomous Driving, Robotics |

## Representative Products

### SenseNova / Embodied Multimodal Models

> SenseNova / Embodied Multimodal Models: Please visit [official materials](https://www.sensetime.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Model Series | SenseNova (Language/Vision/Multimodal/Embodied) | SenseTime official website |
| Parameter Scale | Billions to hundreds of billions (multiple specifications) | SenseTime public materials |
| Capabilities | Image understanding, video analysis, natural language interaction, task planning | SenseTime public materials |
| Embodied Capabilities | Vision-Language-Action (VLA) support, environment understanding, instruction following | Public reports |
| Deployment | Cloud API / Private deployment / Edge adaptation | SenseTime official website |
| Training Computing | SenseCore large-scale AI infrastructure | SenseTime official website |
| Interface | SenseTime API / Enterprise customization | SenseTime official website |
| Pricing | Billed by call volume / private deployment | SenseTime official website |

**Technical Highlights**: Unified multimodal architecture, strong Chinese visual understanding, action planning and scene understanding for embodied intelligence, integrated training and inference on SenseCore.

**Application Scenarios**: Humanoid robot brain, smart customer service, content generation, industrial quality inspection, autonomous driving perception.

### SenseTime SenseCore AI Infrastructure

> SenseTime SenseCore AI Infrastructure: Please visit [official materials](https://www.sensetime.com) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Computing Scale | Lingang AIDC: Tens of thousands of GPUs/AI chips | SenseTime public materials |
| Platform Capabilities | Closed loop of computing power, algorithms, and data | SenseTime official website |
| Service Form | MaaS, model training, fine-tuning, inference | SenseTime official website |
| Model Repository | SenseNova series, industry large models | SenseTime official website |
| Energy Efficiency | Not disclosed | - |
| Deployment | Public cloud, private cloud, hybrid cloud | SenseTime official website |
| Customers | Government/enterprises, automotive, finance, healthcare, etc. | SenseTime annual report |
| Pricing | Billed by computing power / service | SenseTime official website |

**Technical Highlights**: Full-stack AI infrastructure, supporting the entire lifecycle of large models, providing computing power and data closed loop for embodied intelligence.

**Application Scenarios**: Large model training and inference, urban governance, autonomous driving, robotic agents.

## Supply Chain Position

- **Upstream Key Components/Materials**: AI chips/servers, data centers, data annotation, open-source frameworks, computing partners.
- **Downstream Customers/Application Scenarios**: Automotive companies, robot manufacturers, government/enterprise customers, internet platforms, financial institutions.
- **Main Competitors/Peers**: Baidu ERNIE, Alibaba Tongyi, Huawei Pangu, iFlytek Spark, Megvii, CloudWalk.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_sensetime`
- Product Entities: `ent_product_sensetime_ruyi`, `ent_product_sensetime_sensecore`
- Key Relationships:
  - `ent_company_sensetime` -- `manufactures` --> `ent_product_sensetime_ruyi`
  - `ent_company_sensetime` -- `manufactures` --> `ent_product_sensetime_sensecore`
  - `ent_product_sensetime_ruyi` -- `runs_on` --> `ent_product_sensetime_sensecore`
  - `ent_product_sensetime_ruyi` -- `uses` --> `ent_component_gpu_cluster`

## References

1. [Official Website](https://www.sensetime.com)
2. [SenseTime Official Website](https://www.sensetime.com)
3. SenseTime 2024 Annual Report
