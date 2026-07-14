---
$id: ent_paper_berkeley_humanoid_lite_an_open_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot'
  zh: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot'
  ko: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot'
summary:
  en: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot is a 2025 work on hardware
    design for humanoid robots.'
  zh: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot is a 2025 work on hardware
    design for humanoid robots.'
  ko: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot is a 2025 work on hardware
    design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- berkeley_humanoid_lite
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.17249v1.
sources:
- id: src_001
  type: paper
  title: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot (arXiv)'
  url: https://arxiv.org/abs/2504.17249
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Berkeley Humanoid Lite: An Open-source, Accessible, and Customizable 3D-printed Humanoid Robot project page'
  url: https://lite.berkeley-humanoid.org/
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Despite significant interest and advancements in humanoid robotics, most existing commercially available hardware remains high-cost, closed-source, and non-transparent within the robotics community. This lack of accessibility and customization hinders the growth of the field and the broader development of humanoid technologies. To address these challenges and promote democratization in humanoid robotics, we demonstrate Berkeley Humanoid Lite, an open-source humanoid robot designed to be accessible, customizable, and beneficial for the entire community. The core of this design is a modular 3D-printed gearbox for the actuators and robot body. All components can be sourced from widely available e-commerce platforms and fabricated using standard desktop 3D printers, keeping the total hardware cost under $5,000 (based on U.S. market prices). The design emphasizes modularity and ease of fabrication. To address the inherent limitations of 3D-printed gearboxes, such as reduced strength and durability compared to metal alternatives, we adopted a cycloidal gear design, which provides an optimal form factor in this context. Extensive testing was conducted on the 3D-printed actuators to validate their durability and alleviate concerns about the reliability of plastic components. To demonstrate the capabilities of Berkeley Humanoid Lite, we conducted a series of experiments, including the development of a locomotion controller using reinforcement learning. These experiments successfully showcased zero-shot policy transfer from simulation to hardware, highlighting the platform's suitability for research validation. By fully open-sourcing the hardware design, embedded code, and training and deployment frameworks, we aim for Berkeley Humanoid Lite to serve as a pivotal step toward democratizing the development of humanoid robotics. All resources are available at https://lite.berkeley-humanoid.org.

## 核心内容
Despite significant interest and advancements in humanoid robotics, most existing commercially available hardware remains high-cost, closed-source, and non-transparent within the robotics community. This lack of accessibility and customization hinders the growth of the field and the broader development of humanoid technologies. To address these challenges and promote democratization in humanoid robotics, we demonstrate Berkeley Humanoid Lite, an open-source humanoid robot designed to be accessible, customizable, and beneficial for the entire community. The core of this design is a modular 3D-printed gearbox for the actuators and robot body. All components can be sourced from widely available e-commerce platforms and fabricated using standard desktop 3D printers, keeping the total hardware cost under $5,000 (based on U.S. market prices). The design emphasizes modularity and ease of fabrication. To address the inherent limitations of 3D-printed gearboxes, such as reduced strength and durability compared to metal alternatives, we adopted a cycloidal gear design, which provides an optimal form factor in this context. Extensive testing was conducted on the 3D-printed actuators to validate their durability and alleviate concerns about the reliability of plastic components. To demonstrate the capabilities of Berkeley Humanoid Lite, we conducted a series of experiments, including the development of a locomotion controller using reinforcement learning. These experiments successfully showcased zero-shot policy transfer from simulation to hardware, highlighting the platform's suitability for research validation. By fully open-sourcing the hardware design, embedded code, and training and deployment frameworks, we aim for Berkeley Humanoid Lite to serve as a pivotal step toward democratizing the development of humanoid robotics. All resources are available at https://lite.berkeley-humanoid.org.

## 参考
- http://arxiv.org/abs/2504.17249v1

