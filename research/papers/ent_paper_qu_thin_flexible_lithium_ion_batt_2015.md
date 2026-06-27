---
$id: ent_paper_qu_thin_flexible_lithium_ion_batt_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Thin Flexible Lithium Ion Battery Featuring Graphite Paper Based Current Collectors
    with Enhanced Conductivity
  zh: 基于高导电性石墨纸集流体的超薄柔性锂离子电池
  ko: 향상된 전도성의 흑연지 기반 집전체를 갖춘 얇은 유연한 리튬 이온 배터리
summary:
  en: This paper reports an ultrathin (<250 μm including encapsulation), lightweight,
    flexible lithium-ion battery that uses graphite paper coated with nanoscale aluminum
    or copper layers as current collectors, paired with a LiFePO4 cathode, a Li4Ti5O12
    anode, and a LiPF6-soaked polyethylene separator.
  zh: 该论文报道了一种超薄（包括封装层小于250微米）、轻质、柔性的锂离子电池，其采用纳米铝或铜层涂覆的石墨纸作为集流体，并配以磷酸铁锂正极、钛酸锂负极和浸润六氟磷酸锂的聚乙烯隔膜。
  ko: 본 논문은 나노 알루미늄 또는 구리층으로 코팅된 흑연지를 집전체로 사용하고 LiFePO4 양극, Li4Ti5O12 음극, LiPF6에 침적된
    폴리에틸렌 분리막을 결합하여 총 두께 250 μm 미만의 초박형·경량·유연한 리튬 이온 배터리를 보고한다.
domains:
- 02_components
- 01_raw_materials
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- component
- system
tags:
- flexible_battery
- lithium_ion_battery
- graphite_paper_current_collector
- lightweight_power_source
- wearable_energy_storage
- compliant_power
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv abstract and supplied metadata; full-text details,
    especially fabrication parameters and cycling data, require human review.
sources:
- id: src_001
  type: paper
  title: Thin Flexible Lithium Ion Battery Featuring Graphite Paper Based Current
    Collectors with Enhanced Conductivity
  url: https://arxiv.org/abs/1511.03949
  date: '2015'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses the need for power sources that can conform to curved, moving, and weight-sensitive robotic structures. Traditional lithium-ion cells rely on rigid, heavy metal-foil current collectors, which limit mechanical compliance and add mass. To overcome this, the authors replace the metal foil with thin graphite paper that is coated with nanoscale aluminum or copper layers, yielding current collectors that remain conductive while being flexible and lightweight. A full cell assembled with LiFePO4 cathode, Li4Ti5O12 anode, and a LiPF6-soaked polyethylene separator achieves an overall thickness below 250 μm including encapsulation, and the authors report electrochemical behavior comparable to conventional aluminum-foil-based cells.

The fabrication approach emphasizes physical compatibility: the graphite-paper substrate is lightweight, the deposited metal layers are sub-micron thick, and the entire stack can be bent while retaining stable charge/discharge capacity. The authors also note improved electrode yield and adhesion resulting from the nano-metal coating on graphite paper. These characteristics make the design relevant to applications where batteries must occupy irregular volumes or accompany moving parts, such as soft actuators, wearable modules, and compact joints in humanoid systems.

## Key Contributions

- Demonstrated an ultrathin (<250 μm total thickness including encapsulation), lightweight, and highly flexible lithium-ion battery.
- Developed metal-enhanced graphite-paper current collectors that combine mechanical flexibility with adequate electrical conductivity.
- Showed electrochemical performance comparable to conventional aluminum-foil current collectors.
- Achieved stable charge/discharge capacity and >91% coulombic efficiency under both flat and bent states.
- Improved electrode yield and adhesion by nano-metal coating on graphite paper.

## Relevance to Humanoid Robotics

Humanoid robots require energy storage that can be distributed around joints, torsos, and limbs without becoming the dominant structural load. A sub-250 μm, flexible lithium-ion cell can conform to curved surfaces and survive repeated bending, making it a candidate for embedded power in soft actuators, wearable human-robot interfaces, and compact limb segments. The graphite-paper current collector also reduces mass compared with conventional metal foils, which is valuable for mobile robots with strict payload budgets. Because the design uses established electrode chemistries (LiFePO4/Li4Ti5O12) and a thin-film coating process, it could be integrated into humanoid power systems as a manufacturable component once scalability and cycle life are confirmed.
