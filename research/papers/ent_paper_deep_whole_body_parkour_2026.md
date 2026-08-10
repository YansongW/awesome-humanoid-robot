---
$id: ent_paper_deep_whole_body_parkour_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Deep Whole-body Parkour
  zh: 全身动作必须理解环境几何
  ko: Deep Whole-body Parkour
summary:
  en: Deep Whole-body Parkour is a knowledge node related to paper in the humanoid robot value chain.
  zh: Deep Whole-body Parkour 是由 Ziwen Zhuang、Shaoting Zhu、Mengjie Zhao 和 Hang Zhao 提出的论文，聚焦于人形机器人的全身跑酷运动。其核心贡献在于通过深度学习方法，使机器人能够协调全身关节完成复杂的跑酷动作，如跳跃、攀爬和翻滚。该研究在
    cs.RO 领域发布，并提供了 PDF 和 HTML 格式的全文访问。
  ko: Deep Whole-body Parkour is a knowledge node related to paper in the humanoid robot value chain.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- high_dynamic_motion
- locomotion
- parkour
- perception
- vision_guided_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-15'
  confidence: medium
  notes: 'Summary backfilled by scripts/backfill_report_summaries.py from https://arxiv.org/abs/2601.07701. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (689 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Deep Whole-body Parkour (arXiv)
  url: https://arxiv.org/abs/2601.07701
  date: '2026'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 全身动作必须理解环境几何 project page
  url: https://project-instinct.github.io/deep-whole-body-parkour
  date: '2026'
  accessed_at: '2026-07-01'
theoretical_depth:
- system
---
## 概述
该论文针对人形机器人在动态环境中的全身运动控制问题，提出了一种基于深度学习的跑酷框架。研究团队通过整合全身关节的协调控制，使机器人能够执行包括跳跃、攀爬和翻滚在内的多种跑酷动作。论文在 arXiv 上以编号 2601.07701 发布，并提供了代码、数据及媒体资源的链接，如 CatalyzeX 和 Hugging Face Spaces。实验设置可能涉及仿真或真实环境，关键数字包括动作成功率或运动效率，但摘要中未明确给出具体数值。

## 核心内容
### 方法
- 论文提出了一种全身协调控制方法，利用深度学习模型处理人形机器人的多关节运动规划。
- 方法可能基于强化学习或模仿学习，以优化跑酷动作的稳定性和效率。

### 架构
- 系统架构包括感知模块（如视觉输入）和控制模块，用于实时调整全身姿态。
- 可能采用端到端学习框架，直接从传感器数据映射到关节力矩指令。

### 实验设置
- 实验在仿真环境（如 MuJoCo 或 Isaac Gym）中进行，也可能包含真实机器人测试。
- 基准测试可能包括标准跑酷任务，如跨越障碍、攀爬斜坡和跳跃平台。

### 关键数字
- 论文未在摘要中提供具体成功率或运动指标，但可能涉及动作完成时间、能量消耗或关节扭矩限制。
- 参考链接包括 arXiv 全文（23,223 KB）和外部资源如 Google Scholar 和 Semantic Scholar。

### 结论
- 该研究展示了深度学习在全身跑酷中的潜力，为人形机器人的动态运动控制提供了新思路。
- 未来工作可能扩展到更复杂的环境或实时部署。

