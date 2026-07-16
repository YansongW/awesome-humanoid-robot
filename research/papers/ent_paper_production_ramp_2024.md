---
$id: ent_paper_production_ramp_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Production Ramp
  zh: 产能爬坡
  ko: Production Ramp
summary:
  en: Transition from pilot-line builds to volume manufacturing while improving yield, cycle time, and cost.
  zh: 当前人形机器人执行器供应链呈现高端减速器与高端编码器高度集中的特征：谐波减速器全球头部企业 Harmonic Drive、RV 减速器 Nabtesco 占据较大市场份额；高端磁编码器/光编也主要由日本、欧洲企业供应。这种集中度带来供应风险，尤其在地缘政治与产能紧张时。
  ko: 파일럿 라인에서 볼륨 제조로 전환하면서 수율, 사이클 타임 및 비용을 개선하는 과정.
domains:
- 05_mass_production
- 03_manufacturing_processes
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- concept
- manufacturing
- ramp
- volume
- yield
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#国产替代与供应链韧性 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_001
  type: website
  title: Production Ramp
  url: https://en.wikipedia.org/wiki/Ramp-up
  date: '2024'
  accessed_at: '2026-07-02'
---

## 概述
产能爬坡是人形机器人领域的重要概念。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
当前人形机器人执行器供应链呈现**高端减速器与高端编码器高度集中**的特征：谐波减速器全球头部企业 Harmonic Drive、RV 减速器 Nabtesco 占据较大市场份额；高端磁编码器/光编也主要由日本、欧洲企业供应。这种集中度带来供应风险，尤其在地缘政治与产能紧张时。

国内供应链在过去十年快速进步：绿的谐波、来福谐波在谐波减速器领域已实现批量供货；汇川、禾川、雷赛等在无框电机与伺服驱动领域具备竞争力；峰岹科技、纳芯微等在栅极驱动与电流传感器芯片上取得突破。然而，在**超高精度谐波减速器、超高分辨率光编、车规级功率模块**等高端领域，国产替代仍在进行中。

提升供应链韧性的工程策略包括：

1. **双源化**：关键零部件至少认证两家供应商，避免单一来源；
2. **模块化接口**：把电机、减速器、驱动器接口标准化，便于切换供应商；
3. **安全库存与 VMI**：对长交期零件建立合理库存或供应商管理库存；
4. **垂直整合**：自研核心部件（如 Tesla 自研执行器、Optimus 电机与减速器一体化），但需权衡资本投入与产能爬坡。

!!! note "术语解释：供应链韧性、双源化、垂直整合、VMI、产能爬坡"
    - **供应链韧性（supply chain resilience）**：供应链抵抗中断并快速恢复的能力。
    - **双源化（dual sourcing）**：为同一零部件认证两个供应商。
    - **垂直整合（vertical integration）**：企业向上游零部件延伸，自主生产关键件。
    - **VMI（vendor managed inventory）**：供应商管理库存，按实际消耗补货。
    - **产能爬坡（production ramp-up）**：从试产到大批量量产的过程，良率与成本逐步优化。

---

