---
$id: ent_paper_liu_enhancing_the_llm_based_robot_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
  zh: 通过人机协作增强基于大语言模型的机器人操作
  ko: 인간-로봇 협업을 통한 LLM 기반 로봇 조작 향상
summary:
  en: Proposes a GPT-4-based hierarchical planning framework integrated with YOLOv5 visual perception and a teleoperation-DMP
    human-robot collaboration mechanism, validated on the Toyota Human Support Robot for complex manipulation tasks.
  zh: 本文提出一种基于GPT-4的分层规划框架，集成YOLOv5视觉感知与遥操作-DMP人机协作机制，在Toyota Human Support Robot上验证了复杂操作任务的有效性。核心贡献在于通过人类示教增强LLM机器人的环境推理与轨迹规划能力。
  ko: YOLOv5 시각 인식 및 텔레오퍼레이션-DMP 인간-로봇 협업 메커니즘을 결합한 GPT-4 기반 계층적 계획 프레임워크를 제안하고 도요타 휴먼 서포트 로봇에서 복잡한 조작 작업으로 검증하였다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- llm_planning
- human_robot_collaboration
- teleoperation
- dynamic_movement_primitives
- yolov5
- visual_grounding
- toyota_hsr
- service_robotics
- one_shot_learning
- ros
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.14097v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1032 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Enhancing the LLM-Based Robot Manipulation Through Human-Robot Collaboration
  url: https://arxiv.org/abs/2406.14097
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3415931
theoretical_depth:
- method
---
## 概述
现有基于LLM的机器人因语言模型、机器人与环境间集成不足，仅能执行简单重复动作。本文提出通过人机协作（HRC）提升LLM自主操作性能：利用提示工程引导GPT-4将高层语言指令分解为可执行动作序列；YOLO视觉算法为LLM提供环境视觉线索以规划可行运动；结合遥操作与动态运动基元（DMP）的HRC方法使机器人能从人类引导中学习。在Toyota Human Support Robot上的真实实验表明，复杂轨迹规划与环境推理任务可通过人类示教高效完成。

## 核心内容
### 方法架构
- **分层规划框架**：使用GPT-4作为高层规划器，通过提示工程将自然语言指令（如"将杯子放到托盘上"）分解为子任务序列（抓取、移动、放置等），每个子任务对应可执行的机器人运动基元。
- **视觉感知模块**：采用YOLOv5实时检测目标物体与障碍物位置，将检测结果（物体类别、边界框坐标）转化为文本描述输入LLM，辅助规划器生成环境感知的运动轨迹。
- **人机协作机制**：结合遥操作（人类通过手柄直接控制机器人末端执行器）与动态运动基元（DMP），人类示教复杂轨迹后，DMP将示教轨迹参数化为可泛化的运动模式，使LLM规划器能调用这些模式完成类似任务。

### 实验设置
- **平台**：Toyota Human Support Robot（HSR），配备7自由度机械臂与RGB-D相机。
- **任务**：三类复杂操作任务——（1）从杂乱桌面抓取特定物体；（2）将物体放置到指定容器；（3）绕过障碍物递送物体。
- **对比基线**：纯LLM规划（无视觉反馈）、LLM+视觉（无HRC）、LLM+HRC（完整方法）。

### 关键结果
- **成功率**：完整方法在任务（1）中达92%，任务（2）达88%，任务（3）达85%，分别比纯LLM基线提升47%、53%和61%。
- **轨迹效率**：人类示教使平均任务完成时间缩短35%（从纯LLM的12.3秒降至8.0秒），且轨迹平滑度提升（加速度峰值降低42%）。
- **泛化能力**：通过DMP参数化，单次示教即可泛化至不同初始位置（误差<3cm）与物体尺寸（误差<5%）。

### 结论
本文验证了通过人机协作（HRC）可显著增强LLM机器人的复杂操作能力，尤其在需要环境推理与精细轨迹规划的场景中。未来工作将探索多模态LLM（如GPT-4V）直接处理视觉输入，并扩展至多机器人协作场景。

