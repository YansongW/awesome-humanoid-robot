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
  zh: RoBoa 是一款长达 17 米的可转向藤蔓机器人，专为搜救任务设计。它通过外翻软织物管实现运动，并利用尖端内部的 3D 打印气动执行器进行转向，其有效性已在倒塌建筑测试场地中得到验证。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2203.15145v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
RoBoa 是一种类似藤蔓的搜救机器人，能够探索狭窄且杂乱的废墟环境，协助救援队定位并与被困人员沟通。它采用藤蔓机器人的运动原理，通过外翻管尖向前推进，内部的气动执行器则负责实现横向移动。机器人头部搭载传感器并安装在管尖外部，后方的供应箱内装有卷起的软管，并提供压缩空气、电力、计算能力以及用户交互界面。该系统采用去中心化控制方案，减少了所需线缆数量，并负责气动执行器的底层控制。

## 核心内容
### 系统设计与架构
- **运动机制**：RoBoa 利用藤蔓机器人的外翻原理，通过从内部向外翻出软织物管的前端来向前移动，从而在废墟中穿行。
- **转向与传感**：机器人尖端内部集成了 3D 打印的气动执行器，用于实现横向转向；头部外部则安装有传感器，用于环境感知。
- **后端支持**：后方的供应箱包含卷起的软管，并提供压缩空气、电力、计算资源，以及供操作员远程控制的用户界面。
- **控制方案**：采用去中心化控制架构，有效减少了所需线缆数量，并专门负责气动执行器的底层控制。

### 实验评估与关键数据
- **实验环境**：在真实的倒塌建筑测试场地中对完整原型进行了评估。
- **性能表现**：远程控制的 RoBoa 能够成功重复定位被困人员，在约 10 米的行进距离后完成目标。
- **系统验证**：实验展示了系统的完整功能，并验证了其关键组件（包括软管、气动执行器和控制方案）的设计与特性。

## Overview
RoBoa is a vine-like search and rescue robot that can explore narrow and cluttered environments such as destroyed buildings. The robot assists rescue teams in finding and communicating with trapped people. It employs the principle of vine robots for locomotion, everting the tip of its tube to move forward. Inside the tube, pneumatic actuators enable lateral movement. The head carries sensors and is mounted outside at the tip of the tube. At the back, a supply box contains the rolled up tube and provides pressurized air, power, computation, as well as an interface for the user to interact with the system. A decentralized control scheme was implemented that reduces the required number of cables and takes care of the low-level control of the pneumatic actuators. The design, characterization, and experimental evaluation of the system and its crucial components is shown. The complete prototype is fully functional and was evaluated in a realistic environment of a collapsed building where the remote-controlled robot was able to repeatedly locate a trapped person after a travel distance of about 10 m.

## 개요
RoBoa는 덩굴 형태의 수색 및 구조 로봇으로, 붕괴된 건물과 같은 좁고 복잡한 환경을 탐사할 수 있습니다. 이 로봇은 구조대가 매몰자를 찾고 의사소통하는 것을 돕습니다. 이동을 위해 덩굴 로봇의 원리를 사용하며, 튜브 끝을 뒤집어 앞으로 나아갑니다. 튜브 내부에는 공압 액추에이터가 있어 측면 이동을 가능하게 합니다. 헤드에는 센서가 장착되어 있으며 튜브 끝 외부에 설치됩니다. 후방에는 공급 상자가 있어 말린 튜브를 보관하고 압축 공기, 전력, 연산 능력, 그리고 사용자가 시스템과 상호작용할 수 있는 인터페이스를 제공합니다. 케이블 수를 줄이고 공압 액추에이터의 저수준 제어를 담당하는 분산 제어 방식이 구현되었습니다. 시스템과 핵심 구성 요소의 설계, 특성 분석 및 실험적 평가가 제시됩니다. 완전한 프로토타입은 완전히 작동 가능하며, 약 10m 이동 후 원격 제어 로봇이 반복적으로 매몰자를 찾을 수 있었던 붕괴 건물의 실제 환경에서 평가되었습니다.

## 핵심 내용
RoBoa는 덩굴 형태의 수색 및 구조 로봇으로, 붕괴된 건물과 같은 좁고 복잡한 환경을 탐사할 수 있습니다. 이 로봇은 구조대가 매몰자를 찾고 의사소통하는 것을 돕습니다. 이동을 위해 덩굴 로봇의 원리를 사용하며, 튜브 끝을 뒤집어 앞으로 나아갑니다. 튜브 내부에는 공압 액추에이터가 있어 측면 이동을 가능하게 합니다. 헤드에는 센서가 장착되어 있으며 튜브 끝 외부에 설치됩니다. 후방에는 공급 상자가 있어 말린 튜브를 보관하고 압축 공기, 전력, 연산 능력, 그리고 사용자가 시스템과 상호작용할 수 있는 인터페이스를 제공합니다. 케이블 수를 줄이고 공압 액추에이터의 저수준 제어를 담당하는 분산 제어 방식이 구현되었습니다. 시스템과 핵심 구성 요소의 설계, 특성 분석 및 실험적 평가가 제시됩니다. 완전한 프로토타입은 완전히 작동 가능하며, 약 10m 이동 후 원격 제어 로봇이 반복적으로 매몰자를 찾을 수 있었던 붕괴 건물의 실제 환경에서 평가되었습니다.

## 参考
- http://arxiv.org/abs/2203.15145v1
