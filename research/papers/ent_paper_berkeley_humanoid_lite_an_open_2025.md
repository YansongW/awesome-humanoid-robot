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
  zh: Berkeley Humanoid Lite 是加州大学伯克利分校于 2025 年提出的开源人形机器人硬件设计。其核心贡献在于采用模块化 3D 打印摆线齿轮箱，将总硬件成本控制在 5,000 美元以下，并实现了从仿真到硬件的零样本策略迁移。该平台旨在通过完全开源硬件、嵌入式代码及训练框架，推动人形机器人技术的民主化发展。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.17249v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (750 chars, DeepSeek).'
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
针对现有商业人形机器人成本高昂、闭源且不透明的问题，Berkeley Humanoid Lite 提出了一种完全开源、可定制且易于复制的解决方案。该机器人采用模块化 3D 打印齿轮箱设计，所有组件均可通过电商平台采购，并使用标准桌面 3D 打印机完成制造。为克服塑料齿轮箱强度与耐久性不足的固有缺陷，设计团队采用了摆线齿轮结构以优化外形尺寸。通过强化学习开发的运动控制器成功实现了从仿真到硬件的零样本策略迁移，验证了该平台在科研验证中的适用性。

## 核心内容
### 设计动机与目标
- 现有商业人形机器人存在三大痛点：成本高、闭源、不透明，严重阻碍了社区协作与技术发展。
- Berkeley Humanoid Lite 旨在通过开源设计降低准入门槛，促进人形机器人技术的民主化。

### 核心硬件架构
- **模块化 3D 打印齿轮箱**：采用摆线齿轮设计，在塑料材质限制下优化了扭矩密度与耐用性。
- **制造与采购**：所有零件可通过电商平台购买，使用标准桌面 3D 打印机即可制造，总成本低于 5,000 美元（基于美国市场价格）。
- **耐久性验证**：对 3D 打印执行器进行了大量测试，以消除对塑料组件可靠性的担忧。

### 实验与性能验证
- **运动控制器开发**：基于强化学习训练，成功实现了从仿真环境到真实硬件的零样本策略迁移。
- **平台适用性**：实验证明了该硬件在科研验证中的可靠性，尤其适用于算法快速迭代与复现。

### 开源资源与影响
- 完全开源内容包括：硬件设计文件、嵌入式代码、训练与部署框架。
- 所有资源可通过 https://lite.berkeley-humanoid.org 获取，旨在成为人形机器人民主化发展的关键里程碑。

## Overview
Despite significant interest and advancements in humanoid robotics, most existing commercially available hardware remains high-cost, closed-source, and non-transparent within the robotics community. This lack of accessibility and customization hinders the growth of the field and the broader development of humanoid technologies. To address these challenges and promote democratization in humanoid robotics, we demonstrate Berkeley Humanoid Lite, an open-source humanoid robot designed to be accessible, customizable, and beneficial for the entire community. The core of this design is a modular 3D-printed gearbox for the actuators and robot body. All components can be sourced from widely available e-commerce platforms and fabricated using standard desktop 3D printers, keeping the total hardware cost under $5,000 (based on U.S. market prices). The design emphasizes modularity and ease of fabrication. To address the inherent limitations of 3D-printed gearboxes, such as reduced strength and durability compared to metal alternatives, we adopted a cycloidal gear design, which provides an optimal form factor in this context. Extensive testing was conducted on the 3D-printed actuators to validate their durability and alleviate concerns about the reliability of plastic components. To demonstrate the capabilities of Berkeley Humanoid Lite, we conducted a series of experiments, including the development of a locomotion controller using reinforcement learning. These experiments successfully showcased zero-shot policy transfer from simulation to hardware, highlighting the platform's suitability for research validation. By fully open-sourcing the hardware design, embedded code, and training and deployment frameworks, we aim for Berkeley Humanoid Lite to serve as a pivotal step toward democratizing the development of humanoid robotics. All resources are available at https://lite.berkeley-humanoid.org.

## 参考
- http://arxiv.org/abs/2504.17249v1

## 개요
기존 상업용 휴머노이드 로봇의 높은 비용, 폐쇄성, 불투명성 문제를 해결하기 위해, Berkeley Humanoid Lite는 완전히 오픈소스이며 맞춤화 가능하고 복제가 쉬운 솔루션을 제안합니다. 이 로봇은 모듈식 3D 프린팅 기어박스 설계를 채택하며, 모든 부품은 전자상거래 플랫폼에서 구매할 수 있고 표준 데스크톱 3D 프린터로 제조할 수 있습니다. 플라스틱 기어박스의 강도와 내구성 부족이라는 고유한 한계를 극복하기 위해, 설계 팀은 사이클로이드 기어 구조를 사용하여 외형 치수를 최적화했습니다. 강화 학습을 통해 개발된 운동 제어기는 시뮬레이션에서 하드웨어로의 제로샷 정책 전이를 성공적으로 구현하여, 이 플랫폼의 과학적 연구 검증에서의 적합성을 입증했습니다.

## 핵심 내용
### 설계 동기와 목표
- 기존 상업용 휴머노이드 로봇은 비용 높음, 폐쇄성, 불투명성이라는 세 가지 주요 문제점을 가지고 있으며, 이는 커뮤니티 협력과 기술 발전을 심각하게 저해합니다.
- Berkeley Humanoid Lite는 오픈소스 설계를 통해 진입 장벽을 낮추고 휴머노이드 로봇 기술의 민주화를 촉진하는 것을 목표로 합니다.

### 핵심 하드웨어 아키텍처
- **모듈식 3D 프린팅 기어박스**: 사이클로이드 기어 설계를 채택하여 플라스틱 재질의 한계 속에서 토크 밀도와 내구성을 최적화했습니다.
- **제조 및 조달**: 모든 부품은 전자상거래 플랫폼에서 구매할 수 있으며, 표준 데스크톱 3D 프린터로 제조 가능하고 총 비용은 5,000달러 미만입니다 (미국 시장 가격 기준).
- **내구성 검증**: 3D 프린팅 액추에이터에 대한 광범위한 테스트를 수행하여 플라스틱 부품의 신뢰성에 대한 우려를 해소했습니다.

### 실험 및 성능 검증
- **운동 제어기 개발**: 강화 학습 기반으로 훈련되어 시뮬레이션 환경에서 실제 하드웨어로의 제로샷 정책 전이를 성공적으로 구현했습니다.
- **플랫폼 적합성**: 실험을 통해 이 하드웨어가 과학적 연구 검증, 특히 알고리즘의 빠른 반복과 재현에 있어 신뢰할 수 있음을 입증했습니다.

### 오픈소스 리소스 및 영향
- 완전한 오픈소스 콘텐츠에는 하드웨어 설계 파일, 임베디드 코드, 훈련 및 배포 프레임워크가 포함됩니다.
- 모든 리소스는 https://lite.berkeley-humanoid.org 에서 확인할 수 있으며, 휴머노이드 로봇 민주화 발전의 핵심 이정표가 되는 것을 목표로 합니다.
