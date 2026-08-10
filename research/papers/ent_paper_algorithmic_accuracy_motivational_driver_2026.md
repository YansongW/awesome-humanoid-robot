---
$id: ent_paper_algorithmic_accuracy_motivational_driver_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Algorithmic Accuracy as a Motivational Driver in Robot-Mediated Learning: A Comparative Study of Cross-Correlation
    and CNN-Based Sound Detection in an Interactive Quiz Game'
  zh: 'Algorithmic Accuracy as a Motivational Driver in Robot-Mediated Learning: A Comparative Study of Cross-Correlation
    and CNN-Based Sound Detection in an Interactive Quiz Game'
  ko: 'Algorithmic Accuracy as a Motivational Driver in Robot-Mediated Learning: A Comparative Study of Cross-Correlation
    and CNN-Based Sound Detection in an Interactive Quiz Game'
summary:
  en: In competitive learning activities, inaccurate robot decisions may reduce students' perceptions of fairness and competence,
    ultimately affecting their motivation. This paper investigates whether the accuracy of sound detection algorithms influences
    student motivation during a robot-mediated quiz game. A Pepper humanoid robot hosted an interactive buzzer-based quiz
    in which two sound detection.
  zh: 本文首次将机器人底层感知算法的准确率与学习者动机建立实证关联，通过对比CNN与Cross-Correlation两种声音检测算法在Pepper机器人主持的问答游戏中的表现，发现感知准确率的提升能显著增强学生的内在动机。研究基于自我决定理论提出APMR模型，为教育人机交互领域开辟了“算法性能-用户体验”这一新的研究维度。
  ko: In competitive learning activities, inaccurate robot decisions may reduce students' perceptions of fairness and competence,
    ultimately affecting their motivation. This paper investigates whether the accuracy of sound detection algorithms influences
    student motivation during a robot-mediated quiz game. A Pepper humanoid robot hosted an interactive buzzer-based quiz
    in which two sound detection.
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
- algorithmic
- accuracy
- motivational
- driver
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
  title: 'arXiv:2607.16299 Algorithmic Accuracy as a Motivational Driver in Robot-Mediated Learning: A Comp'
  url: https://arxiv.org/abs/2607.16299
  date: '2026-07-13'
  accessed_at: '2026-08-05'
---

## 概述

本文首次将机器人底层感知算法的准确率与学习者动机建立实证关联，通过对比CNN与Cross-Correlation两种声音检测算法在Pepper机器人主持的问答游戏中的表现，发现感知准确率的提升能显著增强学生的内在动机。研究基于自我决定理论提出APMR模型，为教育人机交互领域开辟了“算法性能-用户体验”这一新的研究维度。

## 它改变了什么

教育HRI领域长期存在一个隐含假设：机器人的感知系统是可靠且透明的。研究者们将注意力集中在机器人外观、教学策略、社交行为等“上层”因素对学习动机的影响，却忽视了底层感知算法出错时对交互公平性和学习者信任的破坏性作用。在竞争性学习场景中，一次误判可能直接导致学生失去得分机会，这种不公体验对动机的打击远大于任何教学策略的优化。本文的贡献在于将“感知可靠性”从工程问题提升为教育心理学问题，揭示了算法准确率与动机之间的因果链条。

声音事件检测领域同样存在认知盲区：研究者们用准确率、延迟、鲁棒性等工程指标评估算法优劣，却从未追问这些指标差异对最终用户（学习者）意味着什么。CNN在实验室条件下表现优异，但部署到真实教室环境时因域失配性能骤降；Cross-Correlation虽“技术含量”较低，却能通过环境特定模板自然适应声学条件。本文用实证数据证明，在真实教育场景中，算法的“适应性”比“先进性”更能转化为用户体验的提升，这颠覆了“越复杂越好”的技术直觉。

## 方法拆解

### 系统架构
- **Pepper机器人**：负责对话管理、题目呈现、手势反馈与平板排行榜更新
- **音频采集模块**：单通道麦克风连续采集蜂鸣器声音
- **声音检测模块**：CNN或Cross-Correlation（唯一实验变量）
- **问答管理模块**：题目逻辑、计分规则、反馈生成

