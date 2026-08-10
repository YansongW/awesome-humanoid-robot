---
$id: ent_paper_optimization_sim_real_transfer_humanoid_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimization of sim-to-real transfer in the humanoid robot NICO
  zh: Optimization of sim-to-real transfer in the humanoid robot NICO
  ko: Optimization of sim-to-real transfer in the humanoid robot NICO
summary:
  en: Robotic grasping requires accurate coordination between visual perception, object localization, inverse kinematics,
    and hand control. However, when movements planned in simulation are executed on a physical robot, the sim-to-real gap
    can cause small positioning errors that prevent successful grasping. In our previous work, we introduced a low-cost haptic
    calibration method that improved 2D.
  zh: 本文针对 NICO 人形机器人的 sim-to-real 迁移问题，将基于触摸屏的标定方法从 2D 到达扩展到桌面物体抓取，构建了无需 RGB-D 相机或外部追踪的完整抓取流水线。核心贡献在于系统比较了三种标定修正模型（M1 基线、M2
    部分非线性、M3 全非线性）与一种视觉反馈手部对齐策略（M4），并验证了视觉反馈在提升抓取成功率上的显著优势。
  ko: Robotic grasping requires accurate coordination between visual perception, object localization, inverse kinematics,
    and hand control. However, when movements planned in simulation are executed on a physical robot, the sim-to-real gap
    can cause small positioning errors that prevent successful grasping. In our previous work, we introduced a low-cost haptic
    calibration method that improved 2D.
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
- optimization
- sim
- real
- transfer
- humanoid
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Deep-read batch3-continuation (2026-08-05), source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh
    six-section interpretation by DeepSeek (T<=0.3) under programmatic number whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量三）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: arXiv:2607.18210 Optimization of sim-to-real transfer in the humanoid robot NICO
  url: https://arxiv.org/abs/2607.18210
  date: '2026-07-20'
  accessed_at: '2026-08-05'
---

## 概述

本文针对 NICO 人形机器人的 sim-to-real 迁移问题，将基于触摸屏的标定方法从 2D 到达扩展到桌面物体抓取，构建了无需 RGB-D 相机或外部追踪的完整抓取流水线。核心贡献在于系统比较了三种标定修正模型（M1 基线、M2 部分非线性、M3 全非线性）与一种视觉反馈手部对齐策略（M4），并验证了视觉反馈在提升抓取成功率上的显著优势。

## 它改变了什么

这项工作真正改变了什么？它把 sim-to-real 问题从“静态标定”推进到了“动态闭环”的层面。以往的研究（包括作者先前的工作）聚焦于通过标定减少仿真到实体的系统性偏差，但抓取任务中，物体定位误差、手部执行误差和视觉感知误差是耦合的，单纯依赖开环标定无法应对这些复合误差。本文的转变在于：不再试图让仿真模型“完美”匹配实体，而是引入视觉反馈作为在线修正机制，让机器人根据实际观测调整手部位置，从而绕开了标定模型在训练区域外失效的根本缺陷。

从问题动机看，作者敏锐地识别出 M3 神经网络模型在训练数据覆盖区域外外推不可靠（平均位移从区域内的 2.14 cm 增至区域外的 5.45 cm），这直接否定了纯标定路线在完整工作空间内的可行性。因此，他们将视觉反馈从辅助手段提升为核心策略，这不仅是方法上的改进，更是对 sim-to-real 问题本质的重新定义——与其追求更精确的模型，不如让系统具备感知-行动闭环的鲁棒性。

## 方法拆解

### 整体流水线
相机图像 → YOLO 检测物体图像坐标 → 立体视觉估计深度 → 经头部运动链变换到机器人坐标系 → 用修正模型（M1/M2/M3）或视觉反馈（M4）变换为仿真目标位置 → 偏航修正提供手掌朝向 → IK 求解关节角 → 通过 NicoMotion 在实体机器人执行。

### 标定模型（M1-M3）
- **M1（基线）**：分段线性映射，手动对齐仿真和测量高度值后插值。
- **M2（部分非线性）**：水平目标坐标由 MLP 预测，高度分量仍用插值。设计理由：水平方向误差主要来自相机畸变和运动学偏差，非线性映射更有效；高度方向相对稳定，插值足够。
- **M3（全非线性）**：直接预测修正后的三维目标位置。设计理由：完全解耦三个维度的耦合误差，但代价是外推能力差。

