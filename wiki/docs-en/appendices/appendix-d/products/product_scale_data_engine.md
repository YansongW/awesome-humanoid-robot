# Scale AI Data Engine

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Table of Contents](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Scale AI](../companies/company_scale_ai.md) |
| **Product Category** | AI Training Data Platform / Data Annotation / RLHF |
| **Release Date** | 2016 |
| **Status** | Commercial / Scaled |
| **Official Website/Source** | [Scale Data Engine](https://scale.com/data-engine) |

## Product Overview

Scale Data Engine is Scale AI's core product, covering the full lifecycle of AI training data: data collection, curation, annotation, reinforcement learning from human feedback (RLHF), and model evaluation. The platform supports multimodal data including images, video, 3D point clouds, text, audio, and sensor fusion, serving as critical infrastructure for autonomous driving, robotics, large language models, and government defense projects.

The Data Engine offers two service modes: Rapid (Scale provides the management platform and crowdsourced/expert annotation teams) and Self-Serve (enterprises use Scale's tools with their own teams). The platform leverages AI pre-labeling, human review, consensus mechanisms, and automated quality checks to improve efficiency while ensuring annotation quality.

In 2025, Scale further launched the Physical AI project, specifically collecting first-person operation demonstration data for embodied intelligence and humanoid robots, strengthening its core position in the robot data supply chain.

## Product Image

> Scale Data Engine: Please visit [Official Materials](https://scale.com/data-engine) for details.

## Specification Parameter Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Supported Data Types | Image, Video, 3D Point Cloud, Text, Audio, Sensor Fusion | Scale Official Website |
| Annotation Capabilities | 2D/3D Bounding Boxes, Semantic Segmentation, Keypoints, Trajectories, Attributes | Scale Documentation |
| Service Modes | Rapid (Managed) / Self-Serve | Scale Official Website |
| Quality Mechanisms | AI Pre-labeling + Human Review + Consensus Mechanisms | Public Information |
| Compliance Certifications | SOC 2 Type II, ISO 27001, FedRAMP High | Scale Official Website |
| Robot Data | Multi-sensor annotation for LiDAR, Camera, IMU, Tactile, etc. | Scale Documentation |
| Pricing | Billed based on task complexity | Public Reports |

## Supply Chain Position

- **Manufacturer**: [Scale AI](../companies/company_scale_ai.md)
- **Core Components/Technology Sources**: AWS/Google Cloud/Azure cloud infrastructure, global crowdsourcing and expert network, AI pre-labeling models, data security and compliance systems.
- **Downstream Applications/Customers**: OpenAI, Meta, Microsoft, Google, Toyota, GM, U.S. Department of Defense, autonomous driving companies, robotics companies.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_scale_data_engine`
- Manufacturer Entity: `ent_company_scale_ai`
- Key Relationships:
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_data_engine` (`ent_company_scale_ai` → `manufactures` → `ent_product_scale_data_engine`)

## Application Scenarios

- **Autonomous Driving Perception Training**: 3D point cloud annotation, 2D bounding boxes, lane lines, traffic sign recognition.
- **Robot Grasping and Navigation**: Operation video annotation, object keypoints, force feedback data alignment.
- **Large Language Model RLHF**: Preference ranking, safety evaluation, instruction-following dataset construction.
- **Defense Intelligence Analysis**: Multi-source intelligence data annotation and model evaluation.

## Competitive Comparison

| Comparison Item | Scale Data Engine | Appen | Labelbox |
|----------------|-------------------|-------|----------|
| Positioning | Full-stack AI training data platform | Managed annotation service | Enterprise self-service annotation software |
| Core Advantage | RLHF, government compliance, robot data | Low cost, high volume | Self-service flexibility |
| Service Mode | Rapid + Self-Serve | Primarily managed | Primarily self-service |
| Compliance | FedRAMP High, SOC 2 | Relatively comprehensive | Relatively comprehensive |
| Typical Customers | Frontier AI labs, defense | Large tech enterprises | Mid-sized enterprises |

## Selection and Deployment Recommendations

- For autonomous driving or robotics projects with massive data volumes and high quality requirements, the Rapid mode can be prioritized.
- For enterprises with existing annotation teams that value data privacy, the Self-Serve mode offers greater controllability.
- For government or defense projects, compliance qualifications such as FedRAMP High and data isolation requirements must be confirmed.

## References

1. [Scale Data Engine Product Page](https://scale.com/data-engine)
2. [Scale AI Official Website](https://scale.com)
3. [Scale Physical AI Blog](https://scale.com/blog/physical-ai)
4. [Scale AI Funding and Valuation Report](https://scale.com/blog)