### 两种检测算法
1. **CNN方法**：在受控实验室条件下采集录音训练分类器，部署时不额外重训练。游戏期间持续分析输入音频，基于学习到的声学特征预测蜂鸣事件。检测延迟300 ms，准确率69%。
2. **Cross-Correlation方法**：每次实验前录制参考铃声模板，将输入信号与模板比较波形相似度，归一化相关系数超过预设阈值即判定检测事件。无需依赖先前学习表征，可自然适应部署环境声学特性。检测延迟280 ms，准确率87%。

### 实验设计
- **受试者间设计**：40名大学生，CNN组（n=20）与Cross-Correlation组（n=20）各分4队（每队5人），每条件进行2场对抗赛
- **控制变量**：相同题目、计分规则、机器人行为、教室布局与交互流程
- **动机评估**：内在动机量表（IMI）5个子量表（兴趣/享受、感知胜任、努力/重要性、感知选择、压力/紧张），7点李克特量表，压力/紧张反向编码
- **数据记录**：系统自动记录检测决策与算法性能，进行描述性统计比较

## 关键创新

1. **首次建立“算法准确率-学习动机”实证关联**：此前教育HRI与声音事件检测两个领域独立发展，本文通过受控实验填补了这一空白，证明感知准确率提升（69%→87%）能转化为动机各维度的显著改善，为APMR模型提供了直接证据。

2. **揭示“适应性优于先进性”的设计原则**：CNN虽代表更先进的技术路线，但在真实教室环境中因域失配性能下降；Cross-Correlation通过环境特定模板实现稳健检测。这一发现挑战了“技术越复杂越好”的直觉，为资源受限的教育场景提供了更务实的技术选型依据。

3. **将公平感纳入动机理论框架**：基于自我决定理论，本文提出感知准确率通过增强公平感、胜任感和参与度正向影响动机，将算法可靠性从工程指标升华为影响心理需求的交互设计要素，拓展了教育HRI的理论边界。

## 实验与结果

### 动机结果（IMI子量表，7点李克特）
| 子量表 | CNN组 | Cross-Correlation组 |
|--------|-------|---------------------|
| Interest/Enjoyment | 3.49 ± 0.56 | 4.38 ± 0.54 |
| Perceived Competence | 3.74 ± 0.58 | 4.31 ± 0.48 |
| Effort/Importance | 3.80 ± 0.38 | 4.60 ± 0.46 |
| Perceived Choice | 4.13 ± 0.61 | 4.27 ± 0.71 |
| Pressure/Tension*（反向编码） | 3.86 ± 0.57 | 4.34 ± 0.63 |

### 算法性能对比
| 指标 | CNN | Cross-Correlation |
|------|-----|-------------------|
| Training required | Yes | No |
| Calibration | No | Short template recording |
| Detection latency | 300 ms | 280 ms |
| Detection accuracy | 69% | 87% |

最大动机改善出现在Interest/Enjoyment子量表（3.49→4.38，提升0.89），Perceived Choice差异相对较小（4.13→4.27）。结果表明，感知准确率的提升（由表内数值69%→87%计算）对兴趣与享受的驱动作用最为显著，而对自主选择感的影响有限，这可能因为问答游戏的规则框架限制了感知选择的空间。

## 边界与局限

- **样本局限**：仅涉及40名大学生，样本量相对较小，结论向其他年龄群体（如儿童、青少年）推广需谨慎
- **场景局限**：仅评估单一教育活动（问答游戏）和单一机器人平台（Pepper），其他教育场景（如协作学习、个性化辅导）未考察
- **技术局限**：仅比较两种声音检测方法，且仅在特定教室环境下进行；未测试现代深度学习架构（如域适应、持续学习技术），未考察其他感知模态（如视觉手势识别、多模态融合）
- **阈值细节**：Cross-Correlation的检测阈值具体数值论文未明确，影响复现精度
- **推理频率**：CNN的音频分析推理频率未明确给出，仅描述“持续分析输入音频”

## 工程启示

