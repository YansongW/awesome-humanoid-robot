---
$id: ent_paper_calf_integrated_arms_bimanual_quadruped_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation
  zh: Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation
  ko: Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation
summary:
  en: Most quadruped loco-manipulation designs trade manipulation capability against stance. A trunk-mounted arm sits high
    and usually carries a single arm; using the legs as manipulators lifts the manipulating leg off the ground; and even leg-mounted
    grippers reach two-handed tasks only by rearing onto the hind legs. This paper integrates a manipulator with a prismatic
    slider, two revolute joints, and.
  zh: 本文提出一种将机械臂集成于四足机器人小腿的“腿臂融合”设计，使Unitree Go2在四脚着地、基座可自由行走的前提下，同时具备地面抓取、双手协同操作与长时程技能排序能力。系统由VLM高层技能规划与FSM低层执行构成，在仿真中验证了三个双臂任务，并系统评估了深度噪声鲁棒性。核心贡献在于重新定义了四足机器人操作能力的形态学基础，将操作工作空间从躯干下移至地面附近。
  ko: Most quadruped loco-manipulation designs trade manipulation capability against stance. A trunk-mounted arm sits high
    and usually carries a single arm; using the legs as manipulators lifts the manipulating leg off the ground; and even leg-mounted
    grippers reach two-handed tasks only by rearing onto the hind legs. This paper integrates a manipulator with a prismatic
    slider, two revolute joints, and.
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
- calf
- integrated
- arms
- bimanual
- quadruped
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
  title: arXiv:2607.06186 Calf-Integrated Arms for Bimanual Quadruped Loco-Manipulation
  url: https://arxiv.org/abs/2607.06186
  date: '2026-07-07'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种将机械臂集成于四足机器人小腿的“腿臂融合”设计，使Unitree Go2在四脚着地、基座可自由行走的前提下，同时具备地面抓取、双手协同操作与长时程技能排序能力。系统由VLM高层技能规划与FSM低层执行构成，在仿真中验证了三个双臂任务，并系统评估了深度噪声鲁棒性。核心贡献在于重新定义了四足机器人操作能力的形态学基础，将操作工作空间从躯干下移至地面附近。

## 它改变了什么

现有四足操作设计存在根本性矛盾：躯干安装的机械臂位置高（基座距地面0.36 m），够地面物体需越过腿部且通常只有单臂；腿装夹爪（如LocoMan）虽能解放前腿，但必须靠后腿站立（rearing），固定基座、丧失行走能力。这些方案都将“操作”与“移动”视为互斥资源，无法在连续任务中同时调用。

本文真正改变的是操作能力的空间分布逻辑——将机械臂嵌入小腿，使操作工作空间（距地面0.01 m至0.34 m）与行走时的腿部运动范围自然重叠，基座保持四脚着地、速度跟踪接口不变。这意味着机器人可以在行走过程中随时执行地面抓取，无需牺牲移动性换取操作能力，为“边移动边操作”的连续行为提供了硬件基础。

## 方法拆解

### 机械设计
- 每条前腿小腿集成4自由度机械臂：棱柱滑块（q1，行程0.105 m，步进电机驱动、非反向驱动）+ 俯仰关节（q2）+ 偏航关节（q3）+ 平行爪夹爪（q4，开口4 cm）。
- 每条前腿共7自由度（3原始腿关节 + 4新增），q2/q3/q4由舵机闭环位置控制。
- 机械臂基座距地面0.18 m，对比躯干安装的0.36 m，伸展距离减半。
- 集成代价：小腿远端质量增加、摆动惯量增大；膝盖折叠短8°，仅影响最深蹲姿，正常行走抬腿不受影响。

### 控制架构（两层）
- **高层**：VLM（Kimi K2.6，云API）从预定义技能库S中选择离散技能，输入为头戴RGB-D图像 + 任务状态（二进制进度标志 + 执行历史）。查询在后台线程运行，每技能边界一次，保持运动策略站立。
- **低层**：每个技能由FSM执行，输出身体系速度指令v_cmd=[vx, vy, ωz]给学习运动策略，输出笛卡尔末端目标g_ee*给3自由度DLS逆运动学求解器。

