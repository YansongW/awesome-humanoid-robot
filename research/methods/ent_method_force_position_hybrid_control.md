---
$id: ent_method_force_position_hybrid_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Force/Position Hybrid Control
  zh: 力位混合控制
  ko: 힘/위치 하이브리드 제어
summary:
  en: A control strategy that simultaneously regulates force along constrained directions and position along free directions
    in contact tasks.
  zh: 在接触任务中同时约束方向上控制力、自由方向上控制位置的策略。
  ko: 접촉 작업에서 제약 방향으로는 힘을, 자유 방향으로는 위치를 동시에 제어하는 전략.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
tags:
- method
- chapter_14
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#混合力/位置控制 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
力位混合控制是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
在许多任务中，某些方向需要控制位置，而另一些方向需要控制力。例如，沿桌面推动物体时，水平方向控制位置，垂直方向控制接触力。**混合力/位置控制（hybrid force/position control）**通过选择矩阵 \(\boldsymbol{\Sigma}\) 把任务空间分解为位置控制子空间与力控制子空间：

$$
\boldsymbol{\Sigma} = \text{diag}(\sigma_1, \ldots, \sigma_m), \quad \sigma_i \in \{0,1\}
$$

- 若 \(\sigma_i = 1\)，第 \(i\) 个方向控制位置。
- 若 \(\sigma_i = 0\)，第 \(i\) 个方向控制力。

!!! note "术语解释：混合力/位置控制、选择矩阵、位置控制子空间、力控制子空间"
    - **混合力/位置控制（hybrid force/position control）**：同时控制力和位置的策略。
    - **选择矩阵（selection matrix）**：选择位置控制方向或力控制方向的对角矩阵。
    - **位置控制子空间（position-controlled subspace）**：由选择矩阵选中的位置控制方向。
    - **力控制子空间（force-controlled subspace）**：未被选择矩阵选中的力控制方向。

假设任务空间误差为 \(\mathbf{e} = \mathbf{x}_d - \mathbf{x}\)，力误差为 \(\mathbf{e}_F = \mathbf{F}_d - \mathbf{F}\)，则控制律为：

$$
\mathbf{F}_{\text{cmd}} = \boldsymbol{\Sigma} \, \mathbf{K}_p (\mathbf{x}_d - \mathbf{x}) + (\mathbf{I} - \boldsymbol{\Sigma}) \, \mathbf{K}_f (\mathbf{F}_d - \mathbf{F})
$$

再通过 \(\boldsymbol{\tau} = \mathbf{J}^T \mathbf{F}_{\text{cmd}}\) 映射到关节力矩。这种控制在工业装配（如插轴入孔）中广泛应用。

!!! note "术语解释：位置误差、力误差、比例增益、控制律"
    - **位置误差（position error）**：期望位置与实际位置之差。
    - **力误差（force error）**：期望力与实际力之差。
    - **比例增益（proportional gain）**：控制器中误差的比例系数。
    - **控制律（control law）**：决定控制输出的数学表达式。

```mermaid
flowchart TD
    A["任务空间"] --> B["选择矩阵 Sigma"]
    B --> C["位置控制子空间"]
    B --> D["力控制子空间"]
    C --> E["位置反馈 Kp e_x"]
    D --> F["力反馈 Kf e_F"]
    E --> G["合成任务力 F_cmd"]
    F --> G
    G --> H["tau = J^T F_cmd"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-08.md#混合力/位置控制

