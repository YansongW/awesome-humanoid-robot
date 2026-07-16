# 附录 G 术语表

> 本附录由 `scripts/build_appendices.py` 从知识图谱数据自动生成，随 KG 更新而更新。

知识图谱中概念、原理、算子、算法等形式化实体的一句话定义，按类别分组。


## G.1 概念（17）

| 术语 | 定义 |
|---|---|
| [世界模型](/entry/ent_concept_world_model/) | 预测环境未来状态的习得或 handcrafted 内部模型，支持机器人与AI中的规划与推理。 |
| [产品责任](/entry/ent_concept_product_liability/) | 制造商与销售商因缺陷或不安全产品造成人身伤害或财产损失的法律责任，直接适用于人形机器人。 |
| [产能爬坡](/entry/ent_paper_production_ramp_2024/) | 当前人形机器人执行器供应链呈现高端减速器与高端编码器高度集中的特征：谐波减速器全球头部企业 Harmonic Drive、RV 减速器 Nabtesco 占据较大市场份额；高端磁编码器/光编也主要由日本、欧洲企业供应。 |
| [人机协作安全](/entry/ent_concept_human_robot_collaboration_safety/) | 确保人与机器人安全共存与协作的标准、传感器、控制律与工作环境设计集合，涵盖 ISO 13482、ISO/TS 15066、IEC 61508、ISO 13849、IEC 62368 等核心标准及 CE、UL、FCC、CR、CCC 等区域市场… |
| [从0到1的七个跃迁](/entry/ent_concept_seven_transitions/) | 将人形机器人从样机推向产品所需的技术、系统、供应链、制造、成本、验证与市场七大关键跃迁框架。 |
| [具身通用智能](/entry/ent_concept_embodied_general_intelligence/) | $$ \dot{x}(t) = f\big(x(t), u(t)\big), \quad y(t) = h\big(x(t), u(t)\big) $$ |
| [决策栈](/entry/ent_concept_decision_stack/) | 将感知结果与任务目标转化为规划、策略与行为决策的软件子系统。 |
| [感知栈](/entry/ent_concept_perception_stack/) | 处理传感器数据以估计状态、检测物体并构建环境表示，为决策提供输入的软件子系统。 |
| [执行栈](/entry/ent_concept_actuation_stack/) | 根据决策输出执行底层电机命令、安全限位与故障响应的软硬件子系统。 |
| [数字孪生](/entry/ent_concept_digital_twin/) | 数字孪生（digital twin）是物理实体在数字空间的实时映射，可用于设计验证、虚拟调试、健康监测与预测性维护。 |
| [数据飞轮](/entry/ent_concept_data_flywheel/) | 部署机器人产生数据、数据改进AI模型、模型提升机器人性能并产生更多数据的自我增强循环。 |
| [机器人即服务（RaaS）](/entry/ent_concept_robot_as_a_service/) | 以租赁或订阅而非买断方式提供机器人，并打包维护、软件更新与车队管理的商业模式。 |
| [演示指标与产品指标的鸿沟](/entry/ent_concept_demo_to_product_gap/) | 与 ASIMO 和早期 Atlas 不同，2025–2026 年的新浪潮强调真实场景中的长期部署和量产可行性： |
| [物料清单](/entry/ent_paper_bill_of_materials_2024/) | 构建一台人形机器人所需的所有零件、子装配件和原材料的结构化清单。 |
| [约束规范](/entry/ent_constraint_qualification/) | 概述 优化问题约束的一种正则性条件，保证在局部最优处 Karush-Kuhn-Tucker 最优性必要条件的有效性。 |
| [转矩密度](/entry/ent_metric_torque_density/) | 1. |
| [隐私与生物识别](/entry/ent_concept_privacy_biometrics/) | 机器人采集的个人信息与生物识别数据（如人脸、声纹、步态）的治理。 |

## G.2 原理（10）

