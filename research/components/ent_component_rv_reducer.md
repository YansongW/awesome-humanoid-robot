---
$id: ent_component_rv_reducer
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: RV Reducer
  zh: RV减速器
  ko: RV 감속기
summary:
  en: A high-rigidity, high-torque cycloidal reducer widely used in heavy-load robot joints, especially hips and waists, due
    to its excellent shock resistance and positioning accuracy.
  zh: '核心内容 ### RV减速器的定义与定位 RV减速器属于 **component** 类型。 所属领域包括：02_components。 价值链层级：midstream。 一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。
    英文名称为 *RV Reducer*。 韩文名称为 *RV 감속기*。'
  ko: 고강성·고토크 사이클로이드 감속기로, 충격 저항성과 위치 정밀도가 우수하여 중하량 로봇 관절에 널리 사용됨.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- component
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.3.3 行星减速器与摆线减速器 by scripts/backfill_nonpaper_entries.py. Body backfilled from
    entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。

## 核心内容
### RV减速器的定义与定位
RV减速器属于 **component** 类型。 所属领域包括：02_components。 价值链层级：midstream。 一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。 英文名称为 *RV Reducer*。 韩文名称为 *RV 감속기*。

### RV减速器的工作原理与技术架构
RV减速器的核心机制决定了其在人形机器人系统中的性能边界。理解其内部结构、信号流与控制接口，有助于进行系统集成与优化。
在选型与集成过程中，需要关注其与控制器、通信总线、电源系统与机械结构的兼容性。

### 关键参数与选型要点
在工程实践中，选用RV减速器需要综合考虑性能指标、可靠性、成本、供应链成熟度以及与整机系统的兼容性。
关键参数通常包括精度、带宽、扭矩、功耗、重量、接口协议与环境适应性等。
针对不同应用场景，可能需要在性能与成本之间进行权衡，并预留适当的冗余与安全裕量。

### 典型应用与发展趋势
RV减速器已广泛应用于人形机器人的原型验证、学术研究与早期商业化产品中。
未来随着产业链成熟，其集成度、智能化水平与成本效益有望持续提升。

### 相关标签
- component
- chapter_4
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键component之一，RV减速器在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction


