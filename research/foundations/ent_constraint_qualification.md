---
$id: ent_constraint_qualification
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: concept
names:
  en: Constraint qualification
  zh: 约束规范
  ko: 제약 자격
summary:
  en: A regularity condition on the constraints of an optimization problem that guarantees the validity of the Karush-Kuhn-Tucker
    necessary optimality conditions at a local optimum.
  zh: 概述 优化问题约束的一种正则性条件，保证在局部最优处 Karush-Kuhn-Tucker 最优性必要条件的有效性。
  ko: 최적화 문제의 제약에 대한 정칙성 조건으로, 국부 최적해에서 Karush-Kuhn-Tucker 필요 최적성 조건의 타당성을 보장합니다.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- foundation
tags:
- optimization
- constrained_optimization
- regularity
- licq
- slater
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_nocedal_wright_2006
  type: other
  title: J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
  url: https://doi.org/10.1007/978-0-387-40065-5
  date: '2006-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_active_set_method
  relationship: is_prerequisite_for
  description:
    en: Active-set methods exploit the set of active constraints whose gradients must satisfy a constraint qualification for
      reliable iteration.
    zh: 起作用集方法利用起作用约束集合，其梯度需满足约束规范以保证迭代可靠。
    ko: 활성 집합법은 기울기가 제약 자격을 만족해야 신뢰할 수 있는 반복이 가능한 활성 제약 집합을 활용합니다.
- id: ent_interior_point_method
  relationship: is_prerequisite_for
  description:
    en: Interior-point methods maintain strict inequality feasibility and therefore rely implicitly on constraint qualifications
      to guarantee convergence to KKT points.
    zh: 内点法保持严格不等式可行性，因此隐式依赖约束规范以保证收敛到 KKT 点。
    ko: 내점법은 엄격한 부등식 실행 가능성을 유지하므로 KKT 점으로의 수렴을 보장하기 위해 제약 자격에 암묵적으로 의존합니다.
---

## 概述
优化问题约束的一种正则性条件，保证在局部最优处 Karush-Kuhn-Tucker 最优性必要条件的有效性。

## 核心内容
### 约束规范的定义与定位
约束规范属于 **概念** 类型。 所属领域包括：基础学科。 价值链层级：基础层。 优化问题约束的一种正则性条件，保证在局部最优处 Karush-Kuhn-Tucker 最优性必要条件的有效性。 英文名称为 *Constraint qualification*。 韩文名称为 *제약 자격*。

### 约束规范的关键维度
理解约束规范需要从定义、边界条件、相关实体以及典型应用场景等多个维度展开，以形成系统性的认知。
该实体在人形机器人知识图谱中起到连接基础理论与工程实践的桥梁作用。

### 实践意义
在人形机器人产业化的背景下，约束规范对于技术研究、产品开发、投资决策与生态建设均具有参考价值。
准确把握其内涵与外延，有助于避免概念混淆并推动跨学科协作。

### 研究与发展方向
随着人形机器人技术不断演进，约束规范的相关理论与实践也将持续更新，需要保持跟踪与审校。

### 相关标签
- optimization
- constrained_optimization
- regularity
- licq
- slater

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键概念之一，约束规范在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006](https://doi.org/10.1007/978-0-387-40065-5)


