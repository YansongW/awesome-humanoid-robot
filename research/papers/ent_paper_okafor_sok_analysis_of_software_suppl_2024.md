---
$id: ent_paper_okafor_sok_analysis_of_software_suppl_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoK: Analysis of Software Supply Chain Security by Establishing Secure Design
    Properties'
  zh: SoK：通过建立安全设计属性分析软件供应链安全
  ko: 'SoK: 안전한 설계 속성을 확립하여 소프트웨어 공급망 보안 분석'
summary:
  en: This systematization-of-knowledge paper defines a four-stage software supply
    chain attack pattern (compromise, alteration, propagation, exploitation) and proposes
    transparency, validity, and separation as three orthogonal security properties,
    mapping existing security approaches, tools, and frameworks against them through
    case studies.
  zh: 这篇系统化知识论文定义了软件供应链攻击的四个阶段模式（入侵、篡改、传播、利用），提出透明性、有效性和隔离性作为三个正交安全属性，并通过案例研究将现有安全方法、工具和框架与之对应。
  ko: 이 체계화 지식 논문은 소프트웨어 공급망 공격의 4단계 패턴(침해, 변경, 전파, 이용)을 정의하고 투명성, 유효성, 분리를 세 가지 직교
    보안 속성으로 제안하며, 사례 연구를 통해 기존 보안 접근법, 도구 및 프레임워크를 이에 매핑한다.
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
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text review needed to confirm
    exact section citations and relationship details.
sources:
- id: src_001
  type: paper
  title: 'SoK: Analysis of Software Supply Chain Security by Establishing Secure Design
    Properties'
  url: https://arxiv.org/abs/2406.10109
  date: '2024'
  accessed_at: '2026-06-26'
---


## Overview

The paper systematizes knowledge about secure software supply chain patterns. It identifies four stages of a software supply chain attack: compromise, alteration, propagation, and exploitation. The authors propose three orthogonal security properties—transparency, validity, and separation—as a framework for evaluating and comparing security mechanisms. They map current industry, academic, and government proposals against these properties and analyze their strengths and weaknesses relative to known attacks.

The paper also presents case studies of package repositories (e.g., npm), development environments (e.g., GitHub), end-to-end solutions (e.g., in-toto), and security frameworks (e.g., SLSA, CNCF Best Practices). It notes that most existing approaches focus on artifacts rather than operations and actors, leaving gaps in actor- and operation-centered supply chain security.

## Key Contributions

- A four-stage attack pattern for software supply chain attacks: compromise, alteration, propagation, and exploitation.
- Three orthogonal security properties for secure software supply chains: transparency, validity, and separation.
- A systematic collection and analysis of current security practices mapped to the proposed properties.
- Case studies of package repositories, development environments, end-to-end solutions, and security frameworks.

## Relevance to Humanoid Robotics

Humanoid robots depend on complex, multi-vendor software stacks that integrate open- and closed-source components. The paper's framework of transparency, validity, and separation is directly applicable to ensuring trustworthy composition, update, and deployment of humanoid robot software. As humanoid robots move toward mass production and industrial deployment, applying supply chain security principles becomes critical for safety, reliability, and regulatory compliance.
