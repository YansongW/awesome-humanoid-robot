---
$id: ent_paper_omnih2o_universal_and_dexterou_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniH2O: Universal and Dexterous Human-to- Humanoid Whole-Body Teleoperation
    and Learning'
  zh: OmniH2O｜通用灵巧的人对人全身远程操作和学习
  ko: ''
summary:
  en: OmniH2O 主要解决数据闭环：用语言指令、相机图像/多视角观测、人类视频/动捕轨迹采集人类操作和机器人状态，再通过教师-学生知识迁移、PPO/RL
    策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  zh: OmniH2O 主要解决数据闭环：用语言指令、相机图像/多视角观测、人类视频/动捕轨迹采集人类操作和机器人状态，再通过教师-学生知识迁移、PPO/RL
    策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
  ko: ''
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- balance
- behavioral_foundation_model
- locomotion
- motion_tracking
- omnih2o
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (016). Institution: Carnegie Mellon University、Shanghai
    Jiao Tong University. Full title: OmniH2O: Universal and Dexterous Human-to- Humanoid
    Whole-Body Teleoperation and Learning.'
sources:
- id: src_001
  type: website
  title: OmniH2O project page
  url: https://anonymous-omni-h2o.github.io/
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

OmniH2O 主要解决数据闭环：用语言指令、相机图像/多视角观测、人类视频/动捕轨迹采集人类操作和机器人状态，再通过教师-学生知识迁移、PPO/RL 策略训练、ACT/行为克隆模仿学习转成可训练、可复用的全身轨迹/动作序列、低层控制器目标。关键点是用特权信息训练教师策略，再把能力蒸馏到只能使用部署观测的学生策略。
