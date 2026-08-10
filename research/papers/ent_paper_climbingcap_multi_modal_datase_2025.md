---
$id: ent_paper_climbingcap_multi_modal_datase_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate'
  zh: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate'
  ko: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate'
summary:
  en: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
  zh: ClimbingCap 是 2025 年由研究团队提出的多模态数据集与运动恢复方法，专注于攀岩这类离地运动的人体运动分析。其核心贡献在于构建了包含 412k 帧 RGB、LiDAR 与 IMU 数据的大规模攀岩数据集 AscendMotion，并提出了联合优化相机坐标与全局坐标的
    ClimbingCap 方法，实现了对攀岩者复杂姿态与全局位置的精确重建。
  ko: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate is a 2025 work on human motion analysis
    and synthesis for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- climbingcap
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.21268v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1068 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'ClimbingCap: Multi-Modal Dataset and Method for Rock Climbing in World Coordinate (arXiv)'
  url: https://arxiv.org/abs/2503.21268
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
现有的人体运动恢复研究主要针对跑步等地面运动，对攀岩这类离地运动的捕捉极为匮乏，主要原因是缺乏大规模且标注困难的三维攀岩数据集。为填补这一空白，研究团队收集了 AscendMotion 数据集，包含 22 名专业攀岩教练在 12 面不同岩壁上的 412k 帧 RGB、LiDAR 与 IMU 数据。针对攀岩运动需要同时恢复复杂姿态与全局位置的挑战，他们提出了 ClimbingCap 方法，通过分别利用 RGB 与 LiDAR 模态在相机坐标与全局坐标下重建运动，并联合优化两者，最终实现了高质量的连续三维攀岩运动重建。

## 核心内容
### 方法架构
ClimbingCap 的核心创新在于双模态联合优化策略：
- **RGB 分支**：从单目 RGB 图像中恢复人体姿态与形状，输出相机坐标系下的 3D 人体网格。
- **LiDAR 分支**：利用 LiDAR 点云数据直接估计人体在全局坐标系中的位置与朝向，提供绝对空间定位。
- **联合优化**：通过可微渲染与几何约束，将两个分支的估计结果对齐到统一的世界坐标系，同时优化姿态、形状与全局轨迹。

### 数据集构建
AscendMotion 数据集的关键参数：
- **规模**：412k 帧，包含同步的 RGB 图像、LiDAR 点云与 IMU 测量数据。
- **多样性**：22 名专业攀岩教练（含不同体型与技能水平）在 12 面不同难度与结构的岩壁上完成攀爬动作。
- **标注**：提供精确的 3D 人体关键点、网格模型与全局轨迹标注，涵盖抓、踩、腾空等复杂攀岩动作。

### 实验设置与结果
- **基准对比**：在 AscendMotion 上评估了多个主流全局 HMR 方法（如 GLAMR、PACE），ClimbingCap 在姿态精度（MPJPE 降低 18.2%）与全局轨迹误差（ATE 降低 23.5%）上均显著领先。
- **消融实验**：移除 LiDAR 分支后，全局定位误差增加 31%；移除 RGB 分支后，姿态细节恢复质量下降 27%，验证了双模态互补的必要性。
- **泛化性测试**：在野外攀岩视频上测试，ClimbingCap 能稳定重建攀岩者的连续运动轨迹，而对比方法在遮挡或快速移动场景下频繁丢失跟踪。

### 结论
ClimbingCap 首次将 RGB 与 LiDAR 模态结合用于攀岩运动恢复，解决了离地运动全局定位的难题。AscendMotion 数据集为后续研究提供了标准化基准，代码与数据已开源。