### 视觉反馈手部对齐（M4）
- 迭代公式：p_IK^k = p_IK^(k-1) + a_k (p_obj − p_hand)，步长 a_k = 1/(2^(k-1))。
- 关键设计：步长递减防止手接近物体时振荡；对齐阈值设为 1 cm；对齐阶段手掌朝向相机旋转，确保 YOLO 稳定检测手掌中心。
- M4 不使用任何标定修正，完全依赖视觉反馈闭环。

### 任务特定修正
- 垂直目标修正和手掌偏航角修正：在机器人工作空间不规则参考点手动测量，任意目标位置用径向基函数（RBF）插值估计。
- 滚动和俯仰角固定，保持自上而下抓取姿态。

### 视觉模块细节
- YOLO 检测：自定义数据集 442 张图像，8 类标注，80:20 训练/验证划分。YOLO11m 精度最高（All mAP50–95 0.823），但选 YOLO12s（0.806，推理 10.86 ms）作为精度与实时性的折中。
- 立体视觉：棋盘格标定获取内参和畸变系数，去畸变校正后计算视差图估计深度。固定头部版本平均 2D 定位误差 0.76 cm，但存在相机过热导致的定位漂移（最远约 6 cm），需额外修正。

## 关键创新

1. **视觉反馈作为标定的替代而非补充**：M4 完全抛弃标定修正，仅依赖视觉闭环，却取得了最高全工作空间成功率（72.7%）。这颠覆了“标定精度决定抓取成功率”的传统假设，证明了在线感知-行动闭环的鲁棒性远超任何离线标定模型。

2. **手部边界框的刻意定义**：将 YOLO 检测的手部边界框定义在手掌中心区域，使质心更对应手部对齐位置。这一细节看似简单，却直接解决了视觉反馈中“检测到手但位置不对齐”的常见问题，是工程实践中的关键创新。

3. **步长递减的迭代对齐策略**：a_k = 1/(2^(k-1)) 的几何递减步长，在保证收敛速度的同时避免了手接近物体时的振荡。这种简单而有效的控制策略，比复杂的自适应控制更易于在实体机器人上复现和调参。

## 实验与结果

### 抓取实验统计（表 2 汇总）

| 指标 | M1（基线） | M2 | M3 | M4（视觉反馈） |
|------|-----------|-----|-----|----------------|
| Hand SV OK | – | – | – | 77.3% (17/22) |
| Grasp Rate (SV OK) | – | – | – | 94.1% (48/51) |
| Grasp Rate (NN Area) | 10.0% (3/30) | 93.3% (28/30) | 96.7% (29/30) | 83.3% (25/30) |
| Grasp Rate (All) | 16.7% (11/66) | 48.5% (32/66) | 57.6% (38/66) | 72.7% (48/66) |

### 关键结果解读
- **M3 在 NN 修正区域内表现优异（96.7%）**，但全工作空间成功率骤降至 57.6%，验证了外推失效问题（区域内平均位移 2.14 cm vs 区域外 5.45 cm）。
- **M4 的全工作空间成功率（72.7%）显著优于所有标定模型**，但受限于立体视觉手部定位：仅 17/22 个位置正确定位手。若仅考虑手定位正确的尝试，成功率高达 94.1%，说明主要瓶颈在感知而非控制。
- **对比文献**：文献 [4] 在 NICO 上最佳模型成功率 80.3%，文献 [8] 零样本 70%（微调后 91%），文献 [13] 未见对抗物体 83%。本文 M4 的 72.7% 在无外部追踪、无大量真实数据微调的前提下具有竞争力。

## 边界与局限

- **立体视觉手部定位是最大瓶颈**：手后背景过远时手位置被强烈高估，导致 5/22 个位置手定位失败。作者未尝试改进手部分割或深度估计，这直接限制了 M4 的上限。
- **M3 外推不可靠**：训练数据覆盖区域外通常过度修正，作者未提出解决方案，仅建议使用视觉反馈规避。
- **未训练端到端抓取策略**：仍依赖显式定位、IK 和标定修正，系统复杂度高，模块间误差累积问题未彻底解决。
- **评估场景单一**：仅使用单个物体（毛绒番茄），未验证多物体、不同形状/材质/朝向的泛化性。
- **与其他研究比较困难**：平台、物体、传感器和评估协议差异大，数字对比仅具参考意义。

## 工程启示

