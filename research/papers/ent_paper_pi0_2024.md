---
$id: ent_paper_pi0_2024
$schema: ../../../../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
  zh: π0：用于通用机器人控制的视觉-语言-动作流模型
  ko: 'π0: 범용 로봇 제어를 위한 비전-언어-액션 플로우 모델'
summary:
  en: A flow-matching VLA built on a pretrained VLM, trained on diverse dexterous robot data to perform language-conditioned
    tasks such as laundry folding and box assembly.
  zh: 一种基于预训练视觉-语言模型的流匹配 VLA，在多样化的灵巧机器人数据上训练，可执行如叠衣服、组装盒子等语言条件任务。
  ko: 사전 학습된 VLM 기반의 플로우 매칭 VLA로, 다양한 손재주 있는 로봇 데이터로 학습되어 빨래 개기, 상자 조립 등 언어 조건 작업을 수행함.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- vla
- vision_language_action
- flow_matching
- diffusion
- dexterous_manipulation
- foundation_model
- physical_intelligence
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.24164v4.
sources:
- id: src_paper_pi0_2024
  type: paper
  title: 'π0: A Vision-Language-Action Flow Model for General Robot Control'
  url: https://arxiv.org/abs/2410.24164
  date: '2024-10-31'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_paper_openvla_2024
  relationship: cites
  description:
    en: The π0 paper situates itself within the open VLA landscape and references OpenVLA as a contemporary open-source VLA.
    zh: π0 论文将自身置于开放 VLA 格局中，并将 OpenVLA 作为同期开源 VLA 引用。
    ko: π0 논문은 자신을 오픈 VLA 환경에 위치시키고 동시대 오픈소스 VLA인 OpenVLA를 인용함.
theoretical_depth:
- system
---
## 概述
Robot learning holds tremendous promise to unlock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the deepest questions in artificial intelligence. However, bringing robot learning to the level of generality required for effective real-world systems faces major obstacles in terms of data, generalization, and robustness. In this paper, we discuss how generalist robot policies (i.e., robot foundation models) can address these challenges, and how we can design effective generalist robot policies for complex and highly dexterous tasks. We propose a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge. We then discuss how this model can be trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators. We evaluate our model in terms of its ability to perform tasks in zero shot after pre-training, follow language instructions from people and from a high-level VLM policy, and its ability to acquire new skills via fine-tuning. Our results cover a wide variety of tasks, such as laundry folding, table cleaning, and assembling boxes.

## 核心内容
Robot learning holds tremendous promise to unlock the full potential of flexible, general, and dexterous robot systems, as well as to address some of the deepest questions in artificial intelligence. However, bringing robot learning to the level of generality required for effective real-world systems faces major obstacles in terms of data, generalization, and robustness. In this paper, we discuss how generalist robot policies (i.e., robot foundation models) can address these challenges, and how we can design effective generalist robot policies for complex and highly dexterous tasks. We propose a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) to inherit Internet-scale semantic knowledge. We then discuss how this model can be trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators. We evaluate our model in terms of its ability to perform tasks in zero shot after pre-training, follow language instructions from people and from a high-level VLM policy, and its ability to acquire new skills via fine-tuning. Our results cover a wide variety of tasks, such as laundry folding, table cleaning, and assembling boxes.

## 参考
- http://arxiv.org/abs/2410.24164v4

