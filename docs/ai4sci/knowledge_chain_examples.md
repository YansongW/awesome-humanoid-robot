# 知识链路示例：从系统实现到基础理论（细粒度版）

> **Purpose**: 用 3 条具体链路展示人形机器人知识谱系如何从系统实现（system）一路下钻到基础学科（foundation）。  
> 每个节点都是潜在实体，每条边都是潜在关系。  
> 这一版继续把粒度拆细：方法 → 具体形式化 → 方程 → 子方程/算子/变量/常数 → 算法步骤/近似 → 定理/原理 → 基础学科。

---

## 粒度设计原则

一条“足够细”的知识链路应该满足：

1. **每一层只跨一个理论深度台阶**，不要从 `method` 直接跳到 `foundation`。
2. **方程（equation）要单独成节点**，而不是藏在 `formalism` 的说明里。
3. **算子/数学对象（operator / variable / constant）要单独成节点**，例如 gradient、Hessian、Jacobian、Wiener process。
4. **求解/近似算法（algorithm / approximation）要单独成节点**，例如 active-set、interior-point、DDPM sampler。
5. **算法内部的每个关键步骤也要可下钻**：active-set 有哪几步？每步为什么能工作？用到什么线性代数结构？
6. **每个基础学科节点都要说明它为上层的哪个具体结构提供“土壤”**。
7. **每个具体实体的文件开头要有「生活实例 + 自然语言阐述逻辑」**：用日常例子把公式/概念讲清楚。

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
  ├─ includes ─► Stack-of-tasks (concept)
  │     ├─ uses ─► Task Jacobian J_i (operator)
  │     │     ├─ instantiates ─► CoM Jacobian (operator)
  │     │     ├─ instantiates ─► End-effector geometric Jacobian (operator)
  │     │     └─ has_prerequisite ─► Differential geometry / Linear algebra (foundation)
  │     ├─ uses ─► Desired task acceleration a_i (variable)
  │     └─ uses ─► Task weight matrix W_i (variable)
  └─ formalizes ─► Inverse-dynamics QP formulation (formalism)
        ├─ uses ─► generalized accelerations q̈ (variable)
        ├─ uses ─► contact forces λ (variable)
        ├─ uses ─► joint torques τ (variable)
        ├─ includes ─► Objective function (formalism)
        │     └─ includes ─► Weighted task-error objective (equation)
        │           ├─ includes ─► ½ Σ_i ‖J_i q̈ + J̇_i q̇ − a_i‖²_{W_i} + ½ ρ ‖q̈‖² (equation)
        │           ├─ uses ─► Weighted norm ‖x‖²_W = xᵀ W x (operator)
        │           ├─ uses ─► Time derivative of Jacobian J̇_i (operator)
        │           ├─ uses ─► Regularization parameter ρ (constant)
        │           └─ includes ─► Equivalent quadratic form: ½ q̈ᵀ H q̈ + gᵀ q̈ + const (equation)
        │                 ├─ uses ─► Hessian H = Σ_i J_iᵀ W_i J_i + ρ I (operator/variable)
        │                 ├─ uses ─► Gradient g = Σ_i J_iᵀ W_i (J̇_i q̇ − a_i) (operator/variable)
        │                 ├─ derived_from ─► Quadratic form expansion (theorem)
        │                 └─ has_prerequisite ─► Matrix calculus / Linear algebra (foundation)
        ├─ includes ─► Equality constraints (formalism)
        │     └─ includes ─► Floating-base dynamics (equation)
        │           ├─ includes ─► M(q)q̈ + C(q,q̇)q̇ + g(q) = Sᵀτ + J_cᵀλ (equation)
        │           ├─ uses ─► Mass matrix M(q) (operator)
        │           ├─ uses ─► Coriolis/centrifugal matrix C(q,q̇) (operator)
        │           ├─ uses ─► Gravity vector g(q) (operator)
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
        │           ├─ uses ─► Friction coefficient μ (variable)
        │           └─ derived_from ─► Coulomb friction model (principle)
        │                 └─ has_prerequisite ─► Solid mechanics / Physics (foundation)
        └─ requires ─► Quadratic program solver (algorithm)
              ├─ instantiates ─► Active-set method (algorithm)
              └─ instantiates ─► Interior-point method (algorithm)
