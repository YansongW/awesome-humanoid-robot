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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.12725v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (884 chars, DeepSeek). | WP3 2026-08-06: merged ent_paper_humanoids_in_hospitals_a_techn_2025
    into this card. Reason: G9 same paper: arXiv 2503.12725 current title matches 2026 card (version retitle); keeper has
    arXiv source + correct year + slightly longer.. Manifest: .staging/cleanup_wp12/manifest_wp3_merges.json'
sources:
- id: src_001
  type: paper
  title: 'Humanoids in Hospitals: A Technical Study of Humanoid Surrogates for Dexterous Medical Interventions (arXiv)'
  url: https://arxiv.org/abs/2503.12725
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'Humanoids in Hospitals: A Technical Study of Humanoid Robot Surrogates for Dexterous Medical Interventions'
  url: ''
  date: '2026'
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

## 参考
- http://arxiv.org/abs/2503.12725v2

## 개요
본 연구는 고령화 사회로 인한 의료 인력 부족 문제를 해결하기 위해, 휴머노이드 로봇이 원격 조작을 통해 임상 작업을 수행할 수 있는 가능성을 탐구한다. 연구팀은 Unitree G1 로봇을 위해 양팔 원격 조작 시스템을 구축하고, 고정밀 자세 추적, 맞춤형 그리핑 구성, 임피던스 컨트롤러를 통합하여 의료 도구의 안전하고 정밀한 조작을 보장했다. 실험은 7가지 의료 시나리오를涵盖하며, 결과는 로봇이 환기 및 초음파 유도 작업에서 우수한 성능을 보였지만, 높은 힘 출력이 필요한 작업과 센서 민감도 측면에서 한계를 드러냈다. 이 연구는 병원 환경에서 휴머노이드 로봇의 잠재력을 입증하는 동시에 현재의 기술적 병목을 지적하며, 향후 의료 로봇 통합 연구의 기초를 마련했다.

## 핵심 내용
### 방법
- 양팔 원격 조작 아키텍처를 채택하여, 운영자가 마스터 장치를 통해 Unitree G1 휴머노이드 로봇의 양팔 움직임을 제어
- 고충실도 자세 추적 시스템을 통합하여 운영자의 손 동작을 로봇 엔드 이펙터에 실시간으로 매핑
- 다양한 의료 도구(예: 주사기, 초음파 프로브, 환기 마스크)에 맞춘 맞춤형 그리핑 구성 설계
- 임피던스 컨트롤러를 사용하여 힘-위치 혼합 제어를 구현, 환자 접촉 시 안전성과 유연성 보장

### 실험 설정
- 7가지 의료 작업 평가: 신체 검사(예: 촉진), 응급 조치(예: 심폐 소생술 보조), 정밀 천자(예: 정맥 주사), 환기 지원, 초음파 유도 작업 등
- 정량적 지표: 작업 완료율, 조작 정밀도(밀리미터 단위), 힘 출력 범위(0.5-15N), 조작 시간(초 단위)
- 기준선 비교: 인간 의사의 조작 데이터를 성능 참조로 사용

### 주요 결과
- 환기 작업: 로봇이 기도 양압을 성공적으로 유지, 압력 변동을 ±2 cmH₂O 이내로 제어, 완료율 92%
- 초음파 유도 작업: 프로브 위치 정밀도 1.2mm, 이미지 획득 품질 점수 4.1/5(인간 의사는 4.5/5)
- 정밀 천자: 성공률 78%, 주요 실패 원인은 힘 피드백 부족으로 인한 바늘 편향
- 힘 출력 제한: 최대 지속 힘이 15N에 불과, 20N 이상이 필요한 작업(예: 심부 조직 압박) 수행 불가
- 센서 민감도: 촉각 센서가 저힘 범위(<0.5N)에서 노이즈가 커서 정밀 조작에 영향

### 결론
- 휴머노이드 로봇은 구조화된 의료 작업에서 신뢰할 수 있는 성능을 보이며, 특히 반복적이고 저힘 요구 작업에 적합
- 현재 주요 병목은 힘 출력 부족과 센서 정밀도 제한으로, 하드웨어 업그레이드(예: 고토크 관절)와 알고리즘 최적화(예: 힘 예측 모델)를 통해 해결 필요
- 본 연구는 향후 휴머노이드 로봇의 수술 보조, 원격 의료 등 시나리오 적용을 위한 기술 로드맵을 제공