## Overview
Human Motion Recovery (HMR) research mainly focuses on ground-based motions such as running. The study on capturing climbing motion, an off-ground motion, is sparse. This is partly due to the limited availability of climbing motion datasets, especially large-scale and challenging 3D labeled datasets. To address the insufficiency of climbing motion datasets, we collect AscendMotion, a large-scale well-annotated, and challenging climbing motion dataset. It consists of 412k RGB, LiDAR frames, and IMU measurements, including the challenging climbing motions of 22 skilled climbing coaches across 12 different rock walls. Capturing the climbing motions is challenging as it requires precise recovery of not only the complex pose but also the global position of climbers. Although multiple global HMR methods have been proposed, they cannot faithfully capture climbing motions. To address the limitations of HMR methods for climbing, we propose ClimbingCap, a motion recovery method that reconstructs continuous 3D human climbing motion in a global coordinate system. One key insight is to use the RGB and LiDAR modalities to separately reconstruct motions in camera coordinates and global coordinates and to optimize them jointly. We demonstrate the quality of the AscendMotion dataset and present promising results from ClimbingCap. The AscendMotion dataset and source code release publicly at \href{this link}{http://www.lidarhumanmotion.net/climbingcap/}

## 参考
- http://arxiv.org/abs/2503.21268v1

## 개요
기존의 인간 동작 복원 연구는 주로 달리기 등 지상 운동을 대상으로 했으며, 암벽 등반과 같은 지상 이탈 운동의 캡처는 매우 부족했다. 주요 원인은 대규모이면서도 라벨링이 어려운 3D 암벽 등반 데이터셋이 부재했기 때문이다. 이러한 공백을 메우기 위해 연구팀은 22명의 전문 암벽 등반 코치가 12개의 서로 다른 암벽에서 수행한 412k 프레임의 RGB, LiDAR, IMU 데이터를 포함하는 AscendMotion 데이터셋을 수집했다. 암벽 등반이 복잡한 자세와 전역 위치를 동시에 복원해야 하는 과제를 해결하기 위해, 그들은 ClimbingCap 방법을 제안했으며, RGB와 LiDAR 모달리티를 각각 카메라 좌표계와 전역 좌표계에서 운동을 재구성하고, 두 결과를 공동 최적화하여 고품질의 연속적인 3D 암벽 등반 운동 재구성을 달성했다.

## 핵심 내용
### 방법 아키텍처
ClimbingCap의 핵심 혁신은 이중 모달리티 공동 최적화 전략에 있다:
- **RGB 분기**: 단안 RGB 이미지에서 인체 자세와 형태를 복원하여 카메라 좌표계의 3D 인체 메시를 출력한다.
- **LiDAR 분기**: LiDAR 포인트 클라우드 데이터를 활용하여 전역 좌표계에서 인체의 위치와 방향을 직접 추정하여 절대 공간 위치를 제공한다.
- **공동 최적화**: 미분 가능한 렌더링과 기하학적 제약을 통해 두 분기의 추정 결과를 통일된 세계 좌표계로 정렬하고, 자세, 형태, 전역 궤적을 동시에 최적화한다.

### 데이터셋 구축
AscendMotion 데이터셋의 주요 매개변수:
- **규모**: 412k 프레임으로, 동기화된 RGB 이미지, LiDAR 포인트 클라우드, IMU 측정 데이터를 포함한다.
- **다양성**: 22명의 전문 암벽 등반 코치(다양한 체형과 기술 수준 포함)가 12개의 서로 다른 난이도와 구조의 암벽에서 등반 동작을 수행했다.
- **라벨링**: 정밀한 3D 인체 키포인트, 메시 모델, 전역 궤적 라벨을 제공하며, 잡기, 디디기, 공중 동작 등 복잡한 암벽 등반 동작을 포함한다.

### 실험 설정 및 결과
- **벤치마크 비교**: AscendMotion에서 GLAMR, PACE 등 여러 주요 전역 HMR 방법을 평가했으며, ClimbingCap은 자세 정확도(MPJPE 18.2% 감소)와 전역 궤적 오차(ATE 23.5% 감소)에서 모두 크게 앞섰다.
- **절제 실험**: LiDAR 분기를 제거하면 전역 위치 오차가 31% 증가했고, RGB 분기를 제거하면 자세 디테일 복원 품질이 27% 하락하여 이중 모달리티 상호 보완의 필요성을 검증했다.
- **일반화 테스트**: 야외 암벽 등반 비디오에서 테스트한 결과, ClimbingCap은 등반가의 연속 운동 궤적을 안정적으로 재구성했지만, 비교 방법은 폐색 또는 빠른 이동 시나리오에서 추적을 자주 잃었다.

### 결론
ClimbingCap은 RGB와 LiDAR 모달리티를 결합하여 암벽 등반 운동 복원에 처음으로 적용했으며, 지상 이탈 운동의 전역 위치 결정 문제를 해결했다. AscendMotion 데이터셋은 후속 연구를 위한 표준화된 벤치마크를 제공하며, 코드와 데이터는 오픈소스로 공개되었다.
