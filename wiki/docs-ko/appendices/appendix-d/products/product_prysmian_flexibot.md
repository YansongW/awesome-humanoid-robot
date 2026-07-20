# Prysmian Group Flexibot 로봇 케이블

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [프리즈미안 / Prysmian Group](../companies/company_prysmian.md) |
| **제품 카테고리** | 고유연성 PUR 로봇 케이블 |
| **출시 시간** | 현재 판매 중 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [Prysmian Group 공식 홈페이지](https://www.prysmiangroup.com) |

## 제품 개요

Prysmian Group Flexibot 로봇 케이블은 프리즈미안이 산업용 로봇, 협동 로봇, 휴머노이드 로봇 관절을 대상으로 출시한 고유연성 PUR 로봇 케이블입니다. 이 제품은 표준화된 인터페이스, 안정적인 접촉 및 높은 신뢰성의 산업용 설계를 통해 로봇 시스템의 신호, 전원 또는 데이터 연결에 대한 장기적인 안정적 요구를 충족합니다.

## 제품 이미지

> Prysmian Group Flexibot 로봇 케이블: [공식 자료](https://www.prysmiangroup.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 코어 수 | 맞춤 제작 가능 (일반 4G1.5 mm²) | 공식 카탈로그 |
| 정격 전류 | 미공개 | 공식 데이터시트 |
| 정격 전압 | 300/500 V | 제품 자료 |
| 보호 등급 | IP65 (완제품 케이블 어셈블리) | 제품 자료 |
| 내비틀림 | ±180°/m (일반) | 제품 자료 |
| 외피 재질 | PUR | 제품 자료 |
| 적용 분야 | 산업용 로봇, 협동 로봇, 휴머노이드 로봇 관절 | 제품 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [프리즈미안 / Prysmian Group](../companies/company_prysmian.md)
- **핵심 부품/기술 출처**: 구리/알루미늄 도체, XLPE/PVC/PUR 절연 재료, 차폐 재료, 장갑 재료
- **하위 응용 분야/고객**: 로봇 관절, 용접 로봇, 운반 로봇, 협동 로봇, 휴머노이드 로봇 전체 배선.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_prysmian_flexibot`
- 부품 엔터티: `ent_component_prysmian_flexibot`
- 제조사 엔터티: `ent_company_prysmian`
- 주요 관계:
  - `rel_ent_company_prysmian_manufactures_ent_product_prysmian_flexibot` (`ent_company_prysmian` → `manufactures` → `ent_product_prysmian_flexibot`)
  - `rel_ent_company_prysmian_manufactures_ent_component_prysmian_flexibot` (`ent_company_prysmian` → `manufactures` → `ent_component_prysmian_flexibot`)

## 적용 분야

- **로봇 관절**: 해당 시나리오의 연결 및 배선 요구 사항에 적합.
- **용접 로봇**: 해당 시나리오의 연결 및 배선 요구 사항에 적합.
- **운반 로봇**: 해당 시나리오의 연결 및 배선 요구 사항에 적합.
- **협동 로봇**: 해당 시나리오의 연결 및 배선 요구 사항에 적합.
- **휴머노이드 로봇 전체 배선**: 해당 시나리오의 연결 및 배선 요구 사항에 적합.

## 경쟁 비교

| 비교 항목 | 본 제품 | 국제 브랜드 | 국내 대응 제품 |
|--------|--------|----------|----------|
| 핵심 장점 | 품질 안정, 규격 다양, 글로벌 공급 | 고급 신뢰성 | 비용 및 납기 우위 |
| 납기 | 구성에 따라/안정적 | 중간 | 짧음 |
| 서비스 대응 | 글로벌 유통 네트워크 | 중간 | 신속 |
| 가격 수준 | 중고급 | 고급 | 중저급 |

## 구매 및 배포 제안

- 선정 전 핀 수, 전류, 전압, 보호 등급 및 설치 공간을 확인하고, 필요한 경우 공식 데이터시트와 샘플을 요청하십시오.
- 로봇 응용 분야에서는 내진동, 내굴곡, 내유성 및 EMC 차폐 요구 사항을 중점적으로 평가해야 하며, 프로토타입 검증을 권장합니다.
- 대량 구매 시 공인 대리점 또는 제조사를 통해 납기, MOQ 및 RoHS/REACH 규정 준수 증명을 확인하는 것이 좋습니다.

## 참고 자료

1. [Prysmian Group 공식 홈페이지](https://www.prysmiangroup.com)
2. 제품 데이터시트 및 공개 기술 보도
3. [부록 D 기업 목록](../index-companies.md)