```

### 1.3 从 QP 到优化理论

```
Inverse-dynamics QP formulation (formalism)
  └─ formalizes ─► Standard QP (formalism)
        ├─ includes ─► min_x ½ xᵀ H x + gᵀ x, s.t. A x = b, C x ≤ d (equation)
        ├─ uses ─► Decision variable vector x = [q̈; λ; τ] (variable)
        ├─ uses ─► Hessian matrix H (variable)
        ├─ uses ──► Gradient vector g (variable)
        ├─ uses ──► Equality constraint matrix A and vector b (variable)
        ├─ uses ──► Inequality constraint matrix C and vector d (variable)
        ├─ solved_by ─► Active-set method (algorithm)
        │     ├─ includes ─► Step 1: find feasible starting point (concept)
        │     ├─ includes ─► Step 2: identify active constraints W (concept)
        │     ├─ includes ─► Step 3: solve equality-constrained QP on W (concept)
        │     │     └─ solves ─► KKT system for EQP (equation)
        │     │           ├─ includes ─► [ H  A_Wᵀ ] [  x  ] = [ −g ]
        │     │           │             [ A_W  0  ] [ ν_W ]   [ b_W ] (equation)
        │     │           ├─ uses ─► Saddle-point matrix (operator)
        │     │           ├─ uses ─► Schur complement (operator)
        │     │           └─ has_prerequisite ─► Numerical linear algebra (foundation)
        │     ├─ includes ─► Step 4: check Lagrange multipliers of active inequalities (concept)
        │     ├─ includes ─► Step 5: remove violating constraint and repeat (concept)
        │     └─ has_prerequisite ─► KKT conditions (theorem)
        └─ solved_by ─► Interior-point method (algorithm)
              ├─ includes ─► Barrier problem: min_x f(x) − μ Σ_i log(s_i) (formalism)
              │     ├─ uses ─► Barrier parameter μ (variable)
              │     └─ uses ─► Slack variables s_i = d_i − C_i x (variable)
              ├─ includes ─► Newton step on KKT conditions (concept)
              │     └─ uses ─► Hessian of Lagrangian ∇²_xx L (operator)
              │           └─ has_prerequisite ─► Multivariable calculus (foundation)
              ├─ includes ─► Line search with Wolfe conditions (algorithm)
              │     ├─ uses ─► Armijo condition (concept)
              │     ├─ uses ─► Curvature condition (concept)
              │     └─ has_prerequisite ─► Calculus / Optimization theory (foundation)
              └─ has_prerequisite ─► Convex analysis (foundation)

KKT conditions (theorem)
  ├─ derived_from ─► Lagrangian L(x, ν, μ) (formalism)
  │     ├─ includes ─► L = f(x) + νᵀ(Ax−b) + μᵀ(Cx−d) (equation)
  │     ├─ uses ─► Lagrange multipliers ν, μ (concept/variable)
  │     │     └─ has_prerequisite ─► Multivariable calculus (foundation)
  │     └─ uses ─► Gradient ∇f(x) (operator)
  │           └─ has_prerequisite ─► Multivariable calculus (foundation)
  ├─ includes ─► Stationarity: ∇f(x) + Aᵀν + Cᵀμ = 0 (equation)
  │     └─ uses ─► Transpose of constraint Jacobian Aᵀ, Cᵀ (operator)
  ├─ includes ─► Primal feasibility: A x = b, C x ≤ d (equation)
  ├─ includes ─► Dual feasibility: μ ≥ 0 (equation)
  ├─ includes ─► Complementary slackness: μᵀ(Cx−d) = 0 (equation)
  │     └─ uses ─► Elementwise product / Hadamard product (operator)
  └─ requires ─► Constraint qualification (concept)
        ├─ instantiates ─► LICQ (concept)
        └─ instantiates ─► Slater's condition (concept)
              └─ has_prerequisite ─► Convex analysis (foundation)
