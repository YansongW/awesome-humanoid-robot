---
$id: ent_paper_orchardbench_physically_grounded_gpu_par_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OrchardBench: A Physically-Grounded, GPU-Parallel Apple-Orchard Simulation Benchmark for Agricultural Robotics'
  zh: 'OrchardBench: A Physically-Grounded, GPU-Parallel Apple-Orchard Simulation Benchmark for Agricultural Robotics'
  ko: 'OrchardBench: A Physically-Grounded, GPU-Parallel Apple-Orchard Simulation Benchmark for Agricultural Robotics'
summary:
  en: 'Robotic tree-fruit harvesting is a flagship problem for agricultural automation, but progress is bottlenecked by the
    cost and irreproducibility of field experiments: an orchard is available only weeks a year, every tree is different, and
    a control error can permanently damage the crop or the plant. The tree models used in graphics and agronomy are geometrically
    detailed but physically inert,.'
  zh: OrchardBench 是一个基于 Newton/MuJoCo-Warp 引擎构建的 GPU 并行苹果园仿真基准，由研究团队开发，旨在填补程序化植物建模与物理机器人学习模拟之间的空白。其核心贡献在于提供物理真实、可断裂、带果实的树木模型，并配套标准化任务、指标和评估协议，使农业采摘机器人策略可在安全、可扩展、可复现的条件下迭代。
  ko: 'Robotic tree-fruit harvesting is a flagship problem for agricultural automation, but progress is bottlenecked by the
    cost and irreproducibility of field experiments: an orchard is available only weeks a year, every tree is different, and
    a control error can permanently damage the crop or the plant. The tree models used in graphics and agronomy are geometrically
    detailed but physically inert,.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- orchardbench
