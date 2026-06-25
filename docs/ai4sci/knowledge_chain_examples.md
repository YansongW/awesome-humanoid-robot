# 知识链路示例：从系统实现到基础理论（细粒度版）

> **Purpose**: 用 3 条具体链路展示人形机器人知识谱系如何从系统实现（system）一路下钻到基础学科（foundation）。  
> 每个节点都是潜在实体，每条边都是潜在关系。  
> 这一版把“QP → KKT → 拉格朗日乘子”这类大步骤拆成了“方法 → 具体形式化 → 方程 → 数学对象/算子 → 定理/原理 → 基础学科”的更细层级。

---

## 粒度设计原则

一条“足够细”的知识链路应该满足：

1. **每一层只跨一个理论深度台阶**，不要从 `method` 直接跳到 `foundation`。
2. **方程（equation）要单独成节点**，而不是藏在 `formalism` 的说明里。
3. **算子/数学对象（operator / variable / constant）要单独成节点**，例如 gradient、Hessian、Jacobian、Wiener process。
4. **求解/近似算法（algorithm / approximation）要单独成节点**，例如 active-set、interior-point、DDPM sampler。
5. **每个基础学科节点都要说明它为上层的哪个具体结构提供“土壤”**。

---

## 链路 1：全身控制（Whole-Body Control）

### 1.1 高层方法到具体实现

```
Whole-Body Control (concept/method)
  ├─ instantiates ─► Hierarchical QP WBC (method)
  │     ├─ builds_on ─► Paper: de Lasa et al. 2010 (paper)
  │     ├─ builds_on ─► Paper: Herzog et al. 2016 (paper)
  │     └─ builds_on ─► Paper: Kim et al. 2019, MIT Cheetah (paper)
  ├─ instantiates ─► Passivity-based WBC (method)
  └─ instantiates ─► Centroidal Momentum Control (method)
        └─ builds_on ─► Paper: Orin et al. 2013 (paper)
```

### 1.2 Hierarchical QP WBC 的数学下钻

```
Hierarchical QP WBC (method)
  └─ formalizes ─► Inverse-dynamics QP formulation (formalism)
        ├─ uses ─► generalized accelerations q̈ (variable)
        ├─ uses ─► contact forces λ (variable)
        ├─ uses ─► joint torques τ (variable)
        ├─ includes ─► Objective function (formalism)
        │     └─ includes ─► ½ ‖A_task q̈ − a_desired‖² + regularization (equation)
        │           ├─ uses ─► Least squares (method)
        │           └─ uses ─► Quadratic form q̈ᵀ H q̈ (equation)
        │                 └─ uses ─► Positive semidefinite matrix (concept)
        │                       └─ derived_from ─► Spectral theorem (theorem)
        │                             └─ has_prerequisite ─► Linear algebra (foundation)
        ├─ includes ─► Equality constraints (formalism)
        │     └─ includes ─► Floating-base dynamics: M(q)q̈ + C(q,q̇)q̇ + g(q) = Sᵀτ + J_cᵀλ (equation)
        │           ├─ uses ─► Mass matrix M(q) (operator)
        │           ├─ uses ─► Coriolis/centrifugal matrix C(q,q̇) (operator)
        │           ├─ uses ─► Selection matrix S (operator)
        │           ├─ uses ─► Contact Jacobian J_c (operator)
        │           └─ derived_from ─► Newton-Euler equations (equation)
        │                 ├─ derived_from ─► Newton's second law (principle)
        │                 ├─ derived_from ─► Euler's rotation equations (principle)
        │                 └─ has_prerequisite ─► Classical mechanics (foundation)
        ├─ includes ─► Inequality constraints (formalism)
        │     ├─ includes ─► Torque limits: τ_min ≤ τ ≤ τ_max (equation)
        │     ├─ includes ─► Joint limits: q_min ≤ q ≤ q_max (equation)
        │     └─ includes ─► Friction cone: λ_t ≤ μ λ_n (equation)
        │           └─ derived_from ─► Coulomb friction model (principle)
        │                 └─ has_prerequisite ─► Solid mechanics / Physics (foundation)
        └─ requires ─► Task-space Jacobian J (operator)
              └─ has_prerequisite ─► Differential geometry / Linear algebra (foundation)
```

