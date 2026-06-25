---
$id: "rel_libero_plus_is_version_of_libero"
$schema: "../schema/v1/relationship_schema.json"
$version: 1

type: "is_version_of"

source:
  id: "ent_benchmark_libero_plus"
  name:
    en: "LIBERO-Plus"
    zh: "LIBERO-Plus"
    ko: "LIBERO-Plus"

target:
  id: "ent_benchmark_libero"
  name:
    en: "LIBERO"
    zh: "LIBERO"
    ko: "LIBERO"

domains:
  source_domain: "10_evaluation_benchmarks"
  target_domain: "10_evaluation_benchmarks"

description:
  en: "LIBERO-Plus extends LIBERO with systematic robustness perturbations and a larger task set."
  zh: "LIBERO-Plus 在 LIBERO 基础上增加了系统性鲁棒性扰动和更大的任务集。"
  ko: "LIBERO-Plus는 LIBERO에 체계적 견고성 섭동과 더 큰 작업 세트를 추가하여 확장함."

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Confirmed by the LIBERO-plus arXiv paper and GitHub repository."

sources:
  - id: "src_libero_plus_paper"
    type: "paper"
    title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
    url: "https://arxiv.org/abs/2510.13626"
    date: "2025-10-17"
    accessed_at: "2026-06-22"
---
