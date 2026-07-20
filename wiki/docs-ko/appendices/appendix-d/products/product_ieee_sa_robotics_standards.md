# IEEE 로봇 표준군 / IEEE Robotics Standards Portfolio

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [IEEE 표준 협회 / IEEE SA](../companies/company_ieee_sa.md) |
| **제품 카테고리** | 로봇 본체, 상호운용성 및 윤리 표준군 |
| **출시일** | IEEE 1872-2015; IEEE 7000-2021 |
| **상태** | 현행/지속 유지 |
| **공식 홈페이지/출처** | [IEEE SA 공식 홈페이지](https://standards.ieee.org) |

## 제품 개요

IEEE 로봇 표준군은 IEEE SA가 제정하며, 주로 로봇 시스템의 지식 표현, 온톨로지 모델링, 상호운용성 인터페이스 및 윤리적 위험 처리 문제를 해결합니다. 이 표준군은 로봇 개발 플랫폼, 시뮬레이션 도구, 지식 그래프 및 이기종 시스템 통합에 자주 사용되며, 복잡한 로봇(인간형 로봇 포함)에 공유 가능한 의미 기반을 제공합니다.

## 제품 이미지

> IEEE 로봇 표준군: [공식 자료](https://standards.ieee.org)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|-----------|-----|-----------|
| 표준군 | IEEE 로봇 관련 표준 | IEEE SA |
| 핵심 표준 | IEEE 1872-2015, IEEE 7000-2021 | IEEE 표준 데이터베이스 |
| 적용 범위 | 로봇 본체, 시스템 아키텍처, 윤리 설계 | 공개 자료 |
| 기술 위원회 | IEEE SA 로봇 표준 관련 작업 그룹 | IEEE SA |
| 버전 상태 | 현행/지속 개정 | IEEE 표준 데이터베이스 |
| 페이지 수 | 미공개 | 표준별 상이 |
| 언어 | 영어 | IEEE |
| 준수 프레임워크 | 산업 상호운용성 및 연구개발 규범으로 인용 가능 | IEEE SA |
| 가격 | 미공개 | IEEE 표준 스토어 |
| 인증 속성 | 인증 제품 아님; 기술 사양 및 프로세스 모델 제공 | IEEE SA |

## 공급망 위치

- **제조사**: [IEEE 표준 협회 / IEEE SA](../companies/company_ieee_sa.md)
- **핵심 부품/기술 출처**: IEEE 회원 제안, 작업 그룹 초안, 학술 온톨로지, 산업 사용 사례
- **하위 응용/고객**: 로봇 소프트웨어 개발사, 시뮬레이션 플랫폼, 지식 그래프 프로젝트, 의료/서비스 로봇 기업

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ieee_sa_robotics_standards`
- 부품 엔터티: `ent_component_ieee_sa_robotics_standards_core`
- 제조사 엔터티: `ent_company_ieee_sa`
- 주요 관계:
  - `rel_ent_company_ieee_sa_manufactures_ent_product_ieee_sa_robotics_standards` (`ent_company_ieee_sa` → `manufactures` → `ent_product_ieee_sa_robotics_standards`)
  - `rel_ent_company_ieee_sa_manufactures_ent_component_ieee_sa_robotics_standards_core` (`ent_company_ieee_sa` → `manufactures` → `ent_component_ieee_sa_robotics_standards_core`)
  - `rel_ent_product_ieee_sa_robotics_standards_uses_ent_component_ieee_sa_robotics_standards_core` (`ent_product_ieee_sa_robotics_standards` → `uses` → `ent_component_ieee_sa_robotics_standards_core`)

## 응용 시나리오

- **로봇 지식 그래프**: IEEE 1872는 로봇 및 자동화 분야 온톨로지를 제공하여 의미 검색 및 추론에 사용됩니다.
- **플랫폼 간 상호운용성**: 통일된 용어 및 데이터 모델을 제공하여 ROS/Gazebo 등 도구와 제조사 시스템의 통합을 촉진합니다.
- **윤리 및 신뢰 설계**: IEEE 7000은 요구사항 단계에서 시스템이 윤리적 위험을 식별하고 처리하도록 안내합니다.
- **인간형 로봇 행동 모델링**: 표준화된 동작, 환경 상호작용 및 작업 설명을 위한 참조를 제공합니다.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|-----------|---------|---------------|---------------|
| 성격 | IEEE 로봇 표준군 | ISO/TC 299 표준 | ANSI/RIA R15.06 |
| 중점 | 온톨로지/상호운용성/윤리 | 안전/성능/테스트 | 북미 산업용 로봇 안전 |
| 적용 깊이 | 시스템 아키텍처 및 지식 계층 | 완제품 및 규정 준수 계층 | 안전 규정 준수 계층 |

## 구매 및 배포 권장 사항

- ISO/TC 299 안전 표준과 함께 사용하여 다양한 계층의 요구사항을 충족합니다.
- 로봇 시뮬레이션 및 지식 베이스 프로젝트에서 IEEE 1872 온톨로지를 우선 채택합니다.
- IEEE SA 작업 그룹에 참여하여 최신 초안 및 개정 방향을 확인합니다.

## 관련 항목

- [제조사: IEEE 표준 협회 / IEEE SA](../companies/company_ieee_sa.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [IEEE SA 공식 홈페이지](https://standards.ieee.org)
2. [IEEE 1872-2015](https://standards.ieee.org/standard/1872-2015.html)
3. [IEEE 7000-2021](https://standards.ieee.org/standard/7000-2021.html)
4. [부록 D 기업 목록](../index-companies.md)
