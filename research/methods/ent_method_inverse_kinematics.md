---
$id: ent_method_inverse_kinematics
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Inverse Kinematics
  zh: 逆运动学
  ko: 역욕동학
summary:
  en: The computation of joint angles that realize a desired end-effector pose, often solved numerically via Jacobian pseudoinverse
    or analytically for simple geometries.
  zh: 根据期望的末端执行器位姿反求关节角，常用Jacobian伪逆数值求解或简单几何解析求解。
  ko: 원하는 말단 동작기 자세를 실현하는 관절 각도를 계산하는 방법; Jacobian 의역수나 단순 기하 해석법을 사용.
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
### 8.3.9 Python 算例 4：Jacobian 伪逆数值逆运动学

以下代码展示 3 连杆平面机械臂的数值 IK：给定目标位置，通过 Jacobian 伪逆迭代调整关节角，使末端接近目标。

```python
import numpy as np