| 术语 | 定义 |
|---|---|
| [力闭合](/entry/ent_principle_force_closure/) | 在不改变接触配置的前提下，接触力可平衡物体任意外部力螺旋的抓取条件。 |
| [形闭合](/entry/ent_principle_form_closure/) | 仅通过无摩擦接触的几何与布局即可完全约束物体运动的抓取条件。 |
| [捕获点](/entry/ent_principle_capture_point/) | 捕获点（Capture Point, CP）是人形机器人推恢（push recovery）与步态规划中的核心概念：它是地面上这样一个点——若机器人能在该点立即踩下去并把质心置于支撑脚正上方，则无需再迈下一步即可停止[44][45]。 |
| [最大似然估计](/entry/ent_principle_maximum_likelihood_estimation/) | 一种统计原理，选择使训练数据出现概率最大的模型参数，是交叉熵和下一个 token 预测损失的基础。 |
| [牛顿-欧拉运动方程](/entry/ent_principle_newton_euler_equations/) | 描述力和力矩如何产生刚体平动和转动加速度的耦合平移与旋转方程。 |
| [电流环/速度环/位置环](/entry/ent_principle_current_velocity_position_loops/) | 4. |
| [电荷守恒](/entry/ent_principle_conservation_of_charge/) | 电荷既不能被创造也不能被消灭、只能重新分布的基本原理；它是基尔霍夫电流定律和电化学系统电荷平衡方程的基础。 |
| [菲克定律](/entry/ent_ficks_law/) | 一种本构原理，指出物质的扩散通量与其浓度梯度的负值成正比。 |
| [质心（COM）](/entry/ent_principle_center_of_mass/) | 人形机器人是多连杆系统，其整体运动状态不仅由各连杆速度决定，还可以通过质心动量（centroidal momentum）统一描述。 |
| [零力矩点（ZMP）](/entry/ent_principle_zero_moment_point/) | 8. |

## G.3 算子（3）

| 术语 | 定义 |
|---|---|
| [Softmax 函数](/entry/ent_operator_softmax_function/) | 一种可微算子，将实值分数向量转换为概率分布，突出最大值，同时保持所有概率为正且和为 1。 |
| [任务 Jacobian](/entry/ent_operator_task_jacobian/) | 将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。 |
| [分压器](/entry/ent_operator_voltage_divider/) | 一种线性电路算子，按电阻值比例将总电压分配到串联电阻上。 |

## G.4 算法（9）

| 术语 | 定义 |
|---|---|
| [DDPM 逆过程](/entry/ent_ddpm_reverse_process/) | 去噪扩散概率模型（DDPM）中学习的反向马尔可夫链，逐步将高斯噪声转化为类数据样本。 |
| [二次规划的积极集法](/entry/ent_algorithm_active_set_method/) | 一种求解二次规划的迭代算法，维护一个活动约束工作集，并求解等式约束子问题直到满足最优性条件。 |
| [内点法](/entry/ent_interior_point_method/) | 一类优化算法，通过障碍或惩罚函数在可行域内部沿光滑中心路径求解约束优化问题。 |
| [分数匹配](/entry/ent_score_matching/) | 一种参数估计技术，学习未知对数概率密度的梯度（称为分数），而无需归一化的概率密度。 |
| [反向传播](/entry/ent_backpropagation/) | 一种高效算法，通过按逆序逐层应用链式法则，计算损失函数对前馈神经网络所有参数的梯度。 |
| [梯度下降法](/entry/ent_gradient_descent/) | > 生活实例：想象你在山上蒙着眼睛找最低点。 |
| [起作用集法](/entry/ent_active_set_method/) | > 生活实例：想象拼拼图时先猜哪些块接触边框（起作用约束），只拼这些边框块，再检查内部是否有块凸出。 |
| [软演员-评论家（SAC）](/entry/ent_algorithm_sac/) | 在最大化期望回报的同时最大化策略熵以促进探索的异策演员-评论家强化学习算法。 |
| [近端策略优化（PPO）](/entry/ent_algorithm_ppo/) | 通过限制策略更新步长避免破坏性改变、提高样本效率的策略梯度强化学习算法。 |

## G.5 形式化方法（8）

