---
$id: ent_application_industrial_manufacturing
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: application_scenario
names:
  en: Industrial Manufacturing
  zh: 工业制造
  ko: 산업 제조
summary:
  en: The application of humanoid robots to tasks such as assembly, machine tending, inspection, and material handling in
    factories.
  zh: 概述 工业制造是人形机器人领域的重要application_scenario。以下内容整理自项目 Wiki，供深入查阅。
  ko: 휴로봇을 공장의 조립·기계 관리·검사·자재 취급 등에 적용하는 분야.
domains:
- 11_applications_markets
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- application
- chapter_27
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-06.md#6.8 供应链与主要厂商 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
工业制造是人形机器人领域的重要应用场景。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
人形机器人计算、电源与热管理子系统的供应链高度全球化，同时受到半导体制造、电池材料和热界面材料等上游环节制约。

!!! note "术语解释：供应链、ODM、OEM、IDM、Fabless、Foundry"
    - **供应链（supply chain）**：从原材料到最终产品的所有环节和企业网络。
    - **ODM（Original Design Manufacturer）**：原始设计制造商，负责设计和制造，品牌方贴牌销售。
    - **OEM（Original Equipment Manufacturer）**：原始设备制造商，通常指代工厂或品牌整机厂。
    - **IDM（Integrated Device Manufacturer）**：同时从事芯片设计、制造和封测的垂直整合企业。
    - **Fabless**：无晶圆厂设计公司，只设计芯片，委托 Foundry 制造。
    - **Foundry**：晶圆代工厂，如台积电、三星、Intel Foundry。

**计算平台厂商**：NVIDIA（Jetson 系列、Thor）、Intel（NUC、Xeon）、Qualcomm（RB 系列、QCS 系列）、AMD（Kria FPGA、Ryzen Embedded）、Apple（M 系列）、NXP（i.MX、S32）、Renesas、Horizon Robotics、Rockchip、Allwinner 等。

**电源与电池厂商**：CATL、BYD、LG Energy Solution、Samsung SDI、Panasonic、EVE Energy、欣旺达、亿纬锂能、德州仪器（TI）、ADI、Infineon、ON Semiconductor、MPS、STMicroelectronics 等提供 BMS、功率半导体和电源管理 IC。

**热管理厂商**：Aavid（Boyd）、Delta、Nidec、Fujikura、双鸿、超众、奇鋐等提供散热器、热管、均热板、风扇和液冷方案；Shin-Etsu、Dow、Henkel、信越等提供 TIM 材料。

**制造瓶颈**。先进制程（7 nm 及以下）晶圆代工、HBM 高带宽内存、高端功率半导体（SiC/GaN）是当前机器人与自动驾驶计算平台的关键瓶颈。地缘政治和出口管制进一步增加了供应链不确定性。

**国产替代进展**。中国大陆在计算芯片、功率半导体和电池领域已形成完整产业链：华为昇腾、地平线征程、寒武纪思元、瑞芯微 RK 系列提供从端侧到边缘的 AI 算力；比亚迪、宁德时代在全球动力电池市场占据重要份额；士兰微、华润微、斯达半导、时代电气等在 IGBT 和 SiC 模块领域持续突破。国产替代的成熟度直接影响人形机器人成本可控性和供应链韧性。

!!! note "术语解释：国产替代、IGBT、SiC、GaN、HBM、晶圆代工"
    - **国产替代（domestic substitution）**：用本国或本地供应链产品替代进口产品的过程。
    - **IGBT（Insulated Gate Bipolar Transistor）**：绝缘栅双极型晶体管，中高压功率开关器件。
    - **SiC（Silicon Carbide）**：碳化硅，宽禁带半导体，适合高频高温功率应用。
    - **GaN（Gallium Nitride）**：氮化镓，另一种宽禁带半导体，适合高频高效电源。
    - **HBM（High Bandwidth Memory）**：高带宽存储器，通过 3D 堆叠实现高带宽。
    - **晶圆代工（wafer foundry）**：提供晶圆制造服务的半导体工厂。

**成本结构**。以一台高端人形机器人为例，计算平台（SoM + 载板 + 散热）可能占总 BOM 成本的 10%–20%；电池组占 15%–25%；电机与驱动占 30%–40%；结构件、传感器、线束和组装占其余部分。随着量产规模扩大和芯片集成度提高，计算与电源子系统的成本占比有望下降。