```

### 1.4 这条链路的启示

- 想读懂一篇 WBC 论文，不能只停在“用了 QP”；要看到决策变量、目标函数、等式/不等式约束分别怎么写。
- QP 目标函数展开后，H 和 g 的具体形式直接由任务 Jacobian 和权重决定。
- Active-set 的每一步都有对应的线性代数结构（saddle-point 矩阵、Schur complement）。
- 每个约束背后都有物理/数学原理：动力学约束来自牛顿-欧拉，摩擦约束来自库仑摩擦。

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
        ├─ uses ─► Lattice parameter a, c (variable)
        └─ enables ─► Li⁺ intercalation / deintercalation (process)
              └─ formalizes ─► Intercalation reaction (equation)
                    ├─ includes ─► Li_{1−x}MO₂ + x Li⁺ + x e⁻ ⇌ LiMO₂ (equation)
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
        │     ├─ uses ─► Current density j (variable)
        │     ├─ uses ─► Exchange current density j₀ (variable)
        │     │     └─ includes ─► j₀ = n F k₀ c_R^{α_c} c_O^{α_a} (equation)
        │     │           ├─ uses ─► Rate constant k₀ (variable)
        │     │           ├─ uses ─► Reactant/product concentrations c_R, c_O (variable)
        │     │           └─ derived_from ─► Transition state theory (principle)
        │     │                 └─ has_prerequisite ─► Statistical mechanics / Physical chemistry (foundation)
        │     ├─ uses ─► Activation overpotential η (variable)
        │     │     └─ includes ─► η = φ − φ_eq (equation)
        │     │           └─ uses ─► Equilibrium potential φ_eq from Nernst equation (formalism)
        │     │                 ├─ includes ─► φ_eq = φ° + (RT / nF) ln(a_O / a_R) (equation)
        │     │                 ├─ uses ─► Standard potential φ° (constant)
        │     │                 ├─ uses ─► Activities a_O, a_R (variable)
        │     │                 └─ derived_from ─► Chemical potential equality (principle)
        │     │                       └─ has_prerequisite ─► Thermodynamics (foundation)
        │     ├─ uses ─► Charge transfer coefficients αₐ, α_c (variable)
        │     │     └─ has_prerequisite ─► Electrochemical kinetics (foundation)
        │     ├─ uses ─► Faraday constant F (constant)
        │     ├─ uses ─► Gas constant R (constant)
        │     ├─ uses ─► Temperature T (variable)
        │     └─ has_prerequisite ─► Electrochemical kinetics (foundation)
        └─ approximates ─► Tafel equation at high overpotential (equation)
              └─ has_prerequisite ─► Asymptotic analysis (foundation)

Mass transport in electrolyte (process)
  ├─ formalizes ─► Nernst-Planck equation (equation)
  │     ├─ includes ─► ∂c_i/∂t = −∇·J_i + R_i (equation)
  │     └─ includes ─► J_i = −D_i∇c_i − (z_i u_i F c_i / RT)∇φ + c_i v (equation)
  │           ├─ uses ─► Diffusion flux −D_i∇c_i (operator)
  │           ├─ uses ─► Migration flux −(z_i u_i F c_i / RT)∇φ (operator)
  │           ├─ uses ─► Convection flux c_i v (operator)
  │           └─ has_prerequisite ─► Physical chemistry / Transport phenomena (foundation)
  └─ approximates ─► Fick's laws of diffusion (principle)
        ├─ includes ─► J = −D ∇c (equation)
        └─ has_prerequisite ─► Partial differential equations (foundation)

Solid-state diffusion in cathode particle (process)
  └─ formalizes ─► Fick's second law in spherical coordinates (equation)
        ├─ includes ─► ∂c_s/∂t = D_s (1/r²) ∂/∂r(r² ∂c_s/∂r) (equation)
        ├─ uses ─► Laplacian operator in spherical coordinates (operator)
        ├─ uses ─► Spherical radial coordinate r (variable)
        └─ solved_by ─► Separation of variables / Eigenfunction expansion (algorithm)
              ├─ uses ─► Spherical Bessel functions / Error function (operator)
              └─ has_prerequisite ─► Differential equations / Linear algebra (foundation)
```

### 2.4 SEI 层与等效电路

```
Graphite anode (material)
  └─ produces ─► Solid-electrolyte interphase (SEI) (component/formalism)
        ├─ derived_from ─► Electrolyte reduction at low potential (process)
        ├─ includes ─► SEI resistance R_SEI (variable)
        ├─ includes ─► SEI capacitance C_SEI (variable)
        └─ has_prerequisite ─► Electrochemistry / Polymer chemistry (foundation)

Equivalent circuit model (ECM) (formalism)
  ├─ includes ─► V_t = OCV(SOC) − I R_0 − V_RC (equation)
  ├─ uses ─► Ohmic resistance R_0 (variable)
  ├─ uses ─► RC parallel pair (R_SEI, C_SEI) (component/formalism)
  └─ has_prerequisite ─► Circuit theory / Linear systems (foundation)
```

