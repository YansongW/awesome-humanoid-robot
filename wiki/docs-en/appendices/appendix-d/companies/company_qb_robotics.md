# qb Soft Robotics

> This entry belongs to [Appendix D Enterprise/Product Wiki](../../appendix-d.md).
> Data update time: 2026-07-01. All parameters are based on official public information; missing items are marked as "Not disclosed".

---

## Company Information Card

| Item | Content |
|------|---------|
| **Chinese Name** | qb Soft Robotics |
| **English Name** | qb Soft Robotics |
| **Headquarters** | Pisa, Italy |
| **Founded** | 2011 |
| **Website** | [https://qbrobotics.com](https://qbrobotics.com) |
| **Supply Chain Role** | Soft Dexterous Hand / Soft Robotics / Five-Finger Gripper |
| **Enterprise Attribute** | Pioneer in Soft Robotics Technology |
| **Parent Company/Group** | qbrobotics Srl |
| **Data Source** | Official website, product manuals, public reports, WAIC 2026 reports |

## Company Profile

Developer of humanoid dexterous hands based on soft robotics technology.

qb Soft Robotics (qbrobotics), originating from Pisa, Italy, focuses on soft robotics and bionic five-finger dexterous hands. The qb SoftHand series utilizes single-motor tendon drive combined with soft joint collaboration to achieve human-like grasping and high environmental adaptability. It features self-resetting, high load-to-weight ratio, and plug-and-play capabilities, and is widely used in scientific research, education, collaborative robotics, and human-robot interaction.

## Product Lines

| Product Line | Positioning | Representative Product | Application Areas |
|--------------|-------------|------------------------|-------------------|
| qb SoftHand Research | Research-grade five-finger soft hand | qb SoftHand | Scientific research, education |
| qb SoftHand2 Research | Enhanced dual-coordination | SoftHand2 | Research, industrial testing |
| qb SoftHand Industry | Industrial grade | SoftHand Industry | Collaborative robots, human-robot interaction |

## Representative Products

### qb SoftHand Five-Finger Soft Robotic Hand

> qb SoftHand Five-Finger Soft Robotic Hand: Please visit [official materials](https://qbrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | 1:1 human hand replica, specifics not disclosed | Public information |
| Weight | 500 g | Public information |
| Number of Fingers | 5 | Public information |
| Degrees of Freedom | 19 joints / 1 active coordination (single motor) | Public information |
| Fingertip Pinch Force | 62 N | Public information |
| Rated Load | 1.7 kg (pinch state) | Public information |
| Open Hand to Fist | 1.1 s | Public information |
| Communication Interface | USB / RS485 | Public information |
| Compatibility | ROS, UR+ certified | Public information |
| Price | Not disclosed | - |

**Technical Highlights**: Soft materials with tendon drive coordination, self-resetting joints, single-motor plug-and-play, high load-to-weight ratio, safe human-robot interaction.

**Application Scenarios**: Research grasping, educational demonstrations, collaborative robot end-effectors, medical rehabilitation, human-robot interaction.

### qb SoftHand2 Research

> qb SoftHand2 Research: Please visit [official materials](https://qbrobotics.com) for details.

| Specification | Value | Notes/Source |
|---------------|-------|--------------|
| Dimensions | Not disclosed | - |
| Weight | 0.94 kg | Public information |
| Degrees of Freedom | 19 joints / dual motors / dual coordination | Public information |
| Rated Load | 2 kg (pinch) / 3 kg (grasp) | Public information |
| Open Hand to Fist | Approx. 1 s | Public information |
| Communication Interface | USB / RS485 | Public information |
| Compatibility | ROS / ROS2 | Public information |
| Price | Not disclosed | - |

**Technical Highlights**: The second coordinated motion enhances in-hand manipulation capabilities, allowing object posture adjustment without rotating the wrist.

**Application Scenarios**: Advanced grasping research, industrial testing, human-robot collaboration, complex object manipulation.

## Supply Chain Position

- **Upstream Key Components/Materials**: Elastomer materials, tendons/soft actuators, motors, sensors, 3D-printed structural parts
- **Downstream Customers/Application Scenarios**: Universities, research institutions, collaborative robot manufacturers, medical rehabilitation, industrial testing
- **Main Competitors/Peers**: Shadow Robot, Pisa/IIT SoftHand, Robotiq, Agile Robots

## Knowledge Graph Nodes and Relationships

- Company Entity: `ent_company_qb_robotics`
- Product/Component Entity: `ent_product_qb_hand`
- Key Relationship:
  - `ent_company_qb_robotics` -- `manufactures` --> `ent_product_qb_hand`

## References

1. [Official Website](https://qbrobotics.com)
2. [WAIC 2026 Exhibition Report](https://www.worldrobotconference.com)
3. [Public Product Manuals and Research Reports](https://qbrobotics.com) (Please verify against actual product models)