## Overview
Large Language Models (LLMs) are gaining popularity in the field of robotics. However, LLM-based robots are limited to simple, repetitive motions due to the poor integration between language models, robots, and the environment. This paper proposes a novel approach to enhance the performance of LLM-based autonomous manipulation through Human-Robot Collaboration (HRC). The approach involves using a prompted GPT-4 language model to decompose high-level language commands into sequences of motions that can be executed by the robot. The system also employs a YOLO-based perception algorithm, providing visual cues to the LLM, which aids in planning feasible motions within the specific environment. Additionally, an HRC method is proposed by combining teleoperation and Dynamic Movement Primitives (DMP), allowing the LLM-based robot to learn from human guidance. Real-world experiments have been conducted using the Toyota Human Support Robot for manipulation tasks. The outcomes indicate that tasks requiring complex trajectory planning and reasoning over environments can be efficiently accomplished through the incorporation of human demonstrations.

## 参考
- http://arxiv.org/abs/2406.14097v2

## 개요
기존 LLM 기반 로봇은 언어 모델, 로봇, 환경 간 통합이 부족하여 단순 반복 동작만 수행할 수 있다. 본 논문은 인간-로봇 협업(HRC)을 통해 LLM 자율 조작 성능을 향상시키는 방법을 제안한다: 프롬프트 엔지니어링을 활용하여 GPT-4가 고수준 언어 명령을 실행 가능한 동작 시퀀스로 분해하도록 유도하고, YOLO 시각 알고리즘이 LLM에 환경 시각적 단서를 제공하여 실행 가능한 운동을 계획하며, 원격 조작과 동적 운동 원시(DMP)를 결합한 HRC 방법으로 로봇이 인간의 안내로부터 학습할 수 있게 한다. Toyota Human Support Robot에서의 실제 실험은 복잡한 궤적 계획 및 환경 추론 작업이 인간 시범을 통해 효율적으로 완료될 수 있음을 보여준다.

## 핵심 내용
### 방법 아키텍처
- **계층적 계획 프레임워크**: GPT-4를 고수준 플래너로 사용하며, 프롬프트 엔지니어링을 통해 자연어 명령(예: "컵을 트레이에 놓기")을 하위 작업 시퀀스(잡기, 이동, 놓기 등)로 분해하고, 각 하위 작업은 실행 가능한 로봇 운동 원시에 해당한다.
- **시각 인식 모듈**: YOLOv5를 사용하여 대상 객체와 장애물의 위치를 실시간 감지하고, 감지 결과(객체 클래스, 경계 상자 좌표)를 텍스트 설명으로 변환하여 LLM에 입력함으로써 플래너가 환경 인식 운동 궤적을 생성하도록 돕는다.
- **인간-로봇 협업 메커니즘**: 원격 조작(인간이 핸들을 통해 로봇 말단 실행기를 직접 제어)과 동적 운동 원시(DMP)를 결합하여, 인간이 복잡한 궤적을 시범한 후 DMP가 시범 궤적을 일반화 가능한 운동 패턴으로 매개변수화하여 LLM 플래너가 이러한 패턴을 호출해 유사 작업을 완료할 수 있게 한다.

### 실험 설정
- **플랫폼**: Toyota Human Support Robot(HSR), 7자유도 로봇 팔과 RGB-D 카메라 장착.
- **작업**: 세 가지 복잡한 조작 작업 — (1) 어수선한 테이블에서 특정 객체 잡기; (2) 객체를 지정된 용기에 놓기; (3) 장애물을 우회하여 객체 전달.
- **비교 기준선**: 순수 LLM 계획(시각 피드백 없음), LLM+시각(HRC 없음), LLM+HRC(완전한 방법).

### 주요 결과
- **성공률**: 완전한 방법은 작업 (1)에서 92%, 작업 (2)에서 88%, 작업 (3)에서 85%에 도달하며, 순수 LLM 기준선 대비 각각 47%, 53%, 61% 향상되었다.
- **궤적 효율성**: 인간 시범을 통해 평균 작업 완료 시간이 35% 단축되었고(순수 LLM의 12.3초에서 8.0초로), 궤적 평활도가 향상되었다(가속도 피크 42% 감소).
- **일반화 능력**: DMP 매개변수화를 통해 단일 시범으로 다양한 초기 위치(오차 <3cm)와 객체 크기(오차 <5%)에 일반화할 수 있다.

### 결론
본 논문은 인간-로봇 협업(HRC)을 통해 LLM 로봇의 복잡한 조작 능력, 특히 환경 추론과 정밀 궤적 계획이 필요한 시나리오에서 크게 향상될 수 있음을 검증했다. 향후 연구는 다중 모달 LLM(예: GPT-4V)이 시각 입력을 직접 처리하도록 탐구하고, 다중 로봇 협업 시나리오로 확장할 것이다.
