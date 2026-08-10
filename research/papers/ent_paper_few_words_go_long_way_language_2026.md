---
$id: ent_paper_few_words_go_long_way_language_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A Few Words Go a Long Way: Language Guided Robot Policy Synthesis'
  zh: 'A Few Words Go a Long Way: Language Guided Robot Policy Synthesis'
  ko: 'A Few Words Go a Long Way: Language Guided Robot Policy Synthesis'
summary:
  en: While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally
    black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose
    ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages
    the reasoning capabilities.
  zh: ARCHITECT 是一个将机器人策略获取重构为交互式代码合成任务的框架，由 LLM 作为编排代理，调用异构工具套件生成可执行程序，并通过人类自然语言纠正来迭代改进策略。其核心贡献在于用可解释、可修正的程序替代黑箱 VLA 策略，无需任何机器人特定训练数据，仅靠语言反馈即可实现跨任务技能复用。
  ko: While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally
    black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose
    ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages
    the reasoning capabilities.
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
- few
- words
- go
- long
- way
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
  title: 'arXiv:2607.23784 A Few Words Go a Long Way: Language Guided Robot Policy Synthesis'
  url: https://arxiv.org/abs/2607.23784
  date: '2026-07-26'
  accessed_at: '2026-08-05'
---

## 概述

ARCHITECT 是一个将机器人策略获取重构为交互式代码合成任务的框架，由 LLM 作为编排代理，调用异构工具套件生成可执行程序，并通过人类自然语言纠正来迭代改进策略。其核心贡献在于用可解释、可修正的程序替代黑箱 VLA 策略，无需任何机器人特定训练数据，仅靠语言反馈即可实现跨任务技能复用。

## 它改变了什么

VLA 模型的根本问题不是精度，而是不可修正性。当策略失败时，用户面对的是一个无法解释、无法局部调整的黑箱，只能收集更多演示并重新训练，这在真实场景中几乎不可行。ARCHITECT 改变了这一范式：它把策略从“学出来的权重”变成“写出来的代码”，使失败成为可定位、可对话、可修复的事件。这种转变的意义在于，它将机器人调试从机器学习专家的领域拉回到普通用户的自然语言交互范畴。

另一个被改变的关键点是“规格差距”。传统模块化方法假设初始自然语言指令足以描述任务的全部几何与物理细节，但现实是“把香蕉放到盘子里”这句话远远不够。ARCHITECT 通过人类在循环中的语言纠正来填补这一差距，将模糊的意图逐步精炼为可执行的程序约束，而不是期望一次指令就能覆盖所有情况。

## 方法拆解

### 整体流程
1. 自然语言指令解析并嵌入系统提示词
2. LLM 生成顶层程序，强制先调用 `list_primitives()` 查看可用 API
3. 依次执行 `query_robot_state()`、`get_scene_description()` 进行环境感知
4. 按需调用感知函数（`detect_objects()`、`get_placement_pose()`）
5. 识别子操作并调用 `write_primitive()` 注册为命名原语
6. 调用 `submit_program()` 提交执行
7. 检测失败或回合结束，人类提供语言纠正
8. 纠正被合成为技能并加入技能库，重新生成策略

### 工具套件设计
- **控制原语**：`set_gripper_width()`（宽度范围 0.0–0.085 m）、`move_ee_to_pose()`、`move_ee_guarded()`（示例参数 `distance=-0.25, force_threshold=5.0 N`）
- **感知工具**：`detect_objects()` 链式使用 Grounded SAM2 分割与 AnyGrasp 抓取采样；`get_placement_pose()` 基于 AnyPlace；`get_vqa_response()` 基于 GPT-5.4；`get_keypoints()` 基于 DIFT；`get_keypoints_trajectory()` 基于 ReKep
- **本体感觉工具**：`verify_grasp()` 采用两阶段验证，先本体感觉门控再 VLM 确认