### 关键模块
- **运动策略**：神经网络在Isaac Lab训练，45维观测（基座角速度、重力向量、速度指令、12个腿关节位置/速度、上一动作），12维输出为固定标称姿态的位置残差，50 Hz应用。四脚全程着地。
- **感知**：红色标记（R>150, G<80, B<80）阈值分割，深度反投影到世界坐标，抓取点取轮廓两相对点中点；部分检测时用最近完整检测平均值替代。
- **操作IK**：DLS求解器公式 Δq = J_p^T (J_p J_p^T + λ²I)^{-1} (g_ee* − x_ee(q))，带迭代裁剪与关节极限投影；开环伸展时从多个初始配置取最低残差，闭环跟踪时从当前配置迭代保持连续。

## 关键创新

1. **形态学创新**：将操作器嵌入小腿而非躯干或腿端，使操作工作空间与行走运动空间在物理上共存。这是首个在四脚着地、基座自由行走前提下实现地面抓取与双手协同的设计，打破了“操作需固定基座”的隐含假设。

2. **双臂协同的偏航关节设计**：q3偏航关节使夹爪可扫向身体中心线，左右臂工作空间在中心线重叠，使双臂能协同操作同一物体（如双手抬升、交接）。这是单臂或腿装夹爪方案无法实现的功能维度。

3. **VLM+FSM的分层技能执行**：VLM仅在技能边界查询（延迟16–40 s/查询），FSM负责实时执行，避免高频VLM推理的延迟问题。这种“慢规划、快执行”的架构使长时程任务（如柜子任务18.6 s）成为可能，且查询期间机器人保持稳定站立。

## 实验与结果

### 三个双臂任务（均在四脚着地状态完成）
- **长时程柜子任务**：左臂携篮行走至柜子，右臂开门，放入柜内。
总运动时间18.6 s（抓篮7.1 s + 行走开门9.1 s + 放入2.4 s），VLM共查询4次。
- **协同双手抬升**：双臂抓取箱子两侧把手共同抬起。
- **左到右交接**：左臂抓取，中心线传递给右臂，右臂放置侧面。
### 对比结果
- 单躯干臂无法同时携篮和开门，不能完成柜子任务。
- LocoMan靠后腿站立固定基座，无法完成重定位。
### 深度噪声鲁棒性
| 噪声标准差 | 抓取成功率 |
|-----------|-----------|
| 10 mm     | 70–74%    |
| 30 mm     | 54%       |
（8个固定放置 × 20个噪声样本 = 160次试验/级）
### 训练配置
域随机化：摩擦[0.3, 1.2]、恢复系数[0, 0.15]、附加基座质量[−1, +3] kg。
（本节另有 1 句含无法从全文文本核实的数字，已按纪律移除；论文未明确或以图/表图片形式给出。）

## 边界与局限

- **机械局限**：手臂无滚动关节，夹爪不能绕接近轴旋转，需此旋转的物体（如水壶）无法抓取。
- **技能库覆盖有限**：VLM只能在预定义技能中选择，不创建新技能；重新抓取新接触点、手中旋转物体、携带时避障、抓取失败后改变策略等无法仅靠提示推理解决。
- **感知依赖标记物**：抓取依赖红色标记，学习检测器尚不能替代；YOLO-World和SAM只能定位框/掩码，区域中心距手柄13 cm，远超4 cm夹爪开口，无法产生可用抓取点。
- **纯仿真验证**：所有结果在仿真中（Isaac Lab训练、MuJoCo评估），未测试真实传感、驱动和接触动力学。
- **未实现功能**：stilt-like行走模式（q1伸出、q2锁定向下）、抬前腿将物体放背部篮子。

## 工程启示

- **复现优先核对**：先确认机械参数（q1行程0.105 m、q4开口4 cm、基座距地0.18 m）与运动策略训练配置（4096环境、200 Hz、降采样因子4、PPO 5000迭代）是否一致，这些直接影响工作空间与动态性能。
- **最易踩坑点**：IK求解器的开环伸展初始化——必须从多个分散初始配置求解取最低残差，否则易陷入局部极小导致夹爪折回身体下方；闭环跟踪时须从当前配置迭代保持连续性。
- **感知模块注意**：红色标记阈值（R>150, G<80, B<80）对光照敏感，部分检测处理（用最近完整检测平均值）在遮挡场景可能引入偏差，建议先验证标记可见性。
- **VLM延迟管理**：规划器延迟16–40 s/查询，期间机器人保持站立——若下游任务需要更频繁重规划，需考虑缓存或预查询机制。
- **双臂协同验证**：q3偏航关节是双臂协同的关键，复现时先单独验证左右臂工作空间在中心线的重叠区域，再测试交接与协同抬升。