- **复现优先核对**：Cross-Correlation的参考模板录制流程与阈值设定是复现关键，论文未给出阈值具体数值，需自行标定；CNN的训练数据采集环境与部署教室的声学差异是性能差距的主要来源，复现时需记录环境声学特征
- **选型建议**：在资源受限或环境多变的部署场景，Cross-Correlation的“零训练+环境自适应”特性更具工程优势；若追求更高准确率且能保证环境一致性，CNN仍有潜力，但需引入域适应技术弥补性能衰减
- **最易踩坑**：IMI的压力/紧张子量表需反向编码后分析，直接使用原始分数会导致动机评估偏差；两组实验的教室布局、机器人行为、题目顺序必须严格一致，任何细微差异都可能污染算法性能与动机的因果关系
- **下游团队启示**：教育机器人产品设计应将感知可靠性纳入用户体验指标，而非仅关注功能完成度；建议在开发流程中增加“感知错误率-用户满意度”的联合测试，避免算法团队与交互团队的目标割裂

## Overview
In competitive learning activities, inaccurate robot decisions may reduce students' perceptions of fairness and competence, ultimately affecting their motivation. This paper investigates whether the accuracy of sound detection algorithms influences student motivation during a robot-mediated quiz game. A Pepper humanoid robot hosted an interactive buzzer-based quiz in which two sound detection approaches, a Convolutional Neural Network (CNN) and a Cross-Correlation algorithm, were evaluated using a controlled between-subjects experiment involving 40 university students. Participants were equally assigned to a CNN group (n = 20) and a Cross-Correlation group (n = 20). Both groups completed the same quiz under identical conditions, differing only in the sound detection algorithm used for first-responder identification. Student motivation was assessed using the Intrinsic Motivation Inventory (IMI), while algorithm performance was evaluated through real-time detection accuracy. The results indicate that the Cross-Correlation approach achieved more reliable sound detection under classroom conditions and produced significantly higher scores across all IMI subscales, demonstrating greater student interest, perceived competence, effort, perceived choice, and lower perceived pressure (after reverse coding). These findings provide empirical support for the proposed Algorithmic Precision-Motivation Relationship (APMR) model, demonstrating that algorithmic accuracy is not merely an engineering performance metric but an important factor influencing learner motivation in robot-assisted educational environments.

## 参考
- https://arxiv.org/abs/2607.16299

## 개요

본 논문은 로봇의 저수준 인식 알고리즘 정확도와 학습자 동기 간의 실증적 연관성을 최초로 확립하였다. Pepper 로봇이 진행하는 퀴즈 게임에서 CNN과 Cross-Correlation 두 가지 음향 감지 알고리즘을 비교하여, 인식 정확도의 향상이 학생들의 내적 동기를 유의미하게 강화할 수 있음을 발견하였다. 본 연구는 자기결정성 이론에 기반하여 APMR 모델을 제안하며, 교육용 인간-로봇 상호작용 분야에 '알고리즘 성능-사용자 경험'이라는 새로운 연구 차원을 개척하였다.

## 그것이 바꾼 것

교육 HRI 분야에는 오랫동안 '로봇의 인식 시스템은 신뢰할 수 있고 투명하다'는 암묵적 가정이 존재해 왔다. 연구자들은 로봇의 외형, 교수 전략, 사회적 행동 등 '상위' 요인이 학습 동기에 미치는 영향에 주목해 왔지만, 저수준 인식 알고리즘의 오류가 상호작용의 공정성과 학습자의 신뢰에 미치는 파괴적 영향은 간과해 왔다. 경쟁적 학습 시나리오에서 한 번의 오판은 학생이 득점 기회를 잃게 만들 수 있으며, 이러한 불공정한 경험은 어떤 교수 전략 최적화보다 동기에 더 큰 타격을 준다. 본 논문의 기여는 '인식 신뢰성'을 공학적 문제에서 교육 심리학적 문제로 승격시켜, 알고리즘 정확도와 동기 간의 인과적 사슬을 규명한 데 있다.