### 技能库机制
每次代码生成前，所有已积累的技能加载到上下文。技能包含使用指南、代码示例和规则参数，例如“Guarded Place on Surface”技能将人类纠正文本（“继续向下移动直到接触架子”）转化为 `move_ee_guarded(axis="z", distance=-0.25, force_threshold=5.0)` 的可执行规则。

### 强制工作流约束
系统提示词要求程序必须调用 `submit_program()` 提交，禁止以文本形式输出程序，禁止导入，每个有意义的子操作必须注册为原语。默认采用 VQA 验证-重试模式：对无法仅凭本体感觉确认成功的子操作，执行后通过 `get_vqa_response()` 询问是/否问题，否定则调整参数重试一次。

## 关键创新

**1. 语言纠正作为一等公民而非事后补救**：现有方法要么完全依赖初始指令，要么需要重新训练。ARCHITECT 将人类纠正直接转化为可执行技能并持久化到技能库，使每次失败都成为长期可复用的知识积累，而非一次性修补。这本质上是将上下文学习从“示例”扩展到“交互历史”。

**2. 程序合成与工具调用的结构化约束**：强制工作流步骤（先感知、再规划、后执行）和禁止扁平 API 调用列表，迫使 LLM 生成具有明确子操作边界的程序。这种结构先验使得失败定位成为可能——可以精确指出是哪一行代码或哪个工具调用出了问题，而不是面对一个整体失败的黑箱。

**3. 技能库作为长期上下文学习**：所有技能在每次代码生成前加载到上下文，相当于一种无限长的记忆机制。这使得跨任务迁移成为可能——人类评估中，加载任务 1 技能库后任务 2 成功率从 0/6 升至 4/6，证明语言纠正的积累具有跨场景泛化能力。

## 实验与结果

### 主基准（表 1，8 任务 × 10 episode × 5 方法，共 400 次 rollout）

| 任务 | CaP SR | π₀ SR | π₀.₅ SR | ARCHITECT-VLM SR | ARCHITECT-HiTL SR |
|---|---|---|---|---|---|
| Banana → plate | .20 | .80 | .90 | .80 | .80 |
| Block → basket | .40 | .40 | 1.0 | .70 | .70 |
| Baseball → bucket | .60 | .00 | .20 | .40 | 1.0 |
| Apple, Bread → bowl | .10 | .40 | .40 | .00 | .80 |
| Pick bread from box | .10 | .40 | .40 | .00 | .70 |
| Close drawer | .00 | .10 | .00 | .40 | .90 |
| Fold cloth into triangle | .00 | .00 | .00 | .70 | .80 |
| Banana under cloth | .00 | .10 | .00 | .00 | .80 |

### 附加基线（表 2）
ARCHITECT 在全部 8 个任务上超越 Inner Monologue、ProgPrompt、MolmoAct2、GR00T N1.7。GR00T N1.7 仅在 banana → plate 上有非零成功率（0.40），MolmoAct2 在该任务上与 ARCHITECT 持平但其余任务均落后。

### 语言消融（附录 B，Apple → pan 任务）
ARCHITECT 在 15 种语言变体中保持 1.0 SR，仅“Length long”变体降至 .00 SR（GCR .80）。π₀.₅ 对措辞高度敏感，在“Take the apple and place it onto the pan.”、“Move the apple onto the pan.”、“Onto the pan, place the apple.”等变体上 SR 降至 .00。

### 人类评估（N=6）
平均每试验查询从 4.67 降至 0.83（Δ=3.83，p=0.036），3/6 参与者需 0 次纠正。无技能时任务 2 成功率为 0/6，加载任务 1 技能库后 SR 升至 4/6。3 名给 1 次纠正的参与者中 2 名零样本失败任务 2，3 名给 2 次以上纠正的全部成功。

## 边界与局限

**主要失败模式是抓取**：源于所选的现成抓取生成模块（AnyGrasp），当抓取采样器噪声导致抓取成功未被纠正时，技能库可能缺少纠正未来抓取失败的技能。这意味着 ARCHITECT 的上限受限于底层感知模块的质量，而非 LLM 或程序合成能力。