## Overview
Most quadruped loco-manipulation designs trade manipulation capability against stance. A trunk-mounted arm sits high and usually carries a single arm; using the legs as manipulators lifts the manipulating leg off the ground; and even leg-mounted grippers reach two-handed tasks only by rearing onto the hind legs. This paper integrates a manipulator with a prismatic slider, two revolute joints, and a gripper into each front calf of a Unitree Go2. The two arms grasp objects at ground level and manipulate with both hands while all four feet stay planted, without rearing. With one arm carrying, the base stays free to walk. A vision-language model sequences skills from a predefined library at each skill boundary, conditioned on the head-camera image and task state, for long-horizon autonomy. In simulation, the design performs three bimanual tasks: a long-horizon cabinet task under autonomous skill selection, a cooperative two-handed lift, and an inter-arm handover.

## 参考
- https://arxiv.org/abs/2607.06186

## 개요

본 논문은 기계 팔을 네 발 달린 로봇의 하퇴부에 통합하는 "다리-팔 융합" 설계를 제안하여, Unitree Go2가 네 발을 지면에 붙인 채 베이스가 자유롭게 보행할 수 있는 조건에서 지면 물체 파지, 양팔 협동 조작, 장시간 스킬 순서화 능력을 동시에 갖추도록 한다. 시스템은 VLM 고수준 스킬 계획과 FSM 저수준 실행으로 구성되며, 시뮬레이션에서 세 가지 양팔 작업을 검증하고 깊이 노이즈 강건성을 체계적으로 평가한다. 핵심 기여는 네 발 달린 로봇의 조작 능력에 대한 형태학적 기반을 재정의하여, 조작 작업 공간을 몸통 아래에서 지면 근처로 이동시킨 것이다.

## 무엇을 바꾸는가

기존 네 발 달린 로봇 조작 설계에는 근본적인 모순이 존재한다: 몸통에 장착된 기계 팔은 위치가 높아(베이스에서 지면까지 0.36 m) 지면 물체에 닿으려면 다리를 넘어야 하고 일반적으로 한 팔만 사용할 수 있다. 다리 끝에 장착된 그리퍼(예: LocoMan)는 앞다리를 해방할 수 있지만, 반드시 뒷다리로 서 있어야 하며(rearing) 베이스가 고정되어 보행 능력을 상실한다. 이러한 접근 방식들은 모두 "조작"과 "이동"을 상호 배타적 자원으로 간주하여 연속 작업에서 동시에 호출할 수 없다.

본 논문이 실제로 바꾸는 것은 조작 능력의 공간 분포 논리이다—기계 팔을 하퇴부에 내장하여 조작 작업 공간(지면에서 0.01 m ~ 0.34 m)이 보행 시 다리 운동 범위와 자연스럽게 겹치게 하고, 베이스는 네 발 착지를 유지하며 속도 추적 인터페이스는 변경하지 않는다. 이는 로봇이 보행 중에도 언제든지 지면 파지를 실행할 수 있게 하여, 이동성을 희생하지 않고 조작 능력을 확보하며, "이동하면서 조작하는" 연속 행동을 위한 하드웨어 기반을 제공한다.

## 방법 분해

### 기계 설계
- 각 앞다리 하퇴부에 4자유도 기계 팔 통합: 프리즘 슬라이더(q1, 스트로크 0.105 m, 스테퍼 모터 구동, 비역구동) + 피치 관절(q2) + 요 관절(q3) + 평행 그리퍼(q4, 개구 4 cm).
- 각 앞다리는 총 7자유도(기존 다리 관절 3개 + 신규 4개), q2/q3/q4는 서보 모터 폐루프 위치 제어.
- 기계 팔 베이스는 지면에서 0.18 m, 몸통 장착의 0.36 m와 비교하여 도달 거리가 절반으로 감소.
- 통합 비용: 하퇴부 말단 질량 증가, 스윙 관성 증가; 무릎 접힘 각도 8° 감소, 가장 깊은 스쿼트 자세에만 영향, 정상 보행 시 다리 들기에는 영향 없음.

