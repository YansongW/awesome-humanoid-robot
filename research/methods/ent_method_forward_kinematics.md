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
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-09.md#9.2.2 运动学建模：简化腿的正运动学 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
正运动学是人形机器人领域的重要method。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
为便于分析下肢工作空间，常将单腿简化为 3-DOF 髋（roll/pitch/yaw）+ 1-DOF 膝 + 2-DOF 踝（pitch/roll）的串链。通过改进型 DH 参数或旋量法建立正运动学，可计算机足相对髋的位置。

!!! note "术语解释：正运动学、DH 参数、改进型 DH、旋量、齐次变换"
    - **正运动学（forward kinematics）**：由关节角计算末端位姿的映射。
    - **DH 参数（Denavit-Hartenberg parameters）**：用四个参数（a, α, d, θ）描述相邻连杆坐标系关系。
    - **改进型 DH（modified DH, MDH）**：将连杆长度 α 与扭角 α 定义在前一关节处，避免相邻平行轴奇异。
    - **旋量（screw）**：描述刚体绕轴旋转并沿轴平移的几何量。
    - **齐次变换（homogeneous transformation）**：4×4 矩阵，同时描述旋转与平移。

对于平面简化腿（髋 pitch θ₁、膝 θ₂、踝 pitch θ₃），足端位置可写为：

$$
\begin{aligned}
x &= l_1 \sin\theta_1 + l_2 \sin(\theta_1+\theta_2) + l_3 \sin(\theta_1+\theta_2+\theta_3) \\
z &= -l_1 \cos\theta_1 - l_2 \cos(\theta_1+\theta_2) - l_3 \cos(\theta_1+\theta_2+\theta_3)
\end{aligned}
$$

其中 \(l_1, l_2, l_3\) 分别为大腿、小腿与足长，z 轴向上为正。

```mermaid
flowchart TD
    A["髋关节 θ₁"] --> B["大腿 l₁"]
    B --> C["膝关节 θ₂"]
    C --> D["小腿 l₂"]
    D --> E["踝关节 θ₃"]
    E --> F["足 l₃"]
    F --> G["足端位置 (x, z)"]
```

## 参考
- Wiki extraction
- 项目 Wiki：chapter-09.md#9.2.2 运动学建模：简化腿的正运动学