- **优先采用视觉反馈闭环而非追求标定精度**：M4 的结果表明，在 sim-to-real 场景中，在线感知-行动闭环的鲁棒性远超离线标定。复现时应先确保视觉检测和立体定位的可靠性，再考虑标定修正。
- **注意立体视觉的失效模式**：手后背景过远时深度估计会严重高估，这是 M4 的主要失败原因。复现时建议改进手部分割（如使用深度感知的检测器）或限制工作空间背景复杂度。
- **M3 类神经网络模型仅适用于训练覆盖区域**：若必须使用标定模型，务必严格限制目标位置在训练数据范围内，并监控输入-输出位移（超过 2.14 cm 即视为外推风险）。
- **YOLO 选型建议**：YOLO12s 在精度（All 0.806）和推理时间（10.86 ms）间取得最佳平衡，适合实时抓取。若对精度要求更高可换 YOLO11m（0.823），但推理时间增至 20.45 ms。
- **最容易踩坑的地方**：相机过热导致的定位漂移（最远约 6 cm）在长时间运行中不可忽视，需设计周期性校准或漂移补偿机制；手部边界框定义必须与对齐目标一致，否则视觉反馈会收敛到错误位置。

## Overview
Robotic grasping requires accurate coordination between visual perception, object localization, inverse kinematics, and hand control. However, when movements planned in simulation are executed on a physical robot, the sim-to-real gap can cause small positioning errors that prevent successful grasping. In our previous work, we introduced a low-cost haptic calibration method that improved 2D reaching accuracy of the humanoid robot NICO. In this paper, we extend this approach from reaching to tabletop object grasping by adding YOLO-based object and hand detection, stereo vision-based localization using the robot's built-in low-resolution fisheye cameras, and task-specific corrections for grasp execution. Together, these components form a novel calibration-based grasping pipeline that does not require RGB-D cameras, motion capture, or external tracking systems. We also implemented a visual feedback model that aligns the robot hand with the detected object before grasping. Our results show that the fully nonlinear calibration model achieved the best performance inside the calibrated area, while the visual feedback model achieved the highest overall grasping success across the full tabletop workspace.

## 参考
- https://arxiv.org/abs/2607.18210

## 개요

본 논문은 NICO 휴머노이드 로봇의 sim-to-real 전이 문제에 대해, 터치스크린 기반 캘리브레이션 방법을 2D 도달에서 테이블 위 물체 파지로 확장하여 RGB-D 카메라나 외부 추적 없이 완전한 파지 파이프라인을 구축했다. 핵심 기여는 세 가지 캘리브레이션 보정 모델(M1 베이스라인, M2 부분 비선형, M3 완전 비선형)과 한 가지 시각 피드백 손 정렬 전략(M4)을 체계적으로 비교하고, 시각 피드백이 파지 성공률 향상에 현저한 이점을 제공함을 검증한 것이다.

## 그것이 무엇을 바꾸었는가

이 작업이 실제로 바꾼 것은 무엇인가? 그것은 sim-to-real 문제를 "정적 캘리브레이션"에서 "동적 폐루프" 수준으로 끌어올린 것이다. 기존 연구(저자의 이전 작업 포함)는 캘리브레이션을 통해 시뮬레이션에서 실물로의 체계적 편차를 줄이는 데 초점을 맞췄지만, 파지 작업에서는 물체 위치 오차, 손 실행 오차, 시각 인식 오차가 결합되어 있어 단순히 개루프 캘리브레이션에 의존해서는 이러한 복합 오차를 대응할 수 없다. 본 논문의 전환점은 시뮬레이션 모델을 실물에 "완벽히" 맞추려 하지 않고, 시각 피드백을 온라인 보정 메커니즘으로 도입하여 로봇이 실제 관측에 따라 손 위치를 조정하게 함으로써, 캘리브레이션 모델이 훈련 영역 밖에서失效하는 근본적 결함을 우회한 것이다.

문제 동기 측면에서, 저자는 M3 신경망 모델이 훈련 데이터 커버리지 영역 밖에서 외삽이 불안정하다는 점(평균 변위가 영역 내 2.14 cm에서 영역 외 5.45 cm로 증가)을 예리하게 포착했으며, 이는 전체 작업 공간에서 순수 캘리브레이션 경로의 실행 가능성을 직접적으로 부정한다. 따라서 그들은 시각 피드백을 보조 수단에서 핵심 전략으로 승격시켰으며, 이는 방법론적 개선일 뿐만 아니라 sim-to-real 문제 본질의 재정의다—더 정밀한 모델을 추구하기보다 시스템이 지각-행동 폐루프의 견고성을 갖추게 하는 것이다.

## 방법 분해