### 제어 아키텍처(2계층)
- **고수준**: VLM(Kimi K2.6, 클라우드 API)이 사전 정의된 스킬 라이브러리 S에서 이산 스킬을 선택하며, 입력은 머리 장착 RGB-D 이미지 + 작업 상태(이진 진행 플래그 + 실행 이력). 쿼리는 백그라운드 스레드에서 실행되며, 각 스킬 경계에서 한 번씩 수행되고 운동 정책은 서 있는 상태를 유지.
- **저수준**: 각 스킬은 FSM에 의해 실행되며, 몸체 좌표계 속도 명령 v_cmd=[vx, vy, ωz]를 학습 운동 정책에 출력하고, 데카르트 말단 목표 g_ee*를 3자유도 DLS 역운동학 솔버에 출력.

### 핵심 모듈
- **운동 정책**: 신경망은 Isaac Lab에서 훈련, 45차원 관측(베이스 각속도, 중력 벡터, 속도 명령, 12개 다리 관절 위치/속도, 이전 동작), 12차원 출력은 고정 명목 자세에 대한 위치 잔차이며 50 Hz로 적용. 네 발은全程 착지.
- **인식**: 빨간색 마커(R>150, G<80, B<80) 임계값 분할, 깊이 역투영을 세계 좌표로 변환, 파지점은 윤곽의 두 대응 점의 중점; 부분 감지 시 가장 최근 완전 감지 평균값으로 대체.
- **조작 IK**: DLS 솔버 공식 Δq = J_p^T (J_p J_p^T + λ²I)^{-1} (g_ee* − x_ee(q)), 반복 클리핑 및 관절 한계 투영 포함; 개루프 신장 시 여러 초기 구성에서 최저 잔차를 취하고, 폐루프 추적 시 현재 구성에서 반복하여 연속성 유지.

## 핵심 혁신

1. **형태학적 혁신**: 조작기를 몸통이나 다리 끝이 아닌 하퇴부에 내장하여 조작 작업 공간과 보행 운동 공간이 물리적으로 공존하게 한다. 이는 네 발 착지, 베이스 자유 보행 전제 하에 지면 파지와 양팔 협동을 구현한 최초의 설계로, "조작에는 고정 베이스가 필요하다"는 암묵적 가정을 깨뜨린다.

2. **양팔 협동을 위한 요 관절 설계**: q3 요 관절은 그리퍼가 몸체 중심선을 향해 스윙할 수 있게 하여, 좌우 팔의 작업 공간이 중심선에서 겹치므로 양팔이 동일 물체를 협동 조작할 수 있다(예: 양손 들어 올리기, 인계). 이는 단일 팔 또는 다리 끝 그리퍼 방식으로는 구현할 수 없는 기능 차원이다.

3. **VLM+FSM 계층적 스킬 실행**: VLM은 스킬 경계에서만 쿼리(지연 16–40 s/쿼리), FSM은 실시간 실행을 담당하여 고주파 VLM 추론의 지연 문제를 피한다. 이러한 "느린 계획, 빠른 실행" 아키텍처는 장시간 작업(예: 캐비닛 작업 18.6 s)을 가능하게 하며, 쿼리 동안 로봇은 안정적으로 서 있는 상태를 유지한다.

## 실험 및 결과

