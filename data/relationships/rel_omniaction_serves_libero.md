---
$id: "rel_omniaction_serves_libero"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "serves"

source:
  id: "ent_dataset_omniaction"
  name:
    en: "OmniAction Dataset"
    zh: "OmniAction 数据集"
    ko: "OmniAction 데이터셋"

target:
  id: "ent_benchmark_libero"
  name:
    en: "LIBERO"
    zh: "LIBERO"
    ko: "LIBERO"

domains:
  source_domain: "09_data_datasets"
  target_domain: "10_evaluation_benchmarks"

description:
  en: "OmniAction-LIBERO provides training and evaluation data for models tested on the LIBERO benchmark."
  zh: "OmniAction-LIBERO 为在 LIBERO 基准上测试的模型提供训练与评估数据。"
  ko: "OmniAction-LIBERO는 LIBERO 벤치마크에서 테스트되는 모델을 위한 학습 및 평가 데이터를 제공함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Confirmed by the RoboOmni GitHub repository dataset table."

sources:
  - id: "src_roboomni_repo"
    type: "website"
    title: "OpenMOSS/RoboOmni GitHub Repository"
    url: "https://github.com/OpenMOSS/RoboOmni"
    date: "2025-10-30"
    accessed_at: "2026-06-22"
---
