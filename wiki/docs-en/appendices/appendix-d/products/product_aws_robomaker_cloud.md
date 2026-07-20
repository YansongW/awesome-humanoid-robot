# AWS RoboMaker Cloud Robotics Platform

> This entry belongs to [Appendix D Key Products Wiki](../../appendix-d.md).
> Return to: [Appendix D.4 Key Products Wiki Directory](../index-products.md)
> Data update time: 2026-07-01. All parameters are subject to official public information; missing items are marked as "Not disclosed."

---

## Product Information Card

| Item | Content |
|------|---------|
| **Manufacturer** | [AWS RoboMaker](../companies/company_aws_robomaker.md) |
| **Product Category** | Cloud Robotics Development / Simulation / Fleet Management Platform |
| **Release Date** | Announced in 2018, commercially available in 2019 |
| **Status** | Gradually migrating to open source and AWS service combination |
| **Official Website/Source** | [AWS RoboMaker Official Website](https://aws.amazon.com/robomaker) |

## Product Overview

AWS RoboMaker is an end-to-end cloud robotics platform launched by Amazon Web Services, enabling developers to develop, simulate, test, and deploy robotic applications in the cloud. The platform natively integrates ROS/ROS2 and deeply connects with AWS services such as AWS IoT Greengrass, Amazon SageMaker, Amazon S3, and Amazon CloudWatch.

The core value of RoboMaker lies in migrating traditional local robotics development environments to a scalable cloud: developers can run thousands of scenario regression tests in parallel simulations, train perception and navigation models through SageMaker, and then securely push models to edge robots via Greengrass. The platform also provides example scenarios like Small Warehouse World, facilitating rapid prototyping and validation for AMRs and warehouse robots.

Starting in 2024, AWS recommends that new users build cloud robotics solutions based on the open-source ROS toolchain combined with AWS services. Some managed capabilities of RoboMaker have been migrated or open-sourced.

## Product Image

> AWS RoboMaker Cloud: Please visit the [official website](https://aws.amazon.com/robomaker) for details.

## Specification Parameter Table

| Specification Item | Value | Remarks/Source |
|-------------------|-------|----------------|
| Deployment Form | Public Cloud SaaS / PaaS | AWS Official Website |
| Supported Middleware | ROS 1 / ROS 2 | AWS Documentation |
| Simulation Engine | Gazebo / Ignition | AWS Public Information |
| Concurrent Simulation | On-demand scaling (EC2/SimSpace Weaver) | AWS Documentation |
| Edge Deployment | AWS IoT Greengrass | AWS Documentation |
| ML Training | Amazon SageMaker | AWS Public Information |
| Data Storage | Amazon S3, CloudWatch Logs | AWS Documentation |
| Network | VPC, IAM, TLS Encryption | AWS Documentation |
| Pricing | Billed by simulation hours, storage, and traffic | AWS Pricing Page |

## Supply Chain Position

- **Manufacturer**: [AWS RoboMaker](../companies/company_aws_robomaker.md)
- **Core Components/Technology Sources**: AWS Cloud Infrastructure, NVIDIA/Intel Edge Computing Platforms, ROS/ROS2 Open Source Ecosystem, Gazebo Simulation Engine, SageMaker ML Framework.
- **Downstream Applications/Customers**: AMR Manufacturers, Warehouse Logistics Robots, Service Robots, Autonomous Driving R&D, Universities and Research Institutions.

## Knowledge Graph Nodes and Relationships

- Product Entity: `ent_product_aws_robomaker_cloud`
- Manufacturer Entity: `ent_company_aws_robomaker`
- Key Relationships:
  - `rel_ent_company_aws_robomaker_manufactures_ent_product_aws_robomaker_cloud` (`ent_company_aws_robomaker` → `manufactures` → `ent_product_aws_robomaker_cloud`)

## Application Scenarios

- **AMR Navigation Algorithm Validation**: Test SLAM, path planning, and obstacle avoidance in simulation environments like Small Warehouse World.
- **Digital Twin and Scenario Regression**: Run thousands of simulations in parallel to verify the impact of software updates on robot behavior.
- **Cloud Model Training**: Use SageMaker to train object detection, semantic segmentation, or reinforcement learning policy models.
- **Edge OTA Deployment**: Securely deploy updated models and software to physical robots via Greengrass.

## Competitive Comparison

| Comparison Item | AWS RoboMaker | Google Cloud Robotics | Microsoft Azure IoT + ROS |
|----------------|---------------|----------------------|---------------------------|
| Positioning | End-to-end cloud robotics platform | Kubernetes-native cloud robotics framework | Enterprise IoT and ROS integration |
| Simulation | Gazebo managed simulation | Proprietary/third-party simulation integration | Third-party simulation integration |
| Middleware | ROS/ROS2 | ROS/ROS2 | ROS/ROS2 |
| Edge | AWS IoT Greengrass | Cloud Robotics Core | Azure IoT Edge |
| Business Model | Pay-per-use | Open source + cloud resource billing | Billed by cloud resources |

## Selection and Deployment Recommendations

- New users should evaluate whether to directly use open-source ROS + AWS service combination to reduce reliance on a single managed service.
- For large-scale simulation needs, consider combining SimSpace Weaver or self-managed EC2 clusters to optimize costs.
- Before deployment, plan VPC, IAM permissions, Greengrass device certificates, and OTA pipelines.

## References

1. [AWS RoboMaker Official Website](https://aws.amazon.com/robomaker)
2. [AWS RoboMaker Developer Guide](https://docs.aws.amazon.com/robomaker/)
3. [AWS IoT Greengrass Product Page](https://aws.amazon.com/greengrass/)
4. [AWS Robotics Blog](https://aws.amazon.com/blogs/robotics/)