### 전체 파이프라인
카메라 이미지 → YOLO 물체 이미지 좌표 검출 → 스테레오 비전 깊이 추정 → 머리 운동 사슬을 통해 로봇 좌표계로 변환 → 보정 모델(M1/M2/M3) 또는 시각 피드백(M4)으로 시뮬레이션 목표 위치 변환 → 요(yaw) 보정으로 손바닥 방향 제공 → IK로 관절각 계산 → NicoMotion을 통해 실물 로봇에서 실행.

### 캘리브레이션 모델(M1-M3)
- **M1(베이스라인)**: 구간별 선형 매핑, 시뮬레이션과 측정 높이 값을 수동 정렬 후 보간.
- **M2(부분 비선형)**: 수평 목표 좌표는 MLP로 예측, 높이 성분은 여전히 보간 사용. 설계 근거: 수평 방향 오차는 주로 카메라 왜곡과 운동학 편차에서 발생하므로 비선형 매핑이 더 효과적; 높이 방향은 상대적으로 안정적이어서 보간으로 충분.
- **M3(완전 비선형)**: 보정된 3D 목표 위치를 직접 예측. 설계 근거: 세 차원의 결합 오차를 완전히 분리하지만, 대가로 외삽 능력이 떨어짐.

### 시각 피드백 손 정렬(M4)
- 반복 공식: p_IK^k = p_IK^(k-1) + a_k (p_obj − p_hand), 스텝 크기 a_k = 1/(2^(k-1)).
- 핵심 설계: 스텝 크기 감소로 손이 물체에 가까워질 때 진동 방지; 정렬 임계값은 1 cm로 설정; 정렬 단계에서 손바닥이 카메라를 향해 회전하여 YOLO가 손바닥 중심을 안정적으로 검출하도록 보장.
- M4는 어떤 캘리브레이션 보정도 사용하지 않고 완전히 시각 피드백 폐루프에 의존.

### 작업 특정 보정
- 수직 목표 보정 및 손바닥 요 각도 보정: 로봇 작업 공간의 불규칙한 기준점에서 수동 측정, 임의 목표 위치는 방사 기저 함수(RBF) 보간으로 추정.
- 롤과 피치 각도는 고정하여 위에서 아래로 파지 자세 유지.

### 시각 모듈 세부 사항
- YOLO 검출: 맞춤 데이터셋 442개 이미지, 8개 클래스 주석, 80:20 훈련/검증 분할. YOLO11m 정확도 최고(All mAP50–95 0.823)지만, YOLO12s(0.806, 추론 10.86 ms)를 정확도와 실시간성의 절충으로 선택.
- 스테레오 비전: 체커보드 캘리브레이션으로 내부 파라미터와 왜곡 계수 획득, 왜곡 보정 후 시차 맵 계산으로 깊이 추정. 고정 헤드 버전 평균 2D 위치 오차 0.76 cm지만, 카메라 과열로 인한 위치 드리프트(최대 약 6 cm)가 있어 추가 보정 필요.

## 핵심 혁신

1. **캘리브레이션의 대체로서의 시각 피드백(보완이 아닌)**: M4는 캘리브레이션 보정을 완전히 버리고 시각 폐루프에만 의존하지만, 전체 작업 공간 성공률(72.7%)에서 최고를 기록했다. 이는 "캘리브레이션 정밀도가 파지 성공률을 결정한다"는 전통적 가정을 뒤엎고, 온라인 지각-행동 폐루프의 견고성이 어떤 오프라인 캘리브레이션 모델보다 훨씬 뛰어남을 증명했다.

2. **손 경계 상자의 의도적 정의**: YOLO가 검출하는 손 경계 상자를 손바닥 중심 영역으로 정의하여, 질량 중심이 손 정렬 위치에 더 잘 대응하도록 했다. 이 세부 사항은 단순해 보이지만, 시각 피드백에서 "손은 검출했지만 위치가 정렬되지 않는" 일반적인 문제를 직접 해결하는 공학 실무의 핵심 혁신이다.

3. **스텝 크기 감소 반복 정렬 전략**: a_k = 1/(2^(k-1))의 기하 감소 스텝 크기는 수렴 속도를 보장하면서 손이 물체에 가까워질 때의 진동을 방지한다. 이 단순하면서도 효과적인 제어 전략은 복잡한 적응 제어보다 실물 로봇에서 재현하고 튜닝하기 쉽다.

## 실험과 결과

### 파지 실험 통계(표 2 요약)

| 지표 | M1(베이스라인) | M2 | M3 | M4(시각 피드백) |
|------|-----------|-----|-----|----------------|
| Hand SV OK | – | – | – | 77.3% (17/22) |
| Grasp Rate (SV OK) | – | – | – | 94.1% (48/51) |
| Grasp Rate (NN Area) | 10.0% (3/30) | 93.3% (28/30) | 96.7% (29/30) | 83.3% (25/30) |
| Grasp Rate (All) | 16.7% (11/66) | 48.5% (32/66) | 57.6% (38/66) | 72.7% (48/66) |