### 2.5 BMS 状态估计的下钻

```
Battery Management System (BMS) (system)
  └─ requires ─► State-of-Charge (SOC) estimation (method)
        ├─ instantiates ─► Extended Kalman Filter (EKF) (algorithm)
        │     ├─ is_based_on ─► Kalman filter (algorithm)
        │     │     └─ formalizes ─► Bayesian filtering (formalism)
        │     │           ├─ includes ─► p(x_t | y_{1:t−1}) = ∫ p(x_t | x_{t−1}) p(x_{t−1} | y_{1:t−1}) dx_{t−1} (equation)
        │     │           ├─ includes ─► p(x_t | y_{1:t}) ∝ p(y_t | x_t) p(x_t | y_{1:t−1}) (equation)
        │     │           ├─ uses ─► Gaussian distribution N(μ, Σ) (formalism)
        │     │           │     ├─ uses ─► Mean μ (variable)
        │     │           │     ├─ uses ─► Covariance Σ (variable)
        │     │           │     └─ has_prerequisite ─► Probability & statistics (foundation)
        │     │           └─ has_prerequisite ─► Probability & statistics (foundation)
        │     └─ approximates ─► Linearization via Jacobian (approximation)
        │           ├─ uses ─► State-transition Jacobian F (operator)
        │           ├─ uses ─► Observation Jacobian H (operator)
        │           └─ has_prerequisite ─► Multivariable calculus (foundation)
        └─ is_based_on ─► Equivalent circuit model (ECM) (formalism)
              └─ includes ─► V_t = OCV(SOC) − I R_0 − V_RC (equation)
                    └─ has_prerequisite ─► Circuit theory / Linear systems (foundation)
```

### 2.6 热管理下钻

```
Battery thermal management (system)
  └─ requires ─► Heat generation model (formalism)
        └─ includes ─► Q̇_gen = I(V − OCV) + I T ∂OCV/∂T (Bernardi equation) (equation)
              ├─ uses ─► Reversible heat I T ∂OCV/∂T (operator)
              ├─ uses ─► Irreversible Joule heat I(V − OCV) (operator)
              └─ derived_from ─► Energy balance (principle)
                    └─ has_prerequisite ─► Thermodynamics (foundation)
```

### 2.7 这条链路的启示

- 电池不是“材料 + BMS”两层，而是材料 → 晶体结构 → 反应 → 电极动力学 → 传输现象 → PDE/数值方法。
- Butler-Volmer 方程里的 j₀、η、α 每一个都可以继续拆到更底层的统计力学和热力学。
- SEI 层的形成会引入额外的 R_SEI 和 C_SEI，直接影响 ECM 和 BMS 状态估计精度。

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
        │           ├─ includes ─► E_{t,x₀,ε} [ ‖s_θ(x_t,t) − ∇_{x_t} log p(x_t | x₀)‖² ] (equation)
        │           ├─ uses ─► Forward diffusion kernel p(x_t | x₀) (formalism)
        │           │     ├─ includes ─► q(x_t | x_0) = N(x_t; √(ᾱ_t) x_0, (1−ᾱ_t) I) (equation)
        │           │     ├─ uses ─► Noise schedule β_t (variable)
        │           │     ├─ uses ─► Cumulative product ᾱ_t = ∏_{s=1}^t (1−β_s) (variable)
        │           │     └─ has_prerequisite ─► Gaussian processes / Probability (foundation)
        │           └─ has_prerequisite ─► Probability & statistics (foundation)
        └─ instantiates ─► DDPM reverse process (algorithm)
              ├─ includes ─► dx = [f(x,t) − g(t)² ∇_x log p_t(x)] dt + g(t) dw (equation)
              ├─ uses ─► Drift function f(x,t) (variable/operator)
              ├─ uses ─► Diffusion coefficient g(t) (variable)
              ├─ uses ─► Wiener process w(t) (operator/variable)
              ├─ uses ─► Noise prediction objective: ε_θ(x_t, t) ≈ ε (equation)
              │     ├─ derived_from ─► Tweedie's formula (theorem)
              │     │     └─ has_prerequisite ─► Statistics / Stein's lemma (foundation)
              │     └─ has_prerequisite ─► Probability & statistics (foundation)
              └─ solved_by ─► Euler-Maruyama sampler (algorithm)
                    ├─ uses ─► Discretization time step Δt (variable)
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
              ├─ uses ─► Local truncation error analysis (concept)
              └─ has_prerequisite ─► Numerical analysis (foundation)
