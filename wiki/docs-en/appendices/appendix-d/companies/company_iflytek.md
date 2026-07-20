# iFlytek

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | 科大讯飞 |
| **English Name** | iFlytek |
| **Headquarters** | Hefei, Anhui Province, China |
| **Founded** | 1999 |
| **Official Website** | [https://www.iflytek.com](https://www.iflytek.com) |
| **Supply Chain Role** | Intelligent Voice, Cognitive Large Model, AI Chip, Robotics, Education/Healthcare AI |
| **Company Type** | Listed Company (SZSE: 002230), China's Voice and AI Leader |
| **Parent Company/Group** | None (Independent Listed Entity) |
| **Data Source** | iFlytek Official Website, Annual Reports, Public Press Releases, Industry Research Reports |

## Company Overview

iFlytek, centered on intelligent voice and the iFlytek Spark Cognitive Large Model, provides voice interaction, multimodal understanding, and edge AI capabilities for embodied intelligent robots.

iFlytek is a national AI team in China, long engaged in core technology research in intelligent voice, natural language processing, and machine learning. The iFlytek Spark Large Model covers language, image, code, mathematics, and multimodal capabilities; the company has also launched iFlytek Super Brain, AI learning machines, smart office and robot solutions, and collaborates with robot manufacturers to explore embodied intelligence.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|---|---|---|---|
| iFlytek Spark Large Model | Cognitive Large Model | iFlytek Spark V4.0 | Embodied Intelligence, Education, Healthcare, Office |
| Intelligent Voice & Interaction | Speech Recognition & Synthesis | iFlytek Open Platform, Microphone Array | Robotics, Automotive, Smart Home, Customer Service |
| Robotics & Smart Hardware | Embodied Intelligence & Industry Robots | iFlytek Robot Super Brain, Exoskeleton/Service Robots | Elderly Care, Healthcare, Education, Guided Tours |

## Representative Products

### iFlytek Robot / Embodied Intelligence Solution

> iFlytek Robot / Embodied Intelligence Solution: Please visit [Official Materials](https://www.iflytek.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Core Capabilities | Speech Recognition, Natural Language Understanding, Multimodal Interaction, Task Planning | iFlytek Official Website |
| Brain Platform | iFlytek Spark Large Model + Robot Super Brain | iFlytek Public Materials |
| Voice Interaction | Far-field Pickup, Dialect Recognition, Multi-turn Dialogue | iFlytek Public Materials |
| Visual Understanding | Combined with iFlytek Spark Multimodal Capabilities | Public Reports |
| Motion Control | Joint Development with OEM Partners | Not Disclosed |
| Deployment Method | Cloud + Edge | iFlytek Official Website |
| Application Scenarios | Guided Tours, Companion, Education, Healthcare | Public Reports |
| Price | Not Disclosed | - |

**Technical Highlights**: Leading voice interaction and Chinese large model, Robot Super Brain enabling multimodal perception and task planning, ecosystem collaboration with OEMs.

**Application Scenarios**: Service Robots, Elderly Companion, Education Robots, Exhibition Guided Tours, Healthcare Assistance.

### iFlytek Spark Large Model

> iFlytek Spark Large Model: Please visit [Official Materials](https://www.iflytek.com) for details.

| Specification | Value | Remarks/Source |
|---|---|---|
| Model Version | iFlytek Spark V4.0 | iFlytek Official Website |
| Parameter Scale | Not Disclosed | - |
| Capabilities | Text Generation, Multimodal Understanding, Code, Mathematics, Logical Reasoning | iFlytek Public Materials |
| Voice Capabilities | Multi-emotion Speech Synthesis, Human-like Dialogue | iFlytek Public Materials |
| Deployment | APP, API, Edge, Private Deployment | iFlytek Official Website |
| Industry Applications | Education, Healthcare, Office, Automotive, Robotics | iFlytek Public Materials |
| Training Compute | Self-owned Compute Platform + Domestic Compute Adaptation | Public Reports |
| Price | Basic Features Free; API/Enterprise Version Pay-as-you-go | iFlytek Official Website |

**Technical Highlights**: Leading Chinese semantic understanding, integrated voice and large model, deep integration with education/healthcare/office scenarios, support for domestic compute.

**Application Scenarios**: Embodied Intelligent Interaction, Smart Customer Service, Content Creation, Smart Office, Education Tutoring.

## Supply Chain Position

- **Upstream Key Components/Materials**: AI Chips/Servers, Microphone Arrays, Camera Modules, Cloud Computing Resources, Data Services.
- **Downstream Customers/Application Scenarios**: Education/Healthcare/Government/Automotive/Robotics Industry Clients, Developers, Consumers.
- **Main Competitors/Peers**: Baidu, Alibaba, Huawei, SenseTime, Unisound; Voice domain peers: Amazon Alexa, Google Assistant.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_iflytek`
- Product Entities: `ent_product_iflytek_robot`, `ent_product_iflytek_xinghuo`
- Key Relationships:
  - `ent_company_iflytek` -- `manufactures` --> `ent_product_iflytek_robot`
  - `ent_company_iflytek` -- `manufactures` --> `ent_product_iflytek_xinghuo`
  - `ent_product_iflytek_robot` -- `uses` --> `ent_product_iflytek_xinghuo`
  - `ent_product_iflytek_xinghuo` -- `uses` --> `ent_component_voice_array`

## References

1. [Official Website](https://www.iflytek.com)
2. [iFlytek Official Website](https://www.iflytek.com)
3. iFlytek 2024 Annual Report