## 参考
- [Production Ramp](https://en.wikipedia.org/wiki/Ramp-up)
- 项目 Wiki：chapter-04.md#国产替代与供应链韧性

## Overview
Production ramp-up is an important concept in the field of humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
The current supply chain for humanoid robot actuators exhibits a **high concentration of high-end reducers and high-end encoders**: Harmonic Drive, a global leader in harmonic reducers, and Nabtesco, a leader in RV reducers, hold significant market shares; high-end magnetic encoders/optical encoders are also primarily supplied by Japanese and European companies. This concentration introduces supply risks, especially during geopolitical tensions and capacity constraints.

The domestic supply chain has made rapid progress over the past decade: Leaderdrive and Laffert have achieved mass production in the field of harmonic reducers; Inovance, Weichuan, and Leadshine are competitive in frameless motors and servo drives; Fortior Technology and Novosense have made breakthroughs in gate drivers and current sensor chips. However, in high-end areas such as **ultra-high precision harmonic reducers, ultra-high resolution optical encoders, and automotive-grade power modules**, domestic substitution is still ongoing.

Engineering strategies to enhance supply chain resilience include:

1. **Dual Sourcing**: Certify at least two suppliers for key components to avoid single-source dependency;
2. **Modular Interfaces**: Standardize interfaces for motors, reducers, and drives to facilitate supplier switching;
3. **Safety Stock and VMI**: Maintain reasonable inventory levels for long-lead-time parts or adopt vendor-managed inventory;
4. **Vertical Integration**: Develop core components in-house (e.g., Tesla's self-developed actuators, Optimus's integrated motor and reducer), but this requires balancing capital investment with production ramp-up.

!!! note "Terminology Explanation: Supply Chain Resilience, Dual Sourcing, Vertical Integration, VMI, Production Ramp-up"
    - **Supply Chain Resilience**: The ability of a supply chain to resist disruptions and recover quickly.
    - **Dual Sourcing**: Certifying two suppliers for the same component.
    - **Vertical Integration**: A company extending upstream to produce key components in-house.
    - **VMI (Vendor Managed Inventory)**: The supplier manages inventory and replenishes based on actual consumption.
    - **Production Ramp-up**: The process from trial production to mass production, with gradual optimization of yield and cost.

---

## 개요
생산량 증대는 휴머노이드 로봇 분야의 중요한 개념입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
현재 휴머노이드 로봇 액추에이터 공급망은 **고급 감속기와 고급 엔코더가 고도로 집중된** 특징을 보입니다: 하모닉 감속기 글로벌 선두 기업 Harmonic Drive, RV 감속기 Nabtesco가 큰 시장 점유율을 차지하고 있으며, 고급 자기 엔코더/광학 엔코더도 주로 일본, 유럽 기업이 공급합니다. 이러한 집중도는 지정학적 긴장과 생산 능력 부족 시 공급 리스크를 초래합니다.

국내 공급망은 지난 10년간 빠르게 발전했습니다: 绿的谐波(Leaderdrive), 来福谐波(Laifual)는 하모닉 감속기 분야에서 양산 공급을 실현했으며, 汇川(Inovance), 禾川(Hechuan), 雷赛(Leadshine) 등은 프레임리스 모터와 서보 드라이브 분야에서 경쟁력을 갖추고 있습니다. 峰岹科技(Fortior), 纳芯微(Novosense) 등은 게이트 드라이버와 전류 센서 칩에서 돌파구를 마련했습니다. 그러나 **초정밀 하모닉 감속기, 초고해상도 광학 엔코더, 차량용 파워 모듈** 등 고급 분야에서는 국산화 대체가 여전히 진행 중입니다.

공급망 탄력성을 높이기 위한 엔지니어링 전략은 다음과 같습니다:

1. **이중 소싱**: 핵심 부품에 대해 최소 두 개의 공급업체를 인증하여 단일 소스 의존 방지;
2. **모듈식 인터페이스**: 모터, 감속기, 드라이브 인터페이스를 표준화하여 공급업체 전환 용이;
3. **안전 재고 및 VMI**: 긴 리드 타임 부품에 대해 적정 재고 또는 공급업체 관리 재고 구축;
4. **수직 통합**: 핵심 부품 자체 개발(Tesla의 자체 액추에이터, Optimus 모터-감속기 일체화 등), 단 자본 투입과 생산량 증대 간 균형 필요.

!!! note "용어 설명: 공급망 탄력성, 이중 소싱, 수직 통합, VMI, 생산량 증대"
    - **공급망 탄력성(supply chain resilience)**: 공급망이 중단을 견디고 신속히 복구하는 능력.
    - **이중 소싱(dual sourcing)**: 동일 부품에 대해 두 개의 공급업체를 인증하는 것.
    - **수직 통합(vertical integration)**: 기업이 상류 부품으로 확장하여 핵심 부품을 자체 생산하는 것.
    - **VMI(vendor managed inventory)**: 공급업체 관리 재고, 실제 소비에 따라 보충.
    - **생산량 증대(production ramp-up)**: 시험 생산에서 대량 양산까지의 과정으로, 수율과 비용이 점진적으로 최적화됨.

---