**整机计算架构案例**。当前主流人形机器人厂商多采用“中央大脑 + 分布式小脑”架构：

- **Tesla Optimus**：采用自研 FSD 芯片作为感知与决策主控，躯干和关节通过自定义通信总线连接，强调视觉主导的端到端控制。
- **Boston Dynamics Atlas**：使用嵌入式实时计算机处理状态估计与步态控制，液压/电动执行器由专用驱动板闭环控制，强调高动态运动的确定性。
- **Agility Digit / Figure 02**：采用 NVIDIA Jetson 或类似平台处理多相机感知与导航，下层通过 EtherCAT 或类似总线连接关节驱动器。
- **优必选 Walker / 智元远征 A2 / 傅利叶 GR-1**：多采用 NVIDIA Jetson AGX Orin / Xavier 或国产替代平台作为上位机，结合 ARM MCU/FPGA 做关节实时控制。

这些案例共同表明：人形机器人计算架构正在从早期的 PC/工控机 + 运动控制卡，向高度集成的嵌入式 SoC + 实时总线 + 云端协同演进。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-06.md#6.8 供应链与主要厂商

## Overview
Industrial manufacturing is a key application scenario for humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
The supply chain for computing, power, and thermal management subsystems of humanoid robots is highly globalized, while also constrained by upstream sectors such as semiconductor manufacturing, battery materials, and thermal interface materials.

!!! note "Terminology: Supply Chain, ODM, OEM, IDM, Fabless, Foundry"
    - **Supply chain**: All stages and enterprise networks from raw materials to final products.
    - **ODM (Original Design Manufacturer)**: Designs and manufactures products, which are then branded and sold by another company.
    - **OEM (Original Equipment Manufacturer)**: Typically refers to contract manufacturers or brand integrators.
    - **IDM (Integrated Device Manufacturer)**: Vertically integrated companies that handle chip design, manufacturing, packaging, and testing.
    - **Fabless**: Companies that design chips but outsource manufacturing to foundries.
    - **Foundry**: Wafer fabrication facilities, e.g., TSMC, Samsung, Intel Foundry.

**Computing Platform Vendors**: NVIDIA (Jetson series, Thor), Intel (NUC, Xeon), Qualcomm (RB series, QCS series), AMD (Kria FPGA, Ryzen Embedded), Apple (M series), NXP (i.MX, S32), Renesas, Horizon Robotics, Rockchip, Allwinner, etc.

**Power and Battery Vendors**: CATL, BYD, LG Energy Solution, Samsung SDI, Panasonic, EVE Energy, Sunwoda, Yiwei Lithium Energy, Texas Instruments (TI), ADI, Infineon, ON Semiconductor, MPS, STMicroelectronics, etc., providing BMS, power semiconductors, and power management ICs.

**Thermal Management Vendors**: Aavid (Boyd), Delta, Nidec, Fujikura, Auras, Cooler Master, Wistron, etc., offering heat sinks, heat pipes, vapor chambers, fans, and liquid cooling solutions; Shin-Etsu, Dow, Henkel, etc., providing TIM materials.

**Manufacturing Bottlenecks**. Advanced process (7nm and below) wafer foundry, HBM high-bandwidth memory, and high-end power semiconductors (SiC/GaN) are key bottlenecks for current robot and autonomous driving computing platforms. Geopolitics and export controls further increase supply chain uncertainty.

**Domestic Substitution Progress**. Mainland China has formed a complete industrial chain in computing chips, power semiconductors, and batteries: Huawei Ascend, Horizon Journey, Cambricon Siyuan, Rockchip RK series provide AI computing power from edge to endpoint; BYD and CATL hold significant shares in the global power battery market; Silan Micro, China Resources Microelectronics, Starpower Semiconductor, and Times Electric continue to make breakthroughs in IGBT and SiC modules. The maturity of domestic substitution directly impacts the cost controllability and supply chain resilience of humanoid robots.

!!! note "Terminology: Domestic Substitution, IGBT, SiC, GaN, HBM, Wafer Foundry"
    - **Domestic substitution**: The process of replacing imported products with locally or domestically sourced alternatives.
    - **IGBT (Insulated Gate Bipolar Transistor)**: A medium-to-high voltage power switching device.
    - **SiC (Silicon Carbide)**: A wide-bandgap semiconductor suitable for high-frequency, high-temperature power applications.
    - **GaN (Gallium Nitride)**: Another wide-bandgap semiconductor suitable for high-frequency, high-efficiency power supplies.
    - **HBM (High Bandwidth Memory)**: High-bandwidth memory achieved through 3D stacking.
    - **Wafer foundry**: Semiconductor factories that provide wafer manufacturing services.

