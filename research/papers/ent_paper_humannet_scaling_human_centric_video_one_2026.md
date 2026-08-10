---
$id: ent_paper_humannet_scaling_human_centric_video_one_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanNet: Scaling Human-centric Video Learning to One Million Hours'
  zh: 'HumanNet: Scaling Human-centric Video Learning to One Million Hours'
  ko: 'HumanNet: Scaling Human-centric Video Learning to One Million Hours'
summary:
  en: 'Progress in embodied intelligence increasingly depends on scalable data infrastructure. While vision and language have
    scaled with internet corpora, learning physical interaction remains constrained by the lack of large, diverse, and richly
    annotated human activity data. Institutions per source list: 北京大学（DAGroup-PKU）.'
  zh: HumanNet 是一个包含一百万小时人类活动视频的大型数据集，由研究团队构建，旨在通过人类中心视频推动具身智能学习。其核心贡献在于提供了跨视角、细粒度交互标注的视频语料，并验证了第一人称人类视频可作为机器人数据的可扩展替代方案。
  ko: 'Progress in embodied intelligence increasingly depends on scalable data infrastructure. While vision and language have
    scaled with internet corpora, learning physical interaction remains constrained by the lack of large, diverse, and richly
    annotated human activity data. Institutions per source list: 北京大学（DAGroup-PKU）.'
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
- humannet
- scaling
- human
- centric
- video
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 386 (merged duplicate list rows: [412]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: substring (score 1.0). Abstract and metadata from arXiv API (2605.06747v1); zh content by DeepSeek
    from the abstract. Institutions as given in the source list, not verified. [2026-08-04] body rewritten as full-text six-section
    deep read (.staging/deep_read batch1, DeepSeek deepseek-chat T<=0.3, arXiv HTML full text); en/ko sections regenerated
    by translate pipeline. [2026-08-05] number-audit fix (fallback_trimmed): experiments-section numbers verified against
    full text with programmatic whitelist; derived values explicitly labeled. 深读+数字白名单复核通过 2026-08-10（批量一）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.06747 HumanNet: Scaling Human-centric Video Learning to One Million Hours'
  url: https://arxiv.org/abs/2605.06747
  accessed_at: '2026-07-31'
  date: '2026-05-07'
- id: src_002
  type: website
  title: Project page
  url: https://dagroup-pku.github.io/HumanNet/
  accessed_at: '2026-07-31'
- id: src_003
  type: website
  title: Project page
  url: https://github.com/DAGroup-PKU/HumanNet/
  accessed_at: '2026-07-31'
- id: src_004
  type: website
  title: Project page
  url: https://github.com/DAGroup-PKU/HumanNet
  accessed_at: '2026-07-31'
- id: src_005
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---




## 概述

HumanNet 是一个一百万小时的人类中心视频语料库，由作者团队构建，涵盖第一人称和第三人称视角，旨在通过数据规模扩展来探索具身基础模型的预训练可能性。其核心贡献在于将数据策展、视角多样性和标注分类法视为科学问题，并通过受控实验验证了人类视频作为机器人数据替代或补充的可行性。

## 它改变了什么

具身智能的数据困境一直是个死结：语言模型靠互联网文本实现了规模扩展，而物理交互模型却困在比其小数个数量级的专用数据集里，且被绑定在特定平台、接口和传感栈上。现有的人类活动视频语料要么时长有限（如 Ego4D 的 3,670 小时），要么分散在不同采集工作中，要么针对狭窄下游任务优化，没有一个能支撑起“规模化预训练”的野心。HumanNet 的提出改变了这个格局——它把数据规模推到了百万小时量级，同时明确主张策展、视角多样性和标注分类法本身就是核心科学贡献，而非简单的数据整理工作。这一转变的实质是：将“数据”从工程附属品提升为与模型架构并列的研究对象，为具身基础模型的扩展路径提供了一个以数据为中心的替代方案。

## 方法拆解

### 数据采集
- **关键词发现**：种子关键词 → 关键词扩展 → 基于关键词的爬取 → 频道爬取 → 现有来源整合
- **内容搜索检索**：视频平台搜索、通用网络搜索引擎、直接爬取视频、开源数据集、真实环境自采集，合并为统一混合视频池

### 数据处理（三阶段流水线）
1. **去重与归一化**：统一帧率、分辨率、容器格式
2. **内容过滤**：保留有意义的人类动作和可观察运动
3. **质量过滤**：丢弃严重运动模糊、重度遮挡、静态取景等低质量片段
4. **场景切分**：按视觉变化分割长视频
5. **视频裁剪**：产生固定粒度片段

### 标注体系
- **3D 手部和身体姿态检测**：恢复细粒度运动结构
- **单目 SLAM**：估计满足稳定性和视差要求的第一人称片段相机轨迹
- **运动重定向**：将恢复的人体运动对齐到统一人形骨架；合格标准为**重定向误差 < 15 mm 且有效帧覆盖率 > 60%**，达标片段标记为 robot-ready
- **LLM 辅助字幕**：生成视频字幕、运动描述和活动分类

### 分类法组织
- 多轴分类法：源类型、视角、任务结构、环境、交互风格、运动类别、元数据可用性
- 交互内容围绕物理接地行为组织（操作、工具使用、物体运输、运动、全身运动、环境状态变化、多人协调、长时程程序），标注为多标签而非互斥

### 验证协议
- 固定 LingBot-VLA 架构，仅改变预训练来源，保持策略架构和下游数据固定
- 四种配置：Qwen 基础 VLM；Qwen + 100 小时真实机器人 CoBot 数据；Qwen + 1,000 小时第一人称人类视频；LingBot（Qwen 骨干 + 20,000 小时真实机器人数据）
- 所有变体在同一下游语料上后训练：100 个任务 × 每个任务 20 个片段，总计 34 小时机器人交互数据

## 关键创新

1. **百万小时规模本身即是创新**：现有最大的人类活动视频语料（Ego4D）仅 3,670 小时，HumanNet 将其扩展了近 300 倍，首次将人类中心视频预训练推到了与语言模型语料可比的量级。这一规模使得长尾覆盖（活动、环境、身体运动、交互风格）成为可能，而非仅覆盖头部常见场景。

2. **视角多样性的显式索引与保留**：不同于现有语料通常聚焦单一视角（如 Ego4D 仅第一人称），HumanNet 同时保留并显式索引第一人称和第三人称来源。这一设计承认了不同视角对具身学习的不同价值——第一人称提供手-物接近度和操作细节，第三人称提供全身运动和场景上下文。

3. **robot-ready 标注的量化标准**：通过运动重定向误差（< 15 mm）和有效帧覆盖率（> 60%）定义了可迁移到机器人控制空间的片段标准，将“人类视频是否可用于机器人学习”从定性判断转化为可操作的量化筛选，为下游用户提供了明确的筛选依据。

## 实验与结果


实验采用严格对照设计：四组配置共享同一 LingBot-VLA 架构与固定的下游微调语料（34 小时机器人交互数据，覆盖 100 个任务、每任务 20 个 episode），唯一变量为预训练初始化来源。
评估指标为五个保留任务组上的验证损失。
| 预训练初始化来源 | 预训练数据规模 | 验证损失（五个任务组） |
|---|---|---|
| Qwen 基础 VLM | 无 | 基线（论文未明确具体数值） |
| Qwen + CoBot 真实机器人 | 100 小时 | 参照基准 |
结果含义如下：
这表明人类视频捕获的以动作者为中心的线索、手-物接触模式与程序性结构，在迁移到机器人后训练后依然有效，尽管预训练阶段从未观察真实机器人。
（本节另有 6 句含无法从全文文本核实的数字，已按纪律移除；论文未明确或以图/表图片形式给出。）

## 边界与局限

- **人类行为 ≠ 机器人行为**：即使在一百万小时规模下，人类手、身体、工具、移动性与机器人控制空间之间的具身差距无法消除；数据集的价值在于表示学习和可迁移先验，而非直接替代机器人数据
- **规模引入噪声**：开放世界视频不可避免地包含模糊标签、不一致的任务边界、缺失元数据、视角不平衡和可变的视觉质量；字幕标签、姿态估计和运动标注会引入自身误差
- **覆盖仍不均匀**：数据集可能偏向某些地理区域、社会经济背景、职业、相机视角、体型、家庭日常或公共活动；一百万小时规模可能造成普遍性的错觉，而存在显著盲点
- **隐私与安全问题**：第一人称录制可能捕获旁观者、敏感室内、私人文件、屏幕或专有工作流；第三人称录制可能捕获可识别个人、家庭、工作场所、社交互动
- **未报告新的人到机器人迁移实验**（第 4 节明确说明），验证仅停留在损失对比层面，未涉及真实机器人部署
- **双重用途风险**：可能加速辅助系统和操作研究，也可能强化监控相关感知系统或使模型继承源材料中的社会和地理偏见

## 工程启示

- **先核对数据来源构成**：HumanNet 混合了视频平台、搜索引擎、开源数据集和自采集数据，不同来源的质量和视角分布差异可能极大；复现时需确认自己的下游任务与数据中主导的活动类型是否匹配
- **robot-ready 筛选标准是关键**：重定向误差 < 15 mm 且有效帧覆盖率 > 60% 的片段才标记为 robot-ready；如果你的下游任务需要精细操作，应优先筛选这些片段而非使用全部数据
- **预训练数据量的边际收益递减**：实验显示 1,000 小时人类视频 ≈ 100 小时真实机器人数据，但 20,000 小时真实机器人数据仍显著领先；如果你的团队有真实机器人数据获取能力，不应完全依赖人类视频替代
- **最容易踩坑的地方**：视角不平衡——第一人称和第三人称混合语料中，如果下游任务需要手-物接近度信息，第三人称片段可能提供不了足够的操作细节；建议按视角分桶评估预训练效果
- **标注误差的传导**：LLM 生成的字幕和运动描述会引入自身误差，且姿态估计和 SLAM 的误差会累积到重定向结果中；对精度敏感的下游任务，建议对 robot-ready 片段做人工抽检
- **训练配置细节论文未披露**（学习率、批量大小、epoch 数等），复现时需自行确定；建议从 LingBot-VLA 的原始配置出发做小规模消融

## 参考
- https://arxiv.org/abs/2605.06747
- https://dagroup-pku.github.io/HumanNet/
- https://github.com/DAGroup-PKU/HumanNet/
- https://github.com/DAGroup-PKU/HumanNet
- https://github.com/ImChong/Robotics_Notebooks

## Overview

HumanNet is a one-million-hour human-centric video corpus constructed by the author team, encompassing both first-person and third-person perspectives, aimed at exploring the pretraining potential of embodied foundation models through data-scale expansion. Its core contribution lies in treating data curation, viewpoint diversity, and annotation taxonomy as scientific problems, and validating through controlled experiments the feasibility of human videos as a substitute or supplement for robot data.

## What It Changes

The data dilemma in embodied intelligence has long been a deadlock: language models achieved scale via internet text, while physical interaction models remain confined to specialized datasets several orders of magnitude smaller, bound to specific platforms, interfaces, and sensor stacks. Existing human activity video corpora are either limited in duration (e.g., Ego4D's 3,670 hours), scattered across different collection efforts, or optimized for narrow downstream tasks—none can support the ambition of "scaled pretraining." HumanNet changes this landscape by pushing data scale to the million-hour level while explicitly asserting that curation, viewpoint diversity, and annotation taxonomy are core scientific contributions rather than mere data organization work. The essence of this shift is elevating "data" from an engineering byproduct to a research object on par with model architecture, offering a data-centric alternative path for scaling embodied foundation models.

## Method Breakdown

### Data Collection
- **Keyword Discovery**: Seed keywords → keyword expansion → keyword-based crawling → channel crawling → integration of existing sources
- **Content Search and Retrieval**: Video platform searches, general web search engines, direct video crawling, open-source datasets, and real-world self-collection, merged into a unified mixed video pool

### Data Processing (Three-Stage Pipeline)
1. **Deduplication and Normalization**: Unify frame rate, resolution, and container format
2. **Content Filtering**: Retain meaningful human actions and observable motion
3. **Quality Filtering**: Discard low-quality segments such as severe motion blur, heavy occlusion, and static framing
4. **Scene Segmentation**: Split long videos based on visual changes
5. **Video Cropping**: Produce fixed-granularity clips

### Annotation System
- **3D Hand and Body Pose Estimation**: Recover fine-grained motion structure
- **Monocular SLAM**: Estimate camera trajectories for first-person clips meeting stability and disparity requirements
- **Motion Retargeting**: Align recovered human motion to a unified humanoid skeleton; qualification criteria are **retargeting error < 15 mm and valid frame coverage > 60%**, with qualifying clips marked as robot-ready
- **LLM-Assisted Captioning**: Generate video captions, motion descriptions, and activity classifications

### Taxonomy Organization
- Multi-axis taxonomy: source type, viewpoint, task structure, environment, interaction style, motion category, metadata availability
- Interactive content organized around physically grounded behaviors (manipulation, tool use, object transport, locomotion, whole-body motion, environmental state changes, multi-person coordination, long-horizon procedures), labeled as multi-label rather than mutually exclusive

### Validation Protocol
- Fixed LingBot-VLA architecture, varying only the pretraining source, with policy architecture and downstream data held constant
- Four configurations: Qwen base VLM; Qwen + 100 hours of real robot CoBot data; Qwen + 1,000 hours of first-person human video; LingBot (Qwen backbone + 20,000 hours of real robot data)
- All variants post-trained on the same downstream corpus: 100 tasks × 20 episodes per task, totaling 34 hours of robot interaction data

## Key Innovations

1. **Million-Hour Scale Itself Is an Innovation**: The largest existing human activity video corpus (Ego4D) has only 3,670 hours; HumanNet expands this by nearly 300 times, pushing human-centric video pretraining to a scale comparable to language model corpora for the first time. This scale enables long-tail coverage (activities, environments, body motions, interaction styles) rather than covering only head common scenarios.

2. **Explicit Indexing and Preservation of Viewpoint Diversity**: Unlike existing corpora that typically focus on a single viewpoint (e.g., Ego4D is first-person only), HumanNet simultaneously preserves and explicitly indexes both first-person and third-person sources. This design acknowledges the distinct value of different viewpoints for embodied learning—first-person provides hand-object proximity and manipulation details, while third-person provides whole-body motion and scene context.

3. **Quantitative Criteria for Robot-Ready Annotation**: Defines clip standards transferable to robot control spaces via motion retargeting error (< 15 mm) and valid frame coverage (> 60%), converting "whether human videos can be used for robot learning" from a qualitative judgment into an actionable quantitative filter, providing downstream users with clear screening criteria.

## Experiments and Results

The experiments employ a strictly controlled design: four configurations share the same LingBot-VLA architecture and fixed downstream fine-tuning corpus (34 hours of robot interaction data, covering 100 tasks with 20 episodes per task), with the sole variable being the pretraining initialization source.
The evaluation metric is validation loss on five held-out task groups.
| Pretraining Initialization Source | Pretraining Data Scale | Validation Loss (Five Task Groups) |
|---|---|---|
| Qwen base VLM | None | Baseline (specific values not stated in the paper) |
| Qwen + CoBot real robot | 100 hours | Reference benchmark |
The implications of the results are as follows:
This indicates that actor-centric cues, hand-object contact patterns, and procedural structures captured in human videos remain effective after transfer to robot post-training, despite never observing real robots during the pretraining phase.
(Six additional sentences in this section containing numbers unverifiable from the full text have been removed per discipline; the paper either does not specify them or presents them as figures/tables.)

## Boundaries and Limitations

- **Human Behavior ≠ Robot Behavior**: Even at the million-hour scale, the embodiment gap between human hands, bodies, tools, mobility, and robot control spaces cannot be eliminated; the dataset's value lies in representation learning and transferable priors, not as a direct substitute for robot data
- **Scale Introduces Noise**: Open-world videos inevitably include ambiguous labels, inconsistent task boundaries, missing metadata, viewpoint imbalance, and variable visual quality; caption labels, pose estimation, and motion annotations introduce their own errors
- **Coverage Remains Uneven**: The dataset may be biased toward certain geographic regions, socioeconomic backgrounds, occupations, camera viewpoints, body types, household routines, or public activities; the million-hour scale may create an illusion of universality while significant blind spots exist
- **Privacy and Safety Concerns**: First-person recordings may capture bystanders, sensitive interiors, private documents, screens, or proprietary workflows; third-person recordings may capture identifiable individuals, homes, workplaces, and social interactions
- **No New Human-to-Robot Transfer Experiments Reported** (explicitly stated in Section 4), with validation limited to loss comparisons and not involving real robot deployment
- **Dual-Use Risks**: May accelerate assistive systems and manipulation research, but could also reinforce surveillance-related perception systems or cause models to inherit social and geographic biases from source materials

## Engineering Insights

- **Verify Data Source Composition First**: HumanNet mixes video platforms, search engines, open-source datasets, and self-collected data, where quality and viewpoint distribution may vary significantly across sources; when reproducing, confirm whether your downstream tasks match the dominant activity types in the data
- **Robot-Ready Screening Criteria Are Key**: Only clips with retargeting error < 15 mm and valid frame coverage > 60% are marked as robot-ready; if your downstream tasks require fine manipulation, prioritize screening these clips rather than using all data
- **Diminishing Marginal Returns on Pretraining Data Volume**: Experiments show 1,000 hours of human video ≈ 100 hours of real robot data, but 20,000 hours of real robot data still leads significantly; if your team has access to real robot data collection, do not rely entirely on human video substitution
- **Most Common Pitfall**: Viewpoint imbalance—in mixed first-person and third-person corpora, if downstream tasks require hand-object proximity information, third-person clips may not provide sufficient manipulation detail; it is recommended to evaluate pretraining effects by viewpoint buckets
- **Annotation Error Propagation**: LLM-generated captions and motion descriptions introduce their own errors, and errors from pose estimation and SLAM accumulate into retargeting results; for precision-sensitive downstream tasks, manual spot-checking of robot-ready clips is recommended
- **Training Configuration Details Not Disclosed in the Paper** (learning rate, batch size, number of epochs, etc.), requiring self-determination during reproduction; it is recommended to start from LingBot-VLA's original configuration with small-scale ablations

## 개요

HumanNet은 저자 팀이 구축한 100만 시간 규모의 인간 중심 비디오 코퍼스로, 1인칭 및 3인칭 시점을 모두涵盖하며, 데이터 규모 확장을 통해 구현 기반 모델의 사전 학습 가능성을 탐구하는 것을 목표로 합니다. 핵심 기여는 데이터 큐레이션, 시점 다양성, 주석 분류 체계를 과학적 문제로 간주하고, 통제된 실험을 통해 인간 비디오가 로봇 데이터의 대체 또는 보완재로서의 타당성을 검증한 데 있습니다.

## 무엇을 바꾸었는가

구현 지능의 데이터 딜레마는 오랫동안 해결되지 않은 난제였습니다: 언어 모델은 인터넷 텍스트를 통해 규모 확장을 달성했지만, 물리적 상호작용 모델은 이보다 몇 자릿수 작은 전용 데이터 세트에 갇혀 있으며, 특정 플랫폼, 인터페이스, 센서 스택에 묶여 있습니다. 기존의 인간 활동 비디오 코퍼스는 시간이 제한적이거나(예: Ego4D의 3,670시간), 여러 수집 작업에 분산되어 있거나, 좁은 하위 작업에 최적화되어 있어, "규모화된 사전 학습"이라는 야망을 뒷받침할 수 없었습니다. HumanNet의 등장은 이러한 구도를 바꾸었습니다—데이터 규모를 100만 시간 수준으로 끌어올리면서, 큐레이션, 시점 다양성, 주석 분류 체계 자체가 단순한 데이터 정리 작업이 아닌 핵심 과학적 기여임을 명확히 주장합니다. 이러한 전환의 본질은 "데이터"를 엔지니어링의 부산물에서 모델 아키텍처와 동등한 연구 대상으로 승격시켜, 구현 기반 모델의 확장 경로에 데이터 중심의 대안을 제공한 것입니다.

## 방법 분석

### 데이터 수집
- **키워드 발견**: 시드 키워드 → 키워드 확장 → 키워드 기반 크롤링 → 채널 크롤링 → 기존 소스 통합
- **콘텐츠 검색 및 검색**: 비디오 플랫폼 검색, 일반 웹 검색 엔진, 직접 비디오 크롤링, 오픈소스 데이터 세트, 실제 환경 자체 수집을 통합하여 균일한 혼합 비디오 풀로 구성

### 데이터 처리(3단계 파이프라인)
1. **중복 제거 및 정규화**: 프레임 속도, 해상도, 컨테이너 형식 통일
2. **콘텐츠 필터링**: 의미 있는 인간 동작과 관찰 가능한 움직임 유지
3. **품질 필터링**: 심한 모션 블러, 심한 폐색, 정적 프레이밍 등 저품질 세그먼트 제거
4. **장면 분할**: 시각적 변화에 따라 긴 비디오 분할
5. **비디오 크롭**: 고정된 세분화 세그먼트 생성

### 주석 체계
- **3D 손 및 신체 자세 감지**: 미세한 운동 구조 복원
- **단안 SLAM**: 안정성과 시차 요구 사항을 충족하는 1인칭 세그먼트 카메라 궤적 추정
- **모션 리타게팅**: 복원된 인간 모션을 통일된 휴머노이드 골격에 정렬; 합격 기준은 **리타게팅 오류 < 15mm 및 유효 프레임 커버리지 > 60%**이며, 충족 시 robot-ready로 표시
- **LLM 보조 자막**: 비디오 캡션, 모션 설명, 활동 분류 생성

### 분류 체계 구성
- 다축 분류 체계: 소스 유형, 시점, 작업 구조, 환경, 상호작용 스타일, 모션 범주, 메타데이터 가용성
- 상호작용 콘텐츠는 물리적 접지 행동(조작, 도구 사용, 물체 운반, 운동, 전신 운동, 환경 상태 변화, 다인 협력, 장기 프로그램)을 중심으로 구성되며, 상호 배타적이 아닌 다중 레이블로 주석 처리

### 검증 프로토콜
- 고정된 LingBot-VLA 아키텍처, 사전 학습 소스만 변경, 정책 아키텍처 및 하위 데이터 고정
- 네 가지 구성: Qwen 기본 VLM; Qwen + 100시간 실제 로봇 CoBot 데이터; Qwen + 1,000시간 1인칭 인간 비디오; LingBot(Qwen 백본 + 20,000시간 실제 로봇 데이터)
- 모든 변형은 동일한 하위 코퍼스에서 후속 학습: 100개 작업 × 작업당 20개 에피소드, 총 34시간 로봇 상호작용 데이터

## 핵심 혁신

1. **100만 시간 규모 자체가 혁신**: 기존 최대 인간 활동 비디오 코퍼스(Ego4D)는 3,670시간에 불과하며, HumanNet은 이를 약 300배 확장하여 인간 중심 비디오 사전 학습을 언어 모델 코퍼스와 비교 가능한 규모로 처음 끌어올렸습니다. 이러한 규모는 헤드의 일반적인 장면뿐만 아니라 롱테일 커버리지(활동, 환경, 신체 움직임, 상호작용 스타일)를 가능하게 합니다.

2. **시점 다양성의 명시적 인덱싱 및 보존**: 기존 코퍼스가 일반적으로 단일 시점에 초점을 맞추는 반면(예: Ego4D는 1인칭만), HumanNet은 1인칭과 3인칭 소스를 모두 보존하고 명시적으로 인덱싱합니다. 이 설계는 서로 다른 시점이 구현 학습에 서로 다른 가치를 제공한다는 점을 인정합니다—1인칭은 손-물체 근접성과 조작 세부 사항을 제공하고, 3인칭은 전신 움직임과 장면 맥락을 제공합니다.

3. **robot-ready 주석의 정량적 기준**: 모션 리타게팅 오류(< 15mm)와 유효 프레임 커버리지(> 60%)를 통해 로봇 제어 공간으로 전이 가능한 세그먼트 기준을 정의하여, "인간 비디오가 로봇 학습에 사용될 수 있는지"를 정성적 판단에서 실행 가능한 정량적 필터링으로 전환하고, 하위 사용자에게 명확한 선별 기준을 제공합니다.

## 실험 및 결과

실험은 엄격한 대조 설계를 사용합니다: 네 가지 구성이 동일한 LingBot-VLA 아키텍처와 고정된 하위 미세 조정 코퍼스(34시간 로봇 상호작용 데이터, 100개 작업, 작업당 20개 에피소드)를 공유하며, 유일한 변수는 사전 학습 초기화 소스입니다.
평가 지표는 다섯 개의 보류 작업 그룹에 대한 검증 손실입니다.
| 사전 학습 초기화 소스 | 사전 학습 데이터 규모 | 검증 손실(다섯 개 작업 그룹) |
|---|---|---|
| Qwen 기본 VLM | 없음 | 기준선(논문에서 구체적 수치 미명시) |
| Qwen + CoBot 실제 로봇 | 100시간 | 참조 기준 |
결과의 의미는 다음과 같습니다:
이는 인간 비디오가 포착한 행위자 중심 단서, 손-물체 접촉 패턴, 절차적 구조가 사전 학습 단계에서 실제 로봇을 관찰한 적이 없음에도 불구하고 로봇 후속 학습으로 전이된 후에도 여전히 유효함을 보여줍니다.
(이 섹션에는 전체 텍스트에서 확인할 수 없는 숫자를 포함한 6개의 문장이 더 있으며, 규율에 따라 제거되었습니다; 논문은 명시하지 않거나 그림/표 이미지 형태로 제공합니다.)

## 경계 및 한계

- **인간 행동 ≠ 로봇 행동**: 100만 시간 규모에서도 인간의 손, 신체, 도구, 이동성과 로봇 제어 공간 사이의 구현 격차는 제거할 수 없습니다; 데이터 세트의 가치는 표현 학습과 전이 가능한 사전 지식에 있으며, 로봇 데이터의 직접적 대체가 아닙니다
- **규모가 노이즈를 유발**: 개방형 세계 비디오는 필연적으로 모호한 레이블, 불일치하는 작업 경계, 누락된 메타데이터, 시점 불균형, 가변적인 시각 품질을 포함합니다; 자막 레이블, 자세 추정, 모션 주석은 자체 오류를 유발합니다
- **커버리지 여전히 불균일**: 데이터 세트는 특정 지리적 지역, 사회경제적 배경, 직업, 카메라 시점, 체형, 가정 일상 또는 공공 활동에 편향될 수 있습니다; 100만 시간 규모가 보편성의 착각을 만들 수 있지만 상당한 사각지대가 존재합니다
- **개인정보 및 보안 문제**: 1인칭 녹화는 주변인, 민감한 실내, 개인 문서, 화면 또는 독점 워크플로우를 포착할 수 있습니다; 3인칭 녹화는 식별 가능한 개인, 가족, 직장, 사회적 상호작용을 포착할 수 있습니다
- **새로운 인간-로봇 전이 실험 미보고**(섹션 4에서 명시), 검증은 손실 비교에만 머물며 실제 로봇 배포는 포함하지 않음
- **이중 용도 위험**: 보조 시스템 및 조작 연구를 가속화할 수 있지만, 감시 관련 인식 시스템을 강화하거나 모델이 원본 자료의 사회적 및 지리적 편향을 물려받을 수 있습니다

## 엔지니어링 시사점

- **먼저 데이터 소스 구성을 확인**: HumanNet은 비디오 플랫폼, 검색 엔진, 오픈소스 데이터 세트, 자체 수집 데이터를 혼합하며, 소스별 품질과 시점 분포 차이가 클 수 있습니다; 재현 시 하위 작업과 데이터에서 지배적인 활동 유형이 일치하는지 확인해야 합니다
- **robot-ready 선별 기준이 핵심**: 리타게팅 오류 < 15mm 및 유효 프레임 커버리지 > 60%인 세그먼트만 robot-ready로 표시됩니다; 하위 작업이 정밀 조작을 요구한다면 전체 데이터가 아닌 이러한 세그먼트를 우선 선별해야 합니다
- **사전 학습 데이터 양의 한계 수익 체감**: 실험은 1,000시간 인간 비디오 ≈ 100시간 실제 로봇 데이터를 보여주지만, 20,000시간 실제 로봇 데이터는 여전히 크게 앞섭니다; 팀에 실제 로봇 데이터 획득 능력이 있다면 인간 비디오 대체에 완전히 의존해서는 안 됩니다
- **가장 함정에 빠지기 쉬운 부분**: 시점 불균형—1인칭과 3인칭 혼합 코퍼스에서 하위 작업이 손-물체 근접성 정보를 요구한다면, 3인칭 세그먼트는 충분한 조작 세부 사항을 제공하지 못할 수 있습니다; 시점별 버킷으로 사전 학습 효과를 평가하는 것이 좋습니다
- **주석 오류의 전파**: LLM이 생성한 자막과 모션 설명은 자체 오류를 유발하며, 자세 추정과 SLAM의 오류는 리타게팅 결과에 누적됩니다; 정밀도에 민감한 하위 작업에서는 robot-ready 세그먼트에 대한 수동 샘플링 검사를 권장합니다
- **훈련 구성 세부 사항은 논문에 미공개**(학습률, 배치 크기, 에폭 수 등), 재현 시 직접 결정해야 합니다; LingBot-VLA의 원래 구성에서 시작하여 소규모 절제 실험을 권장합니다
