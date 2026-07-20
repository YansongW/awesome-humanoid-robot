# ANSI/RIA R15.06 산업용 로봇 안전 표준 / ANSI/RIA R15.06 Industrial Robot Safety Standard

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [ANSI/RIA](../companies/company_ansi_ria.md) |
| **제품 카테고리** | 산업용 로봇 안전 국가 표준 |
| **발행일** | 2012 (R15.06-2012) |
| **상태** | 현행/지속 유지 |
| **공식 홈페이지/출처** | [ANSI/RIA R15.06 표준 페이지](https://webstore.ansi.org/standards/ria/ansiriar15062012) |

## 제품 개요

ANSI/RIA R15.06은 미국 산업용 로봇 안전의 핵심 국가 표준으로, ANSI와 RIA(현 A3)가 공동 발행했습니다. 이 표준은 ISO 10218-1 및 ISO 10218-2를 채택 및 조정하여 산업용 로봇, 로봇 시스템 및 통합 애플리케이션의 안전 설계, 설치, 운영 및 유지보수 요구 사항을 규정하며, 북미 시장에서 로봇 규정 준수의 기초가 됩니다.

## 제품 이미지

> ANSI/RIA R15.06: [공식 자료](https://webstore.ansi.org/standards/ria/ansiriar15062012)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 표준 번호 | ANSI/RIA R15.06-2012 | ANSI/A3 |
| 채택 국제 표준 | ISO 10218-1:2011, ISO 10218-2:2011 | 공개 자료 |
| 적용 범위 | 산업용 로봇, 로봇 시스템, 통합 애플리케이션 | R15.06 |
| 기술 내용 | 위험 평가, 안전 설계, 설치 요구 사항, 운영 유지보수, 검증 | 공개 자료 |
| 버전 상태 | 현행/개정 예정 | ANSI/A3 |
| 페이지 수 | 미공개 | ANSI 스토어 |
| 언어 | 영어 | ANSI |
| 규정 준수 프레임워크 | OSHA, NFPA, 미국 주 규정 및 보험 요구 사항 지원 | 공개 해설 |
| 가격 | 미공개 | ANSI/A3 스토어 |
| 인증 속성 | 비인증 제품; 규정 인용 및 시장 규정 준수 근거로 사용 | ANSI/A3 |

## 공급망 위치

- **제조사**: [ANSI/RIA](../companies/company_ansi_ria.md)
- **핵심 부품/기술 출처**: ISO/TC 299 기술 입력, RIA/A3 회원사 실무, 사고 데이터, 테스트 방법
- **하위 애플리케이션/고객**: 북미 로봇 OEM, 자동차/전자 제조사, 시스템 통합업체, 보험사, 규제 기관

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_ansi_ria_r15_06`
- 부품 엔터티: `ent_component_ansi_ria_r15_06_core`
- 제조사 엔터티: `ent_company_ansi_ria`
- 주요 관계:
  - `rel_ent_company_ansi_ria_manufactures_ent_product_ansi_ria_r15_06` (`ent_company_ansi_ria` → `manufactures` → `ent_product_ansi_ria_r15_06`)
  - `rel_ent_company_ansi_ria_manufactures_ent_component_ansi_ria_r15_06_core` (`ent_company_ansi_ria` → `manufactures` → `ent_component_ansi_ria_r15_06_core`)
  - `rel_ent_product_ansi_ria_r15_06_uses_ent_component_ansi_ria_r15_06_core` (`ent_product_ansi_ria_r15_06` → `uses` → `ent_component_ansi_ria_r15_06_core`)

## 적용 시나리오

- **산업용 로봇 작업장 안전 설계**: 위험 평가, 안전 보호, 비상 정지 및 인터록.
- **시스템 통합 규정 준수**: 로봇과 주변 장비 통합 시 안전 거리 및 레이아웃 요구 사항.
- **협동 로봇 북미 도입**: ISO/TS 15066 및 R15.06과 함께 힘/속도 제한 검증 수행.
- **보험 및 책임 판정**: 사고 조사 및 안전 감사의 기준 문서로 사용.

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 성격 | 미국 산업용 로봇 안전 국가 표준 | ISO/TC 299 국제 표준 | CSA Z434 (캐나다) |
| 적용 범위 | 북미 산업용 로봇 및 통합 시스템 | 전 세계 공통 | 캐나다 시장 |
| 규정 연계 | OSHA, NFPA, 보험 체계 | CE/UKCA 인용 | 캐나다 규정 |

## 구매 및 배포 권장 사항

- 미국 시장 진출 시 제품이 R15.06 및 OSHA 인용 요구 사항을 충족하는지 확인해야 합니다.
- UL, TÜV SÜD 등 인증 기관과 협력하여 차이 분석 및 테스트를 수행하십시오.
- ANSI/A3의 R15.06 개정 동향을 주시하십시오.

## 관련 항목

- [제조사: ANSI/RIA](../companies/company_ansi_ria.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [ANSI 공식 홈페이지](https://www.ansi.org)
2. [A3 공식 홈페이지](https://www.a3.org)
3. [ANSI/RIA R15.06 표준 페이지](https://webstore.ansi.org/standards/ria/ansiriar15062012)
4. [부록 D 기업 목록](../index-companies.md)
