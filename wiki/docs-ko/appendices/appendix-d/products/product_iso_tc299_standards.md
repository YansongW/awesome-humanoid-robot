# ISO/TC 299 로봇 표준군 / ISO/TC 299 Robotics Standards

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [국제표준화기구 / ISO](../companies/company_iso.md) |
| **제품 카테고리** | 로봇 안전 및 성능 표준군 |
| **출시일** | 지속적 업데이트 (ISO/TC 299는 2015년 설립) |
| **상태** | 현행/지속적 유지보수 |
| **공식 홈페이지/출처** | [ISO/TC 299 기술위원회 페이지](https://www.iso.org/committee/5915511.html) |

## 제품 개요

ISO/TC 299 로봇 표준군은 국제표준화기구가 주도하여 제정한 글로벌 로봇 기술 규격 모음으로, 산업용, 서비스용, 협동 및 휴머노이드 로봇의 안전 요구사항, 시험 방법, 용어 정의 및 상호운용성 프레임워크를 포괄합니다. 이 표준군은 로봇 설계, 제조, 통합 및 운영에 대한 국제적으로 인정된 규정 준수 기준을 제공하며, EU, 미국, 중국 등 주요 시장에서 국가 표준 또는 법규 인용 문서로 채택되었습니다.

## 제품 이미지

> ISO/TC 299 표준군: [공식 자료](https://www.iso.org/committee/5915511.html)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 표준군 | ISO/TC 299 로봇 표준 | ISO 공식 홈페이지 |
| 핵심 표준 | ISO 10218-1/-2, ISO/TS 15066, ISO 13482, ISO/TR 20218-1/-2, ISO/TS 18849 등 | ISO/TC 299 |
| 적용 범위 | 산업용 로봇, 협동 로봇, 개인 케어 로봇, 이동 서비스 로봇, 휴머노이드 로봇 | 공개 자료 |
| 기술위원회 | ISO/TC 299 (로봇) | ISO 공식 홈페이지 |
| 버전 상태 | 현행/지속적 개정 | ISO 온라인 스토어 |
| 페이지 수 | 미공개 | 표준별 상이 |
| 언어 | 영어, 프랑스어; 중국어는 국가 채택 버전 | ISO |
| 규정 준수 프레임워크 | CE, UKCA, CCC 등 시장 진입 지원 가능 | 공개 해설 |
| 가격 | 미공개 | ISO 온라인 스토어 |
| 인증 속성 | 인증 제품 아님; 제3자 시험 및 법규 근거 제공 | ISO |

## 공급망 위치

- **제조사**: [국제표준화기구 / ISO](../companies/company_iso.md)
- **핵심 부품/기술 출처**: 회원국 기술 전문가 입력, IEC/TC 44 합동 작업반, 산업 협회, 학술 연구, 사고 데이터
- **하위 응용/고객**: 로봇 OEM, 시스템 통합업체, 인증 기관, 규제 기관, 시험 연구소, 최종 사용자

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_iso_tc299_standards`
- 부품 엔터티: `ent_component_iso_tc299_standards_core`
- 제조사 엔터티: `ent_company_iso`
- 주요 관계:
  - `rel_ent_company_iso_manufactures_ent_product_iso_tc299_standards` (`ent_company_iso` → `manufactures` → `ent_product_iso_tc299_standards`)
  - `rel_ent_company_iso_manufactures_ent_component_iso_tc299_standards_core` (`ent_company_iso` → `manufactures` → `ent_component_iso_tc299_standards_core`)
  - `rel_ent_product_iso_tc299_standards_uses_ent_component_iso_tc299_standards_core` (`ent_product_iso_tc299_standards` → `uses` → `ent_component_iso_tc299_standards_core`)

## 응용 시나리오

- **산업용 로봇 안전**: ISO 10218은 로봇 및 로봇 시스템의 안전 설계 및 통합 요구사항을 제공합니다.
- **협동 로봇**: ISO/TS 15066은 협동 작업의 안전 요구사항, 힘/토크 한계값 및 검증 방법을 정의합니다.
- **개인 케어 로봇**: ISO 13482는 이동 서비스 로봇, 신체 보조 로봇의 안전 요구사항을 다룹니다.
- **휴머노이드 로봇 규정 준수**: 전체 기계 및 시스템 통합 안전 평가의 기본 표준 참조로 사용됩니다.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁 제품 A | 주요 경쟁 제품 B |
|--------|--------|------------|------------|
| 성격 | 국제 로봇 표준군 | IEEE 로봇 표준 | ANSI/RIA R15.06 |
| 적용 범위 | 산업/서비스/협동/휴머노이드 로봇 | 시스템/윤리/상호운용성 중심 | 북미 산업용 로봇 안전 중심 |
| 시장 채택 | 전 세계에서 가장 널리 사용 | 북미/학계/산업 협회 | 미국 시장 |

## 구매 및 배포 권장 사항

- 목표 시장 법규에 따라 해당 국가 표준 채택 버전을 선택하십시오.
- TÜV SÜD, SGS, UL 등 notified body와 협력하여 적합성 평가를 수행하십시오.
- ISO/TC 299의 개정 및 신규 표준을 지속적으로 모니터링하십시오.

## 관련 항목

- [제조사: 국제표준화기구 / ISO](../companies/company_iso.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [ISO 공식 홈페이지](https://www.iso.org)
2. [ISO/TC 299 로봇 기술위원회](https://www.iso.org/committee/5915511.html)
3. ISO 온라인 스토어 및 공개 기술 보고서
4. [부록 D 기업 목록](../index-companies.md)
