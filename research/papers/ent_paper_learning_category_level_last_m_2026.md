---
$id: ent_paper_learning_category_level_last_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
  zh: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
  ko: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance
summary:
  en: 'arXiv:2512.11173v4 Announce Type: replace Abstract: Achieving precise positioning of the mobile manipulator''s base
    is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee
    coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This
    gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting
    in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for
    last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only
    RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view
    RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation
    module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world
    data from a single object instance within a category, the system generalizes to unseen object instances across diverse
    environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics:
    an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well
    the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42%
    success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter
    navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward
    unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/'
  zh: 本文提出一种面向物体中心的模仿学习框架，用于解决移动操作机器人的“最后一米”精确定位问题。该方法由RPM Lab团队开发，仅依靠RGB相机观测，无需深度、LiDAR或地图先验，即可实现类别级别的精确定位，在未见目标物体上达到74.58%的边缘对齐成功率和89.42%的物体对齐成功率。
  ko: 'arXiv:2512.11173v4 Announce Type: replace Abstract: Achieving precise positioning of the mobile manipulator''s base
    is essential for successful manipulation actions that follow. Most of the RGB-based navigation systems only guarantee
    coarse, meter-level accuracy, making them less suitable for the precise positioning phase of mobile manipulation. This
    gap prevents manipulation policies from operating within the distribution of their training demonstrations, resulting
    in frequent execution failures. We address this gap by introducing an object-centric imitation learning framework for
    last-meter navigation, enabling a quadruped mobile manipulator robot to achieve manipulation-ready positioning using only
    RGB observations from its onboard cameras. Our method conditions the navigation policy on three inputs: goal images, multi-view
    RGB observations from the onboard cameras, and a text prompt specifying the target object. A language-driven segmentation
    module and a spatial score-matrix decoder then supply explicit object grounding and relative pose reasoning. Using real-world
    data from a single object instance within a category, the system generalizes to unseen object instances across diverse
    environments with challenging lighting and background conditions. To comprehensively evaluate this, we introduce two metrics:
    an edge-alignment metric, which uses ground truth orientation, and an object-alignment metric, which evaluates how well
    the robot visually faces the target. Under these metrics, our policy achieves 74.58% success in edge-alignment and 89.42%
    success in object-alignment when positioning relative to unseen target objects. These results show that precise last-meter
    navigation can be achieved at a category-level without depth, LiDAR, or map priors, enabling a scalable pathway toward
    unified mobile manipulation. Project page: https://rpm-lab-umn.github.io/category-level-last-meter-nav/'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- learning_category_level_last_m
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.11173v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1029 chars, DeepSeek). [2026-08-21] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: Learning Category-level Last-meter Navigation from RGB Demonstrations of a Single-instance (arXiv)
  url: https://arxiv.org/abs/2512.11173
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述

本文提出物体中心模仿学习框架，以仅RGB观测实现类别级“最后一米导航”，由明尼苏达大学团队完成。核心贡献在于将导航精度从米级提升至厘米级，通过冻结DINOv2编码器、两阶段分割与显式得分矩阵，在未见实例上达到96.94%物体对齐成功率。

## 它改变了什么

现有RGB导航系统普遍将成功定义为在目标约1米内停止，这一粗粒度精度与移动操作所需的厘米级定位之间存在根本性不匹配。操作策略仅在机器人位姿落入训练演示分布内时可靠，导航误差直接导致下游任务频繁失败。作者敏锐地指出，问题不在于全局路径规划，而在于“最后一米”——即从全局导航切换到局部操作之间的过渡阶段，这一阶段需要同时满足位置与方向的精确对齐。

该工作真正改变了“导航与操作精度鸿沟”的处理方式：不再依赖高分辨率地图、NeRF环境先验或深度/LiDAR等额外传感模态，而是证明仅凭RGB观测与类别级物体知识即可实现足够精确的定位。这打破了传统精确导航对稠密环境重建的依赖，将问题重新定义为“以物体为中心的条件行为克隆”，而非“更精确的地图构建”。其隐含假设——目标保持可见且路径无遮挡——虽简化了问题，但为后续研究提供了清晰的可扩展基线。

## 方法拆解

### 问题形式化
策略 π: (O_t, O_goal, φ_text) → A_t，其中 O_t 为当前多视角RGB观测（覆盖360度，O ∈ {I_front, I_right, I_back, I_left}），O_goal 为目标观测，φ_text 为文本提示。动作 A_t 由三个运动原语组成：前向（x）、横向（y）、旋转（θ），每个离散化为负、零、正三类。