음향 이벤트 감지 분야에도 인식적 사각지대가 존재한다. 연구자들은 정확도, 지연 시간, 견고성 등의 공학적 지표로 알고리즘을 평가하지만, 이러한 지표의 차이가 최종 사용자(학습자)에게 무엇을 의미하는지는 묻지 않았다. CNN은 실험실 조건에서 우수한 성능을 보이지만, 실제 교실 환경에 배포되면 도메인 불일치로 인해 성능이 급락한다. Cross-Correlation은 '기술적 수준'이 낮지만 환경 특정 템플릿을 통해 음향 조건에 자연스럽게 적응할 수 있다. 본 논문은 실증 데이터를 통해 실제 교육 시나리오에서 알고리즘의 '적응성'이 '선진성'보다 사용자 경험 향상에 더 크게 기여함을 증명하며, '복잡할수록 좋다'는 기술적 직관을 뒤집는다.

## 방법 분해

### 시스템 아키텍처
- **Pepper 로봇**: 대화 관리, 문제 제시, 제스처 피드백 및 태블릿 순위표 업데이트 담당
- **오디오 수집 모듈**: 단일 채널 마이크로 버저 소리 연속 수집
- **음향 감지 모듈**: CNN 또는 Cross-Correlation(유일한 실험 변수)
- **퀴즈 관리 모듈**: 문제 로직, 채점 규칙, 피드백 생성

### 두 가지 감지 알고리즘
1. **CNN 방법**: 통제된 실험실 조건에서 녹음을 수집하여 분류기를 훈련하고, 배포 시 추가 재훈련 없이 사용. 게임 중 입력 오디오를 지속적으로 분석하여 학습된 음향 특징을 기반으로 버저 이벤트를 예측. 감지 지연 시간 300ms, 정확도 69%.
2. **Cross-Correlation 방법**: 각 실험 전에 기준 벨소리 템플릿을 녹음하고, 입력 신호와 템플릿의 파형 유사도를 비교하여 정규화 상관 계수가 사전 설정된 임계값을 초과하면 감지 이벤트로 판정. 사전 학습 표현에 의존하지 않으며 배포 환경의 음향 특성에 자연스럽게 적응 가능. 감지 지연 시간 280ms, 정확도 87%.

### 실험 설계
- **피험자 간 설계**: 대학생 40명, CNN 그룹(n=20)과 Cross-Correlation 그룹(n=20) 각각 4팀(팀당 5명)으로 구성, 각 조건에서 2회의 대항전 진행
- **통제 변수**: 동일한 문제, 채점 규칙, 로봇 행동, 교실 배치 및 상호작용 절차
- **동기 평가**: 내적 동기 척도(IMI) 5개 하위 척도(흥미/즐거움, 지각된 유능감, 노력/중요성, 지각된 선택, 압력/긴장), 7점 리커트 척도, 압력/긴장은 역코딩
- **데이터 기록**: 시스템이 감지 결정과 알고리즘 성능을 자동 기록, 기술 통계 비교 수행

## 핵심 혁신

1. **'알고리즘 정확도-학습 동기'의 실증적 연관성 최초 확립**: 이전에는 교육 HRI와 음향 이벤트 감지 두 분야가 독립적으로 발전해 왔으나, 본 논문은 통제된 실험을 통해 이 공백을 메우고 인식 정확도 향상(69%→87%)이 동기의 여러 차원에서 유의미한 개선으로 전환될 수 있음을 증명하여 APMR 모델에 직접적인 증거를 제공한다.

2. **'적응성이 선진성보다 우월하다'는 설계 원칙 규명**: CNN은 더 진보된 기술 경로를 대표하지만 실제 교실 환경에서는 도메인 불일치로 성능이 저하된다. Cross-Correlation은 환경 특정 템플릿을 통해 견고한 감지를 구현한다. 이 발견은 '기술이 복잡할수록 좋다'는 직관에 도전하며, 자원이 제한된 교육 시나리오에 더 실용적인 기술 선택 근거를 제공한다.

3. **공정감을 동기 이론 프레임워크에 통합**: 자기결정성 이론에 기반하여, 본 논문은 인식 정확도가 공정감, 유능감, 참여도를 강화함으로써 동기에 긍정적 영향을 미친다고 제안하며, 알고리즘 신뢰성을 공학적 지표에서 심리적 욕구에 영향을 미치는 상호작용 설계 요소로 승격시켜 교육 HRI의 이론적 경계를 확장한다.

## 실험 및 결과

