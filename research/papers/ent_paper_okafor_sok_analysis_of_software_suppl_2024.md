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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10109v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (709 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2406.10109v1

## 개요
이 논문은 소프트웨어 공급망 보안 패턴을 체계적으로 정리하여, 공격 과정을 침입, 변조, 전파, 이용의 네 단계로 구분합니다. 저자는 투명성, 유효성, 격리성을 공급망 보안의 핵심 속성으로 제안하고, 사례 연구를 통해 기존 보안 방법, 도구, 프레임워크를 이러한 속성에 매핑합니다. 논문은 알려진 공격에 대한 현재 기술의 장단점을 평가하고 다양한 보안 프레임워크를 상세히 소개하며, 마지막으로 행위자와 운영 중심의 공급망 보안 기술에서 존재하는 잠재적 공백을 지적합니다.

## 핵심 내용
### 공격 패턴과 보안 속성
- 논문은 소프트웨어 공급망 공격을 침입(compromise), 변조(alteration), 전파(propagation), 이용(exploitation)의 네 단계로 요약합니다.
- 세 가지 직교 보안 속성을 제안합니다: 투명성(transparency)은 공급망의 각 단계가 감사 가능하도록 보장하고, 유효성(validity)은 구성 요소의 출처와 무결성을 검증 가능하게 하며, 격리성(separation)은 공격의 영향 범위를 제한합니다.

### 기존 기술 매핑
- 사례 연구를 통해 기존 보안 방법(예: 서명 검증, SBOM, 신뢰할 수 있는 빌드)을 세 가지 속성에 매핑한 결과, 대부분의 도구가 단일 속성만을 다루는 것을 발견합니다.
- 현재 프레임워크(예: SLSA, in-toto)의 장단점을 분석합니다: SLSA는 빌드 무결성을 강조하지만 런타임 격리가 부족하고, in-toto는 메타데이터 검증을 제공하지만 투명성 메커니즘이 불완전합니다.

### 주요 발견과 공백
- 기존 기술은 '전파'와 '이용' 단계의 방어가 약하며, 특히 의존성 혼동(dependency confusion)과 악성 업데이트 공격에 취약합니다.
- 행위자 중심(actor-centered) 기술(예: 접근 제어)과 운영 중심(operation-centered) 기술(예: CI/CD 감사) 간의 협력이 부족하여 공격 표면이 완전히 커버되지 않습니다.
- 논문은 투명성과 격리성을 결합하여 공급망 내 수평 이동을 탐지하는 등, 단계 간 통합 방어가 필요하다고 지적합니다.
