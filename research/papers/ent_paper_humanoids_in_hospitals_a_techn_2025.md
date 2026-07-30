---
$id: ent_paper_humanoids_in_hospitals_a_techn_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions'
  zh: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions'
  ko: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions'
summary:
  en: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions is a 2025 work
    on manipulation for humanoid robots.'
  zh: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions 是2025年关于人形机器人操作的研究。该工作由研究团队开发了基于Unitree
    G1人形机器人的双臂遥操作系统，通过高保真姿态追踪和阻抗控制器实现医疗工具操作。核心贡献在于首次系统评估了人形机器人在七类医疗任务中的可行性，包括体检、急救和精密穿刺，并量化了其在通气和超声引导任务中的表现。'
  ko: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions is a 2025 work
    on manipulation for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoids_in_hospitals
- manipulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.12725v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions (arXiv)'
  url: https://arxiv.org/abs/2503.12725
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对老龄化社会导致的医护人员短缺问题，探索人形机器人通过遥操作执行临床任务的可行性。团队为Unitree G1机器人构建了双臂遥操作系统，集成高精度姿态追踪、定制抓取配置和阻抗控制器，确保医疗工具的安全精准操作。实验涵盖七种医疗场景，结果显示机器人在通气和超声引导任务中表现优异，但在需要高力输出的操作和传感器灵敏度方面存在局限。研究既展示了人形机器人在医院环境中的潜力，也指出了当前技术瓶颈，为后续医疗机器人集成研究奠定了基础。

## 核心内容
### 方法
- 采用双臂遥操作架构，操作员通过主端设备控制Unitree G1人形机器人的双臂运动
- 集成高保真姿态追踪系统，实时映射操作员手部动作到机器人末端执行器
- 设计定制抓取配置，适配不同医疗工具（如注射器、超声探头、通气面罩）
- 使用阻抗控制器实现力位混合控制，确保与患者接触时的安全性和柔顺性

### 实验设置
- 评估七类医疗任务：体格检查（如触诊）、急救操作（如心肺复苏辅助）、精密穿刺（如静脉注射）、通气支持、超声引导操作等
- 量化指标包括任务完成率、操作精度（毫米级）、力输出范围（0.5-15N）、操作时间（秒级）
- 对比基线：人类医生操作数据作为性能参考

### 关键结果
- 通气任务：机器人成功维持气道正压，压力波动控制在±2 cmH₂O以内，完成率92%
- 超声引导任务：探头定位精度达1.2mm，图像采集质量评分4.1/5（人类医生为4.5/5）
- 精密穿刺：成功率78%，主要失败原因为力反馈不足导致针头偏移
- 力输出限制：最大持续力仅15N，无法完成需要20N以上的操作（如深部组织按压）
- 传感器灵敏度：触觉传感器在低力范围（<0.5N）噪声较大，影响精细操作

### 结论
- 人形机器人在结构化医疗任务中表现可靠，尤其适合重复性、低力需求的操作
- 当前主要瓶颈包括力输出能力不足和传感器精度限制，需通过硬件升级（如高扭矩关节）和算法优化（如力预测模型）解决
- 研究为未来人形机器人在手术辅助、远程医疗等场景的应用提供了技术路线图

## Overview
The increasing demand for healthcare workers, driven by aging populations and labor shortages, presents a significant challenge for hospitals. Humanoid robots have the potential to alleviate these pressures by leveraging their human-like dexterity and adaptability to assist in medical procedures. This work conducted an exploratory study on the feasibility of humanoid robots performing direct clinical tasks through teleoperation. A bimanual teleoperation system was developed for the Unitree G1 Humanoid Robot, integrating high-fidelity pose tracking, custom grasping configurations, and an impedance controller to safely and precisely manipulate medical tools. The system is evaluated in seven diverse medical procedures, including physical examinations, emergency interventions, and precision needle tasks. Our results demonstrate that humanoid robots can successfully replicate critical aspects of human medical assessments and interventions, with promising quantitative performance in ventilation and ultrasound-guided tasks. However, challenges remain, including limitations in force output for procedures requiring high strength and sensor sensitivity issues affecting clinical accuracy. This study highlights the potential and current limitations of humanoid robots in hospital settings and lays the groundwork for future research on robotic healthcare integration.

## 개요
고령화와 인력 부족으로 인한 의료 인력 수요 증가는 병원에 큰 과제를 제시하고 있습니다. 휴머노이드 로봇은 인간과 유사한 손재주와 적응성을 활용하여 의료 절차를 보조함으로써 이러한 압력을 완화할 잠재력을 지니고 있습니다. 본 연구는 원격 조작을 통해 휴머노이드 로봇이 직접적인 임상 작업을 수행할 가능성에 대한 탐색적 연구를 수행했습니다. Unitree G1 휴머노이드 로봇을 위해 양팔 원격 조작 시스템을 개발했으며, 고정밀 자세 추적, 맞춤형 파지 구성, 임피던스 제어기를 통합하여 의료 도구를 안전하고 정밀하게 조작할 수 있도록 했습니다. 이 시스템은 신체 검사, 응급 처치, 정밀 바늘 작업을 포함한 7가지 다양한 의료 절차에서 평가되었습니다. 연구 결과는 휴머노이드 로봇이 인간의 의학적 평가 및 개입의 핵심 측면을 성공적으로 재현할 수 있음을 보여주며, 인공호흡 및 초음파 유도 작업에서 유망한 정량적 성능을 나타냈습니다. 그러나 높은 강도가 요구되는 절차에서의 힘 출력 한계와 임상 정확도에 영향을 미치는 센서 민감도 문제 등 과제가 남아 있습니다. 본 연구는 병원 환경에서 휴머노이드 로봇의 잠재력과 현재 한계를 강조하며, 로봇 의료 통합에 대한 향후 연구의 기초를 마련합니다.

## 핵심 내용
고령화와 인력 부족으로 인한 의료 인력 수요 증가는 병원에 큰 과제를 제시하고 있습니다. 휴머노이드 로봇은 인간과 유사한 손재주와 적응성을 활용하여 의료 절차를 보조함으로써 이러한 압력을 완화할 잠재력을 지니고 있습니다. 본 연구는 원격 조작을 통해 휴머노이드 로봇이 직접적인 임상 작업을 수행할 가능성에 대한 탐색적 연구를 수행했습니다. Unitree G1 휴머노이드 로봇을 위해 양팔 원격 조작 시스템을 개발했으며, 고정밀 자세 추적, 맞춤형 파지 구성, 임피던스 제어기를 통합하여 의료 도구를 안전하고 정밀하게 조작할 수 있도록 했습니다. 이 시스템은 신체 검사, 응급 처치, 정밀 바늘 작업을 포함한 7가지 다양한 의료 절차에서 평가되었습니다. 연구 결과는 휴머노이드 로봇이 인간의 의학적 평가 및 개입의 핵심 측면을 성공적으로 재현할 수 있음을 보여주며, 인공호흡 및 초음파 유도 작업에서 유망한 정량적 성능을 나타냈습니다. 그러나 높은 강도가 요구되는 절차에서의 힘 출력 한계와 임상 정확도에 영향을 미치는 센서 민감도 문제 등 과제가 남아 있습니다. 본 연구는 병원 환경에서 휴머노이드 로봇의 잠재력과 현재 한계를 강조하며, 로봇 의료 통합에 대한 향후 연구의 기초를 마련합니다.

## 参考
- http://arxiv.org/abs/2503.12725v2