```

### 3.4 Transformer 骨干的下钻

```
Transformer architecture (method)
  └─ formalizes ─► Self-attention mechanism (formalism)
        └─ includes ─► Attention(Q,K,V) = softmax(QKᵀ / √d_k) V (equation)
              ├─ uses ─► Input embedding matrix X (variable)
              ├─ uses ─► Learned projection matrices W_Q, W_K, W_V (variable)
              ├─ uses ─► Query Q = X W_Q (equation)
              ├─ uses ─► Key K = X W_K (equation)
              ├─ uses ─► Value V = X W_V (equation)
              ├─ uses ─► Scaling factor 1/√d_k (constant)
              ├─ uses ─► Matrix multiplication QKᵀ (operator)
              ├─ uses ─► Softmax function (operator)
              │     ├─ includes ─► softmax(z_i) = exp(z_i) / Σ_j exp(z_j) (equation)
              │     ├─ uses ─► Exponential function exp(·) (operator)
              │     ├─ uses ─► Normalization Σ_j exp(z_j) (operator)
              │     └─ has_prerequisite ─► Probability / Measure theory (foundation)
              └─ has_prerequisite ─► Linear algebra (foundation)

Layer normalization (method)
  └─ formalizes ─► LayerNorm(x) (formalism)
        └─ includes ─► y = γ (x − μ) / √(σ² + ε) + β (equation)
              ├─ uses ─► Mean μ = (1/d) Σ_i x_i (operator)
              ├─ uses ─► Variance σ² = (1/d) Σ_i (x_i − μ)² (operator)
              ├─ uses ─► Small constant ε for numerical stability (constant)
              ├─ uses ─► Learnable scale γ and shift β (variable)
              └─ has_prerequisite ─► Statistics / Linear algebra (foundation)
```

### 3.5 训练与优化的下钻

```
VLA training (process)
  └─ uses ─► Behavior cloning objective (formalism)
        ├─ includes ─► L_BC = E[ ‖π_θ(s) − a‖² ] (equation, continuous actions)
        ├─ includes ─► L_CE = − Σ_t log π_θ(a_t | s_t) (equation, discrete tokenized actions)
        └─ minimized_by ─► Gradient descent (algorithm)
              ├─ includes ─► θ_{t+1} = θ_t − η ∇_θ L(θ_t) (equation)
              │     ├─ uses ─► Learning rate η (variable)
              │     └─ uses ─► Gradient ∇_θ L (operator)
              ├─ uses ─► Backpropagation (algorithm)
              │     ├─ uses ─► Chain rule (theorem)
              │     │     └─ includes ─► ∂L/∂W = (∂L/∂h)(∂h/∂W) (equation)
              │     │           └─ has_prerequisite ─► Multivariable calculus (foundation)
              │     └─ instantiates ─► Automatic differentiation (algorithm)
              │           ├─ uses ─► Computational graph (formalism)
              │           └─ has_prerequisite ─► Compiler theory / Graph algorithms (foundation)
              └─ instantiates ─► Adam optimizer (algorithm)
                    ├─ builds_on ─► Gradient descent (algorithm)
                    ├─ includes ─► m_t = β₁ m_{t−1} + (1−β₁) g_t (equation)
                    ├─ includes ─► v_t = β₂ v_{t−1} + (1−β₂) g_t² (equation)
                    ├─ includes ─► bias-corrected estimates m̂_t, v̂_t (equation)
                    ├─ uses ─► Exponential moving average (operator)
                    └─ has_prerequisite ─► Optimization theory / Probability (foundation)
