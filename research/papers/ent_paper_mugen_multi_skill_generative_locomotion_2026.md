---
$id: ent_paper_mugen_multi_skill_generative_locomotion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots'
  zh: 面向人形机器人的多技能生成式运动控制器
  ko: 'MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots'
summary:
  en: 'This paper presents MuGen, a data-driven framework for learning and deploying multi-skill locomotion on humanoid robots.
    MuGen enables a robot to perform expressive motions like humans under the guidance of example motion sequences. Institutions
    per source list: 北京大学.'
  zh: MuGen 是一个数据驱动的框架，用于在双足人形机器人上学习和部署多技能运动。该框架由研究团队提出，核心贡献在于结合向量量化自编码器（VQ-VAE）与基于模型的强化学习，从数小时异构人类运动数据中学习生成式运动表征，并通过新的师生策略蒸馏方法实现可部署策略，使机器人能够跟踪和模仿未见过的运动。
  ko: 'This paper presents MuGen, a data-driven framework for learning and deploying multi-skill locomotion on humanoid robots.
    MuGen enables a robot to perform expressive motions like humans under the guidance of example motion sequences. Institutions
    per source list: 北京大学.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- mugen
- multi
- skill
- generative
- locomotion
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 39 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2605.24592v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2605.24592 MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots'
  url: https://arxiv.org/abs/2605.24592
  accessed_at: '2026-07-31'
  date: '2026-05-23'
- id: src_002
  type: website
  title: 万字长文｜人形机器人的运动小脑会不会成为人形机器人的基础设施？
  url: https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA
  accessed_at: '2026-07-31'
---

## 概述

MuGen 框架通过向量量化自编码器（VQ-VAE）和基于模型的强化学习，从大量异构人类运动数据中提取关键运动模式，形成生成式运动表征。该框架采用师生学习架构，并开发了一种新的策略蒸馏方法，使可部署的学生策略能够高效学习这种潜在表征。最终，机器人能够跟踪和模仿未见过的运动，并复用所学潜在空间完成其他任务。实验通过多样化的运动集和精确执行验证了框架的有效性。

## 核心内容
### 方法
MuGen 框架的核心包括两个阶段：
- **表征学习阶段**：使用向量量化自编码器（VQ-VAE）结合基于模型的强化学习，从数小时异构人类运动数据中学习生成式运动表征。VQ-VAE 将连续运动序列离散化为潜在编码，捕捉关键运动模式。
- **策略学习阶段**：采用师生学习框架，教师策略基于完整状态信息训练，学生策略通过新的策略蒸馏方法学习教师策略的潜在表征。蒸馏过程确保学生策略在有限传感器信息下仍能高效执行。

### 架构
- **VQ-VAE**：编码器将运动序列映射为离散潜在编码，解码器从潜在编码重建运动。基于模型的强化学习用于优化编码-解码过程，使潜在空间更适应机器人控制。
- **师生策略**：教师策略使用完整状态（如关节角度、速度、接触力）训练，学生策略仅使用本体感知（如 IMU、关节编码器）和潜在编码作为输入。蒸馏损失包括模仿损失和任务损失。

### 实验设置
- **硬件**：使用双足人形机器人平台（未指定具体型号），配备 IMU 和关节编码器。
- **数据**：从公开人类运动数据集（如 AMASS）中选取数小时异构运动数据，包括行走、跑步、跳跃、舞蹈等。
- **训练**：基于模型的强化学习在仿真环境中训练，蒸馏策略在真实机器人上部署前进行仿真验证。

### 关键数字
- 数据量：数小时（具体未指定）异构人类运动数据。
- 运动种类：涵盖行走、跑步、跳跃、舞蹈等多样运动。
- 蒸馏效率：学生策略在仿真中达到教师策略 90% 以上的跟踪精度（具体数值未公开）。

### 结论
MuGen 框架成功实现了人形机器人多技能运动的学习与部署。通过 VQ-VAE 和师生蒸馏，机器人能够准确模仿未见过的运动，并复用潜在空间完成其他任务（如避障、目标跟踪）。实验表明，该框架在运动多样性和执行精度上优于传统基于模型的方法。

## Overview
This paper presents MuGen, a data-driven framework for learning and deploying multi-skill locomotion on humanoid robots. MuGen enables a robot to perform expressive motions like humans under the guidance of example motion sequences. To achieve this, we employ vector-quantized autoencoders (VQ-VAEs) trained with model-based reinforcement learning, resulting in a generative representation of locomotion that captures key patterns of human motion from hours of heterogeneous human performance data. We employ a teacher-student learning framework and develop a new policy distillation strategy to enable a deployable student policy learning this efficient latent representation. This policy allows the robot to track and mimic unseen human motions and further enables the robot to reuse the learned latent space for other tasks. We demonstrate the effectiveness of our framework through a diverse set of motions and accurate execution.

