# Open Robotics / Open Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed."

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | Open Robotics |
| **English Name** | Open Robotics |
| **Headquarters** | Mountain View, California, USA |
| **Founded** | 2012 |
| **Website** | [https://www.openrobotics.org](https://www.openrobotics.org) |
| **Supply Chain Role** | Open-source robot software platform, middleware, simulation |
| **Enterprise Attribute** | Non-profit foundation (OSRF) + Intrinsic acquisition of commercial subsidiary |
| **Parent Company/Group** | Open Source Robotics Foundation (OSRF) |
| **Data Source** | Open Robotics official website, ROS and Gazebo official documentation |

## Company Profile

Open Robotics maintains ROS, ROS 2, the Gazebo simulator, and Open-RMF, serving as the de facto standard for global robot software.

ROS/ROS 2 provides robot middleware, algorithm libraries, and toolchains; Gazebo offers high-fidelity 3D physics simulation; Open-RMF coordinates multi-robot fleets. Most humanoid robot projects rely on these open-source platforms.

## Product Lines

| Product Line | Positioning | Representative Products | Application Areas |
|--------------|-------------|------------------------|-------------------|
| ROS 2 | Second generation robot operating system | ROS 2 Jazzy, etc. | Middleware, navigation, control, perception |
| Gazebo | 3D physics simulator | Gazebo Harmonic/Ionic | Robot simulation, Sim2Real, sensor validation |
| Open-RMF | Robot middleware framework | Open-RMF | Multi-robot scheduling and coordination |

## Representative Products

### ROS 2

> ROS 2: Please visit [official resources](https://www.openrobotics.org) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Version | Jazzy Jalisco (LTS, 2024), etc. | ROS official documentation |
| License | Apache 2.0 / BSD | Official repository |
| Communication Middleware | DDS (default eProsima Fast DDS) | Official documentation |
| Supported Languages | C++ / Python | Official documentation |
| Supported Platforms | Linux, RTOS, Embedded | Official documentation |
| Real-time Capability | Supports real-time control (depends on platform and RMW) | Official documentation |
| Core Ecosystem | Nav2, MoveIt 2, ros2_control, rviz2 | Official documentation |
| Price | Free and open-source | - |

**Technical Highlights**: Decentralized architecture, DDS communication, cross-platform support, vast algorithm and tool ecosystem, adopted by the majority of humanoid robots.

**Application Scenarios**: Robot software development, navigation, manipulation, simulation to real-world deployment.

### Gazebo

> Gazebo: Please visit [official resources](https://www.openrobotics.org) for details.

| Specification | Value | Remarks/Source |
|---------------|-------|----------------|
| Version | Harmonic / Ionic, etc. | Gazebo official |
| License | Apache 2.0 | Official repository |
| Physics Engines | ODE, Bullet, DART, Simbody | Official documentation |
| Rendering | OGRE | Official documentation |
| Model Formats | SDF, URDF | Official documentation |
| ROS Integration | ros_gz_bridge and native plugins | Official documentation |
| Sensor Simulation | Camera, LiDAR, IMU, depth camera, GPS, etc. | Official documentation |
| Price | Free and open-source | - |

**Technical Highlights**: Multi-physics engine support, high-quality sensor simulation, deep integration with ROS/ROS 2, widely used in Sim2Real research.

**Application Scenarios**: Robot algorithm validation, digital twins, reinforcement learning training, sensor model testing.

## Supply Chain Position

- **Upstream Key Components/Materials**: DDS implementations, physics engines, graphics rendering, operating systems and compilation toolchains.
- **Downstream Customers/Application Scenarios**: Almost all humanoid robot OEMs, research institutions, autonomous driving and logistics robot companies.
- **Main Competitors/Comparables**: NVIDIA Isaac Sim, Unity, Unreal Engine, CoppeliaSim, Webots.

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_open_robotics`
- Product/Platform Entities: `ent_software_platform_open_robotics_ros2`, `ent_software_platform_open_robotics_gazebo`
- Key Relationships:
  - `rel_ent_company_open_robotics_develops_ent_software_platform_open_robotics_ros2` (`ent_company_open_robotics` → `develops` → `ent_software_platform_open_robotics_ros2`)
  - `rel_ent_company_open_robotics_develops_ent_software_platform_open_robotics_gazebo` (`ent_company_open_robotics` → `develops` → `ent_software_platform_open_robotics_gazebo`)

## References

1. [Open Robotics Official Website](https://www.openrobotics.org)
2. [ROS 2 Official Documentation](https://docs.ros.org/en/rolling/)
3. [Gazebo Official Documentation](https://gazebosim.org/home)