```

### 3.6 这条链路的启示

- VLA 不是“Transformer + 扩散”一句话能说清的。训练目标、动作表示（连续/离散/扩散）、推理采样器、数值稳定性都需要分开建模。
- DDPM 的 noise-prediction 目标与 score function 之间通过 Tweedie's formula 联系，这背后是统计推断。
- Adam 里的 β₁、β₂ 是指数移动平均，和信号处理里的低通滤波是同一个数学结构。

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
| `constant` | F、R、d_k、β_t | 公式中的常数/超参数 |
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
| `solves` | Active-set method solves QP | 算法求解问题 |
| `estimates` | Score matching estimates score function | 算法估计某个量 |
| `minimizes` | Gradient descent minimizes loss | 算法最小化目标 |
| `approximates` | Fick's laws approximate Nernst-Planck | 近似关系 |
| `instantiates` | EKF instantiates Kalman filter | 具体实例 |
| `builds_on` | Adam builds on gradient descent | 继承/改进 prior work |

---

## 「生活实例 + 自然语言阐述逻辑」写法示例

每个具体实体文件的开头应该先用日常语言解释它是什么、为什么需要它。下面是几个示例。

### 示例 1：KKT 条件

> **生活实例**：想象你在一个商场里想找到离出口最近的位置，但被告知“不能走进商店内部”（不等式约束）且“必须站在过道正中线上”（等式约束）。KKT 条件就是一套判断标准：如果你站的位置最优，那么要么你不在边界上（约束不影响你），要么边界上的“推力”刚好把你顶在最优位置。 stationarity 说的是“合力为零”；complementary slackness 说的是“要么你在边界上，要么那个约束不起作用”。
>
> **自然语言逻辑**：把带约束的优化问题写成拉格朗日函数 → 对原变量和乘子分别求导并令其为零 → 得到 KKT 条件 → 这些条件是局部最优的必要条件（在凸问题下也是充分条件）。

### 示例 2：Butler-Volmer 方程

> **生活实例**：电池充电就像很多人同时挤过一扇旋转门。如果门很窄（高过电位），大家就会挤成一团，电流（人流）增长变慢；如果门很宽（低过电位），人流和门的“宽松程度”近似成正比。Butler-Volmer 方程就是描述“门宽”与“人流”之间非线性关系的公式。
>
> **自然语言逻辑**：电极表面发生氧化/还原反应 → 反应速率受电势差驱动 → 正向/反向电流分别与电势差呈指数关系 → 净电流是两者之差 → 得到 Butler-Volmer 方程。

### 示例 3：Self-Attention

> **生活实例**：你在读一段中文时，每个字都会“回头看”整句话，并根据相关性决定把注意力放在哪些字上。比如“我把苹果吃了”里，“吃”更关注“苹果”而不是“我”。Self-attention 就是让模型自动学习这种“谁该看谁”的权重机制。
>
> **自然语言逻辑**：把输入序列映射成 Query、Key、Value → Query 和 Key 做内积得到相似度 → 用 softmax 归一化得到注意力权重 → 权重乘以 Value 得到输出 → 缩放因子 1/√d_k 防止点积过大导致 softmax 饱和。

---

## 这些链路对工作流的启示

1. **一条工作流只能覆盖一个深度层**：研究 Butler-Volmer 方程需要电化学工作流；研究其离散求解需要 PDE 数值方法工作流。
2. **同一基础学科会被多棵树共享**：Linear algebra 同时是 WBC、VLA、SLAM、经济学的根系。
3. **方程和算子应该被显式抽提**：文献阅读 Agent 不应该只总结“用了 QP”，而要抽出 QP 的具体形式、H 矩阵的含义、约束的来源。
4. **每个实体文件都需要“翻译”成自然语言**：公式本身只是符号，真正理解它需要在文件开头用生活例子讲清楚逻辑。
5. **跨域关系天然存在**：电池热管理的 Bernardi 方程和热力学是电池树的根，但热传导 PDE 也可能用于电机散热树。

---

## 下一步建议

- [ ] 从链路 1 开始，真正创建一批实体文件（如 `ent_wbc_hierarchical_qp.md`、`ent_kkt_conditions.md`、`ent_newton_euler.md`）。
- [ ] 每个实体文件开头必须包含 `## 生活实例 + 自然语言阐述逻辑` 小节。
- [ ] 创建对应的基础学科工作流 YAML：`convex_optimization.yaml`、`rigid_body_dynamics.yaml`、`electrochemistry.yaml`、`stochastic_calculus.yaml`。
- [ ] 在 `WORKSTREAM_TREE.md` 中把这些节点标记为 `[x]`，并标注它们支撑哪些工程领域。
