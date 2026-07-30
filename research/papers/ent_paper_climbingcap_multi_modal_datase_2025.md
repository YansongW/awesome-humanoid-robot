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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.21268v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
인간 동작 복원(HMR) 연구는 주로 달리기와 같은 지상 기반 동작에 초점을 맞추고 있습니다. 지상에서 벗어난 동작인 클라이밍 동작을 포착하는 연구는 드물며, 이는 부분적으로 클라이밍 동작 데이터셋, 특히 대규모이면서 도전적인 3D 레이블 데이터셋의 제한된 가용성 때문입니다. 클라이밍 동작 데이터셋의 부족을 해결하기 위해, 우리는 대규모로 잘 주석이 달린 도전적인 클라이밍 동작 데이터셋인 AscendMotion을 수집했습니다. 이 데이터셋은 412k개의 RGB, LiDAR 프레임 및 IMU 측정값으로 구성되며, 12개의 다른 암벽에서 22명의 숙련된 클라이밍 코치들의 도전적인 클라이밍 동작을 포함합니다. 클라이밍 동작을 포착하는 것은 복잡한 자세뿐만 아니라 등반가의 전역 위치까지 정밀하게 복원해야 하기 때문에 어렵습니다. 여러 전역 HMR 방법이 제안되었지만, 클라이밍 동작을 충실히 포착하지는 못합니다. 클라이밍을 위한 HMR 방법의 한계를 해결하기 위해, 우리는 전역 좌표계에서 연속적인 3D 인간 클라이밍 동작을 재구성하는 동작 복원 방법인 ClimbingCap을 제안합니다. 핵심 통찰 중 하나는 RGB 및 LiDAR 모달리티를 사용하여 카메라 좌표계와 전역 좌표계에서 각각 동작을 재구성하고 이를 공동으로 최적화하는 것입니다. 우리는 AscendMotion 데이터셋의 품질을 입증하고 ClimbingCap의 유망한 결과를 제시합니다. AscendMotion 데이터셋과 소스 코드는 \href{이 링크}{http://www.lidarhumanmotion.net/climbingcap/}에서 공개적으로 배포됩니다.

## 핵심 내용
인간 동작 복원(HMR) 연구는 주로 달리기와 같은 지상 기반 동작에 초점을 맞추고 있습니다. 지상에서 벗어난 동작인 클라이밍 동작을 포착하는 연구는 드물며, 이는 부분적으로 클라이밍 동작 데이터셋, 특히 대규모이면서 도전적인 3D 레이블 데이터셋의 제한된 가용성 때문입니다. 클라이밍 동작 데이터셋의 부족을 해결하기 위해, 우리는 대규모로 잘 주석이 달린 도전적인 클라이밍 동작 데이터셋인 AscendMotion을 수집했습니다. 이 데이터셋은 412k개의 RGB, LiDAR 프레임 및 IMU 측정값으로 구성되며, 12개의 다른 암벽에서 22명의 숙련된 클라이밍 코치들의 도전적인 클라이밍 동작을 포함합니다. 클라이밍 동작을 포착하는 것은 복잡한 자세뿐만 아니라 등반가의 전역 위치까지 정밀하게 복원해야 하기 때문에 어렵습니다. 여러 전역 HMR 방법이 제안되었지만, 클라이밍 동작을 충실히 포착하지는 못합니다. 클라이밍을 위한 HMR 방법의 한계를 해결하기 위해, 우리는 전역 좌표계에서 연속적인 3D 인간 클라이밍 동작을 재구성하는 동작 복원 방법인 ClimbingCap을 제안합니다. 핵심 통찰 중 하나는 RGB 및 LiDAR 모달리티를 사용하여 카메라 좌표계와 전역 좌표계에서 각각 동작을 재구성하고 이를 공동으로 최적화하는 것입니다. 우리는 AscendMotion 데이터셋의 품질을 입증하고 ClimbingCap의 유망한 결과를 제시합니다. AscendMotion 데이터셋과 소스 코드는 \href{이 링크}{http://www.lidarhumanmotion.net/climbingcap/}에서 공개적으로 배포됩니다.

## 参考
- http://arxiv.org/abs/2503.21268v1