| 术语 | 定义 |
|---|---|
| [Thevenin 等效电路](/entry/ent_formalism_thevenin_equivalent_circuit/) | 一种形式化方法，将任意线性电网络从两个端子看进去替换为一个等效理想电压源串联一个等效电阻。 |
| [Transformer 动作解码器形式化](/entry/ent_formalism_transformer_action_decoder/) | 一种使用 Transformer 架构和学习的动作 token 词表，从视觉-语言上下文解码机器人动作的形式化生成框架。 |
| [拉格朗日量](/entry/ent_lagrangian/) | 通过动能与势能之差（或更一般组合）刻画系统动力学，并由变分原理导出运动方程的标量函数。 |
| [标准二次规划（QP）](/entry/ent_qp_standard_form/) | 现代 WBC 的主流实现是全身 QP 控制。 |
| [欧拉-拉格朗日方程](/entry/ent_formalism_euler_lagrange_equations/) | 由作用量变分驻值条件导出的二阶微分方程组，给出广义坐标下机械系统的运动方程。 |
| [浮动基动力学](/entry/ent_formalism_floating_base_dynamics/) | 人形机器人不同于固定基座的工业机械臂，其基座（躯干）可在空间中自由移动。 |
| [贝叶斯滤波](/entry/ent_bayesian_filtering/) | 利用动力学模型与带噪观测递归地维护并更新隐状态信念分布的概率框架。 |
| [逆动力学二次规划形式化](/entry/ent_formalism_inverse_dynamics_qp/) | 一种二次规划形式化，通过最小化任务跟踪误差并受浮动基动力学和物理约束，计算广义加速度、接触力和关节力矩。 |

## G.6 定理（2）

| 术语 | 定义 |
|---|---|
| [Karush-Kuhn-Tucker（KKT）条件](/entry/ent_kkt_conditions/) | > 生活实例：想象你在一个商场里想找到离出口最近的位置，但被告知“不能走进任何商店内部”（不等式约束），同时“必须站在过道的中线上”（等式约束）。 |
| [链式法则](/entry/ent_chain_rule/) | 一个基本微积分法则，给出复合函数导数等于各组成函数导数的乘积。 |

## G.7 方程（7）

| 术语 | 定义 |
|---|---|
| [Butler-Volmer 方程](/entry/ent_butler_volmer_equation/) | > 生活实例：电池充电就像很多人同时挤过一扇旋转门。 |
| [Thevenin 端电压方程](/entry/ent_equation_thevenin_terminal_voltage/) | 给出 Thevenin 等效电路端电压等于开路电压减去等效电阻上压降的方程。 |
| [加权任务误差目标函数](/entry/ent_equation_weighted_task_error_objective/) | 惩罚期望任务加速度与预测任务加速度之间加权平方差，并对广义加速度添加正则项的 QP 目标。 |
| [牛顿-欧拉方程](/entry/ent_newton_euler_equations/) | 描述刚体或铰接多体系统运动的一组耦合的力平衡与力矩平衡方程。 |
| [缩放点积自注意力](/entry/ent_self_attention_equation/) | > 生活实例：你在读一句话时，每个字都会“回头看”整句话，并根据相关性决定把注意力放在哪些字上。 |
| [能斯特-普朗克方程](/entry/ent_nernst_planck_equation/) | 描述带电粒子在浓度梯度与电场共同作用下的通量，融合扩散与电迁移的输运方程。 |
| [连续性方程](/entry/ent_continuity_equation/) | 一种偏微分方程，通过将某物理量的变化率等于其通量散度的负值来表达局部守恒。 |

## G.8 基础学科（5）

| 术语 | 定义 |
|---|---|
| [凸优化](/entry/ent_foundation_convex_optimization/) | 在凸集上最小化凸函数的数学学科，保证任何局部最优也是全局最优。 |
| [概率论](/entry/ent_foundation_probability_theory/) | 关于不确定性、随机变量、分布和期望的数学基础，是机器人和机器学习中所有概率模型的根基。 |
| [电化学](/entry/ent_foundation_electrochemistry/) | 锂离子电池的能量存储本质上是锂在正负极活性材料晶格中的可逆嵌入/脱嵌反应。 |
| [线性代数](/entry/ent_foundation_linear_algebra/) | 研究向量空间、线性变换、矩阵和线性方程组的数学分支。 |
| [经典力学](/entry/ent_foundation_classical_mechanics/) | 描述宏观物体在力作用下运动的物理学分支，包括牛顿定律、守恒原理和刚体动力学。 |