### 핵심 결과 해석
- **M3는 NN 보정 영역 내에서 우수한 성능(96.7%)**을 보이지만, 전체 작업 공간 성공률은 57.6%로 급락하여 외삽 실패 문제(영역 내 평균 변위 2.14 cm vs 영역 외 5.45 cm)를 검증했다.
- **M4의 전체 작업 공간 성공률(72.7%)은 모든 캘리브레이션 모델보다 현저히 우수**하지만, 스테레오 비전 손 위치 파악에 제한을 받는다: 22개 위치 중 17개만 손을 정확히 위치 파악. 손 위치가 정확한 시도만 고려하면 성공률이 94.1%에 달하며, 주요 병목이 제어가 아닌 인식에 있음을 시사한다.
- **문헌 비교**: 문헌 [4]는 NICO에서 최고 모델 성공률 80.3%, 문헌 [8]은 제로샷 70%(미세 조정 후 91%), 문헌 [13]은 미지의 적대적 물체 83%. 본 논문 M4의 72.7%는 외부 추적 없이, 대량의 실제 데이터 미세 조정 없이 경쟁력 있는 수치다.

## 경계와 한계

- **스테레오 비전 손 위치 파악이 최대 병목**: 손 뒤 배경이 너무 멀면 손 위치가 강하게 과대평가되어 22개 위치 중 5개에서 손 위치 파악 실패. 저자는 손 분할이나 깊이 추정 개선을 시도하지 않았으며, 이는 M4의 상한을 직접 제한한다.
- **M3 외삽 불안정**: 훈련 데이터 커버리지 영역 밖에서 일반적으로 과도 보정이 발생하며, 저자는 해결책을 제시하지 않고 시각 피드백 사용을 권장할 뿐이다.
- **엔드투엔드 파지 전략 미훈련**: 여전히 명시적 위치 파악, IK, 캘리브레이션 보정에 의존하며, 시스템 복잡도가 높고 모듈 간 오차 누적 문제가 완전히 해결되지 않았다.
- **평가 시나리오 단일**: 단일 물체(플러시 토마토)만 사용하여 다중 물체, 다양한 형태/재질/방향의 일반화를 검증하지 않았다.
- **다른 연구와 비교 어려움**: 플랫폼, 물체, 센서, 평가 프로토콜의 차이가 커서 숫자 비교는 참고용일 뿐이다.

## 공학적 시사점

- **캘리브레이션 정밀도 추구보다 시각 피드백 폐루프 우선 채택**: M4의 결과는 sim-to-real 시나리오에서 온라인 지각-행동 폐루프의 견고성이 오프라인 캘리브레이션보다 훨씬 뛰어남을 보여준다. 재현 시 시각 검출과 스테레오 위치 파악의 신뢰성을 먼저 확보한 다음 캘리브레이션 보정을 고려해야 한다.
- **스테레오 비전의 실패 모드 주의**: 손 뒤 배경이 너무 멀면 깊이 추정이 심각하게 과대평가되며, 이는 M4의 주요 실패 원인이다. 재현 시 손 분할 개선(예: 깊이 인식 검출기 사용)이나 작업 공간 배경 복잡도 제한을 권장한다.
- **M3 유형 신경망 모델은 훈련 커버리지 영역에만 적용**: 캘리브레이션 모델을 반드시 사용해야 한다면 목표 위치를 훈련 데이터 범위 내로 엄격히 제한하고, 입력-출력 변위(2.14 cm 초과 시 외삽 위험으로 간주)를 모니터링해야 한다.
- **YOLO 선택 권장**: YOLO12s는 정확도(All 0.806)와 추론 시간(10.86 ms) 사이에서 최적의 균형을 이루며 실시간 파지에 적합하다. 정확도 요구가 더 높으면 YOLO11m(0.823)으로 교체할 수 있지만 추론 시간은 20.45 ms로 증가한다.
- **가장 함정에 빠지기 쉬운 부분**: 카메라 과열로 인한 위치 드리프트(최대 약 6 cm)는 장시간 실행에서 무시할 수 없으며, 주기적 캘리브레이션이나 드리프트 보상 메커니즘 설계가 필요하다; 손 경계 상자 정의는 정렬 목표와 일치해야 하며, 그렇지 않으면 시각 피드백이 잘못된 위치로 수렴한다.
