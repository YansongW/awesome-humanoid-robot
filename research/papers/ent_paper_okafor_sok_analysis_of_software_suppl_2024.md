---
$id: ent_paper_okafor_sok_analysis_of_software_suppl_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties'
  zh: SoK：通过建立安全设计属性分析软件供应链安全
  ko: 'SoK: 안전한 설계 속성을 확립하여 소프트웨어 공급망 보안 분석'
summary:
  en: This systematization-of-knowledge paper defines a four-stage software supply chain attack pattern (compromise, alteration,
    propagation, exploitation) and proposes transparency, validity, and separation as three orthogonal security properties,
    mapping existing security approaches, tools, and frameworks against them through case studies.
  zh: 这篇系统化知识论文定义了软件供应链攻击的四个阶段（入侵、篡改、传播、利用），并提出透明度、有效性和隔离性三个正交安全属性。作者通过案例研究将现有安全方法、工具和框架映射到这些属性上，分析了当前技术的优势与不足。
  ko: 이 체계화 지식 논문은 소프트웨어 공급망 공격의 4단계 패턴(침해, 변경, 전파, 이용)을 정의하고 투명성, 유효성, 분리를 세 가지 직교 보안 속성으로 제안하며, 사례 연구를 통해 기존 보안 접근법, 도구
    및 프레임워크를 이에 매핑한다.
domains:
- 08_software_middleware
- 05_mass_production
- 12_policy_regulation_ethics
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- knowledge
- policy
tags:
- software_supply_chain_security
- secure_design
- transparency
- validity
- separation
- slsa
- in_toto
- supply_chain_attack
- open_source_software
- multi_vendor_software
- package_repository
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10109v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'SoK: Analysis of Software Supply Chain Security by Establishing Secure Design Properties'
  url: https://arxiv.org/abs/2406.10109
  date: '2024'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该论文系统化梳理了软件供应链安全模式，将攻击过程划分为入侵、篡改、传播和利用四个阶段。作者提出透明度、有效性和隔离性作为保障供应链安全的核心属性，并通过案例研究将现有安全方法、工具和框架与这些属性进行映射。论文评估了当前技术相对于已知攻击的优缺点，并详细介绍了各类安全框架，最后指出以行为者和操作为中心的供应链安全技术中存在的潜在空白。

## 核心内容
### 攻击模式与安全属性
- 论文将软件供应链攻击归纳为四个阶段：入侵（compromise）、篡改（alteration）、传播（propagation）和利用（exploitation）。
- 提出三个正交安全属性：透明度（transparency）确保供应链各环节可审计；有效性（validity）保证组件来源与完整性可验证；隔离性（separation）限制攻击影响范围。

### 现有技术映射
- 通过案例研究将现有安全方法（如签名验证、SBOM、可信构建）映射到三个属性，发现多数工具仅覆盖单一属性。
- 分析当前框架（如SLSA、in-toto）的优缺点：SLSA强调构建完整性但缺乏运行时隔离，in-toto提供元数据验证但透明度机制不完善。

### 关键发现与空白
- 现有技术对“传播”和“利用”阶段的防护较弱，尤其是针对依赖混淆和恶意更新攻击。
- 以行为者为中心（actor-centered）的技术（如访问控制）和以操作为中心（operation-centered）的技术（如CI/CD审计）之间存在协同不足，导致攻击面未被完全覆盖。
- 论文指出需要跨阶段联合防御，例如将透明度与隔离性结合以检测供应链中的横向移动。

## Overview
This paper systematizes knowledge about secure software supply chain patterns. It identifies four stages of a software supply chain attack and proposes three security properties crucial for a secured supply chain: transparency, validity, and separation. The paper describes current security approaches and maps them to the proposed security properties, including research ideas and case studies of supply chains in practice. It discusses the strengths and weaknesses of current approaches relative to known attacks and details the various security frameworks put out to ensure the security of the software supply chain. Finally, the paper highlights potential gaps in actor and operation-centered supply chain security techniques

## Overview
This paper systematizes knowledge about secure software supply chain patterns. It identifies four stages of a software supply chain attack and proposes three security properties crucial for a secured supply chain: transparency, validity, and separation. The paper describes current security approaches and maps them to the proposed security properties, including research ideas and case studies of supply chains in practice. It discusses the strengths and weaknesses of current approaches relative to known attacks and details the various security frameworks put out to ensure the security of the software supply chain. Finally, the paper highlights potential gaps in actor and operation-centered supply chain security techniques.

## Content
This paper systematizes knowledge about secure software supply chain patterns. It identifies four stages of a software supply chain attack and proposes three security properties crucial for a secured supply chain: transparency, validity, and separation. The paper describes current security approaches and maps them to the proposed security properties, including research ideas and case studies of supply chains in practice. It discusses the strengths and weaknesses of current approaches relative to known attacks and details the various security frameworks put out to ensure the security of the software supply chain. Finally, the paper highlights potential gaps in actor and operation-centered supply chain security techniques.

## 개요
본 논문은 안전한 소프트웨어 공급망 패턴에 대한 지식을 체계화합니다. 소프트웨어 공급망 공격의 네 가지 단계를 식별하고, 안전한 공급망에 중요한 세 가지 보안 속성(투명성, 유효성, 분리)을 제안합니다. 현재의 보안 접근 방식을 설명하고 이를 제안된 보안 속성에 매핑하며, 연구 아이디어와 실제 공급망 사례 연구를 포함합니다. 알려진 공격과 관련된 현재 접근 방식의 강점과 약점을 논의하고, 소프트웨어 공급망의 보안을 보장하기 위해 제시된 다양한 보안 프레임워크를 상세히 설명합니다. 마지막으로, 행위자 및 운영 중심의 공급망 보안 기술에서 잠재적인 격차를 강조합니다.

## 핵심 내용
본 논문은 안전한 소프트웨어 공급망 패턴에 대한 지식을 체계화합니다. 소프트웨어 공급망 공격의 네 가지 단계를 식별하고, 안전한 공급망에 중요한 세 가지 보안 속성(투명성, 유효성, 분리)을 제안합니다. 현재의 보안 접근 방식을 설명하고 이를 제안된 보안 속성에 매핑하며, 연구 아이디어와 실제 공급망 사례 연구를 포함합니다. 알려진 공격과 관련된 현재 접근 방식의 강점과 약점을 논의하고, 소프트웨어 공급망의 보안을 보장하기 위해 제시된 다양한 보안 프레임워크를 상세히 설명합니다. 마지막으로, 행위자 및 운영 중심의 공급망 보안 기술에서 잠재적인 격차를 강조합니다.

## 参考
- http://arxiv.org/abs/2406.10109v1