**Cost Structure**. For a high-end humanoid robot, the computing platform (SoM + carrier board + cooling) may account for 10%–20% of the total BOM cost; the battery pack accounts for 15%–25%; motors and drives account for 30%–40%; structural parts, sensors, wiring harnesses, and assembly make up the remainder. As production scales up and chip integration increases, the cost share of computing and power subsystems is expected to decline.

**Whole-Robot Computing Architecture Examples**. Current mainstream humanoid robot manufacturers often adopt a "central brain + distributed cerebellum" architecture:

- **Tesla Optimus**: Uses a self-developed FSD chip as the main controller for perception and decision-making, with the torso and joints connected via a custom communication bus, emphasizing vision-driven end-to-end control.
- **Boston Dynamics Atlas**: Uses embedded real-time computers for state estimation and gait control, with hydraulic/electric actuators controlled in closed loop by dedicated drive boards, emphasizing deterministic high-dynamic motion.
- **Agility Digit / Figure 02**: Uses NVIDIA Jetson or similar platforms for multi-camera perception and navigation, with lower-level joint drives connected via EtherCAT or similar buses.
- **UBTECH Walker / Zhiyuan Expedition A2 / Fourier GR-1**: Often use NVIDIA Jetson AGX Orin / Xavier or domestic alternatives as the upper computer, combined with ARM MCU/FPGA for real-time joint control.

These cases collectively indicate that the computing architecture of humanoid robots is evolving from early PC/industrial PC + motion control cards to highly integrated embedded SoCs + real-time buses + cloud collaboration.

## 개요
산업 제조는 휴머노이드 로봇 분야의 중요한 응용 시나리오입니다. 다음 내용은 프로젝트 Wiki에서 정리한 것으로, 심층적인 참고를 위해 제공됩니다.

## 핵심 내용
휴머노이드 로봇의 컴퓨팅, 전원 및 열 관리 서브시스템의 공급망은 고도로 글로벌화되어 있으며, 동시에 반도체 제조, 배터리 재료 및 열 인터페이스 재료와 같은 상류 단계의 제약을 받습니다.

!!! note "용어 설명: 공급망, ODM, OEM, IDM, Fabless, Foundry"
    - **공급망(supply chain)**: 원자재부터 최종 제품까지의 모든 단계와 기업 네트워크.
    - **ODM(Original Design Manufacturer)**: 오리지널 디자인 제조사, 설계와 제조를 담당하며 브랜드사가 OEM으로 판매.
    - **OEM(Original Equipment Manufacturer)**: 오리지널 장비 제조사, 일반적으로 위탁 생산 공장 또는 브랜드 완제품 공장을 의미.
    - **IDM(Integrated Device Manufacturer)**: 칩 설계, 제조 및 패키징/테스트를 동시에 수행하는 수직 통합 기업.
    - **Fabless**: 팹리스 설계 회사, 칩만 설계하고 Foundry에 제조 위탁.
    - **Foundry**: 웨이퍼 파운드리, 예: TSMC, 삼성, Intel Foundry.

**컴퓨팅 플랫폼 제조사**: NVIDIA(Jetson 시리즈, Thor), Intel(NUC, Xeon), Qualcomm(RB 시리즈, QCS 시리즈), AMD(Kria FPGA, Ryzen Embedded), Apple(M 시리즈), NXP(i.MX, S32), Renesas, Horizon Robotics, Rockchip, Allwinner 등.

**전원 및 배터리 제조사**: CATL, BYD, LG Energy Solution, Samsung SDI, Panasonic, EVE Energy, 신왕다(欣旺达), 이위리튬에너지(亿纬锂能), 텍사스 인스트루먼트(TI), ADI, Infineon, ON Semiconductor, MPS, STMicroelectronics 등이 BMS, 전력 반도체 및 전원 관리 IC를 제공.

**열 관리 제조사**: Aavid(Boyd), Delta, Nidec, Fujikura, 쌍홍(双鸿), 초중(超众), 치홍(奇鋐) 등이 방열판, 히트파이프, 베이퍼 챔버, 팬 및 액체 냉각 솔루션을 제공; Shin-Etsu, Dow, Henkel, 신에츠(信越) 등이 TIM 재료를 제공.