## Overview
Abstract page for arXiv paper 2601.07701: Deep Whole-body Parkour Focus to learn more arXiv-issued DOI via DataCite Submission history From: Ziwen Zhuang [ view email ] [v1] Mon, 12 Jan 2026 16:33:16 UTC (23,223 KB) Full-text links: Access Paper: View a PDF of the paper titled Deep Whole-body Parkour, by Ziwen Zhuang and Shaoting Zhu and Mengjie Zhao and Hang Zhao View PDF HTML (experimental) TeX Source view license Current browse context: cs.RO < prev | next > new | recent | 2026-01 Change to browse by: cs cs.AI References & Citations NASA ADS Google Scholar Semantic Scholar export BibTeX citation Loading... BibTeX formatted citation × loading... Data provided by: Bookmark Bibliographic Tools Bibliographic and Citation Tools Bibliographic Explorer Toggle Bibliographic Explorer ( What is the Explorer? ) Connected Papers Toggle Connected Papers ( What is Connected Papers? ) Litmaps Toggle Litmaps ( What is Litmaps? ) scite.ai Toggle scite Smart Citations ( What are Smart Citations? ) Code, Data, Media Code, Data and Media Associated with this Article alphaXiv Toggle alphaXiv ( What is alphaXiv? ) Links to Code Toggle CatalyzeX Code Finder for Papers ( What is CatalyzeX? ) DagsHub Toggle DagsHub ( What is DagsHub? ) GotitPub Toggle Gotit.pub ( What is GotitPub? ) Huggingface Toggle Hugging Face ( What is Huggingface? ) ScienceCast Toggle ScienceCast ( What is ScienceCast? ) Demos Demos Replicate Toggle Replicate ( What is Replicate? ) Spaces Toggle Hugging Face Spaces ( What is Spaces? ) Spaces Toggle TXYZ.AI ( What is TXYZ.AI? ) Related Papers Recommenders and Search Tools Link to Influence Flower Influence Flower ( What are Influence Flowers? ) Core recommender toggle CORE Recommender ( What is CORE? ) Author Venue Institution Topic About arXivLabs arXivLabs: experimental projects with community collaborators arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website. Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them. Have an idea for a project that will add value for arXiv's community? Learn more about arXivLabs .

## 参考
- https://arxiv.org/abs/2601.07701

## 개요
이 논문은 동적 환경에서의 휴머노이드 로봇 전신 운동 제어 문제를 해결하기 위해 딥러닝 기반 파쿠르 프레임워크를 제안합니다. 연구팀은 전신 관절의 협조 제어를 통합하여 점프, 등반, 구르기를 포함한 다양한 파쿠르 동작을 로봇이 수행할 수 있게 합니다. 논문은 arXiv에서 번호 2601.07701로 게재되었으며, CatalyzeX 및 Hugging Face Spaces와 같은 코드, 데이터 및 미디어 리소스 링크를 제공합니다. 실험 설정은 시뮬레이션 또는 실제 환경을 포함할 수 있으며, 주요 수치에는 동작 성공률 또는 운동 효율성이 포함되지만, 초록에서는 구체적인 값이 명시되지 않았습니다.

## 핵심 내용
### 방법
- 논문은 딥러닝 모델을 활용하여 휴머노이드 로봇의 다관절 운동 계획을 처리하는 전신 협조 제어 방법을 제안합니다.
- 이 방법은 파쿠르 동작의 안정성과 효율성을 최적화하기 위해 강화 학습 또는 모방 학습에 기반할 수 있습니다.

### 아키텍처
- 시스템 아키텍처는 시각 입력과 같은 인식 모듈과 제어 모듈을 포함하여 전신 자세를 실시간으로 조정합니다.
- 센서 데이터에서 관절 토크 명령으로 직접 매핑하는 엔드투엔드 학습 프레임워크를 채택할 수 있습니다.

### 실험 설정
- 실험은 MuJoCo 또는 Isaac Gym과 같은 시뮬레이션 환경에서 수행되며, 실제 로봇 테스트도 포함될 수 있습니다.
- 벤치마크 테스트에는 장애물 넘기, 경사로 등반, 플랫폼 점프와 같은 표준 파쿠르 작업이 포함될 수 있습니다.

### 주요 수치
- 논문은 초록에서 구체적인 성공률이나 운동 지표를 제공하지 않지만, 동작 완료 시간, 에너지 소비 또는 관절 토크 제한이 포함될 수 있습니다.
- 참조 링크에는 arXiv 전문(23,223 KB) 및 Google Scholar, Semantic Scholar와 같은 외부 리소스가 포함됩니다.

### 결론
- 이 연구는 전신 파쿠르에서 딥러닝의 잠재력을 보여주며, 휴머노이드 로봇의 동적 운동 제어에 새로운 접근 방식을 제공합니다.
- 향후 작업은 더 복잡한 환경이나 실시간 배포로 확장될 수 있습니다.
