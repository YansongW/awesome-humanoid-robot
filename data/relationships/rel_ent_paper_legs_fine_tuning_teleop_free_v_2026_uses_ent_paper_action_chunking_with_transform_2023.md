---
$id: rel_ent_paper_legs_fine_tuning_teleop_free_v_2026_uses_ent_paper_action_chunking_with_transform_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_legs_fine_tuning_teleop_free_v_2026
  name:
    en: 'LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World'
    zh: LEGS｜微调无TeleopVLA，用于体现高斯泼溅世界中的人形移动操作
target:
  id: ent_paper_action_chunking_with_transform_2023
  name:
    en: Action Chunking with Transformers
    zh: 基于Transformer的动作分块
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'LEGS: Fine-Tuning Teleop-Free VLAs for Humanoid Loco-manipulation in an Embodied Gaussian Splatting World uses Action
    Chunking with Transformers.'
  zh: LEGS｜微调无TeleopVLA，用于体现高斯泼溅世界中的人形移动操作使用基于Transformer的动作分块。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用ACT（Action Chunking with Transformers）行为克隆进行模仿学习，因此使用了该方法。
    | 证据: **方法或模型框架**：LEGS 构建了一个端到端的多模态学习框架，其核心流程分为三步：首先，将语言指令、多视角相机图像、本体状态（关节角度、IMU 数据）与关节序列编码为统一的多模态表征；其次，采用 ACT（Action
    Chunking with Transformers）行为克隆与 VLA 多模态动作模型进行模仿学习，同时引入世界模型/视频预测模块，对地形、场景与物体动态进行隐式建模；最后，预测低层控制器目标（如关节力矩、足端轨迹），并通过高斯泼溅场景表示实现可微的视觉-物理联合优化。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_legs_fine_tuning_teleop_free_v_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_legs_fine_tuning_teleop_free_v_2026/
  accessed_at: '2026-07-16'
---