**제조 병목 현상**. 첨단 공정(7nm 이하) 웨이퍼 파운드리, HBM 고대역폭 메모리, 고급 전력 반도체(SiC/GaN)는 현재 로봇 및 자율주행 컴퓨팅 플랫폼의 핵심 병목입니다. 지정학적 요인과 수출 통제는 공급망 불확실성을 더욱 증가시킵니다.

**국산 대체 현황**. 중국 본토는 컴퓨팅 칩, 전력 반도체 및 배터리 분야에서 완전한 산업 체인을 형성했습니다: 화웨이昇腾(昇腾), Horizon Robotics征程(征程), Cambricon思元(思元), Rockchip RK 시리즈가 엣지부터 엣지까지 AI 연산력을 제공; BYD, CATL은 글로벌 동력 배터리 시장에서 중요한 점유율을 차지; 실란마이크로(士兰微), 차이나리소스마이크로(华润微), 스타파워세미(斯达半导), 타임즈일렉트릭(时代电气) 등이 IGBT 및 SiC 모듈 분야에서 지속적으로 돌파구를 마련. 국산 대체의 성숙도는 휴머노이드 로봇의 비용 통제 가능성과 공급망 탄력성에 직접적인 영향을 미칩니다.

!!! note "용어 설명: 국산 대체, IGBT, SiC, GaN, HBM, 웨이퍼 파운드리"
    - **국산 대체(domestic substitution)**: 자국 또는 현지 공급망 제품으로 수입 제품을 대체하는 과정.
    - **IGBT(Insulated Gate Bipolar Transistor)**: 절연 게이트 양극성 트랜지스터, 중고압 전력 스위칭 소자.
    - **SiC(Silicon Carbide)**: 탄화규소, 광대역 반도체, 고주파 고온 전력 응용에 적합.
    - **GaN(Gallium Nitride)**: 질화갈륨, 또 다른 광대역 반도체, 고주파 고효율 전원에 적합.
    - **HBM(High Bandwidth Memory)**: 고대역폭 메모리, 3D 적층을 통해 높은 대역폭 구현.
    - **웨이퍼 파운드리(wafer foundry)**: 웨이퍼 제조 서비스를 제공하는 반도체 공장.

**비용 구조**. 고급 휴머노이드 로봇 한 대를 예로 들면, 컴퓨팅 플랫폼(SoM + 캐리어 보드 + 방열)은 전체 BOM 비용의 10%–20%를 차지할 수 있음; 배터리 팩은 15%–25%; 모터 및 드라이브는 30%–40%; 구조 부품, 센서, 배선 및 조립이 나머지를 차지. 양산 규모가 확대되고 칩 집적도가 높아짐에 따라 컴퓨팅 및 전원 서브시스템의 비용 비중은 감소할 것으로 예상됩니다.

**완제품 컴퓨팅 아키텍처 사례**. 현재 주류 휴머노이드 로봇 제조사는 대부분 "중앙 두뇌 + 분산 소뇌" 아키텍처를 채택:

- **Tesla Optimus**: 자체 개발 FSD 칩을 인식 및 의사 결정 메인 컨트롤러로 사용, 몸체와 관절은 맞춤형 통신 버스로 연결, 시각 중심의 엔드투엔드 제어 강조.
- **Boston Dynamics Atlas**: 임베디드 실시간 컴퓨터를 사용하여 상태 추정 및 보행 제어 처리, 유압/전기 액추에이터는 전용 드라이브 보드로 폐루프 제어, 고역학적 움직임의 결정성 강조.
- **Agility Digit / Figure 02**: NVIDIA Jetson 또는 유사 플랫폼을 사용하여 다중 카메라 인식 및 내비게이션 처리, 하위 계층은 EtherCAT 또는 유사 버스를 통해 관절 드라이버 연결.
- **UBTECH Walker / 지위안 원정 A2 / Fourier GR-1**: 대부분 NVIDIA Jetson AGX Orin / Xavier 또는 국산 대체 플랫폼을 상위 컴퓨터로 사용, ARM MCU/FPGA를 결합하여 관절 실시간 제어.

이러한 사례들은 공통적으로 보여줍니다: 휴머노이드 로봇 컴퓨팅 아키텍처는 초기의 PC/산업용 컴퓨터 + 모션 제어 카드에서 고도로 통합된 임베디드 SoC + 실시간 버스 + 클라우드 협력으로 진화하고 있습니다.