**深度估计不准确时放置姿态难以确定**：如向桶中放物品时可能抬得过高，这是底层模块的局限，虽然可通过用户纠正解决，但增加了交互轮次。

**cuRobo 运动规划失败**：当无法为目标姿态生成无碰撞轨迹时，ARCHITECT 会遇到规划错误，论文未明确该情况的处理策略。

**纠正数量是关键变量**：提供 1 次纠正的参与者未能在无额外纠正下完成任务 2，表明构建有用技能库需要足够的纠正积累。论文未研究纠正质量对策略的影响，也未进行机器人特定微调或使用演示数据。

## 工程启示

**复现时先核对感知模块的确定性**：ARCHITECT 的性能高度依赖 AnyGrasp 的抓取采样和 AnyPlace 的放置预测。如果这些模块在你的硬件上表现不稳定，整个框架的成功率会显著下降。建议先单独验证 `detect_objects()` 和 `get_placement_pose()` 在你的场景中的可靠性，再接入完整流程。

**技能库的积累策略直接影响跨任务泛化**：人类评估显示，纠正次数少于 2 次的参与者无法在零样本下完成结构相似的新任务。这意味着在实际部署中，需要为每个新任务准备至少 2-3 轮纠正，否则技能库可能不足以支撑迁移。

**最容易踩坑的是 `move_ee_guarded()` 的力阈值**：论文给出的 5.0 N 适用于刚性表面，软表面需略增。如果目标物体或接触面材质变化，这个参数需要重新校准，否则会导致放置失败或物体损坏。

**语言消融结果提示 VLA 的脆弱性远超预期**：π₀.₅ 在“Move the apple onto the pan.”这种看似无害的变体上 SR 从 1.0 跌至 .00，而 ARCHITECT 保持 1.0。如果你的下游团队正在评估 VLA 方案，务必在多种措辞下测试，而不是只验证单一指令模板。

## Overview
While vision-language-action models have demonstrated impressive zero-shot manipulation capabilities, they remain fundamentally black box policies that are difficult to interpret, adapt, or correct when they inevitably fail. In this work, we propose ARCHITECT, a framework that treats robot policy acquisition as an interactive program synthesis task. ARCHITECT leverages the reasoning capabilities of LLM coding agents to synthesize modular robot programs that utilize a suite of perception and control tools. Unlike end-to-end models where distribution shift leads to unpredictable, cascading failures, our modular architecture allows users to isolate failures and localize feedback at the level of abstraction required. We introduce an iterative process where a human supervisor provides natural language corrections to steer the policy. These corrections are grounded in the policy code by program execution traces and distilled into a persistent skill library, a form of long-term in-context learning which enables the agent to accumulate a repertoire of reusable, interpretable behaviors. In a benchmark evaluation on a Franka Panda robot, ARCHITECT outperforms state-of-the-art VLA models and program synthesis baselines on complex, long-horizon tasks, including articulated object manipulation and cloth folding. Our results demonstrate that the synthesized skill library enables the system to transfer to novel tasks with decreasing human intervention, providing a steerable and data-efficient alternative to black-box robot learning. Website: https://robo-architect.github.io/

## 参考
- https://arxiv.org/abs/2607.23784

## 개요

ARCHITECT는 로봇 정책 획득을 인터랙티브 코드 합성 작업으로 재구성하는 프레임워크로, LLM이 오케스트레이션 에이전트로 작동하여 이기종 도구 모음을 호출해 실행 가능한 프로그램을 생성하고, 인간의 자연어 교정을 통해 정책을 반복적으로 개선합니다. 핵심 기여는 블랙박스 VLA 정책을 해석 가능하고 수정 가능한 프로그램으로 대체하여, 로봇 특화 훈련 데이터 없이 언어 피드백만으로도 작업 간 기술 재사용을 가능하게 한다는 점입니다.

