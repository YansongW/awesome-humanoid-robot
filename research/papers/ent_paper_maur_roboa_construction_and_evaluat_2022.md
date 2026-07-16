---
$id: ent_paper_maur_roboa_construction_and_evaluat_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoBoa: Construction and Evaluation of a Steerable Vine Robot for Search and Rescue Applications'
  zh: RoBoa：面向搜索救援应用的可转向藤蔓机器人的构建与评估
  ko: 'RoBoa: 탐색 및 구조 응용을 위한 조향 가능한 덩굴 로봇의 구축 및 평가'
summary:
  en: RoBoa is a 17-meter steerable vine robot for search and rescue that everts a soft fabric tube for locomotion and uses
    internal 3D-printed pneumatic actuators at the tip for steering, validated in a collapsed-building test site.
  zh: RoBoa is a vine-like search and rescue robot that can explore narrow and cluttered environments such as destroyed buildings.
    The robot assists rescue teams in finding and communicating with trapped people. It employs the principle of vine robots
    for locomotion, everting the tip of its tube to move forward. Inside the tube, pneumatic actuators enable lateral movement.
    The head carries sensors and is mounted outside at the tip of the tube. At the back, a supply box contains the rolled
    up tube and provides pressurized air, power, computation, as well as an interface for the user to interact with
  ko: RoBoa는 17m 길이의 조향 가능한 덩굴 탐색 및 구조 로봇으로, 부드러운 직물 튜브를 에버팅하여 이동하고 끝단 내부의 3D 프린팅 공압 액추에이터를 이용해 조향하며, 붕괴된 건물 시험 현장에서 검증되었다.
domains:
- 02_components
- 03_manufacturing_processes
- 05_mass_production
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- vine_robot
- soft_robot
- pneumatic_actuator
- search_and_rescue
- continuum_robot
- soft_actuator
- disaster_response
- eversion_locomotion
- tip_steering
- decentralized_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.15145v1.
sources:
- id: src_001
  type: paper
  title: 'RoBoa: Construction and Evaluation of a Steerable Vine Robot for Search and Rescue Applications'
  url: https://arxiv.org/abs/2203.15145
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## 概述
RoBoa is a vine-like search and rescue robot that can explore narrow and cluttered environments such as destroyed buildings. The robot assists rescue teams in finding and communicating with trapped people. It employs the principle of vine robots for locomotion, everting the tip of its tube to move forward. Inside the tube, pneumatic actuators enable lateral movement. The head carries sensors and is mounted outside at the tip of the tube. At the back, a supply box contains the rolled up tube and provides pressurized air, power, computation, as well as an interface for the user to interact with the system. A decentralized control scheme was implemented that reduces the required number of cables and takes care of the low-level control of the pneumatic actuators. The design, characterization, and experimental evaluation of the system and its crucial components is shown. The complete prototype is fully functional and was evaluated in a realistic environment of a collapsed building where the remote-controlled robot was able to repeatedly locate a trapped person after a travel distance of about 10 m.

## 核心内容
RoBoa is a vine-like search and rescue robot that can explore narrow and cluttered environments such as destroyed buildings. The robot assists rescue teams in finding and communicating with trapped people. It employs the principle of vine robots for locomotion, everting the tip of its tube to move forward. Inside the tube, pneumatic actuators enable lateral movement. The head carries sensors and is mounted outside at the tip of the tube. At the back, a supply box contains the rolled up tube and provides pressurized air, power, computation, as well as an interface for the user to interact with the system. A decentralized control scheme was implemented that reduces the required number of cables and takes care of the low-level control of the pneumatic actuators. The design, characterization, and experimental evaluation of the system and its crucial components is shown. The complete prototype is fully functional and was evaluated in a realistic environment of a collapsed building where the remote-controlled robot was able to repeatedly locate a trapped person after a travel distance of about 10 m.

## 参考
- http://arxiv.org/abs/2203.15145v1


