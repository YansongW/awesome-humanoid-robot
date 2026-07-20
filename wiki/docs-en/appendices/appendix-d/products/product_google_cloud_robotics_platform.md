# Google Cloud Robotics Platform

> This entry belongs to [Appendix D Key Product Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Product Wiki Index](../index-products.md)
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [Google Cloud Robotics](../companies/company_google_cloud_robotics.md) |
| **Product Category** | Cloud Robotics Platform / Robot-Cloud Federation Orchestration |
| **Release Date** | Announced in 2018, Developer Preview in 2019 |
| **Status** | Open Source Core + Enterprise Cloud Service |
| **Official Website/Source** | [Google Cloud Robotics](https://cloud.google.com/solutions/robotics) |

## Product Overview

Google Cloud Robotics Platform is a cloud robotics solution launched by Google Cloud for robot developers and enterprises. Based on the open-source project Cloud Robotics Core, the platform connects robots and the cloud through a Kubernetes federation architecture, enabling developers to manage robot applications as they would cloud applications.

The platform provides secure bidirectional communication, application package distribution, device identity management, and seamlessly integrates Google services such as Vertex AI, Cloud Storage, BigQuery, Cloud Operations Suite, and Cartographer SLAM. Its design emphasizes openness: customers own their data, can migrate as needed, and the core infrastructure is open source.

Unlike the managed approach of AWS RoboMaker, Google Cloud Robotics leans more towards a "platform + open-source core" model, suitable for enterprises requiring high customization, multi-cloud/hybrid cloud deployments, or deep integration with Google AI capabilities.

## Product Image

> Google Cloud Robotics Platform: Please visit the [official documentation](https://cloud.google.com/solutions/robotics) for details.

## Specification Table

| Specification Item | Value | Notes/Source |
|-------------------|-------|--------------|
| Deployment Model | Public Cloud PaaS / Open Source Core | Google Cloud Official Website |
| Open Source Core | Cloud Robotics Core | GitHub |
| Orchestration Engine | Kubernetes / GKE | Google Cloud Documentation |
| Middleware Support | ROS / ROS2 | Cloud Robotics Core Documentation |
| Communication Protocols | gRPC, MQTT, HTTPS | Public Information |
| AI/ML Services | Vertex AI, AutoML, TensorFlow | Google Cloud Public Information |
| Spatial Intelligence | Cartographer 2D/3D SLAM | Google Open Source Project |
| Data Services | Cloud Storage, BigQuery | Google Cloud Documentation |
| Pricing | Billed based on Google Cloud resource usage | Google Cloud Pricing Page |

## Supply Chain Position

- **Manufacturer**: [Google Cloud Robotics](../companies/company_google_cloud_robotics.md)
- **Core Component/Technology Sources**: Google Cloud Infrastructure, Kubernetes Ecosystem, ROS/ROS2, Cartographer, Edge TPU, Vertex AI.
- **Downstream Applications/Customers**: Industrial Robot OEMs, AMR Manufacturers, System Integrators, Logistics and Manufacturing Enterprises, Research Institutions.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_google_cloud_robotics_platform`
- Manufacturer Entity: `ent_company_google_cloud_robotics`
- Key Relationships:
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_platform` (`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_platform`)

## Application Scenarios

- **Multi-Brand AMR Fleet Orchestration**: Use Kubernetes application packages to uniformly manage robot software and configurations from different manufacturers.
- **Cloud-Based SLAM and Map Sharing**: Leverage Cartographer and Cloud Storage for multi-robot map updates and sharing.
- **Vision-Language-Action Models**: Combine Vertex AI and Gemini API to provide multimodal perception and reasoning capabilities for robots.
- **Industrial Digital Twins**: Build high-fidelity digital twin environments using Google Cloud simulation and AI services.

## Competitive Comparison

| Comparison Item | Google Cloud Robotics | AWS RoboMaker | Formant |
|----------------|-----------------------|---------------|---------|
| Positioning | Kubernetes-native cloud robotics platform | End-to-end managed cloud robotics service | Robot data and operations platform |
| Openness | Core is open source | Some services gradually migrated/open sourced | Commercial SaaS |
| AI Integration | Vertex AI / Gemini | SageMaker | Third-party integration |
| Orchestration | Kubernetes Federation | AWS Managed Services | Platform built-in |
| Target Users | Enterprises with DevOps capabilities | Developers looking to quickly move to the cloud | Operational robot customers |

## Selection and Deployment Recommendations

- Suitable for teams with existing Kubernetes/GKE experience who want deep customization of cloud-edge collaborative architectures.
- The open-source Cloud Robotics Core can be used for private cloud or hybrid cloud deployments, reducing vendor lock-in risk.
- Before deployment, plan for device identity authentication, network policies, federation resource configuration, and data pipelines with Vertex AI.

## References

1. [Google Cloud Robotics Official Website](https://cloud.google.com/solutions/robotics)
2. [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
3. [Cloud Robotics Core Documentation](https://googlecloudrobotics.github.io/core/)
4. [The Robot Report – Google Cloud Robotics Platform Coverage](https://www.therobotreport.com/google-cloud-robotics-platform/)