- physically
- grounded
- gpu
- par
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch4-catchup (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section
    interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量四）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.06337 OrchardBench: A Physically-Grounded, GPU-Parallel Apple-Orchard Simulation Bench'
  url: https://arxiv.org/abs/2607.06337
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

OrchardBench 是一个基于 Newton/MuJoCo-Warp 引擎构建的 GPU 并行苹果园仿真基准，由研究团队开发，旨在填补程序化植物建模与物理机器人学习模拟之间的空白。其核心贡献在于提供物理真实、可断裂、带果实的树木模型，并配套标准化任务、指标和评估协议，使农业采摘机器人策略可在安全、可扩展、可复现的条件下迭代。

## 它改变了什么

它改变了农业机器人仿真中“树木只是静态背景”的现状。此前，图形学树木模型几何精细但物理惰性，机器人学习模拟器则缺乏合理的树木物理，导致田间实验成本高、不可复现且失败代价大——规划不当的运动可能撕裂主枝或剥落果实。OrchardBench 将树木从装饰物提升为具有梁理论动力学、可断裂树枝和可脱落果实的物理实体，使损伤（断枝、落果）成为与成功率同等重要的评估指标，这是对现有基准（如 Isaac Gym、MuJoCo）在农业场景下评估体系的重要补充。

## 方法拆解

### 树木生成与动力学
- 每棵树由随机 L-system 生成，实例化为完全铰接的刚体，节间为刚性链接，分支连接处为顺应性扭转弹簧-阻尼器。
- 刚度遵循欧拉-伯努利梁理论：\( K_p = \frac{\pi}{4} \frac{E r^4}{\ell} = \frac{EI}{\ell} \)，阻尼 \( K_d = c_d K_p \)。由于 \( K_p \propto r^4 \) 且半径按管道模型锥化，细外枝比树干柔软多个数量级。

### 断裂与果实模型
- 树枝断裂：当传递弯矩超过 \( M_{\max} = \sigma_r \frac{\pi r^3}{4} \) 时断裂，采用 N 帧滞后抑制速率尖峰。断裂后通过就地清零设备数组中的增益和偏置行实现自由铰链，无需重编译。
- 果实：独立刚体，通过单侧弹簧-阻尼系绳悬挂，脱落力 \( f_{\text{detach}} \in [14, 23] \, \mathrm{N} \)。弹性系绳力减去静态重量后反作用于父枝，使拉动果实能加载树枝。

### 域随机化与求解器
- 每个 GPU 批处理环境是一棵不同的树，固定离散拓扑，仅扰动连续量（弯曲、生长习性、木材密度、杨氏模量、断裂应力、果实属性等）。
- 默认使用共轭梯度（CG）求解器，比 Newton 默认的阻塞 Cholesky 算法快约 7 倍。薄枝通过额外 armature 和接触边距处理质量比（约 \(10^4:1\)）。

### 感知与基线控制器
- 无学习的检测器：深度图像反投影为点云，分割为深度连续块，用线性最小二乘拟合球体，按半径（2–5.8 cm）、拟合残差、凸性等门控。
- 自主采摘基线为解析状态机：扫描、对齐、到达（阻尼最小二乘逆运动学）、抓取、拉取、放置，含失败处理（黑名单目标）。

## 关键创新

1. **物理真实的树木动力学**：首次将欧拉-伯努利梁理论应用于 GPU 并行仿真中的树枝，使细枝柔软度与树干相差多个数量级，并支持树枝断裂和果实脱落，这是现有农业仿真器未提供的。
2. **损伤作为一等公民指标**：将断枝数和落果数纳入评估协议，与采摘完整性并列，使策略优化需在产量与损伤间权衡，更贴近田间实际约束。
3. **域随机化与批处理同质性的平衡**：固定离散拓扑、扰动连续量，既满足 GPU 批处理的结构同质性要求，又提供丰富的域随机化，且不同运行产生不同结构。

## 实验与结果

| 指标 | 名义条件值 |
|------|-----------|
| 每次尝试成功 | 0.41 |
| 采摘完整性（采摘/可达） | 0.12 |
| 每机器人吞吐量（果实/分钟） | 1.9 |
| 平均采摘周期时间（秒） | 7.3 |
| 检测精度 | 0.90 |
| 每树折断树枝 | ∼0.2 |
| 每树掉落果实 | ∼6 |
| 最大茎拉拔力（N，峰值） | 29 |

- 并行性：单树步进率 60–100 fps，同质批和共享维度域随机化批均达到 512 棵树，吞吐量约 3500–4400 环境步/秒；不同几何 DR 降至约 140 环境步/秒（32 棵树时 66 fps 对比 4.4 fps，约 15× 差距）。
- 叶密度从 0 升至 1.5，检测精度从 0.98 降至 0.81；果实负载从 20 增至 60 个苹果，完整性从 0.26 降至 0.13。
- 树冠分区：中树冠成功率最高（∼0.55），下-外和上分区最低（0.37–0.42）；树间变异：18 棵树每树放置苹果数 2.4±1.5（范围 0–5）。

## 边界与局限

论文未明确物理验证：物理基于文献而非针对真实树枝断裂或抓取实验验证，Euler–Bernoulli 扭转弹簧集总是理想化，绿木模量和断裂应力是从干木参考值降低的估计。分离力未校准到具体值，果实模型省略果柄扭转（仅拉力触发分离）。感知仅深度，RGB 感知迁移超出范围。无 sim-to-real 演示，域随机化是动机而非已证明能实现迁移。仅评估解析基线，学习型或智能体基线是未来工作。结果应视为仿真内相对比较，而非田间性能的绝对预测。

## 工程启示

复现时先核对物理参数表（表 III）：默认杨氏模量 7 GPa、断裂模量 50 MPa、密度 850 kg/m³，这些值决定树枝刚度与断裂行为，若目标场景为较软树苗需调整。最容易踩坑的是域随机化轴的选择：每分支尺寸（段长、厚度、全局缩放）会显著降低批处理步率（降至 8–13 fps），而果实和叶属性随机化几乎免费，建议优先使用后者。断裂实现依赖就地清零设备数组，需确保不触发 CUDA 图重捕获。基线控制器中，抓取停滞和假阳性检测是主要失败原因，下游团队若开发学习型策略，应优先改进感知门控而非导航。

## Overview
Robotic tree-fruit harvesting is a flagship problem for agricultural automation, but progress is bottlenecked by the cost and irreproducibility of field experiments: an orchard is available only weeks a year, every tree is different, and a control error can permanently damage the crop or the plant. The tree models used in graphics and agronomy are geometrically detailed but physically inert, while the GPU-parallel simulators used in robot learning contain no plausible trees. We present OrchardBench, a physically-grounded, GPU-parallel simulation of apple-orchard trees on the Newton engine. Each tree is grown by a stochastic L-system and instantiated as a fully articulated body: branches are compliant torsional spring-dampers whose stiffness follows Euler-Bernoulli beam theory, they break at a wood modulus of rupture and fall as free hinges, and apples are independent bodies on stem tethers that detach at literature-grounded pull forces and load the branch when pulled. A moving, density-controllable foliage layer occludes the canopy as real leaves do. Every physical parameter is tied to a published source. Per-environment domain randomization makes each batched world a distinct tree, and a mobile manipulator with a wrist depth camera closes the loop with geometric fruit perception and an autonomous harvesting baseline. Careful engineering of the solver and the model lets OrchardBench run many parallel environments at interactive rates on a laptop GPU. We define the tasks and a metric suite spanning harvest completeness, throughput, and plant damage (with a per-canopy-zone breakdown), and report baseline results across foliage, fruit load, terrain, canopy zone, and parallelism. The analytic baseline succeeds on about 40% of the fruit it detects and harvests only about an eighth of the reachable fruit on a tree, leaving clear headroom for novel autonomy approaches.

## 参考
- https://arxiv.org/abs/2607.06337

## 개요

OrchardBench는 Newton/MuJoCo-Warp 엔진 기반으로 구축된 GPU 병렬 사과 과수원 시뮬레이션 벤치마크로, 연구팀이 개발했으며 절차적 식물 모델링과 물리 기반 로봇 학습 시뮬레이션 사이의 간극을 메우는 것을 목표로 한다. 핵심 기여는 물리적으로 사실적이고, 파손 가능하며, 과실이 달린 나무 모델을 제공하고, 표준화된 작업, 지표 및 평가 프로토콜을 함께 제공하여 농업용 수확 로봇 정책이 안전하고 확장 가능하며 재현 가능한 조건에서 반복 개발될 수 있게 한다는 점이다.

## 무엇을 바꾸었는가

이는 농업 로봇 시뮬레이션에서 "나무는 단지 정적 배경"이라는 현상을 바꾼다. 이전에는 그래픽스 나무 모델이 기하학적으로 정교했지만 물리적으로는 비활성적이었고, 로봇 학습 시뮬레이터는 합리적인 나무 물리를 갖추지 못해 현장 실험이 비용이 높고 재현 불가능하며 실패 비용이 컸다—잘못 계획된 동작은 주 가지를 찢거나 과실을 떨어뜨릴 수 있었다. OrchardBench는 나무를 장식물에서 보 이론 동역학, 파손 가능한 가지, 탈락 가능한 과실을 갖춘 물리적 실체로 승격시켜, 손상(가지 부러짐, 과실 낙하)을 성공률과 동등한 중요도의 평가 지표로 만든다. 이는 Isaac Gym, MuJoCo와 같은 기존 벤치마크의 농업 시나리오 평가 체계에 대한 중요한 보완이다.

## 방법 분해

### 나무 생성 및 동역학
- 각 나무는 무작위 L-system으로 생성되며, 완전 관절 강체로 인스턴스화되고, 마디는 강성 링크, 가지 연결부는 순응형 비틀림 스프링-댐퍼로 구성된다.
- 강성은 오일러-베르누이 보 이론을 따른다: \( K_p = \frac{\pi}{4} \frac{E r^4}{\ell} = \frac{EI}{\ell} \), 감쇠 \( K_d = c_d K_p \). \( K_p \propto r^4 \)이고 반경이 파이프 모델에 따라 테이퍼링되므로, 가는 바깥 가지는 줄기보다 수 자릿수 더 유연하다.

### 파손 및 과실 모델
- 가지 파손: 전달 모멘트가 \( M_{\max} = \sigma_r \frac{\pi r^3}{4} \)를 초과하면 파손되며, N-프레임 지연으로 속도 스파이크를 억제한다. 파손 후 디바이스 배열의 게인 및 바이어스 행을 제자리에서 0으로 설정하여 자유 힌지를 구현하며, 재컴파일이 필요 없다.
- 과실: 독립 강체로, 단측 스프링-댐퍼 테더로 매달리며, 탈락력 \( f_{\text{detach}} \in [14, 23] \, \mathrm{N} \). 탄성 테더 힘에서 정적 중량을 뺀 값이 부모 가지에 반작용하여, 과실을 당기면 가지에 하중이 가해진다.

### 도메인 무작위화 및 솔버
- 각 GPU 배치 환경은 서로 다른 나무이며, 이산 토폴로지는 고정하고 연속량(굽힘, 생장 습성, 목재 밀도, 영률, 파손 응력, 과실 속성 등)만 교란한다.
- 기본적으로 공액 기울기(CG) 솔버를 사용하며, Newton의 기본 블로킹 촐레스키 알고리즘보다 약 7배 빠르다. 얇은 가지는 추가 아마추어와 접촉 마진으로 질량비(약 \(10^4:1\))를 처리한다.

### 인식 및 기준 컨트롤러
- 학습 없는 검출기: 깊이 이미지를 역투영하여 포인트 클라우드로 만들고, 깊이 연속 블록으로 분할한 후 선형 최소 제곱으로 구체를 피팅하고, 반경(2–5.8 cm), 피팅 잔차, 볼록성 등으로 게이팅한다.
- 자율 수확 기준은 해석적 상태 머신이다: 스캔, 정렬, 도달(감쇠 최소 제곱 역기구학), 파지, 당김, 배치, 실패 처리(블랙리스트 대상)를 포함한다.

## 핵심 혁신

1. **물리적으로 사실적인 나무 동역학**: GPU 병렬 시뮬레이션의 가지에 오일러-베르누이 보 이론을 최초로 적용하여, 가는 가지의 유연성이 줄기와 수 자릿수 차이가 나고, 가지 파손 및 과실 탈락을 지원한다. 이는 기존 농업 시뮬레이터가 제공하지 못한 기능이다.
2. **손상을 일급 지표로 채택**: 부러진 가지 수와 낙하 과실 수를 평가 프로토콜에 포함시켜 수확 완전성과 병렬로 다루며, 정책 최적화가 수확량과 손상 사이의 균형을 요구하도록 하여 현장의 실제 제약에 더 가깝게 만든다.
3. **도메인 무작위화와 배치 동질성의 균형**: 이산 토폴로지를 고정하고 연속량을 교란하여 GPU 배치의 구조적 동질성 요구를 충족하면서도 풍부한 도메인 무작위화를 제공하며, 실행마다 다른 구조가 생성된다.

## 실험 및 결과

| 지표 | 명목 조건 값 |
|------|-----------|
| 시도당 성공 | 0.41 |
| 수확 완전성(수확/도달 가능) | 0.12 |
| 로봇당 처리량(과실/분) | 1.9 |
| 평균 수확 주기 시간(초) | 7.3 |
| 검출 정밀도 | 0.90 |
| 나무당 부러진 가지 | ∼0.2 |
| 나무당 낙하 과실 | ∼6 |
| 최대 줄기 당김 힘(N, 피크) | 29 |

- 병렬성: 단일 나무 스텝 속도 60–100 fps, 동질 배치 및 공유 차원 도메인 무작위화 배치 모두 512개 나무에 도달, 처리량 약 3500–4400 환경 스텝/초; 서로 다른 기하 DR은 약 140 환경 스텝/초로 감소(32개 나무에서 66 fps 대 4.4 fps, 약 15배 차이).
- 잎 밀도가 0에서 1.5로 증가하면 검출 정밀도가 0.98에서 0.81로 감소; 과실 부하가 20에서 60개 사과로 증가하면 완전성이 0.26에서 0.13으로 감소.
- 수관 분할: 중간 수관 성공률이 가장 높고(∼0.55), 하부-외곽 및 상부 분할이 가장 낮음(0.37–0.42); 나무 간 변이: 18개 나무에서 나무당 사과 수 2.4±1.5(범위 0–5).

## 경계 및 한계

논문은 물리 검증을 명시하지 않았다: 물리는 문헌 기반이며 실제 가지 파손이나 파지 실험으로 검증되지 않았고, 오일러-베르누이 비틀림 스프링 집합은 항상 이상화되며, 녹목 탄성률과 파손 응력은 건조 목재 참조값에서 낮춘 추정치이다. 분리력은 특정 값으로 보정되지 않았고, 과실 모델은 과경 비틀림을 생략한다(인장력만 분리를 유발). 인식은 깊이만 사용하며 RGB 인식 전이는 범위를 벗어난다. sim-to-real 데모가 없으며, 도메인 무작위화는 동기 부여일 뿐 전이를 입증하지 못한다. 해석적 기준만 평가했으며, 학습 기반 또는 에이전트 기준은 향후 작업이다. 결과는 시뮬레이션 내 상대 비교로 간주해야 하며, 현장 성능의 절대 예측으로 보아서는 안 된다.

## 공학적 시사점

재현 시 먼저 물리 파라미터 표(표 III)를 확인하라: 기본 영률 7 GPa, 파손 계수 50 MPa, 밀도 850 kg/m³. 이 값들이 가지 강성과 파손 거동을 결정하며, 대상 시나리오가 더 부드러운 묘목이라면 조정이 필요하다. 가장 쉽게 실수하는 지점은 도메인 무작위화 축 선택이다: 가지별 크기(세그먼트 길이, 두께, 전역 스케일)는 배치 스텝 속도를 크게 낮추고(8–13 fps로), 과실 및 잎 속성 무작위화는 거의 비용이 없으므로 후자를 우선 사용하는 것이 좋다. 파손 구현은 디바이스 배열을 제자리에서 0으로 설정하는 데 의존하므로 CUDA 그래프 재캡처를 유발하지 않도록 해야 한다. 기준 컨트롤러에서 파지 정체와 오탐지 검출이 주요 실패 원인이며, 하류 팀이 학습 기반 정책을 개발한다면 내비게이션보다 인식 게이팅 개선을 우선해야 한다.