### 1.3 从 QP 到优化理论

```
Inverse-dynamics QP formulation (formalism)
  └─ formalizes ─► Standard QP (formalism)
        ├─ includes ─► min_x ½ xᵀ H x + gᵀ x, s.t. A x = b, C x ≤ d (equation)
        ├─ solved_by ─► Active-set method (algorithm)
        │     ├─ has_prerequisite ─► KKT conditions (theorem)
        │     └─ uses ─► Linear system solver: LU / Cholesky / QR (algorithm)
        │           └─ has_prerequisite ─► Linear algebra (foundation)
        └─ solved_by ─► Interior-point method (algorithm)
              └─ has_prerequisite ─► Barrier function (formalism)
                    └─ has_prerequisite ─► Convex analysis (foundation)

KKT conditions (theorem)
  ├─ derived_from ─► Lagrangian L(x, ν, μ) (formalism)
  │     ├─ includes ─► L = f(x) + νᵀ(Ax−b) + μᵀ(Cx−d) (equation)
  │     ├─ uses ─► Lagrange multipliers ν, μ (concept/variable)
  │     │     └─ has_prerequisite ─► Multivariable calculus (foundation)
  │     └─ uses ─► Gradient ∇f(x) (operator)
  │           └─ has_prerequisite ─► Multivariable calculus (foundation)
  ├─ includes ─► Stationarity: ∇f(x) + Aᵀν + Cᵀμ = 0 (equation)
  ├─ includes ─► Primal feasibility: A x = b, C x ≤ d (equation)
  ├─ includes ─► Dual feasibility: μ ≥ 0 (equation)
  ├─ includes ─► Complementary slackness: μᵀ(Cx−d) = 0 (equation)
  └─ requires ─► Constraint qualification (concept)
        ├─ instantiates ─► LICQ (concept)
        └─ instantiates ─► Slater's condition (concept)
              └─ has_prerequisite ─► Convex analysis (foundation)
```

### 1.4 这条链路的启示

- 想读懂一篇 WBC 论文，不能只停在“用了 QP”；要看到决策变量、目标函数、等式/不等式约束分别怎么写。
- 每个约束背后都有物理/数学原理：动力学约束来自牛顿-欧拉，摩擦约束来自库仑摩擦。
- 求解 QP 时，active-set / interior-point 的选择会影响实时性；这又回到了数值线性代数。

---

## 链路 2：锂电池（Li-ion Battery）

### 2.1 系统到材料

```
Li-ion battery pack (system)
  ├─ is_part_of ─► Battery module (system)
  │     └─ is_part_of ─► Battery cell (system)
  │           ├─ consumes ─► Cathode active material NMC811 (material)
  │           ├─ consumes ─► Anode graphite (material)
  │           ├─ consumes ─► Electrolyte: LiPF6 in EC/DMC (material)
  │           └─ requires ─► Separator (component)
  └─ integrates ─► Battery Management System (BMS) (system)
```

### 2.2 正极材料的化学下钻

```
Cathode active material NMC811 (material)
  └─ has ─► Crystal structure: layered α-NaFeO₂-type (formalism)
        ├─ is_based_on ─► Transition metal oxide lattice (concept)
        └─ enables ─► Li⁺ intercalation / deintercalation (process)
              └─ formalizes ─► Intercalation reaction (equation)
                    └─ includes ─► Li_{1−x}MO₂ + x Li⁺ + x e⁻ ⇌ LiMO₂ (equation)
                          ├─ uses ─► Faraday constant F (constant)
                          ├─ uses ─► Charge number n (variable)
                          └─ derived_from ─► Faraday's laws of electrolysis (principle)
                                └─ has_prerequisite ─► Electrochemistry (foundation)
```

### 2.3 电极动力学到物理化学

