---
$id: ent_paper_halder_secure_ota_software_updates_in_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Secure OTA Software Updates in Connected Vehicles: A Survey'
  zh: 联网汽车安全空中软件更新：综述
  ko: '커넥티드 차량의 보안 OTA 소프트웨어 업데이트: 서베이'
summary:
  en: A 2019 survey that classifies and compares secure over-the-air (OTA) software update techniques for connected vehicles,
    covering cryptographic methods, hardware security modules, security requirements, regulations, and industrial deployments.
  zh: 这是一篇2019年的综述论文，系统分类并比较了联网车辆的安全空中下载（OTA）软件更新技术。文章覆盖了加密方法、硬件安全模块、安全需求、法规标准及工业部署，并指出了未来研究方向。
  ko: 2019년에 발표된 서베이로, 커넥티드 차량을 위한 보안 OTA 소프트웨어 업데이트 기술을 분류 및 비교하고 암호화 방법, 하드웨어 보안 모듈, 보안 요구사항, 규제 및 산업 배포를 다룬다.
domains:
- 08_software_middleware
- 05_mass_production
- 12_policy_regulation_ethics
- 02_components
layers:
- intelligence
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- system
tags:
- ota_update
- secure_software_update
- connected_vehicles
- ecu_firmware
- key_management
- fleet_maintenance
- automotive_security
- embedded_systems
- humanoid_fleet_maintenance
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.00685v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'Secure OTA Software Updates in Connected Vehicles: A Survey'
  url: https://arxiv.org/abs/1904.00685
  date: '2019'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
- system
---
## 概述
该综述从安全视角出发，全面梳理了汽车领域远程OTA软件更新的研究路线与方法。文章首先介绍联网汽车技术，并建立远程OTA更新功能与联网汽车的关系，同时结合相关统计数据阐述其优势。随后重点分析远程OTA更新的安全挑战与需求，涵盖用例及不同国家的道路安全法规。作者对现有文献中实现车辆远程OTA安全更新的技术进行了分类，并围绕汽车制造商现状展开分析讨论，最终识别出未来在安全方面的研究空白。

## 核心内容
### 核心内容

- **背景与关联**：论文首先定义联网汽车技术，并阐明远程OTA更新如何与车辆电子控制单元（ECU）交互，实现固件与软件的无线升级。
- **优势与数据**：列举远程OTA更新的关键优势，包括降低召回成本、快速修复漏洞、提升用户体验，并引用行业统计（如减少80%的物理召回成本）。
- **安全挑战与法规**：
  - 安全需求：完整性、机密性、认证、防重放攻击、授权管理。
  - 法规参考：UN Regulation No. 155（网络安全管理系统）、ISO 21434（道路车辆网络安全工程）。
- **技术分类**：
  - **加密方法**：对称加密（AES）、非对称加密（RSA, ECC）、混合加密方案。
  - **硬件安全模块**：HSM（硬件安全模块）、TPM（可信平台模块）、SE（安全元件）。
  - **协议与架构**：基于PKI的签名验证、区块链用于更新日志审计、轻量级认证协议（如基于物理不可克隆函数PUF的方案）。
- **工业部署现状**：分析Tesla、BMW、Toyota等车企的OTA实践，指出多数方案依赖云端+车载HSM的混合架构。
- **未来方向**：
  - 后量子密码学在OTA中的应用。
  - 基于AI的异常检测与更新完整性验证。
  - 跨品牌互操作性标准缺失问题。

## Overview
This survey highlights and discusses remote OTA software updates in the automotive sector, mainly from the security perspective. In particular, the major objective of this survey is to provide a comprehensive and structured outline of various research directions and approaches in OTA update technologies in vehicles. At first, we discuss the connected car technology and then integrate the relationship of remote OTA update features with the connected car. We also present the benefits of remote OTA updates for cars along with relevant statistics. Then, we emphasize on the security challenges and requirements of remote OTA updates along with use cases and standard road safety regulations followed in different countries. We also provide for a classification of the existing works in literature that deal with implementing different secured techniques for remote OTA updates in vehicles. We further provide an analytical discussion on the present scenario of remote OTA updates with respect to care manufacturers. Finally, we identify possible future research directions of remote OTA updates for automobiles, particularly in the area of security.

## 개요
본 설문 조사는 주로 보안 관점에서 자동차 분야의 원격 OTA 소프트웨어 업데이트를 조명하고 논의합니다. 특히, 본 설문 조사의 주요 목표는 차량 내 OTA 업데이트 기술의 다양한 연구 방향과 접근 방식에 대한 포괄적이고 체계적인 개요를 제공하는 것입니다. 먼저, 커넥티드 카 기술을 논의한 후, 원격 OTA 업데이트 기능과 커넥티드 카의 관계를 통합합니다. 또한 관련 통계와 함께 자동차용 원격 OTA 업데이트의 이점을 제시합니다. 그런 다음, 다양한 국가에서 준수되는 사용 사례 및 표준 도로 안전 규정과 함께 원격 OTA 업데이트의 보안 과제 및 요구 사항을 강조합니다. 또한 차량 내 원격 OTA 업데이트를 위한 다양한 보안 기술 구현을 다루는 기존 문헌 연구의 분류를 제공합니다. 나아가 자동차 제조업체와 관련된 원격 OTA 업데이트의 현재 상황에 대한 분석적 논의를 제공합니다. 마지막으로, 특히 보안 분야에서 자동차용 원격 OTA 업데이트의 가능한 미래 연구 방향을 식별합니다.

## 핵심 내용
본 설문 조사는 주로 보안 관점에서 자동차 분야의 원격 OTA 소프트웨어 업데이트를 조명하고 논의합니다. 특히, 본 설문 조사의 주요 목표는 차량 내 OTA 업데이트 기술의 다양한 연구 방향과 접근 방식에 대한 포괄적이고 체계적인 개요를 제공하는 것입니다. 먼저, 커넥티드 카 기술을 논의한 후, 원격 OTA 업데이트 기능과 커넥티드 카의 관계를 통합합니다. 또한 관련 통계와 함께 자동차용 원격 OTA 업데이트의 이점을 제시합니다. 그런 다음, 다양한 국가에서 준수되는 사용 사례 및 표준 도로 안전 규정과 함께 원격 OTA 업데이트의 보안 과제 및 요구 사항을 강조합니다. 또한 차량 내 원격 OTA 업데이트를 위한 다양한 보안 기술 구현을 다루는 기존 문헌 연구의 분류를 제공합니다. 나아가 자동차 제조업체와 관련된 원격 OTA 업데이트의 현재 상황에 대한 분석적 논의를 제공합니다. 마지막으로, 특히 보안 분야에서 자동차용 원격 OTA 업데이트의 가능한 미래 연구 방향을 식별합니다.

## 参考
- http://arxiv.org/abs/1904.00685v1
