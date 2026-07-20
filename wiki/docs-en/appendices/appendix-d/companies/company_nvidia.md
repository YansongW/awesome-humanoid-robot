# NVIDIA Corporation

> This entry belongs to [Appendix D: Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | NVIDIA (英伟达) |
| **English Name** | NVIDIA Corporation |
| **Headquarters** | Santa Clara, California, USA |
| **Founded** | 1993 |
| **Website** | [https://www.nvidia.com](https://www.nvidia.com) |
| **Supply Chain Role** | AI computing platform, robotics software/simulation, chip supplier |
| **Enterprise Type** | Public company (NASDAQ: NVDA) |
| **Parent Company/Group** | None (NVIDIA Corporation is the listed entity) |
| **Data Source** | NVIDIA official website, Jetson/Isaac official documentation, public press releases |

## Company Overview

NVIDIA provides Jetson edge computing, Isaac Sim simulation, Isaac Lab training, and the GR00T humanoid foundation model for robotics and humanoid robots, serving as a core enabler of physical AI.

Jetson Thor is designed specifically for physical AI and humanoid robots, integrating a Blackwell GPU with large-capacity unified memory; Isaac Sim offers high-fidelity simulation and synthetic data; GR00T provides a VLA foundation model. Several leading humanoid robot companies adopt the NVIDIA platform.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| Jetson | Edge AI computing modules | Jetson Thor / AGX Orin, etc. | Robot/humanoid brain, perception, inference |
| Isaac Sim / Isaac Lab | Simulation and training platform | Isaac Sim / Isaac Lab | Sim2Real, digital twins, reinforcement learning |
| Isaac GR00T | Humanoid robot foundation model | GR00T N1.5, etc. | VLA, natural language task execution |

## Representative Products

### NVIDIA Jetson Thor (T5000)

> NVIDIA Jetson Thor (T5000): Please visit [official documentation](https://www.nvidia.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| AI Compute | Up to 2070 FP4 TFLOPS | NVIDIA Official |
| GPU Architecture | NVIDIA Blackwell | NVIDIA Official |
| CPU | 14-core Arm Neoverse-V3AE | NVIDIA Official |
| Memory | 128 GB LPDDR5X (273 GB/s) | NVIDIA Official |
| Networking | 4×25 GbE | NVIDIA Official |
| Power Consumption | 40–130 W configurable | NVIDIA Official |
| Dimensions | 100 mm × 87 mm (module) | NVIDIA Official |
| Price | Developer kit 3,499 USD; module 2,999 USD (1k qty) | NVIDIA Public Pricing |

**Technical Highlights**: Blackwell GPU, large-capacity unified memory, support for multimodal generative AI and VLA models, 4×25GbE high-bandwidth sensor interface, designed for humanoid robots.

**Application Scenarios**: Humanoid robot main controller, autonomous driving, medical robotics, industrial AMR.

### NVIDIA Isaac Sim

> NVIDIA Isaac Sim: Please visit [official documentation](https://www.nvidia.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Underlying Platform | NVIDIA Omniverse / PhysX | NVIDIA Official |
| Rendering | RTX real-time ray tracing | NVIDIA Official |
| Physics Engine | PhysX | NVIDIA Official |
| ROS Integration | ROS 2 bridge and Isaac ROS | NVIDIA Official |
| Training Framework | Isaac Lab (reinforcement learning/imitation learning) | NVIDIA Official |
| Digital Twins | Supports USD scenes and sensor models | NVIDIA Official |
| Deployment Method | Local, container, cloud | NVIDIA Official |
| Price | Free (requires NVIDIA account/Omniverse) | Official Statement |

**Technical Highlights**: Photorealistic simulation, PhysX physics, Sim2Real pipeline integrated with Jetson/GR00T, large-scale synthetic data generation.

**Application Scenarios**: Humanoid robot training, digital twin factories, sensor validation, reinforcement learning research.

## Supply Chain Position

- **Upstream Key Components/Materials**: TSMC foundry, memory, sensor and camera partners, Omniverse ecosystem.
- **Downstream Customers/Application Scenarios**: OEMs and developers such as Tesla, Figure AI, Boston Dynamics, Agility Robotics, Apptronik, 1X Technologies.
- **Main Competitors/Comparables**: Qualcomm RB, Intel Movidius/AMD, simulation platforms Gazebo/Unity/Unreal.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_nvidia`
- Product/Platform Entities: `ent_software_platform_nvidia_jetson_thor`, `ent_software_platform_nvidia_isaac_sim`
- Key Relationships:
  - `rel_ent_company_nvidia_develops_ent_software_platform_nvidia_jetson_thor` (`ent_company_nvidia` → `develops` → `ent_software_platform_nvidia_jetson_thor`)
  - `rel_ent_company_nvidia_develops_ent_software_platform_nvidia_isaac_sim` (`ent_company_nvidia` → `develops` → `ent_software_platform_nvidia_isaac_sim`)

## References

1. [NVIDIA Official Website](https://www.nvidia.com)
2. [NVIDIA Jetson Thor Product Page](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-thor/)
3. [NVIDIA Isaac Sim Official Page](https://developer.nvidia.com/isaac/sim)
