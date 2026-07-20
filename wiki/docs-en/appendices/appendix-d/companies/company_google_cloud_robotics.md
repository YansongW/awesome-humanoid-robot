# Google Cloud Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).  
> Data updated: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Google Cloud Robotics |
| **English Name** | Google Cloud Robotics |
| **Headquarters** | Mountain View, California, USA |
| **Founded** | Announced in 2018, developer preview in 2019 |
| **Official Website** | [https://cloud.google.com/solutions/robotics](https://cloud.google.com/solutions/robotics) |
| **Supply Chain Role** | Cloud robotics platform, robot-cloud federation orchestration, AI/ML services |
| **Enterprise Attribute** | Public cloud department service |
| **Parent Company/Group** | Google Cloud / Alphabet Inc. |
| **Data Source** | Google Cloud official website, Cloud Robotics Core GitHub, The Robot Report |

## Company Overview

Google Cloud Robotics is a cloud robotics platform launched by Google Cloud for robot developers and enterprises. Its core goal is to leverage Kubernetes, Google AI/ML services, and the open-source ROS ecosystem to build scalable robot fleet management and automation solutions.

The platform is built around Cloud Robotics Core as its core open-source project, providing secure bidirectional robot-cloud communication, application package management, federated configuration, and deep integration with Google Cloud services (Vertex AI, BigQuery, Cloud Storage, Cartographer SLAM, TensorFlow). Its "Object Intelligence" and "Spatial Intelligence" services support grasp planning, inventory management, and robot perception in dynamic environments.

Although the full commercialization path of Google Cloud Robotics is more low-key compared to AWS RoboMaker, its open-source core and Kubernetes-native architecture are representative in multi-cloud/hybrid cloud deployments and DevOps-friendly robot application distribution.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Cloud Robotics Core Platform | Open-source robot-cloud federation framework | Cloud Robotics Core | Industrial automation, AMR fleets |
| AI/ML Services | Object recognition, pose estimation, SLAM | Vertex AI + Cartographer | Grasping, navigation, digital twins |
| Robot Application Marketplace | Kubernetes application package distribution | Cloud Robotics App Management | Multi-brand robot integration |
| Data and Monitoring | Logging, monitoring, alerting | Google Cloud Operations Suite | Remote operations, fleet analytics |

## Representative Products

### Google Cloud Robotics Platform

> Google Cloud Robotics Platform: Please visit [official documentation](https://cloud.google.com/solutions/robotics) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Deployment Model | Public cloud PaaS / Open-source core | Google Cloud official website |
| Open-source Core | Cloud Robotics Core (GitHub) | Google Cloud Robotics GitHub |
| Orchestration Engine | Kubernetes / GKE | Google Cloud documentation |
| Middleware Support | ROS / ROS2 | Cloud Robotics Core documentation |
| Communication Protocols | gRPC, MQTT, HTTPS | Public information |
| AI Services | Vertex AI, AutoML, TensorFlow | Google Cloud public information |
| Spatial Intelligence | Cartographer (2D/3D SLAM) | Google open-source project |
| Pricing | Billed based on Google Cloud resource usage | Google Cloud pricing page |

**Technical Highlights**: Kubernetes-native robot application management, secure bidirectional robot-cloud communication, perception and decision-making integrated with Vertex AI, open-source Cloud Robotics Core, portable data ownership model.

**Application Scenarios**: Multi-brand AMR fleet orchestration, industrial digital twins, cloud-based SLAM and map sharing, robot vision-language-action models based on Gemini/Vertex AI.

### Cloud Robotics Core

> Cloud Robotics Core: Please visit [official documentation](https://cloud.google.com/solutions/robotics) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Code Repository | github.com/googlecloudrobotics/core | GitHub |
| Open-source License | Apache 2.0 | GitHub |
| Primary Languages | Go, Bazel, Terraform | GitHub |
| Core Capabilities | Federated configuration, application packages, secure communication | GitHub README |
| Deployment Method | Cloud cluster + robot edge cluster | Documentation |
| Authentication Method | OAuth / Workload Identity | Documentation |
| Pricing | Open-source and free; cloud resources billed per Google Cloud | GitHub / Google Cloud |

**Technical Highlights**: Declarative robot-cloud resource configuration, application lifecycle management, device identity and certificate management, unified identity authentication with Google Cloud services.

**Application Scenarios**: Enterprise private cloud robot platform setup, cross-regional robot fleet management, highly customizable cloud-edge collaborative robot systems.

## Supply Chain Position

- **Upstream Key Components/Materials**: Google Cloud infrastructure, Kubernetes ecosystem, ROS/ROS2, Edge TPU, NVIDIA/Intel computing platforms, open-source SLAM/perception algorithms.
- **Downstream Customers/Application Scenarios**: Industrial robot OEMs, AMR manufacturers, system integrators, logistics and manufacturing enterprises, research institutions.
- **Main Competitors/Comparables**: AWS RoboMaker, Microsoft Azure IoT / ROS, Formant, InOrbit, Freedom Robotics.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_google_cloud_robotics`
- Product/Platform Entities: `ent_product_google_cloud_robotics_platform`, `ent_product_google_cloud_robotics_core`
- Key Relationships:
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_platform` (`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_platform`)
  - `rel_ent_company_google_cloud_robotics_manufactures_ent_product_google_cloud_robotics_core` (`ent_company_google_cloud_robotics` → `manufactures` → `ent_product_google_cloud_robotics_core`)

## References

1. [Google Cloud Robotics Official Website](https://cloud.google.com/solutions/robotics)
2. [Cloud Robotics Core GitHub](https://github.com/googlecloudrobotics/core)
3. [Cloud Robotics Core Documentation](https://googlecloudrobotics.github.io/core/)
4. [The Robot Report – Google Cloud Robotics Platform Coverage](https://www.therobotreport.com/google-cloud-robotics-platform/)