### 架构三模块
- **视觉编码器**：DINOv2，冻结预训练形式，不微调。每张640×480图像处理为ℝ^{34×34×1024}嵌入。选择冻结策略旨在降低计算成本、防止小数据集过拟合，并保留大规模预训练的泛化特性。
- **分割模块**：两阶段文本驱动分割。OwlV2检测语言提示指定的物体并生成边界框，SAM2细化生成分割掩码。
- **动作解码器**：边界框坐标经MLP投影为ℝ^{4096}框嵌入；掩码嵌入池化、展平后计算ℝ^{64×64}得分矩阵；展平得分矩阵与框嵌入拼接，经MLP输出三个3类分类头。

### 关键设计决策
- **显式得分矩阵**：建模当前与目标视图的空间关系，作者认为其优于标准交叉注意力，因后者难以显式编码相对位置变化。
- **辅助停止机制**：基于预测边界框和分割目标物体的质心终止rollout，解决纯学习策略难以可靠产生连续停止动作的问题。终止条件为模型连续预测两个停止动作 A_t ∈ {0,0,0}。
- **目标条件化**：策略同时以目标观测和文本提示为条件，目标观测可在映射阶段捕获或从操作策略训练数据集中获取。

### 训练配置
- 损失函数：最小化专家动作负对数似然 L(ω) = -E[log π_ω(A_t* | O_t, O_goal, φ_text)]。
- 数据：715条轨迹，伪目标观测从同一轨迹未来时间步采样。
- 终止容差：平移0.2米，方向±6°。

## 关键创新

1. **类别级泛化的RGB-only精确导航**：以往精确导航要么绑定特定实例（需重新训练），要么依赖额外传感模态。本工作首次证明，仅凭RGB与文本提示，策略可泛化到未见实例（物体对齐96.94%）与未见环境（室内91%），这得益于冻结DINOv2的强语义先验与分割模块的类别级物体理解。

2. **显式得分矩阵替代交叉注意力**：标准Transformer交叉注意力在视觉导航中难以捕捉精细空间关系。作者设计的ℝ^{64×64}得分矩阵直接建模当前视图与目标视图的逐像素对应关系，这一归纳偏置显著提升了定位精度，且计算开销可控。

3. **辅助停止机制解决学习策略的“最后一帧”问题**：纯行为克隆策略常因停止动作在数据中占比不均而难以可靠终止。通过几何线索（边界框与质心）显式判断到达状态，绕开了学习停止策略的脆弱性，这一设计对实际部署至关重要。

## 实验与结果

### 训练环境（seen instance）
| 指标 | 成功率 |
|------|--------|
| 边缘对齐 | 97.96% |
| 物体对齐 | 100% |

### 未见实例（unseen instances）
| 指标 | 成功率 |
|------|--------|
| 边缘对齐 | 73.47% |
| 物体对齐 | 96.94% |

### 未见环境
| 环境 | 边缘对齐 | 物体对齐 |
|------|----------|----------|
| 室外 | 85% | 95% |
| 室内（平均） | 79% | 91% |

### 定性研究与基线
- 十种未见场景平均成功率75%，但场景3（昏暗环境）成功率0%，凸显分割质量对光照的敏感性。
- 基线对比：DinoTxtAttention在seen和unseen物体上均零成功；DinoScore优于DinoAttention，验证得分矩阵设计的有效性。

结果含义：物体对齐成功率显著高于边缘对齐，说明策略在位置精度上表现优异，但方向对齐（±8°内）仍是瓶颈。昏暗场景的完全失败直接指向分割模块的脆弱性，而非导航策略本身。

## 边界与局限

- **分割质量依赖**：系统性能直接受限于OwlV2与SAM2的分割质量，低光照或杂乱背景下成功率骤降（昏暗场景0%）。
- **简化假设**：目标物体必须全程可见且路径无遮挡，未处理探索、避障或目标临时丢失场景。
- **传感模态限制**：未使用深度、LiDAR或地图先验，这既是优势也是局限——在无纹理或重复纹理环境中，RGB-only方法可能失效。
- **方向精度**：边缘对齐成功率（73.47%未见实例）显著低于物体对齐，方向控制仍是未完全解决的问题。
- **数据规模**：仅715条轨迹且训练物体单一（绿色椅子），类别级泛化是否可推广至更多物体类别，论文未明确。

## 工程启示