```
Charge transfer at electrode-electrolyte interface (process)
  └─ formalizes ─► Butler-Volmer equation (equation)
        ├─ includes ─► j = j₀ [ exp(αₐ nFη / RT) − exp(−α_c nFη / RT) ] (equation)
        ├─ uses ─► Exchange current density j₀ (variable)
        │     └─ derived_from ─► Transition state theory (principle)
        │           └─ has_prerequisite ─► Statistical mechanics / Physical chemistry (foundation)
        ├─ uses ─► Activation overpotential η (variable)
        ├─ uses ─► Charge transfer coefficients αₐ, α_c (variable)
        ├─ uses ─► Faraday constant F (constant)
        ├─ uses ─► Gas constant R (constant)
        ├─ uses ─► Temperature T (variable)
        └─ has_prerequisite ─► Electrochemical kinetics (foundation)

Mass transport in electrolyte (process)
  ├─ formalizes ─► Nernst-Planck equation (equation)
  │     ├─ includes ─► ∂c_i/∂t = −∇·J_i + R_i (equation)
  │     └─ includes ─► J_i = −D_i∇c_i − (z_i u_i F c_i / RT)∇φ + c_i v (equation)
  │           └─ has_prerequisite ─► Physical chemistry / Transport phenomena (foundation)
  └─ approximates ─► Fick's laws of diffusion (principle)
        └─ includes ─► J = −D ∇c (equation)
              └─ has_prerequisite ─► Partial differential equations (foundation)

Solid-state diffusion in cathode particle (process)
  └─ formalizes ─► Fick's second law in spherical coordinates (equation)
        ├─ includes ─► ∂c_s/∂t = D_s (1/r²) ∂/∂r(r² ∂c_s/∂r) (equation)
        ├─ uses ─► Laplacian operator in spherical coordinates (operator)
        └─ solved_by ─► Separation of variables / Eigenfunction expansion (algorithm)
              └─ has_prerequisite ─► Differential equations / Linear algebra (foundation)
```

### 2.4 BMS 状态估计的下钻

```
Battery Management System (BMS) (system)
  └─ requires ─► State-of-Charge (SOC) estimation (method)
        ├─ instantiates ─► Extended Kalman Filter (EKF) (algorithm)
        │     ├─ is_based_on ─► Kalman filter (algorithm)
        │     │     └─ formalizes ─► Bayesian filtering (formalism)
        │     │           ├─ includes ─► p(x_t | y_{1:t−1}) = ∫ p(x_t | x_{t−1}) p(x_{t−1} | y_{1:t−1}) dx_{t−1} (equation)
        │     │           ├─ includes ─► p(x_t | y_{1:t}) ∝ p(y_t | x_t) p(x_t | y_{1:t−1}) (equation)
        │     │           └─ has_prerequisite ─► Probability & statistics (foundation)
        │     └─ approximates ─► Linearization via Jacobian (approximation)
        │           └─ has_prerequisite ─► Multivariable calculus (foundation)
        └─ is_based_on ─► Equivalent circuit model (ECM) (formalism)
              └─ includes ─► V_t = OCV(SOC) − I R_0 − V_RC (equation)
                    └─ has_prerequisite ─► Circuit theory / Linear systems (foundation)
```

### 2.5 热管理下钻

```
Battery thermal management (system)
  └─ requires ─► Heat generation model (formalism)
        └─ includes ─► Q̇_gen = I(V − OCV) + I T ∂OCV/∂T (Bernardi equation) (equation)
              └─ derived_from ─► Energy balance (principle)
                    └─ has_prerequisite ─► Thermodynamics (foundation)
```

### 2.6 这条链路的启示

- 电池不是“材料 + BMS”两层，而是材料 → 晶体结构 → 反应 → 电极动力学 → 传输现象 → PDE/数值方法。
- 一个电池参数（如交换电流密度 j₀）背后可以追溯到过渡态理论和统计力学。
- BMS 里的 EKF 线性化误差会直接影响 SOC 精度，这背后是贝叶斯推断和微积分。

---

## 链路 3：视觉-语言-动作模型（VLA）

### 3.1 系统到动作生成模块

```
VLA foundation model (system/method)
  ├─ instantiates ─► GR00T N1 (technology)
  ├─ instantiates ─► OpenVLA (technology)
  ├─ instantiates ─► π0 (technology)
  └─ includes ─► Action generation module (method)
        ├─ instantiates ─► Diffusion policy (method)
        ├─ instantiates ─► Flow matching policy (method)
        └─ instantiates ─► ACT / VQ-VAE action chunking (method)
```

