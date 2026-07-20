# 레니쇼 RESOLUTE 앱솔루트 광학 엔코더 / Renishaw RESOLUTE Absolute Encoder

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [레니쇼 / Renishaw](../companies/company_renishaw.md) |
| **제품 카테고리** | 앱솔루트 광학 엔코더 (직선/회전) |
| **출시 시기** | 지속 판매/업데이트 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [레니쇼 RESOLUTE 앱솔루트 광학 엔코더 제품/자료 페이지](https://www.renishaw.com/en/resolute-absolute-encoder--9533) |

## 제품 개요

RESOLUTE는 레니쇼가 출시한 진정한 앱솔루트 광학 엔코더 시스템으로, 단일 트랙 30 µm 피치 눈금과 고급 광학 리드 헤드를 사용하여 전원을 켜는 즉시 절대 위치를 확인할 수 있습니다. 시스템 최고 분해능은 1 nm, 최대 속도는 100 m/s이며, BiSS C, DRIVE-CLiQ, FANUC, Mitsubishi 등 다양한 직렬 인터페이스를 지원하여 고정밀 공작 기계, 로봇 관절 및 반도체 장비에 널리 사용됩니다.

## 제품 이미지

> 레니쇼 RESOLUTE 앱솔루트 광학 엔코더: [공식 자료](https://www.renishaw.com/en/resolute-absolute-encoder--9533)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 유형 | 진정한 앱솔루트 광학 엔코더 | Renishaw datasheet |
| 피치 | 30 µm | Renishaw datasheet |
| 분해능 | 최고 1 nm | Renishaw datasheet |
| 정밀도 | ±1 µm/m (RELA) / ±5 µm/m (RTLA) | Renishaw datasheet |
| 최대 속도 | 최고 100 m/s | Renishaw datasheet |
| 세분화 오차 (SDE) | ±40 nm | Renishaw datasheet |
| 지터 | 7 nm RMS | Renishaw datasheet |
| 인터페이스 | BiSS C / DRIVE-CLiQ / FANUC / Mitsubishi / Panasonic | Renishaw datasheet |
| 보호 등급 | IP64 | Renishaw datasheet |
| 작동 온도 | 0℃ – +55℃ | Renishaw datasheet |
| 기능 안전 | 선택 가능 SIL2 / PL d | Renishaw datasheet |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [레니쇼 / Renishaw](../companies/company_renishaw.md)
- **핵심 부품/기술 출처**: 광학 리드 헤드, 유리/강철/저팽창 합금 스케일, ASIC, 케이블 및 커넥터
- **하위 응용/고객**: 공작 기계 OEM, 로봇 제조사, 반도체 장비, CMM 제조사, 항공 우주

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_renishaw_resolute_encoder`
- 부품 엔터티: `ent_component_renishaw_resolute_readhead`
- 제조사 엔터티: `ent_company_renishaw`
- 주요 관계:
  - `rel_ent_company_renishaw_manufactures_ent_product_renishaw_resolute_encoder` (`ent_company_renishaw` → `manufactures` → `ent_product_renishaw_resolute_encoder`)
  - `rel_ent_company_renishaw_manufactures_ent_component_renishaw_resolute_readhead` (`ent_company_renishaw` → `manufactures` → `ent_component_renishaw_resolute_readhead`)
  - `ent_product_renishaw_resolute_encoder` -- `uses` --> `ent_component_renishaw_resolute_readhead`

## 응용 시나리오

- **고정밀 CNC 공작 기계, 리니어 모터, 로봇 관절, 반도체 장비, 3차원 측정기, 천체 망원경**

## 경쟁 비교

| 비교 항목 | 본 제품 | 주요 경쟁사 A | 주요 경쟁사 B |
|--------|--------|------------|------------|
| 유형 | 사양 매개변수 표 참조 | 동종 제품 | 동종 제품 |
| 핵심 장점 | 공식 공개 성능 지표 | 경쟁사 공개 지표 | 경쟁사 공개 지표 |
| 생태계/서비스 | 제조사 공식 지원 | 경쟁사 생태계 | 경쟁사 생태계 |

## 구매 및 배포 권장 사항

- 대상 응용 분야의 분해능, 측정 범위, 정밀도 또는 연산 능력 요구 사항에 따라 특정 모델을 선택하십시오.
- 배포 전 인터페이스, 전원 공급, 방열, 기계적 설치 및 환경 온도 범위가 일치하는지 확인하십시오.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것이 좋습니다.

## 관련 항목

- [제조사: 레니쇼 / Renishaw](../companies/company_renishaw.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [레니쇼 공식 홈페이지](https://www.renishaw.com)
2. [레니쇼 RESOLUTE 앱솔루트 광학 엔코더 제품/자료 페이지](https://www.renishaw.com/en/resolute-absolute-encoder--9533)
3. 제품 데이터시트 및 공개 기술 보도
4. [부록 D 기업 목록](../index-companies.md)