- **复现优先级**：先核对分割模块（OwlV2+SAM2）在目标环境中的鲁棒性，这是整个系统的性能瓶颈。建议在低光照条件下额外采集数据或引入光照增强。
- **停止机制实现**：辅助停止依赖边界框与质心，需确保分割掩码的质心计算稳定；若目标部分遮挡，质心可能偏移，建议增加掩码面积阈值作为额外停止条件。
- **动作离散化**：三个运动原语各3类（共27种组合）的离散空间可能限制精细调整能力，若下游操作需要更高精度，可考虑增加级别数或引入连续残差动作。
- **方向对齐优化**：边缘对齐成功率较低，建议在训练数据中增加方向偏差较大的起始位姿（当前接近角覆盖-90°到90°，但rollout测试仅用±80°），或引入方向感知的损失加权。
- **跨环境部署**：室外表现（85%边缘对齐）优于室内（79%），可能与室内光照变化和纹理稀疏有关；部署前应在目标环境采集少量数据微调分割模块，而非重新训练策略。

## 参考
- http://arxiv.org/abs/2512.11173v4

## 개요
기존 RGB 기반 내비게이션 시스템은 일반적으로 미터 단위 정밀도만 제공하여, 이동 조작에서 로봇 팔이 정밀한 파지를 수행하기 전의 위치 파악 요구를 충족할 수 없습니다. 본 논문은 객체 중심의 모방 학습 프레임워크를 제안하여, 네 발 달린 이동 조작 로봇이 온보드 다중 시점 RGB 이미지와 텍스트 프롬프트만으로 조작 준비가 된 정밀 위치 파악을 달성할 수 있게 합니다. 이 방법은 언어 기반 분할 모듈과 공간 점수 행렬 디코더를 활용하여 명시적인 객체 위치 파악과 상대 자세 추론을 제공하며, 단일 객체 인스턴스의 실제 데이터만으로 훈련하여 동일 범주 내에서 보지 못한 객체 인스턴스로 일반화할 수 있고, 복잡한 조명 및 배경 조건에서도 견고성을 유지합니다.

## 핵심 내용
### 방법 아키텍처
- **입력 조건**: 내비게이션 정책은 세 가지 입력을 수신합니다——목표 이미지(goal images), 온보드 다중 시점 RGB 관측, 지정된 목표 객체를 나타내는 텍스트 프롬프트.
- **핵심 모듈**:
  - **언어 기반 분할 모듈**: 텍스트 프롬프트에 따라 다중 시점 RGB 이미지를 의미론적으로 분할하여 목표 객체의 명시적 공간 위치를 추출합니다.
  - **공간 점수 행렬 디코더**: 분할된 특징을 상대 자세 점수로 매핑하여 로봇이 목표 객체에 대한 정밀한 방향과 거리 정보를 출력합니다.
- **훈련 데이터**: 동일 범주 내 단일 객체 인스턴스의 실제 세계 시연 데이터(RGB 이미지)만 사용하며, 깊이 또는 포인트 클라우드 주석이 필요 없습니다.

### 실험 설정
- **로봇 플랫폼**: 네 발 달린 이동 조작 로봇, 온보드 RGB 카메라 탑재.
- **평가 지표**:
  - **가장자리 정렬 지표(edge-alignment)**: 실제 방향 정보를 사용하여 로봇 베이스와 목표 객체 가장자리의 정밀한 정렬 정도를 평가합니다.
  - **객체 정렬 지표(object-alignment)**: 로봇이 목표 객체를 정면으로 바라보는지, 즉 시각적 방향의 정확성을 평가합니다.
- **테스트 환경**: 다양한 조명 조건과 복잡한 배경을 포함한 다양한 실제 장면, 목표 객체는 훈련에서 보지 못한 동일 범주 인스턴스입니다.

### 주요 결과
- 보지 못한 목표 객체에서 가장자리 정렬 성공률은 74.58%, 객체 정렬 성공률은 89.42%에 도달했습니다.
- 이 방법은 깊이 센서, LiDAR 또는 지도 사전 정보 없이 RGB 비전과 텍스트 프롬프트만으로 범주 수준의 마지막 1미터 정밀 위치 파악을 달성할 수 있습니다.
- 실험은 이 프레임워크가 통합 이동 조작을 위한 확장 가능한 경로를 제공하여, 내비게이션 정책이 후속 조작 정책의 훈련 분포와 일관성을 유지하고 실행 실패를 줄일 수 있음을 보여줍니다.

### 결론
본 논문은 객체 중심의 모방 학습을 통해 깊이, LiDAR, 지도 사전 정보 없이 범주 수준의 정밀 위치 파악을 달성할 수 있음을 증명하며, 이동 조작 로봇의 실제 배치를 위한 저비용, 높은 일반화 솔루션을 제공합니다. 프로젝트 페이지: https://rpm-lab-umn.github.io/category-level-last-meter-nav/
