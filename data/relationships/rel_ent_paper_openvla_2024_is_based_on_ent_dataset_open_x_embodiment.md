---
$id: "rel_ent_paper_openvla_2024_is_based_on_ent_dataset_open_x_embodiment"
$schema: "../../../../../data/schema/v1/relationship_schema.json"
$version: 1

type: "is_based_on"

source:
  id: "ent_paper_openvla_2024"
  name:
    en: "OpenVLA: An Open-Source Vision-Language-Action Model"
    zh: "OpenVLA：一个开源的视觉-语言-动作模型"
    ko: "OpenVLA: 오픈소스 비전-언어-액션 모델"

target:
  id: "ent_dataset_open_x_embodiment"
  name:
    en: "Open X-Embodiment"
    zh: "Open X-Embodiment"
    ko: "Open X-Embodiment"

domains:
  source_domain: "07_ai_models_algorithms"
  target_domain: "09_data_datasets"

description:
  en: "OpenVLA is pretrained on 970k real-world robot demonstrations from the Open X-Embodiment dataset."
  zh: "OpenVLA 基于 Open X-Embodiment 数据集的 97 万条真实机器人演示进行预训练。"
  ko: "OpenVLA는 Open X-Embodiment 데이터셋의 97만 개 실제 로봇 데모로 사전 학습되었음."

verification:
  status: "partially_verified"
  reviewed_by: "ai"
  reviewed_at: "2026-06-25"
  confidence: "medium"
  notes: "Claim is directly supported by the OpenVLA abstract and paper."

sources:
  - id: "src_paper_openvla_2024"
    type: "paper"
    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
    url: "https://arxiv.org/abs/2406.09246"
    date: "2024-06-13"
    accessed_at: "2026-06-25"
---
