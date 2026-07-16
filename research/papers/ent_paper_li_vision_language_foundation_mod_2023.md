---
$id: ent_paper_li_vision_language_foundation_mod_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Vision-Language Foundation Models as Effective Robot Imitators
  zh: RoboFlamingo
  ko: Vision-Language Foundation Models as Effective Robot Imitators
summary:
  en: Vision-Language Foundation Models as Effective Robot Imitators (RoboFlamingo), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by ByteDance Research, Tsinghua University, Shanghai Jiao Tong University,
    National University of Singapore, and published at ICLR 2024.
  zh: Vision-Language Foundation Models as Effective Robot Imitators (RoboFlamingo), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by ByteDance Research, Tsinghua University, Shanghai Jiao Tong University,
    National University of Singapore, and published at ICLR 2024.
  ko: Vision-Language Foundation Models as Effective Robot Imitators (RoboFlamingo), is a 2023 generalized vision-language-action
    model for robotic manipulation, introduced by ByteDance Research, Tsinghua University, Shanghai Jiao Tong University,
    National University of Singapore, and published at ICLR 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- roboflamingo
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2311.01378v3.
sources:
- id: src_001
  type: paper
  title: RoboFlamingo source
  url: https://openreview.net/forum?id=lFYj0oibGR
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation. We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data. To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms. By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks. We believe RoboFlamingo has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy.

## 核心内容
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation. We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data. To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms. By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks. We believe RoboFlamingo has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy.

## 参考
- http://arxiv.org/abs/2311.01378v3

## Overview
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation. We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data. To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms. By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks. We believe RoboFlamingo has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy.

## Content
Recent progress in vision language foundation models has shown their ability to understand multimodal data and resolve complicated vision language tasks, including robotics manipulation. We seek a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics data. To this end, we derive a simple and novel vision-language manipulation framework, dubbed RoboFlamingo, built upon the open-source VLMs, OpenFlamingo. Unlike prior works, RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned manipulation datasets. Such a decomposition provides RoboFlamingo the flexibility for open-loop control and deployment on low-performance platforms. By exceeding the state-of-the-art performance with a large margin on the tested benchmark, we show RoboFlamingo can be an effective and competitive alternative to adapt VLMs to robot control. Our extensive experimental results also reveal several interesting conclusions regarding the behavior of different pre-trained VLMs on manipulation tasks. We believe RoboFlamingo has the potential to be a cost-effective and easy-to-use solution for robotics manipulation, empowering everyone with the ability to fine-tune their own robotics policy.

## 개요
최근 비전-언어 기반 모델의 발전은 멀티모달 데이터를 이해하고 로봇 조작을 포함한 복잡한 비전-언어 작업을 해결할 수 있는 능력을 보여주고 있습니다. 우리는 기존의 비전-언어 모델(VLM)을 로봇 데이터에 간단한 미세 조정만으로 활용할 수 있는 직관적인 방법을 모색합니다. 이를 위해 오픈소스 VLM인 OpenFlamingo를 기반으로 한 간단하고 새로운 비전-언어 조작 프레임워크인 RoboFlamingo를 개발했습니다. 기존 연구와 달리 RoboFlamingo는 사전 학습된 VLM을 단일 단계 비전-언어 이해에 활용하고, 명시적 정책 헤드를 통해 순차적 이력 정보를 모델링하며, 언어 조건부 조작 데이터셋에서 모방 학습을 통해 약간의 미세 조정만 수행합니다. 이러한 분해는 RoboFlamingo에게 개방 루프 제어와 저성능 플랫폼 배포의 유연성을 제공합니다. 테스트된 벤치마크에서 최첨단 성능을 큰 폭으로 초과함으로써, RoboFlamingo가 VLM을 로봇 제어에 적용하는 효과적이고 경쟁력 있는 대안이 될 수 있음을 보여줍니다. 또한 광범위한 실험 결과를 통해 다양한 사전 학습된 VLM이 조작 작업에서 보이는 행동에 관한 몇 가지 흥미로운 결론을 도출했습니다. 우리는 RoboFlamingo가 비용 효율적이고 사용하기 쉬운 로봇 조작 솔루션이 되어, 누구나 자신의 로봇 정책을 미세 조정할 수 있는 능력을 제공할 잠재력이 있다고 믿습니다.

## 핵심 내용
최근 비전-언어 기반 모델의 발전은 멀티모달 데이터를 이해하고 로봇 조작을 포함한 복잡한 비전-언어 작업을 해결할 수 있는 능력을 보여주고 있습니다. 우리는 기존의 비전-언어 모델(VLM)을 로봇 데이터에 간단한 미세 조정만으로 활용할 수 있는 직관적인 방법을 모색합니다. 이를 위해 오픈소스 VLM인 OpenFlamingo를 기반으로 한 간단하고 새로운 비전-언어 조작 프레임워크인 RoboFlamingo를 개발했습니다. 기존 연구와 달리 RoboFlamingo는 사전 학습된 VLM을 단일 단계 비전-언어 이해에 활용하고, 명시적 정책 헤드를 통해 순차적 이력 정보를 모델링하며, 언어 조건부 조작 데이터셋에서 모방 학습을 통해 약간의 미세 조정만 수행합니다. 이러한 분해는 RoboFlamingo에게 개방 루프 제어와 저성능 플랫폼 배포의 유연성을 제공합니다. 테스트된 벤치마크에서 최첨단 성능을 큰 폭으로 초과함으로써, RoboFlamingo가 VLM을 로봇 제어에 적용하는 효과적이고 경쟁력 있는 대안이 될 수 있음을 보여줍니다. 또한 광범위한 실험 결과를 통해 다양한 사전 학습된 VLM이 조작 작업에서 보이는 행동에 관한 몇 가지 흥미로운 결론을 도출했습니다. 우리는 RoboFlamingo가 비용 효율적이고 사용하기 쉬운 로봇 조작 솔루션이 되어, 누구나 자신의 로봇 정책을 미세 조정할 수 있는 능력을 제공할 잠재력이 있다고 믿습니다.
