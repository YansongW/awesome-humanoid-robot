# Scale AI

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).  
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Scale AI |
| **English Name** | Scale AI |
| **Headquarters** | San Francisco, California, USA |
| **Founded** | 2016 |
| **Website** | [https://scale.com](https://scale.com) |
| **Supply Chain Role** | AI/Robotics Data Annotation, Data Engine, Model Evaluation, RLHF |
| **Company Type** | Startup (Unlisted) |
| **Parent Company/Group** | None |
| **Data Source** | Scale AI Official Website, Scale Blog, Public Funding Reports |

## Company Overview

Scale AI is a world-leading AI training data infrastructure company. Its core product, the Scale Data Engine, covers the entire lifecycle of data collection, filtering, annotation, Reinforcement Learning from Human Feedback (RLHF), and model evaluation.

The platform supports multimodal data including images, video, 3D point clouds, text, audio, and sensor fusion, and is widely used in autonomous driving, robotics, large language models (LLMs), and government defense projects. Scale offers two modes: Rapid (managed by Scale's platform and annotator team) and Self-Serve (enterprises use Scale's tools with their own teams). In 2025, Scale launched the Physical AI project, specifically collecting first-person demonstration data for training embodied intelligence and robots.

In June 2025, Meta acquired 49% of Scale AI's equity for $14.3 billion, valuing the company at $29 billion.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| AI Training Data Engine | Full lifecycle data platform | Scale Data Engine | Autonomous Driving, Robotics, LLM |
| Generative AI Data | RLHF, Fine-tuning, Preference Alignment | Scale Generative AI Data Engine | Large Language Models, Multimodal Models |
| Government & Defense | Secure AI Decision Platform | Scale Donovan | Defense Intelligence, Command Decision |
| Model Testing & Evaluation | Red Teaming, Safety Evaluation | Scale Test & Evaluation | Frontier Model Safety |
| Physical AI Data | Robot Manipulation Demonstration Data | Scale Physical AI | Humanoid Robots, Embodied Intelligence |

## Representative Products

### Scale Data Engine

> Scale Data Engine: Please refer to [Official Documentation](https://scale.com) for details.

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Supported Data Types | Image, Video, 3D Point Cloud, Text, Audio, Sensor Fusion | Scale Official Website |
| Annotation Capabilities | 2D/3D Bounding Boxes, Semantic Segmentation, Keypoints, Trajectories, Attributes | Scale Documentation |
| Service Mode | Rapid (Managed) / Self-Serve | Scale Official Website |
| Quality Mechanism | AI Pre-annotation + Human Review + Consensus Mechanism | Public Information |
| Compliance Certifications | SOC 2 Type II, ISO 27001, FedRAMP High | Scale Official Website |
| Robotics Data | Supports multi-sensor annotation including LiDAR, Camera, IMU, Tactile | Scale Documentation |
| Pricing | Billed by task complexity (from a few cents to several dollars per task) | Public Reports |

**Technical Highlights**: AI-assisted pre-annotation, multimodal data pipeline, enterprise-grade quality and security compliance, specialized toolchains for autonomous driving and robotics, global crowdsourcing and expert review network.

**Application Scenarios**: Autonomous driving perception model training, robot grasping/navigation data annotation, large language model RLHF, medical imaging and defense intelligence analysis.

### Scale Physical AI

> Scale Physical AI: Please refer to [Official Documentation](https://scale.com) for details.

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Data Type | First-Person View (POV) Manipulation Demonstration Videos | Scale News |
| Collection Method | Collected by global contractors wearing devices | Public Reports |
| Task Scenarios | Housework, Assembly, Handling, Tool Use | Scale Blog |
| Annotation Content | Action Segmentation, Object Interaction, Force Feedback, Language Instructions | Public Information |
| Target Model | Humanoid Robot / Embodied Intelligence VLA Model | Scale News |
| Pricing | Enterprise Customization | Official Inquiry |

**Technical Highlights**: Large-scale human manipulation data collection for embodied intelligence, multi-view and multimodal synchronization, action-language-vision alignment, supporting imitation learning and reinforcement learning training.

**Application Scenarios**: Humanoid robot housework operation training, industrial assembly skill learning, service robot interaction strategy, robot foundation model data supply.

## Supply Chain Position

- **Upstream Key Components/Materials**: AWS/Google Cloud/Azure Cloud Infrastructure, Global Crowdsourcing and Expert Annotation Network, AI Pre-annotation Models, Data Security and Compliance System.
- **Downstream Customers/Application Scenarios**: OpenAI, Meta, Microsoft, Google, Toyota, GM, U.S. Department of Defense, Autonomous Driving Companies, Robotics Companies.
- **Main Competitors/Peers**: Appen, Labelbox, Surge AI, Tesla's In-house Annotation Team, Covariant Data Flywheel.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_scale_ai`
- Product/Platform Entities: `ent_product_scale_data_engine`, `ent_product_scale_physical_ai`
- Key Relationships:
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_data_engine` (`ent_company_scale_ai` → `manufactures` → `ent_product_scale_data_engine`)
  - `rel_ent_company_scale_ai_manufactures_ent_product_scale_physical_ai` (`ent_company_scale_ai` → `manufactures` → `ent_product_scale_physical_ai`)

## References

1. [Scale AI Official Website](https://scale.com)
2. [Scale Data Engine Product Page](https://scale.com/data-engine)
3. [Scale Physical AI Blog](https://scale.com/blog/physical-ai)
4. [Scale AI Funding and Valuation Reports](https://scale.com/blog)
