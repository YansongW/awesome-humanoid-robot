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
  zh: 一种高刚性、高扭矩的摆线针轮减速器，抗冲击性与定位精度优异，常用于重载机器人臀、腰等关节。
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
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
### 4.3.3 行星减速器与摆线减速器

**行星减速器**由太阳轮、行星轮、齿圈和行星架组成。太阳轮输入，行星架输出，齿圈固定时传动比为

$$
G = 1 + \frac{z_r}{z_s}
$$

其中 \(z_r\) 为齿圈齿数，\(z_s\) 为太阳轮齿数。行星减速器效率高（可达 97%）、承载能力强，常用于机器人关节的中低减速比段。