## 무엇을 바꾸는가

VLA 모델의 근본적인 문제는 정확성이 아니라 수정 불가능성입니다. 정책이 실패했을 때, 사용자는 설명할 수 없고 부분 조정이 불가능한 블랙박스를 마주하게 되며, 더 많은 데모를 수집하고 재훈련하는 수밖에 없는데 이는 실제 시나리오에서 거의 불가능합니다. ARCHITECT는 이 패러다임을 바꿉니다. 정책을 "학습된 가중치"에서 "작성된 코드"로 전환하여 실패를 위치 추적 가능하고 대화 가능하며 수리 가능한 사건으로 만듭니다. 이 전환의 의미는 로봇 디버깅을 머신러닝 전문가의 영역에서 일반 사용자의 자연어 상호작용 범주로 끌어내린다는 점입니다.

또 다른 핵심 변화 지점은 "사양 격차"입니다. 기존 모듈식 접근법은 초기 자연어 명령이 작업의 모든 기하학적·물리적 세부 사항을 설명하기에 충분하다고 가정하지만, 현실에서 "바나나를 접시에 놓아라"라는 문장은 턱없이 부족합니다. ARCHITECT는 인간이 루프에 참여하는 언어 교정을 통해 이 격차를 메우며, 모호한 의도를 한 번의 명령으로 모든 상황을 커버하려 하지 않고 실행 가능한 프로그램 제약 조건으로 점진적으로 정제합니다.

## 방법 분해

### 전체 프로세스
1. 자연어 명령을 파싱하여 시스템 프롬프트에 임베딩
2. LLM이 최상위 프로그램을 생성하며, 먼저 `list_primitives()`를 호출해 사용 가능한 API를 확인하도록 강제
3. `query_robot_state()`, `get_scene_description()`을 순차 실행하여 환경 인식
4. 필요에 따라 인식 함수 호출 (`detect_objects()`, `get_placement_pose()`)
5. 하위 작업 식별 후 `write_primitive()`를 호출하여 명명된 프리미티브로 등록
6. `submit_program()`을 호출하여 실행 제출
7. 실패 감지 또는 에피소드 종료 시, 인간이 언어 교정 제공
8. 교정을 스킬로 합성하여 스킬 라이브러리에 추가하고, 정책 재생성

### 도구 모음 설계
- **제어 프리미티브**: `set_gripper_width()` (폭 범위 0.0–0.085 m), `move_ee_to_pose()`, `move_ee_guarded()` (예시 파라미터 `distance=-0.25, force_threshold=5.0 N`)
- **인식 도구**: `detect_objects()`는 Grounded SAM2 분할과 AnyGrasp 그랩 샘플링을 체이닝; `get_placement_pose()`는 AnyPlace 기반; `get_vqa_response()`는 GPT-5.4 기반; `get_keypoints()`는 DIFT 기반; `get_keypoints_trajectory()`는 ReKep 기반
- **고유수용감각 도구**: `verify_grasp()`는 2단계 검증으로, 먼저 고유수용감각 게이팅 후 VLM 확인

### 스킬 라이브러리 메커니즘
코드 생성 전마다 축적된 모든 스킬이 컨텍스트에 로드됩니다. 스킬에는 사용 가이드, 코드 예시, 규칙 파라미터가 포함되며, 예를 들어 "Guarded Place on Surface" 스킬은 인간 교정 텍스트("계속 아래로 이동하여 선반에 닿을 때까지")를 `move_ee_guarded(axis="z", distance=-0.25, force_threshold=5.0)`의 실행 가능한 규칙으로 변환합니다.

### 강제 워크플로우 제약
시스템 프롬프트는 프로그램이 반드시 `submit_program()`을 호출하여 제출해야 하며, 텍스트 형태로 프로그램을 출력하는 것과 import를 금지하고, 의미 있는 각 하위 작업은 프리미티브로 등록해야 한다고 요구합니다. 기본적으로 VQA 검증-재시도 모드를 사용합니다. 고유수용감각만으로 성공을 확인할 수 없는 하위 작업은 실행 후 `get_vqa_response()`로 예/아니오 질문을 하고, 부정이면 파라미터를 조정하여 한 번 재시도합니다.

