# AWS RoboMaker

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Amazon Web Services RoboMaker |
| **English Name** | AWS RoboMaker |
| **Headquarters** | Seattle, Washington, USA |
| **Founded** | Released in 2018 (officially commercialized in 2019) |
| **Official Website** | [https://aws.amazon.com/robomaker](https://aws.amazon.com/robomaker) |
| **Supply Chain Role** | Cloud robotics platform, robot simulation, fleet management |
| **Enterprise Attribute** | Public cloud department service |
| **Parent Company/Group** | Amazon Web Services (AWS) / Amazon.com Inc. |
| **Data Source** | AWS official website, AWS RoboMaker product page, AWS blog and announcements |

## Company Overview

AWS RoboMaker is a cloud robotics development platform launched by Amazon Web Services, designed to provide robot developers with cloud-based simulation, machine learning, fleet management, and continuous integration/continuous deployment (CI/CD) capabilities.

The platform natively integrates Robot Operating System (ROS/ROS2). Developers can run Gazebo simulations at scale in the cloud, train models using Amazon SageMaker, and deploy models to edge robots via AWS IoT Greengrass. RoboMaker also offers sample applications and world files (such as Small Warehouse World) to accelerate prototyping of AMRs, warehouse robots, and outdoor mobile robots.

Starting in 2024, AWS has gradually migrated some of RoboMaker's managed capabilities to the open-source ROS ecosystem and a broader set of AWS services (such as IoT, SageMaker, SimSpace Weaver), recommending that new customers build their own cloud robotics solutions based on open-source toolchains and AWS services.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Cloud Robotics Development Platform | Cloud-based ROS/ROS2 development and simulation | AWS RoboMaker | AMR, warehousing, service robots |
| Simulation and Digital Twin | Large-scale parallel physics simulation | RoboMaker Simulation | Algorithm validation, scenario regression testing |
| Fleet and Edge Management | Robot OTA, monitoring, task scheduling | AWS IoT Greengrass + RoboMaker Fleet Management | Field deployment, remote operations |
| Machine Learning Services | Cloud model training and edge inference | Amazon SageMaker + RoboMaker ML | Perception, navigation, manipulation |

## Representative Products

### AWS RoboMaker Cloud Robotics Platform

> AWS RoboMaker: Please visit the [official page](https://aws.amazon.com/robomaker) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Deployment Form | Public cloud SaaS / PaaS | AWS official website |
| Supported Middleware | ROS 1 / ROS 2 | AWS RoboMaker documentation |
| Simulation Engine | Gazebo / Ignition | AWS public information |
| Maximum Concurrent Simulations | On-demand scaling (AWS compute resources) | AWS official website |
| Edge Deployment | AWS IoT Greengrass | AWS documentation |
| ML Training Integration | Amazon SageMaker | AWS public information |
| Data Storage | Amazon S3, Amazon CloudWatch | AWS documentation |
| Pricing | Billed by simulation hours, storage, and data transfer | AWS pricing page |

**Technical Highlights**: Cloud-based ROS development environment, large-scale parallel simulation, model training integrated with SageMaker, Greengrass edge deployment, sample warehouse world and navigation stack.

**Application Scenarios**: AMR navigation algorithm validation, warehouse robot digital twin, remote monitoring of service robots, OTA updates for robot models.

### AWS IoT Greengrass (Robot Edge Deployment)

> AWS IoT Greengrass: Please visit the [official page](https://aws.amazon.com/robomaker) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Deployment Form | Edge runtime + cloud management | AWS official website |
| Supported Protocols | MQTT, HTTP, local Lambda | AWS documentation |
| Security Mechanisms | Device certificates, IAM, TLS encryption | AWS public information |
| Offline Operation | Supports local computation and message queuing | AWS documentation |
| Supported Hardware | ARM / x86 edge gateways, NVIDIA Jetson, etc. | AWS public information |
| Container Support | Docker compatible | AWS documentation |
| Pricing | Billed by device connections and messages | AWS pricing page |

**Technical Highlights**: Edge-cloud collaboration, local Lambda computation, secure OTA, device shadow and state synchronization, integration with RoboMaker fleet management.

**Application Scenarios**: On-site robot task execution, local decision-making in offline/weak network environments, factory line edge inference, fleet-level configuration distribution.

## Supply Chain Position

- **Upstream Key Components/Materials**: AWS self-developed cloud infrastructure, NVIDIA/Intel edge computing modules, ROS/ROS2 open-source ecosystem, Gazebo simulation engine.
- **Downstream Customers/Application Scenarios**: Warehouse logistics AMRs, service robot manufacturers, autonomous driving R&D, educational and research institutions.
- **Main Competitors/Comparables**: Google Cloud Robotics, Microsoft Azure IoT + ROS, Formant, InOrbit, Freedom Robotics.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_aws_robomaker`
- Product/Platform Entities: `ent_product_aws_robomaker_cloud`, `ent_product_aws_iot_greengrass`
- Key Relationships:
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_robomaker_cloud` (`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_robomaker_cloud`)
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_iot_greengrass` (`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_iot_greengrass`)

## References

1. [AWS RoboMaker Official Website](https://aws.amazon.com/robomaker)
2. [AWS RoboMaker Documentation](https://docs.aws.amazon.com/robomaker/)
3. [AWS IoT Greengrass Product Page](https://aws.amazon.com/greengrass/)
4. [AWS Blog – RoboMaker Migration Announcement](https://aws.amazon.com/blogs/robotics/)
