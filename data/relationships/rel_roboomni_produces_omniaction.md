---
$id: "rel_roboomni_produces_omniaction"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "produces"

source:
  id: "ent_paper_roboomni_2025"
  name:
    en: "RoboOmni: Proactive Robot Manipulation in Omni-modal Context"
    zh: "RoboOmni：全模态上下文中的主动式机器人操作"
    ko: "RoboOmni: 옴니모달 맥락에서의 주도적 로봇 조작"

target:
  id: "ent_dataset_omniaction"
  name:
    en: "OmniAction Dataset"
    zh: "OmniAction 数据集"
    ko: "OmniAction 데이터셋"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "09_data_datasets"

description:
  en: "The RoboOmni paper introduces and releases the OmniAction dataset for training omni-modal VLA models."
  zh: "RoboOmni 论文引入并发布了用于训练全模态 VLA 模型的 OmniAction 数据集。"
  ko: "RoboOmni 논문은 옴니모달 VLA 모델 학습을 위한 OmniAction 데이터셋을 소개하고 공개함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Confirmed by the RoboOmni arXiv paper and GitHub repository."

sources:
  - id: "src_roboomni_paper"
    type: "paper"
    title: "RoboOmni: Proactive Robot Manipulation in Omni-modal Context"
    url: "https://arxiv.org/abs/2510.23763"
    date: "2025-10-30"
    accessed_at: "2026-06-22"
---
