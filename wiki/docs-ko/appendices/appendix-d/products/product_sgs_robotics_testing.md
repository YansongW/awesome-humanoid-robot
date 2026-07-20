# SGS 로봇 검사 인증 서비스 / SGS Robotics Testing and Certification Service

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [SGS / 스위스 범용 공증행](../companies/company_sgs.md) |
| **제품 카테고리** | 로봇 검사, 인증 및 시장 진입 서비스 |
| **출시 시간** | 지속적으로 제공 |
| **상태** | 상용/프로젝트 기반 |
| **공식 홈페이지/출처** | [SGS 공식 홈페이지](https://www.sgs.com) |

## 제품 개요

SGS 로봇 검사 인증 서비스는 산업용 로봇, 협동 로봇, 서비스 로봇 및 휴머노이드 로봇의 전체 수명 주기를 대상으로 전기 안전, 기계 안전, 전자파 적합성, 무선 주파수, 기능 안전, 소프트웨어 및 네트워크 보안, 환경 신뢰성 및 글로벌 시장 진입 인증을 제공합니다. 서비스는 연구 개발 단계 사전 테스트, 공식 인증, 공장 심사 및 지속적인 감독을 포괄하여 고객의 시장 출시 기간을 단축하고 규정 준수 위험을 낮춥니다.

## 제품 이미지

> SGS 로봇 검사 인증: [공식 자료](https://www.sgs.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 서비스 유형 | 검사, 인증, 검증, 심사, 교육 | SGS 공식 홈페이지 |
| 적용 로봇 | 산업용, 협동, 서비스, 휴머노이드 로봇 | 공개 자료 |
| 적용 규정 | CE, UKCA, FCC, IC, VCCI, CCC 등 | SGS |
| 적용 표준 | ISO 10218, ISO/TS 15066, ISO 13482, IEC 61508, ISO 13849, IEC 60204, IEC 62443 | 공개 자료 |
| 테스트 내용 | 전기 안전, 기계 안전, EMC, 무선, 기능 안전, 환경 신뢰성, 네트워크 보안 | SGS |
| 서비스 기간 | 미공개 | 프로젝트 기반 |
| 인증 마크 | SGS 마크, CE, CB, NRTL 등 | SGS |
| 가격 | 미공개 | 비즈니스 견적 |
| 글로벌 네트워크 | 유럽, 아시아 태평양, 북미, 라틴 아메리카 다수 지역 연구소 | SGS 공식 홈페이지 |

## 공급망 위치

- **제조사**: [SGS / 스위스 범용 공증행](../companies/company_sgs.md)
- **핵심 부품/기술 출처**: 국제 표준 문서, 테스트 장비, 인증 자격, 기능 안전 및 네트워크 보안 전문가 팀
- **하류 응용/고객**: 로봇 OEM, 부품 공급업체, 시스템 통합업체, 국경 간 무역업체, 소매업체

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_sgs_robotics_testing`
- 부품 엔터티: `ent_component_sgs_robotics_testing_core`
- 제조사 엔터티: `ent_company_sgs`
- 주요 관계:
  - `rel_ent_company_sgs_manufactures_ent_product_sgs_robotics_testing` (`ent_company_sgs` → `manufactures` → `ent_product_sgs_robotics_testing`)
  - `rel_ent_company_sgs_manufactures_ent_component_sgs_robotics_testing_core` (`ent_company_sgs` → `manufactures` → `ent_component_sgs_robotics_testing_core`)
  - `rel_ent_product_sgs_robotics_testing_uses_ent_component_sgs_robotics_testing_core` (`ent_product_sgs_robotics_testing` → `uses` → `ent_component_sgs_robotics_testing_core`)

## 응용 시나리오

- **소비자용 로봇 출시**: 청소 로봇, 교육 로봇 등의 전기/EMC/무선 인증.
- **산업용 로봇 수출**: CE, UKCA, 북미 시장 진입 및 규정 준수 문서 지원.
- **협동 로봇 안전 검증**: ISO/TS 15066 및 ISO 10218 차이 분석 및 테스트.
- **휴머노이드 로봇 전체 체인 규정 준수**: 관절, 컨트롤러에서 전체 기계까지의 안전, 기능 안전 및 네트워크 보안 평가.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 기관 | SGS | TÜV SÜD | UL Solutions |
| 강점 지역 | 글로벌 소비재, 국경 간 무역 | 독일/유럽 자동차 및 산업 | 북미 안전 마크 |
| 특징 | 전 품목, 가장 넓은 글로벌 네트워크 | 기능 안전 깊이 | UL 마크 권위 |

## 구매 및 배포 제안

- 목표 시장에 따라 사전에 인증 경로를 계획하여 중복 테스트를 피하십시오.
- SGS 사전 테스트 서비스를 활용하여 설계 단계에서 잠재적인 규정 준수 문제를 발견하십시오.
- 인증을 가속화하기 위해 완전한 BOM, 회로도, 위험 분석 및 소프트웨어 문서를 준비하십시오.

## 관련 항목

- [제조사: SGS / 스위스 범용 공증행](../companies/company_sgs.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [SGS 공식 홈페이지](https://www.sgs.com)
2. [SGS 서비스 카탈로그](https://www.sgs.com)
3. SGS 공개 서비스 매뉴얼
4. [부록 D 기업 목록](../index-companies.md)