### 동기 결과(IMI 하위 척도, 7점 리커트)
| 하위 척도 | CNN 그룹 | Cross-Correlation 그룹 |
|--------|-------|---------------------|
| Interest/Enjoyment | 3.49 ± 0.56 | 4.38 ± 0.54 |
| Perceived Competence | 3.74 ± 0.58 | 4.31 ± 0.48 |
| Effort/Importance | 3.80 ± 0.38 | 4.60 ± 0.46 |
| Perceived Choice | 4.13 ± 0.61 | 4.27 ± 0.71 |
| Pressure/Tension*(역코딩) | 3.86 ± 0.57 | 4.34 ± 0.63 |

### 알고리즘 성능 비교
| 지표 | CNN | Cross-Correlation |
|------|-----|-------------------|
| Training required | Yes | No |
| Calibration | No | Short template recording |
| Detection latency | 300 ms | 280 ms |
| Detection accuracy | 69% | 87% |

가장 큰 동기 개선은 Interest/Enjoyment 하위 척도에서 나타났으며(3.49→4.38, 0.89 향상), Perceived Choice의 차이는 상대적으로 작았다(4.13→4.27). 결과는 인식 정확도의 향상(표의 69%→87% 값으로 계산)이 흥미와 즐거움에 가장 큰 영향을 미치며, 자율적 선택감에는 제한적인 영향을 미친다는 것을 보여준다. 이는 퀴즈 게임의 규칙 프레임워크가 지각된 선택의 공간을 제한하기 때문일 수 있다.

## 경계 및 한계

- **표본 한계**: 대학생 40명만 대상으로 표본 크기가 상대적으로 작아, 다른 연령대(예: 아동, 청소년)로의 일반화는 신중해야 함
- **시나리오 한계**: 단일 교육 활동(퀴즈 게임)과 단일 로봇 플랫폼(Pepper)만 평가했으며, 다른 교육 시나리오(예: 협력 학습, 개인 맞춤 튜터링)는 검토하지 않음
- **기술 한계**: 두 가지 음향 감지 방법만 비교했고 특정 교실 환경에서만 수행됨. 현대 딥러닝 아키텍처(예: 도메인 적응, 지속 학습 기술)는 테스트하지 않았으며, 다른 인식 양식(예: 시각적 제스처 인식, 다중 모달 융합)도 검토하지 않음
- **임계값 세부 사항**: Cross-Correlation의 감지 임계값 구체적 수치가 논문에 명시되지 않아 재현 정밀도에 영향
- **추론 빈도**: CNN의 오디오 분석 추론 빈도가 명확히 제시되지 않았으며, '입력 오디오 지속 분석'으로만 설명됨

## 공학적 시사점

- **재현 시 우선 확인 사항**: Cross-Correlation의 참조 템플릿 녹음 절차와 임계값 설정이 재현의 핵심이며, 논문에 임계값 구체적 수치가 없으므로 자체 캘리브레이션 필요. CNN의 훈련 데이터 수집 환경과 배포 교실의 음향 차이가 성능 격차의 주요 원인이므로, 재현 시 환경 음향 특성을 기록해야 함
- **선택 권장 사항**: 자원이 제한되거나 환경 변화가 많은 배포 시나리오에서 Cross-Correlation의 '제로 트레이닝 + 환경 적응' 특성이 공학적 이점이 더 큼. 더 높은 정확도를 추구하고 환경 일관성을 보장할 수 있다면 CNN도 잠재력이 있지만, 성능 저하를 보완하기 위해 도메인 적응 기술을 도입해야 함
- **가장 흔한 실수**: IMI의 압력/긴장 하위 척도는 역코딩 후 분석해야 하며, 원점수를 직접 사용하면 동기 평가에 편향이 발생함. 두 그룹 실험의 교실 배치, 로봇 행동, 문제 순서는 엄격히 일치해야 하며, 사소한 차이도 알고리즘 성능과 동기의 인과 관계를 오염시킬 수 있음
- **하위 팀 시사점**: 교육용 로봇 제품 설계는 기능 완성도에만 집중하지 말고 인식 신뢰성을 사용자 경험 지표에 포함해야 함. 개발 프로세스에 '인식 오류율-사용자 만족도'의 통합 테스트를 추가하여 알고리즘 팀과 상호작용 팀의 목표 분리를 방지할 것을 권장함