### 3.2 扩散策略的下钻

```
Diffusion policy (method)
  └─ formalizes ─► Score-based generative model (formalism)
        ├─ includes ─► s_θ(x, t) ≈ ∇_x log p_t(x) (equation)
        │     ├─ uses ─► Score function ∇_x log p_t(x) (operator)
        │     └─ estimates ─► Denoising score matching (algorithm)
        │           └─ includes ─► E_{t,x₀,ε} [ ‖s_θ(x_t,t) − ∇_{x_t} log p(x_t | x₀)‖² ] (equation)
        │                 ├─ uses ─► Forward diffusion kernel p(x_t | x₀) (formalism)
        │                 └─ has_prerequisite ─► Probability & statistics (foundation)
        └─ instantiates ─► DDPM reverse process (algorithm)
              ├─ includes ─► dx = [f(x,t) − g(t)² ∇_x log p_t(x)] dt + g(t) dw (equation)
              ├─ uses ─► Drift function f(x,t) (variable/operator)
              ├─ uses ─► Diffusion coefficient g(t) (variable)
              ├─ uses ─► Wiener process w(t) (operator/variable)
              └─ solved_by ─► Euler-Maruyama sampler (algorithm)
                    └─ has_prerequisite ─► Stochastic calculus / Itô calculus (foundation)
                          └─ has_prerequisite ─► Measure-theoretic probability (foundation)
```

### 3.3 Flow Matching 的下钻

```
Flow matching policy (method)
  └─ formalizes ─► Probability flow ODE (formalism)
        ├─ includes ─► dx/dt = v_t(x) (equation)
        │     ├─ uses ─► Vector field v_t(x) (operator/variable)
        │     └─ derived_from ─► Continuity equation (equation)
        │           ├─ includes ─► ∂p_t/∂t + ∇·(p_t v_t) = 0 (equation)
        │           ├─ uses ─► Divergence operator ∇· (operator)
        │           └─ has_prerequisite ─► Partial differential equations (foundation)
        └─ solved_by ─► ODE solver: Euler / Runge-Kutta (algorithm)
              └─ has_prerequisite ─► Numerical analysis (foundation)
```

### 3.4 Transformer 骨干的下钻

```
Transformer architecture (method)
  └─ formalizes ─► Self-attention mechanism (formalism)
        └─ includes ─► Attention(Q,K,V) = softmax(QKᵀ / √d_k) V (equation)
              ├─ uses ─► Query Q, Key K, Value V matrices (variable)
              ├─ uses ─► Matrix multiplication QKᵀ (operator)
              ├─ uses ─► Softmax function (operator)
              │     └─ includes ─► softmax(z_i) = exp(z_i) / Σ_j exp(z_j) (equation)
              │           ├─ uses ─► Exponential function exp(·) (operator)
              │           └─ uses ─► Normalization Σ_j exp(z_j) (operator)
              └─ has_prerequisite ─► Linear algebra (foundation)

Vision-language alignment (method)
  └─ is_based_on ─► Contrastive learning (method)
        └─ formalizes ─► InfoNCE loss (formalism)
              └─ includes ─► L = − E[ log( exp(sim(x_i,y_i)/τ) / Σ_j exp(sim(x_i,y_j)/τ) ) ] (equation)
                    ├─ uses ─► Similarity function sim(·,·) (operator)
                    ├─ uses ─► Temperature parameter τ (variable)
                    └─ has_prerequisite ─► Information theory (foundation)
                          └─ has_prerequisite ─► Probability & statistics (foundation)
```

### 3.5 训练与优化的下钻

```
VLA training (process)
  └─ uses ─► Behavior cloning objective (formalism)
        ├─ includes ─► L_BC = E[ ‖π_θ(s) − a‖² ] (equation, continuous actions)
        ├─ includes ─► L_CE = − Σ_t log π_θ(a_t | s_t) (equation, discrete tokenized actions)
        └─ minimized_by ─► Gradient descent (algorithm)
              ├─ uses ─► Backpropagation (algorithm)
              │     └─ uses ─► Chain rule (theorem)
              │           └─ has_prerequisite ─► Multivariable calculus (foundation)
              └─ requires ─► Automatic differentiation (algorithm)
                    └─ has_prerequisite ─► Computational graphs / Compiler theory (foundation)
```

