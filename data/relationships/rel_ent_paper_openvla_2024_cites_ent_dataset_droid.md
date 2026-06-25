---
$id: "rel_ent_paper_openvla_2024_cites_ent_dataset_droid"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "cites"

source:
  id: "ent_paper_openvla_2024"
  name:
    en: "OpenVLA: An Open-Source Vision-Language-Action Model"
    zh: "OpenVLA：一个开源的视觉-语言-动作模型"
    ko: "OpenVLA: 오픈소스 비전-언어-액션 모델"

target:
  id: "ent_dataset_droid"
  name:
    en: "DROID"
    zh: "DROID"
    ko: "DROID"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "09_data_datasets"

description:
  en: "The OpenVLA paper discusses DROID as part of the diverse robot demonstration data used for pretraining."
  zh: "OpenVLA 论文将 DROID 作为预训练所使用的多样化机器人演示数据的一部分进行讨论。"
  ko: "OpenVLA 논문은 사전 학습에 사용된 다양한 로봇 데모 데이터의 일부로 DROID를 다룸."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "DROID is a component of Open X-Embodiment; the OpenVLA paper references the aggregate dataset. Specific citation of DROID within the paper should be verified by human review."

sources:
  - id: "src_paper_openvla_2024"
    type: "paper"
    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
    url: "https://arxiv.org/abs/2406.09246"
    date: "2024-06-13"
    accessed_at: "2026-06-25"
---