### 세 가지 양팔 작업(모두 네 발 착지 상태에서 완료)
- **장시간 캐비닛 작업**: 왼팔이 바구니를 들고 캐비닛까지 보행, 오른팔이 문을 열고, 바구니를 캐비닛 안에 넣음.
총 운동 시간 18.6 s(바구니 파지 7.1 s + 보행 및 문 열기 9.1 s + 넣기 2.4 s), VLM 쿼리 총 4회.
- **협동 양손 들어 올리기**: 양팔이 상자 양쪽 손잡이를 잡고 함께 들어 올림.
- **왼쪽에서 오른쪽으로 인계**: 왼팔이 파지, 중심선에서 오른팔로 전달, 오른팔이 측면에 배치.
### 비교 결과
- 단일 몸통 팔은 바구니를 들고 동시에 문을 열 수 없어 캐비닛 작업을 완료할 수 없음.
- LocoMan은 뒷다리로 서서 베이스를 고정하므로 재배치를 수행할 수 없음.
### 깊이 노이즈 강건성
| 노이즈 표준편차 | 파지 성공률 |
|-----------|-----------|
| 10 mm     | 70–74%    |
| 30 mm     | 54%       |
(8개 고정 배치 × 20개 노이즈 샘플 = 160회 시도/수준)
### 훈련 구성
도메인 무작위화: 마찰 [0.3, 1.2], 복원 계수 [0, 0.15], 추가 베이스 질량 [−1, +3] kg.
(이 절에는 전체 텍스트에서 확인할 수 없는 숫자가 포함된 문장 1개가 있어 규율에 따라 제거됨; 논문에 명시되지 않았거나 그림/표 이미지로 제공됨.)

## 경계 및 한계

- **기계적 한계**: 팔에 롤 관절이 없어 그리퍼가 접근 축을 중심으로 회전할 수 없으며, 이러한 회전이 필요한 물체(예: 주전자)는 파지할 수 없음.
- **스킬 라이브러리 적용 범위 제한**: VLM은 사전 정의된 스킬에서만 선택할 수 있고 새 스킬을 만들지 못함; 새로운 접촉점 재파지, 손 안에서 물체 회전, 운반 중 장애물 회피, 파지 실패 후 전략 변경 등은 프롬프트 추론만으로 해결할 수 없음.
- **인식이 마커에 의존**: 파지는 빨간색 마커에 의존하며, 학습 기반 검출기로는 아직 대체할 수 없음; YOLO-World와 SAM은 경계 상자/마스크만 위치시킬 수 있고, 영역 중심은 손잡이에서 13 cm 떨어져 있어 4 cm 그리퍼 개구를 훨씬 초과하므로 사용 가능한 파지점을 생성할 수 없음.
- **순수 시뮬레이션 검증**: 모든 결과는 시뮬레이션(Isaac Lab 훈련, MuJoCo 평가)에서 얻은 것으로, 실제 센서, 구동 및 접촉 역학은 테스트되지 않음.
- **미구현 기능**: stilt-like 보행 모드(q1 신장, q2 잠금 하향), 앞다리를 들어 물체를 등쪽 바구니에 넣기.

## 공학적 시사점

- **재현 시 우선 확인 사항**: 기계 파라미터(q1 스트로크 0.105 m, q4 개구 4 cm, 베이스 지면 거리 0.18 m)와 운동 정책 훈련 구성(4096 환경, 200 Hz, 다운샘플링 계수 4, PPO 5000 반복)이 일치하는지 먼저 확인—이들은 작업 공간과 동적 성능에 직접 영향을 미침.
- **가장 함정에 빠지기 쉬운 지점**: IK 솔버의 개루프 신장 초기화—여러 분산된 초기 구성에서 해를 구해 최저 잔차를 취해야 하며, 그렇지 않으면 국소 최소값에 빠져 그리퍼가 몸체 아래로 접힐 수 있음; 폐루프 추적 시 현재 구성에서 반복하여 연속성을 유지해야 함.
- **인식 모듈 주의 사항**: 빨간색 마커 임계값(R>150, G<80, B<80)은 조명에 민감하며, 부분 감지 처리(가장 최근 완전 감지 평균값 사용)는 가림 시나리오에서 편향을 유발할 수 있으므로 마커 가시성을 먼저 검증할 것.
- **VLM 지연 관리**: 플래너 지연 16–40 s/쿼리, 그 동안 로봇은 서 있는 상태 유지—하위 작업이 더 빈번한 재계획을 필요로 한다면 캐싱 또는 사전 쿼리 메커니즘을 고려해야 함.
- **양팔 협동 검증**: q3 요 관절은 양팔 협동의 핵심이므로, 재현 시 먼저 좌우 팔 작업 공간의 중심선 중첩 영역을 단독으로 검증한 후 인계와 협동 들어 올리기를 테스트할 것.