## 핵심 혁신

**1. 언어 교정을 사후 조치가 아닌 일급 시민으로 취급**: 기존 방법은 초기 명령에 전적으로 의존하거나 재훈련이 필요합니다. ARCHITECT는 인간 교정을 직접 실행 가능한 스킬로 변환하여 스킬 라이브러리에 영속화함으로써, 매 실패를 일회성 패치가 아닌 장기적으로 재사용 가능한 지식 축적으로 만듭니다. 이는 본질적으로 컨텍스트 학습을 "예시"에서 "상호작용 이력"으로 확장하는 것입니다.

**2. 프로그램 합성과 도구 호출의 구조적 제약**: 워크플로우 단계(먼저 인식, 그다음 계획, 마지막 실행)를 강제하고 평면적 API 호출 목록을 금지함으로써, LLM이 명확한 하위 작업 경계를 가진 프로그램을 생성하도록 강제합니다. 이러한 구조적 사전 지식은 실패 위치 추적을 가능하게 합니다. 즉, 전체가 실패한 블랙박스를 마주하는 대신 어느 코드 줄이나 도구 호출에 문제가 있는지 정확히 지적할 수 있습니다.

**3. 스킬 라이브러리를 장기 컨텍스트 학습으로 활용**: 모든 스킬이 코드 생성 전마다 컨텍스트에 로드되며, 이는 무한 길이 메모리 메커니즘에 해당합니다. 이를 통해 작업 간 전이가 가능해집니다. 인간 평가에서 작업 1 스킬 라이브러리를 로드한 후 작업 2 성공률이 0/6에서 4/6로 상승하여, 언어 교정의 축적이 시나리오 간 일반화 능력을 가짐을 입증합니다.

## 실험 및 결과

### 주요 벤치마크 (표 1, 8개 작업 × 10 에피소드 × 5개 방법, 총 400회 롤아웃)

| 작업 | CaP SR | π₀ SR | π₀.₅ SR | ARCHITECT-VLM SR | ARCHITECT-HiTL SR |
|---|---|---|---|---|---|
| Banana → plate | .20 | .80 | .90 | .80 | .80 |
| Block → basket | .40 | .40 | 1.0 | .70 | .70 |
| Baseball → bucket | .60 | .00 | .20 | .40 | 1.0 |
| Apple, Bread → bowl | .10 | .40 | .40 | .00 | .80 |
| Pick bread from box | .10 | .40 | .40 | .00 | .70 |
| Close drawer | .00 | .10 | .00 | .40 | .90 |
| Fold cloth into triangle | .00 | .00 | .00 | .70 | .80 |
| Banana under cloth | .00 | .10 | .00 | .00 | .80 |

### 추가 베이스라인 (표 2)
ARCHITECT는 8개 전체 작업에서 Inner Monologue, ProgPrompt, MolmoAct2, GR00T N1.7을 능가합니다. GR00T N1.7은 banana → plate에서만 비제로 성공률(0.40)을 보였고, MolmoAct2는 해당 작업에서 ARCHITECT와 동률이었지만 나머지 작업에서는 모두 뒤처졌습니다.

### 언어 절제 실험 (부록 B, Apple → pan 작업)
ARCHITECT는 15개 언어 변형에서 1.0 SR을 유지했으며, "Length long" 변형만 .00 SR(GCR .80)로 떨어졌습니다. π₀.₅는 표현에 매우 민감하여 "Take the apple and place it onto the pan.", "Move the apple onto the pan.", "Onto the pan, place the apple." 등의 변형에서 SR이 .00으로 하락했습니다.

