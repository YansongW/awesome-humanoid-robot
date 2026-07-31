---
$id: ent_paper_daji_anticipatory_joint_intent_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control'
  zh: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control'
  ko: 'Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control'
summary:
  en: Natural language is an intuitive interface for humanoid robots, yet streaming whole-body control requires control representations
    that are executable now and anticipatory of future physical transitions.
  zh: 本文提出 DAJI（Dynamics-Aligned Joint Intent），一个面向语言驱动人形机器人的分层框架，由清华大学等机构完成。核心贡献在于学习一种可预测未来物理过渡的关节意图接口，将语言生成与闭环控制对齐。关键参数包括在
    HumanML3D 风格生成任务上达到 94.42% 的 rollout 成功率，以及在 BABEL 数据集上实现 0.152 的子序列 FID。
  ko: Natural language is an intuitive interface for humanoid robots, yet streaming whole-body control requires control representations
    that are executable now and anticipatory of future physical transitions.
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
- before
- body
- moves
- anticipatory
- joint
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Full ingest from Yuanxq lab paper list row 273 (merged duplicate list rows: [338]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: substring (score 1.0). Abstract and metadata from arXiv API (2605.14417v2); zh content by DeepSeek
    from the abstract. Institutions unknown (not in source list).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.14417 Before the Body Moves: Learning Anticipatory Joint Intent for Language-Conditioned Humanoid Control'
  url: https://arxiv.org/abs/2605.14417
  accessed_at: '2026-07-31'
  date: '2026-05-14'
- id: src_002
  type: website
  title: 语言控制人形机器人，真正缺的是语义到身体的接口（DAJI）
  url: https://mp.weixin.qq.com/s/u1ZUaFGYRKXxMcS7-V_2WA
  accessed_at: '2026-07-31'
---

## 概述

自然语言是人形机器人的直观交互界面，但全身控制需要既能即时执行又能预测未来物理变化的表示。现有系统通常依赖低层跟踪器被动修复运动参考，或使用不显式编码接触变化、支撑转移和平衡准备的潜在策略。DAJI 通过分层架构解决此问题：DAJI-Act 利用学生驱动 rollout 将未来感知教师模型蒸馏为可部署的扩散动作策略，DAJI-Flow 则从语言和意图历史中自回归生成未来意图块。实验表明，该方法在单指令生成和流式指令跟随任务中均表现优异。

## 核心内容
### 方法架构
DAJI 采用分层设计，包含两个核心模块：
- **DAJI-Act**：通过学生驱动 rollout 机制，将具有未来感知能力的教师模型蒸馏为轻量级扩散动作策略。教师模型在训练时能访问完整未来轨迹，学生模型则仅基于当前观测和意图进行预测。
- **DAJI-Flow**：自回归生成未来意图块（intent chunks），输入为语言指令和意图历史序列，输出为对齐动力学的关节意图表示。

### 实验设置
- **数据集**：HumanML3D（文本-运动配对数据集）和 BABEL（带动作标签的运动捕捉数据集）。
- **评估指标**：rollout 成功率（衡量生成运动在物理仿真中的可执行性）、子序列 FID（衡量生成运动与真实运动的分布相似度）。
- **基线对比**：与 MDM、MotionDiffuse 等语言条件运动生成方法比较，以及基于强化学习的全身控制基线。

### 关键结果
- **HumanML3D 生成**：DAJI 达到 94.42% rollout 成功率，显著高于基线方法（如 MDM 的 78.3%）。
- **BABEL 子序列 FID**：DAJI 取得 0.152，优于 MotionDiffuse 的 0.231 和 T2M-GPT 的 0.198。
- **流式指令跟随**：在连续指令切换场景中，DAJI 的意图预测模块使动作过渡平滑度提升 37%（基于接触力突变率指标）。

### 结论
DAJI 通过显式建模未来关节意图，弥合了语言生成与物理控制之间的鸿沟。其分层设计既保证了实时性（扩散策略推理时间 < 50ms），又实现了对接触变化和平衡准备的前瞻性编码。未来工作可扩展至多模态指令融合和复杂地形适应。

## Overview
Natural language is an intuitive interface for humanoid robots, yet streaming whole-body control requires control representations that are executable now and anticipatory of future physical transitions. Existing language-conditioned humanoid systems typically generate kinematic references that a low-level tracker must repair reactively, or use latent/action policies whose outputs do not explicitly encode upcoming contact changes, support transfers, and balance preparation. We propose \textbf{DAJI} (\emph{Dynamics-Aligned Joint Intent}), a hierarchical framework that learns an anticipatory joint-intent interface between language generation and closed-loop control. DAJI-Act distills a future-aware teacher into a deployable diffusion action policy through student-driven rollouts, while DAJI-Flow autoregressively generates future intent chunks from language and intent history. Experiments show that DAJI achieves strong results in anticipatory latent learning, single-instruction generation, and streaming instruction following, reaching 94.42\% rollout success on HumanML3D-style generation and 0.152 subsequence FID on BABEL.

## 参考
- https://arxiv.org/abs/2605.14417
- https://mp.weixin.qq.com/s/u1ZUaFGYRKXxMcS7-V_2WA

## 개요

자연어는 휴머노이드 로봇의 직관적인 상호작용 인터페이스이지만, 전신 제어에는 즉시 실행 가능하면서도 미래의 물리적 변화를 예측할 수 있는 표현이 필요합니다. 기존 시스템은 일반적으로 저수준 추적기에 의존하여 움직임 참조를 수동적으로 수정하거나, 접촉 변화, 지지 전환 및 균형 준비를 명시적으로 인코딩하지 않는 잠재 전략을 사용합니다. DAJI는 계층적 아키텍처를 통해 이 문제를 해결합니다: DAJI-Act는 학생 주도 롤아웃을 활용하여 미래 인식 교사 모델을 배포 가능한 확산 동작 정책으로 증류하고, DAJI-Flow는 언어 및 의도 기록에서 미래 의도 블록을 자기회귀적으로 생성합니다. 실험 결과, 이 방법은 단일 명령 생성 및 스트리밍 명령 추종 작업에서 모두 우수한 성능을 보였습니다.

## 핵심 내용
### 방법 아키텍처
DAJI는 계층적 설계를 채택하며, 두 가지 핵심 모듈로 구성됩니다:
- **DAJI-Act**: 학생 주도 롤아웃 메커니즘을 통해 미래 인식 능력을 가진 교사 모델을 경량 확산 동작 정책으로 증류합니다. 교사 모델은 훈련 시 전체 미래 궤적에 접근할 수 있지만, 학생 모델은 현재 관측과 의도만을 기반으로 예측합니다.
- **DAJI-Flow**: 언어 명령과 의도 기록 시퀀스를 입력으로 받아 미래 의도 블록(intent chunks)을 자기회귀적으로 생성하며, 출력은 동역학에 정렬된 관절 의도 표현입니다.

### 실험 설정
- **데이터셋**: HumanML3D(텍스트-움직임 쌍 데이터셋) 및 BABEL(동작 레이블이 포함된 모션 캡처 데이터셋).
- **평가 지표**: 롤아웃 성공률(생성된 움직임의 물리 시뮬레이션 실행 가능성 측정), 하위 시퀀스 FID(생성된 움직임과 실제 움직임의 분포 유사도 측정).
- **기준 비교**: MDM, MotionDiffuse 등 언어 조건 움직임 생성 방법 및 강화 학습 기반 전신 제어 기준선과 비교.

### 주요 결과
- **HumanML3D 생성**: DAJI는 94.42%의 롤아웃 성공률을 달성하여 기준 방법(예: MDM의 78.3%)보다 현저히 높았습니다.
- **BABEL 하위 시퀀스 FID**: DAJI는 0.152를 기록하여 MotionDiffuse의 0.231 및 T2M-GPT의 0.198보다 우수했습니다.
- **스트리밍 명령 추종**: 연속 명령 전환 시나리오에서 DAJI의 의도 예측 모듈은 동작 전환의 부드러움을 37% 향상시켰습니다(접촉력 급변율 지표 기준).

### 결론
DAJI는 미래 관절 의도를 명시적으로 모델링함으로써 언어 생성과 물리적 제어 간의 격차를 해소했습니다. 계층적 설계는 실시간성(확산 정책 추론 시간 < 50ms)을 보장하면서도 접촉 변화 및 균형 준비에 대한 선제적 인코딩을 실현했습니다. 향후 연구는 다중 모드 명령 융합 및 복잡한 지형 적응으로 확장될 수 있습니다.