### 3.6 这条链路的启示

- VLA 不是“Transformer + 扩散”一句话能说清的。训练目标、动作表示（连续/离散/扩散）、推理采样器、数值稳定性都需要分开建模。
- 扩散策略的 reverse SDE 中，score 函数是核心；要理解它为什么能工作，需要回到随机分析和测度论。
- 自动微分让深度学习工程化，但背后的链式法则是微积分。

---

## 实体类型在这些链路中的用法

| 类型 | 示例 | 作用 |
|------|------|------|
| `concept` | WBC、constraint qualification、decision variable | 高层概念或问题 framing |
| `method` | Hierarchical QP WBC、Diffusion policy、Contrastive learning | 算法或技术路线 |
| `formalism` | QP formulation、Butler-Volmer、Score-based model | 数学/物理形式化 |
| `equation` | KKT stationarity、Self-attention、Reverse SDE | 具体公式 |
| `operator` | Gradient、Jacobian、Divergence、Softmax | 数学算子或变换 |
| `variable` | q̈、λ、η、τ、w(t) | 公式中的变量 |
| `constant` | F、R、d_k | 公式中的常数/超参数 |
| `algorithm` | Active-set method、DDPM sampler、Backpropagation | 求解或训练算法 |
| `approximation` | Linearization via Jacobian、Fick's laws vs Nernst-Planck | 近似方法 |
| `theorem` / `principle` | KKT conditions、Newton's second law、Chain rule | 定理或原理 |
| `foundation` | Linear algebra、Thermodynamics、Probability | 基础学科 |
| `paper` / `technology` | de Lasa 2010、GR00T N1、π0 | 具体论文或产品 |

---

## 关系类型在这些链路中的用法

| 关系 | 示例 | 语义 |
|------|------|------|
| `formalizes` | WBC formalizes QP | 方法形式化为数学对象 |
| `includes` | QP includes objective equation | 父对象包含子对象 |
| `uses` | Equation uses operator / variable | 使用某个数学对象 |
| `derived_from` | KKT derived from Lagrangian | 推导来源 |
| `has_prerequisite` | Convex analysis → Linear algebra | 知识前置 |
| `solved_by` | QP solved by active-set | 问题由算法求解 |
| `estimates` | Score matching estimates score function | 算法估计某个量 |
| `minimized_by` | Objective minimized by gradient descent | 目标由算法最小化 |
| `approximates` | Fick's laws approximate Nernst-Planck | 近似关系 |
| `instantiates` | EKF instantiates Kalman filter | 具体实例 |
| `builds_on` | Hierarchical QP builds on de Lasa 2010 | 继承/基于 prior work |
| `requires` / `enables` / `is_based_on` | 已有通用关系 | — |

---

## 这些链路对工作流的启示

1. **一条工作流只能覆盖一个深度层**：研究 Butler-Volmer 方程需要电化学工作流；研究其离散求解需要 PDE 数值方法工作流。
2. **同一基础学科会被多棵树共享**：Linear algebra 同时是 WBC、VLA、SLAM、经济学的根系。
3. **方程和算子应该被显式抽提**：文献阅读 Agent 不应该只总结“用了 QP”，而要抽出 QP 的具体形式、H 矩阵的含义、约束的来源。
4. **跨域关系天然存在**：电池热管理的 Bernardi 方程和热力学是电池树的根，但热传导 PDE 也可能用于电机散热树。

---

## 下一步建议

- 从链路 1 开始，真正创建一批实体文件（如 `ent_wbc_hierarchical_qp.md`、`ent_kkt_conditions.md`、`ent_newton_euler.md`）。
- 创建对应的基础学科工作流 YAML：`convex_optimization.yaml`、`rigid_body_dynamics.yaml`、`electrochemistry.yaml`、`stochastic_calculus.yaml`。
- 在 `WORKSTREAM_TREE.md` 中把这些节点标记为 `[x]`，并标注它们支撑哪些工程领域。
