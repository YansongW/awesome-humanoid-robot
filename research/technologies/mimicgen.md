---
$id: "ent_tech_mimicgen"
$schema: "../../data/schema/v1/entry_schema.json"
$version: 1

type: "technology"

names:
  en: "MimicGen"
  zh: "MimicGen"
  ko: "MimicGen"

summary:
  en: "A demonstration augmentation framework that scales a small set of human seed demonstrations in simulation by perturbing object poses and initial conditions."
  zh: "一种演示增强框架，通过扰动物体位姿和初始条件，在仿真中扩展少量人类种子演示。"
  ko: "물체 자세 및 초기 조건을 변형하여 시뮬레이션에서 소량의 인간 시드 데모를 확장하는 데모 증강 프레임워크."

domains:
  - "08_software_middleware"
  - "09_data_datasets"

layers:
  - "intelligence"

functional_roles:
  - "intelligence"
  - "tool_equipment"

tags:
  - "data_engine"
  - "demonstration_augmentation"
  - "simulation"
  - "data_generation"
  - "vla"
  - "imitation_learning"

verification:
  status: "verified"
  reviewed_by: "human_and_ai"
  reviewed_at: "2026-06-22"
  confidence: "high"
  notes: "Scope confirmed by original RSS 2023 paper and Wang et al. 2026 VLA survey."

sources:
  - id: "src_mimicgen_paper"
    type: "paper"
    title: "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations"
    url: "https://arxiv.org/abs/2310.17596"
    date: "2023-10-26"
    accessed_at: "2026-06-22"
  - id: "src_mimicgen_code"
    type: "website"
    title: "MimicGen GitHub Repository"
    url: "https://github.com/NVlabs/mimicgen"
    date: "2023-10-26"
    accessed_at: "2026-06-22"

related_entities:
  - id: "ent_paper_wang_vla_survey_2026"
    relationship: "cites"
    description:
      en: "Wang et al. 2026 survey discusses MimicGen as a demonstration augmentation method that scales simulator data."
      zh: "Wang 等人 2026 综述将 MimicGen 作为扩展仿真器数据的演示增强方法进行讨论。"
      ko: "Wang et al. 2026 서베이는 MimicGen을 시뮬레이터 데이터를 확장하는 데모 증강 방법으로 논의함."
---

# MimicGen

## Overview

MimicGen is a data-generation system that takes a small number of human demonstrations and automatically produces a large, diverse dataset by perturbing scene configurations in simulation. It is designed to reduce the cost of collecting large-scale robot demonstration data.

## Key Characteristics

- **Seed-driven**: starts from a small set of high-quality human demonstrations.
- **Perturbation-based**: varies object poses, camera viewpoints, and initial conditions.
- **Simulation-native**: operates in physics simulators such as MuJoCo and Isaac Sim.
- **Scalable**: can generate orders of magnitude more data than the original demonstrations.

## Limitations

- Quality depends on the diversity and correctness of the seed demonstrations.
- Perturbations are limited to parametric variations; novel long-horizon compositions are not generated.
- Sim-to-real transfer requires additional domain randomization or calibration.

## Relevance to Humanoid Robotics

MimicGen's seed-and-perturb paradigm could reduce the cost of humanoid data collection, but applying it to whole-body locomotion and manipulation requires handling balance, contact, and morphological constraints that are absent in arm-only tasks.