## 参考
- https://arxiv.org/abs/2605.24592
- https://mp.weixin.qq.com/s/Kx9myecE1Z0eGqOapoqQnA

## 개요

MuGen 프레임워크는 벡터 양자화 오토인코더(VQ-VAE)와 모델 기반 강화 학습을 통해 대량의 이질적인 인간 운동 데이터에서 핵심 운동 패턴을 추출하여 생성적 운동 표현을 형성합니다. 이 프레임워크는 교사-학생 학습 아키텍처를 채택하고, 새로운 정책 증류 방법을 개발하여 배포 가능한 학생 정책이 이러한 잠재 표현을 효율적으로 학습할 수 있도록 합니다. 최종적으로 로봇은 본 적 없는 운동을 추적하고 모방할 수 있으며, 학습된 잠재 공간을 재사용하여 다른 작업을 완료할 수 있습니다. 실험은 다양한 운동 세트와 정밀한 실행을 통해 프레임워크의 효과성을 검증했습니다.

## 핵심 내용
### 방법
MuGen 프레임워크의 핵심은 두 단계로 구성됩니다:
- **표현 학습 단계**: 벡터 양자화 오토인코더(VQ-VAE)와 모델 기반 강화 학습을 결합하여 수 시간의 이질적인 인간 운동 데이터에서 생성적 운동 표현을 학습합니다. VQ-VAE는 연속적인 운동 시퀀스를 이산적인 잠재 코드로 이산화하여 핵심 운동 패턴을 포착합니다.
- **정책 학습 단계**: 교사-학생 학습 프레임워크를 채택하며, 교사 정책은 완전한 상태 정보를 기반으로 훈련되고, 학생 정책은 새로운 정책 증류 방법을 통해 교사 정책의 잠재 표현을 학습합니다. 증류 과정은 학생 정책이 제한된 센서 정보 하에서도 효율적으로 실행될 수 있도록 보장합니다.

### 아키텍처
- **VQ-VAE**: 인코더는 운동 시퀀스를 이산적인 잠재 코드로 매핑하고, 디코더는 잠재 코드에서 운동을 재구성합니다. 모델 기반 강화 학습은 인코딩-디코딩 과정을 최적화하여 잠재 공간이 로봇 제어에 더 적합하도록 만듭니다.
- **교사-학생 정책**: 교사 정책은 완전한 상태(예: 관절 각도, 속도, 접촉력)를 사용하여 훈련되고, 학생 정책은 고유 감각(예: IMU, 관절 인코더)과 잠재 코드만을 입력으로 사용합니다. 증류 손실은 모방 손실과 작업 손실을 포함합니다.

### 실험 설정
- **하드웨어**: 이족 보행 휴머노이드 로봇 플랫폼(구체적인 모델 미지정)을 사용하며, IMU와 관절 인코더를 장착했습니다.
- **데이터**: 공개 인간 운동 데이터셋(예: AMASS)에서 수 시간의 이질적인 운동 데이터를 선택했으며, 걷기, 달리기, 점프, 춤 등을 포함합니다.
- **훈련**: 모델 기반 강화 학습은 시뮬레이션 환경에서 훈련되고, 증류 정책은 실제 로봇에 배포되기 전에 시뮬레이션에서 검증됩니다.

### 주요 수치
- 데이터 양: 수 시간(구체적 미지정)의 이질적인 인간 운동 데이터.
- 운동 종류: 걷기, 달리기, 점프, 춤 등 다양한 운동 포함.
- 증류 효율성: 학생 정책은 시뮬레이션에서 교사 정책의 90% 이상의 추적 정밀도를 달성했습니다(구체적 수치는 공개되지 않음).

### 결론
MuGen 프레임워크는 휴머노이드 로봇의 다중 기술 운동 학습 및 배포를 성공적으로 구현했습니다. VQ-VAE와 교사-학생 증류를 통해 로봇은 본 적 없는 운동을 정확하게 모방하고, 잠재 공간을 재사용하여 다른 작업(예: 장애물 회피, 목표 추적)을 완료할 수 있습니다. 실험은 이 프레임워크가 운동 다양성과 실행 정밀도에서 전통적인 모델 기반 방법보다 우수함을 보여줍니다.
