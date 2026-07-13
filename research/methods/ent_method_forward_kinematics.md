---
$id: ent_method_forward_kinematics
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Forward Kinematics
  zh: 正运动学
  ko: 정욕동학
summary:
  en: The computation of end-effector position and orientation from given joint angles, using a chain of homogeneous transformations
    or product-of-exponentials.
  zh: 根据给定关节角，通过齐次变换链或指数积计算末端执行器位姿的方法。
  ko: 주어진 관절 각도로부터 동차 변환 사슬 또는 지수곱을 이용해 말단 동작기 위치·방향을 계산하는 방법.
domains:
- 06_design_engineering
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_8
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
### 8.3.3 正运动学：从关节空间到操作空间

**正运动学（forward kinematics）**解决：给定关节角 $\mathbf{q}$，计算末端执行器在基坐标系中的位姿。通过连乘各连杆变换矩阵得到：

$$
{}^0\mathbf{T}_n(\mathbf{q}) = {}^0\mathbf{T}_1(q_1) \cdot {}^1\mathbf{T}_2(q_2) \cdots {}^{n-1}\mathbf{T}_n(q_n)
$$

末端位姿由 ${}^0\mathbf{T}_n$ 的旋转部分 $\mathbf{R}$ 和平移部分 $\mathbf{p}$ 给出。

!!! note "术语解释：正运动学、关节空间、操作空间、末端执行器"
    - **正运动学（forward kinematics）**：由关节变量计算末端位姿的映射。
    - **关节空间（joint space）**：以关节变量为坐标的空间。
    - **操作空间（task/operational space）**：以末端位姿为坐标的空间。
    - **末端执行器（end-effector）**：机器人与环境交互的末端装置。

```mermaid
flowchart LR
    A["关节角 q1..qn"] -->|"DH 变换连乘"| B["0Tn"]
    B --> C["末端位置 p"]
    B --> D["末端姿态 R"]
```
