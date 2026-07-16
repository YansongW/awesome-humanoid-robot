---
$id: ent_standard_ul_fcc_ce
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: standard
names:
  en: Regional Market Certifications (UL / FCC / CE)
  zh: 区域准入认证
  ko: 지역별 시장 인증(UL/FCC/CE)
summary:
  en: The set of mandatory or voluntary certifications required to sell robots in specific regions, such as UL for North America,
    CE for Europe, and FCC for electromagnetic compatibility.
  zh: 人形机器人进入各区域市场所需的强制或自愿性认证汇总，涵盖 ISO 13482、ISO/TS 15066、ISO 13849-1、IEC 61508、IEC 62368-1、UL 1740、FCC Part 15、CE 标志、CR 认证与
    CCC 的制定机构、适用范围与核心关注点。
  ko: 특정 지역에서 로봇을 판매하기 위해 필요한 강제 또는 자발적 인증; 북미 UL, 유럽 CE, 전자기 적합성 FCC 등.
domains:
- 12_policy_regulation_ethics
layers:
- validation_markets
functional_roles:
- knowledge
tags:
- standard
- chapter_12
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-01.md#1.13.2 主要国际与区域标准概览 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---


## 概述
区域准入认证是人形机器人领域的重要标准。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
| 标准/认证 | 制定机构 | 适用范围 | 核心关注点 |
|----------|---------|---------|-----------|
| ISO 13482:2014 | ISO | 个人护理机器人 | 机械安全、速度/力限制、接触安全 |
| ISO/TS 15066:2016 | ISO | 协作机器人 | 最大允许压力/力、安全功能 |
| ISO 13849-1:2023 | ISO | 机械安全控制系统 | 控制系统安全相关部件可靠性 |
| IEC 61508:2010 | IEC | 功能安全通用标准 | SIL 等级、安全生命周期 |
| IEC 62368-1:2018 | IEC | 信息技术设备安全 | 电气安全、火灾、能量危险 |
| UL 1740 | UL | 工业机器人安全 | 机器人系统安全评估 |
| FCC Part 15 | FCC | 美国无线电设备 | 电磁兼容与射频干扰 |
| CE 标志 | 欧盟 | 欧盟市场准入 | 符合相关指令（机械指令、低电压指令等） |
| CR 认证 | 中国机器人联盟/认监委 | 中国机器人市场准入 | 安全、EMC、性能、可靠性 |
| CCC | 中国质检总局 | 强制性产品认证 | 电气安全等 |

!!! note "术语解释：CE 标志与 CCC 认证"
    CE 标志是产品进入欧盟市场的合格声明标志，表示产品符合欧盟相关指令的基本要求。CCC（China Compulsory Certification）是中国强制性产品认证，涉及人身安全、动植物生命健康和环境保护的产品必须获得 CCC 认证方可销售。

## 参考
- Wiki extraction
- 项目 Wiki：chapter-01.md#1.13.2 主要国际与区域标准概览

## Overview
Regional access certification is an important standard in the field of humanoid robots. The following content is compiled from the project Wiki for in-depth reference.

## Content
| Standard/Certification | Issuing Body | Scope | Core Focus |
|----------|---------|---------|-----------|
| ISO 13482:2014 | ISO | Personal care robots | Mechanical safety, speed/force limits, contact safety |
| ISO/TS 15066:2016 | ISO | Collaborative robots | Maximum allowable pressure/force, safety functions |
| ISO 13849-1:2023 | ISO | Safety-related parts of control systems | Reliability of safety-related parts of control systems |
| IEC 61508:2010 | IEC | General functional safety standard | SIL levels, safety lifecycle |
| IEC 62368-1:2018 | IEC | Safety of information technology equipment | Electrical safety, fire, energy hazards |
| UL 1740 | UL | Industrial robot safety | Robot system safety assessment |
| FCC Part 15 | FCC | Radio frequency devices in the US | Electromagnetic compatibility and radio frequency interference |
| CE Marking | European Union | EU market access | Compliance with relevant directives (Machinery Directive, Low Voltage Directive, etc.) |
| CR Certification | China Robot Alliance / Certification and Accreditation Administration | China robot market access | Safety, EMC, performance, reliability |
| CCC | General Administration of Quality Supervision, Inspection and Quarantine of China | Compulsory product certification | Electrical safety, etc. |

!!! note "Term Explanation: CE Marking and CCC Certification"
    CE Marking is a declaration of conformity for products entering the EU market, indicating that the product meets the essential requirements of relevant EU directives. CCC (China Compulsory Certification) is China's compulsory product certification system; products involving personal safety, animal and plant life and health, and environmental protection must obtain CCC certification before being sold.

## 개요
지역 접근 인증은 휴머노이드 로봇 분야의 중요한 표준입니다. 아래 내용은 프로젝트 Wiki에서 정리한 것으로, 심층 참고용으로 제공됩니다.

## 핵심 내용
| 표준/인증 | 제정 기관 | 적용 범위 | 핵심 관심 사항 |
|----------|---------|---------|-----------|
| ISO 13482:2014 | ISO | 개인 케어 로봇 | 기계적 안전, 속도/힘 제한, 접촉 안전 |
| ISO/TS 15066:2016 | ISO | 협동 로봇 | 최대 허용 압력/힘, 안전 기능 |
| ISO 13849-1:2023 | ISO | 기계 안전 제어 시스템 | 제어 시스템 안전 관련 부품 신뢰성 |
| IEC 61508:2010 | IEC | 기능 안전 일반 표준 | SIL 등급, 안전 수명 주기 |
| IEC 62368-1:2018 | IEC | 정보 기술 장비 안전 | 전기 안전, 화재, 에너지 위험 |
| UL 1740 | UL | 산업용 로봇 안전 | 로봇 시스템 안전 평가 |
| FCC Part 15 | FCC | 미국 무선 장비 | 전자기 적합성 및 무선 주파수 간섭 |
| CE 마크 | 유럽 연합 | EU 시장 접근 | 관련 지침 준수 (기계 지침, 저전압 지침 등) |
| CR 인증 | 중국 로봇 연맹/인증감독위원회 | 중국 로봇 시장 접근 | 안전, EMC, 성능, 신뢰성 |
| CCC | 중국 품질감독검사검역총국 | 강제 제품 인증 | 전기 안전 등 |

!!! note "용어 설명: CE 마크와 CCC 인증"
    CE 마크는 제품이 EU 시장에 진입하기 위한 적합성 선언 마크로, 제품이 EU 관련 지침의 기본 요구 사항을 충족함을 나타냅니다. CCC(China Compulsory Certification)는 중국 강제 제품 인증으로, 인체 안전, 동식물 생명 건강 및 환경 보호와 관련된 제품은 CCC 인증을 받아야 판매가 가능합니다.
