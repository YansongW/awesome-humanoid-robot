---
$id: ent_paper_pomerleau_robotics_in_snow_and_ice_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robotics in Snow and Ice
  zh: 冰雪机器人学
  ko: 눈과 얼음 속의 로봇공학
summary:
  en: A survey chapter that defines robotics in snow and ice, taxonomizes cryosphere
    sub-domains, and synthesizes lessons from historical field deployments of ground,
    aerial, and underwater robots in cold environments.
  zh: 本章定义了冰雪机器人学，对冰冻圈子领域进行分类，并综合了地面、空中和水下机器人在寒冷环境中历史野外部署的经验教训。
  ko: 이 장은 눈과 얼음 속의 로봇공학을 정의하고, 저온권 하위 영역을 분류하며, 지상·공중·수중 로봇의 역사적 현장 배포에서 얻은 교훈을 종합한다.
domains:
- 06_design_engineering
- 02_components
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- cryospheric_robotics
- cold_environment_robotics
- polar_robotics
- winter_navigation
- outdoor_humanoid_operations
- environmental_robustness
- energy_management
- perception_in_snow
verification:
  status: partially_verified
  reviewed_by: ai_autonomous
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the arXiv full text (ar5iv HTML); requires human review
    before verification.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: Robotics in Snow and Ice
  url: https://arxiv.org/abs/2208.05095
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- system
---

## Overview

The chapter defines robotics in snow and ice as the study and deployment of robotic systems in environments where water exists in solid form. It organizes the discussion around cryosphere sub-domains—snow cover, freshwater ice, frozen ground, sea ice, glaciers, ice caps, and ice sheets on the ground; freezing rain, hail, pellets, and snow in the air—rather than around latitude or elevation. Each sub-domain imposes a distinct combination of extreme cold, precipitation, and terrain that affects robot visibility, maneuverability, and endurance. The text reviews how subzero temperatures stress platforms, degrade batteries and seals, and induce material failures; how precipitation degrades stereo vision and lidar, occludes millimetre-wave radar, and creates slippery surfaces; and how whiteouts erase visual features and make ground and sky indistinguishable. It then surveys pioneering deployments such as Dante, Dante II, Nomad, the Tumbleweed Polar Rover, Cool Robot, Yeti, and ROC6, describing their scientific goals, distances traveled, and the operational lessons learned. Application areas span volcanology, mineralogy, atmospheric science, seismology, glaciology, ice-road and crevasse inspection, snow removal, forestry, and space-exploration analogs. The chapter closes by identifying open research directions, including winter autonomous driving datasets, navigation in whiteout conditions, long-range communication, energy harvesting, and mobility on variable snow and ice surfaces.

## Key Contributions

- Taxonomy of cryosphere sub-domains and their specific robotics challenges
- Review of pioneering deployments such as Dante, Nomad, Yeti, ROC6, and Tumbleweed
- Analysis of perception and locomotion difficulties in snow, ice, and whiteout conditions
- Identification of application areas in Earth science, transportation, forestry, and space analogs
- Outline of future research directions for autonomous winter navigation and polar robotics

## Relevance to Humanoid Robotics

Although the chapter focuses on ground, aerial, and underwater robots, its findings are directly transferable to humanoids intended for outdoor winter or cold industrial sites. Subzero operation requires thermal management of actuators and batteries, robust seals, and materials that tolerate thermal stress; humanoids must solve the same problems while maintaining balance on slippery and deformable terrain. The perception challenges—textureless snow, washed-out features, dynamic topology, and whiteouts—apply equally to bipedal systems, and energy-management trade-offs between batteries, solar panels, and gas engines are relevant for mobile humanoids with limited payload. Locomotion lessons from tracked and wheeled polar rovers, including sinkage, traction loss, and turning in deep snow, inform foot-and-ankle design, gait planning, and fall recovery for humanoids. Likewise, the emphasis on remote deployment logistics, minimal repair infrastructure, and long-range communication is pertinent to humanoid robots sent to remote facilities or planetary-analog missions. The chapter therefore provides a systems-level foundation for cold-environment humanoid requirements.
