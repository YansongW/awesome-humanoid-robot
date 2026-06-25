# 知识链路示例：从基础理论到系统实现

> **Purpose**: 用 3 条具体链路展示人形机器人知识谱系如何从底层基础学科（foundation）生长到系统实现（system）。  
> 每条链路中的节点都是潜在实体，节点之间的边都是潜在关系。

---

## 链路 1：全身控制（Whole-Body Control）

```
WBC (concept/method)
  ├─ formalizes ─► QP formulation (formalism)
  │     ├─ derived_from ─► KKT conditions (theorem/principle)
  │     │     ├─ derived_from ─► Lagrange multipliers (foundation)
  │     │     │     └─ has_prerequisite ─► Multivariable calculus (foundation)
  │     │     └─ has_prerequisite ─► Linear algebra (foundation)
  │     └─ has_prerequisite ─► Convex optimization (foundation)
  ├─ requires ─► Floating-base dynamics (formalism/principle)
  │     └─ derived_from ─► Newton-Euler equations (principle)
  │           └─ has_prerequisite ─► Classical mechanics (foundation)
  ├─ requires ─► Joint torque/force sensors (component/system)
  └─ instantiates ─► Paper: "Whole-Body Control for Humanoids" (paper/method)
```

**说明**：
- 从“全身控制”这一高层方法出发，下钻到 QP 优化形式；
- QP 的求解依赖 KKT 条件，KKT 条件又依赖拉格朗日乘子；
- 拉格朗日乘子背后是多变量微积分与线性代数；
- 同时，WBC 还需要浮动基动力学，其根基是牛顿-欧拉方程与经典力学。

---

## 链路 2：锂电池（Li-ion Battery）

```
Li-ion battery pack (component/system)
  ├─ is_part_of ─► Battery management system (BMS) (component/system)
  │     └─ requires ─► State estimation algorithms (method)
  │           └─ formalizes ─► Kalman filter (formalism/method)
  │                 └─ has_prerequisite ─► Probability & statistics (foundation)
  ├─ consumes ─► Cathode material (material)
  │     └─ derived_from ─► Layered oxide chemistry (principle)
  │           └─ has_prerequisite ─► Electrochemistry (foundation)
  ├─ consumes ─► Electrolyte (material)
  │     └─ derived_from ─► Ion transport theory (principle)
  │           └─ has_prerequisite ─► Physical chemistry (foundation)
  └─ enables ─► Tesla Optimus / Unitree G1 runtime (system)
```

**说明**：
- 电池包是系统实现；
- BMS 中的状态估计用卡尔曼滤波，其理论基础是概率统计；
- 电池材料（正极、电解液）背后是电化学与物理化学；
- 最终，电池系统支撑整机续航。

---

## 链路 3：视觉-语言-动作模型（VLA）

```
VLA foundation model (method/system)
  ├─ is_based_on ─► Transformer architecture (method)
  │     ├─ formalizes ─► Self-attention mechanism (formalism)
  │     │     └─ has_prerequisite ─► Linear algebra (foundation)
  │     └─ has_prerequisite ─► Probability & statistics (foundation)
  ├─ is_based_on ─► Diffusion / flow matching (method)
  │     ├─ formalizes ─► Stochastic differential equations (formalism)
  │     │     └─ has_prerequisite ─► Differential equations (foundation)
  │     └─ has_prerequisite ─► Probability & statistics (foundation)
  ├─ requires ─► Edge AI compute (component/system)
  │     └─ enables ─► On-device inference (system)
  ├─ consumes ─► Vision-language pre-training data (dataset)
  │     └─ is_based_on ─► Contrastive learning (method)
  │           └─ has_prerequisite ─► Information theory (foundation)
  └─ instantiates ─► GR00T N1 / OpenVLA / π0 (paper/technology)
```

**说明**：
- VLA 作为系统/方法，建立在 Transformer、扩散模型、对比学习等多种方法之上；
- 这些方法的形式化工具包括自注意力、随机微分方程、信息论；
- 底层根基是线性代数、概率统计、微分方程；
- 同时，VLA 的运行依赖边缘 AI 计算硬件。

---

## 这些链路对工作流的启示

1. **每个上层工作流都会触发基础学科工作流**：研究 WBC 时，必然需要补充凸优化、动力学；研究电池时，必然需要电化学。
2. **基础学科工作流是跨领域的**：线性代数同时支撑控制、AI、视觉 SLAM、经济学模型。
3. **关系类型需要支持“下钻”**：`formalizes`、`derived_from`、`uses_theorem`、`has_prerequisite` 让知识树可以从叶子反向追溯到根系。

---

## 下一步建议

- 为每条链路创建实体草稿（可以先从 WBC 链路开始）。
- 创建对应的基础学科工作流 YAML（如 `convex_optimization.yaml`、`rigid_body_dynamics.yaml`）。
- 在 `WORKSTREAM_TREE.md` 中标记这些基础学科工作流为 `[x]` 当它们被创建并执行。