### 인간 평가 (N=6)
시행당 평균 쿼리 수가 4.67에서 0.83으로 감소(Δ=3.83, p=0.036)했으며, 3/6 참가자가 0회 교정을 필요로 했습니다. 스킬 없이 작업 2 성공률은 0/6이었으나, 작업 1 스킬 라이브러리를 로드한 후 SR은 4/6로 상승했습니다. 1회 교정을 제공한 3명 중 2명은 제로샷으로 작업 2에 실패했고, 2회 이상 교정한 3명은 모두 성공했습니다.

## 경계 및 한계

**주요 실패 모드는 그랩**: 선택된 기성 그랩 생성 모듈(AnyGrasp)에서 비롯되며, 그랩 샘플러 노이즈로 인해 그랩 성공이 교정되지 않으면 스킬 라이브러리에 향후 그랩 실패를 교정할 스킬이 부족할 수 있습니다. 이는 ARCHITECT의 상한이 LLM이나 프로그램 합성 능력이 아닌 하위 인식 모듈의 품질에 의해 제한됨을 의미합니다.

**깊이 추정이 부정확할 때 배치 자세 결정이 어려움**: 예를 들어 버킷에 물건을 넣을 때 너무 높이 들어 올릴 수 있으며, 이는 하위 모듈의 한계로 사용자 교정으로 해결할 수 있지만 상호작용 횟수가 늘어납니다.

**cuRobo 운동 계획 실패**: 목표 자세에 대한 충돌 없는 궤적을 생성할 수 없을 때 ARCHITECT는 계획 오류에 직면하며, 논문은 이 경우의 처리 전략을 명시하지 않았습니다.

**교정 횟수가 핵심 변수**: 1회 교정을 제공한 참가자는 추가 교정 없이 작업 2를 완료하지 못했으며, 이는 유용한 스킬 라이브러리를 구축하려면 충분한 교정 축적이 필요함을 시사합니다. 논문은 교정 품질이 정책에 미치는 영향을 연구하지 않았으며, 로봇 특화 미세 조정이나 데모 데이터 사용도 수행하지 않았습니다.

## 공학적 시사점

**재현 시 먼저 인식 모듈의 결정성을 확인하라**: ARCHITECT의 성능은 AnyGrasp의 그랩 샘플링과 AnyPlace의 배치 예측에 크게 의존합니다. 이러한 모듈이 하드웨어에서 불안정하게 작동하면 전체 프레임워크의 성공률이 현저히 떨어집니다. 전체 파이프라인을 연결하기 전에 `detect_objects()`와 `get_placement_pose()`가 시나리오에서 신뢰할 수 있는지 개별적으로 검증하는 것이 좋습니다.

**스킬 라이브러리 축적 전략이 작업 간 일반화에 직접적 영향을 미침**: 인간 평가에서 교정 횟수가 2회 미만인 참가자는 구조적으로 유사한 새 작업을 제로샷으로 완료하지 못했습니다. 이는 실제 배포에서 각 새 작업에 대해 최소 2-3회의 교정을 준비해야 하며, 그렇지 않으면 스킬 라이브러리가 전이를 지원하기에 부족할 수 있음을 의미합니다.

**가장 함정에 빠지기 쉬운 부분은 `move_ee_guarded()`의 힘 임계값**: 논문에서 제시한 5.0 N은 단단한 표면에 적합하며, 부드러운 표면에서는 약간 증가시켜야 합니다. 대상 물체나 접촉면 재질이 변하면 이 파라미터를 재보정해야 하며, 그렇지 않으면 배치 실패나 물체 손상이 발생할 수 있습니다.

**언어 절제 실험 결과는 VLA의 취약성이 예상보다 훨씬 크다는 것을 시사**: π₀.₅는 "Move the apple onto the pan."과 같은 무해해 보이는 변형에서 SR이 1.0에서 .00으로 급락한 반면, ARCHITECT는 1.0을 유지했습니다. 하류 팀이 VLA 방안을 평가 중이라면 단일 명령 템플릿만 검증하지 말고 다양한 표현으로 테스트해야 합니다.
