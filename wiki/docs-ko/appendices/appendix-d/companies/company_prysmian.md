# 프리즈미안 / Prysmian Group

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | 프리즈미안 |
| **영문명** | Prysmian Group |
| **본사** | 이탈리아 밀라노 |
| **설립 연도** | 1879 (전신 Pirelli Cavi) |
| **공식 웹사이트** | [https://www.prysmiangroup.com](https://www.prysmiangroup.com) |
| **공급망 단계** | 전력 케이블, 통신 케이블, 산업 특수 케이블 |
| **기업 속성** | 상장 기업 (BIT: PRY) |
| **모회사/소속 그룹** | 독립 상장 |
| **데이터 출처** | 공식 웹사이트, 연례 보고서, 제품 카탈로그 |

## 회사 소개

Prysmian Group은 세계 최대의 케이블 시스템 제조업체 중 하나로, 에너지, 통신, 건축 및 산업 특수 케이블을 포괄합니다. 로봇/트랙 케이블 및 플렉시블 케이블은 높은 동적 성능, 내비틀림, 내유성, 내화학성을 요구하는 로봇 애플리케이션에 적합합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Flexibot / 로봇 케이블 | 고플렉시블 동력/제어 케이블 | Flexibot 시리즈 | 산업용 로봇, 협동 로봇 |
| Afumex 케이블 | 저연무할로겐 케이블 | Afumex Green Power | 건축, 신재생 에너지 |
| Sicon 케이블 | 산업 통신/데이터 케이블 | Sicon 시리즈 | 산업 네트워크, 센서 |

## 대표 제품

### Prysmian Group Flexibot 로봇 케이블

> Prysmian Group Flexibot 로봇 케이블: [공식 자료](https://www.prysmiangroup.com)를 방문하여 확인하십시오.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 코어 수 | 맞춤 제작 (일반 4G1.5 mm²) | 공식 카탈로그 |
| 정격 전류 | 미공개 | 공식 데이터시트 |
| 정격 전압 | 300/500 V | 제품 자료 |
| 보호 등급 | IP65 (완제 케이블 어셈블리) | 제품 자료 |
| 내비틀림 | ±180°/m (일반) | 제품 자료 |
| 외피 재질 | PUR | 제품 자료 |
| 적용 시나리오 | 산업용 로봇, 협동 로봇, 휴머노이드 로봇 관절 | 제품 자료 |
| 가격 | 미공개 | 미공개 |

**기술 하이라이트**: PUR 외피는 내유성, 내마모성, 내굴곡성을 갖추며 비틀림 및 트랙 운동을 지원하여 로봇 동력 및 신호 전송에 적합합니다.

**적용 시나리오**: 로봇 관절, 용접 로봇, 운반 로봇, 협동 로봇, 휴머노이드 로봇 전체 배선.

### Prysmian Group Afumex Green Power 케이블

> Prysmian Group Afumex Green Power 케이블: [공식 자료](https://www.prysmiangroup.com)를 방문하여 확인하십시오.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 코어 수 | 맞춤 제작 | 공식 카탈로그 |
| 정격 전류 | 미공개 | 공식 데이터시트 |
| 정격 전압 | 0.6/1 kV | 제품 자료 |
| 보호 등급 | IP 미공개 | 제품 자료 |
| 난연/연기 밀도 | 저연무할로겐 | 제품 자료 |
| 적용 시나리오 | 건축, 신재생 에너지, 충전 시설 | 제품 자료 |
| 가격 | 미공개 | 미공개 |

**기술 하이라이트**: 저연무할로겐, 난연성, 친환경적이며 공공 건축물 및 신재생 에너지 인프라에 적합합니다.

**적용 시나리오**: 데이터 센터, 충전소, 건축 배전, 신재생 에너지 발전소.

## 공급망 위치

- **상류 핵심 부품/재료**: 구리/알루미늄 도체, XLPE/PVC/PUR 절연 재료, 차폐 재료, 장갑 재료
- **하류 고객/적용 시나리오**: 전력, 통신, 건축, 신재생 에너지, 로봇, 자동차
- **주요 경쟁사/벤치마크**: LEONI, Nexans, NKT, Lapp, Igus

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_prysmian`
- 제품 엔터티: `ent_product_prysmian_flexibot`
- 부품 엔터티: `ent_component_prysmian_flexibot`
- 주요 관계:
  - `rel_ent_company_prysmian_manufactures_ent_product_prysmian_flexibot` (`ent_company_prysmian` → `manufactures` → `ent_product_prysmian_flexibot`)
  - `rel_ent_company_prysmian_manufactures_ent_component_prysmian_flexibot` (`ent_company_prysmian` → `manufactures` → `ent_component_prysmian_flexibot`)

## 참고 자료

1. [공식 웹사이트](https://www.prysmiangroup.com)
2. 제품 데이터시트 및 공개 기술 보도
3. [부록 D 제품 목록](../index-products.md)
