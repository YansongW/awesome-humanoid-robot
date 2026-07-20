# Kollmorgen AKM2G 서보 모터 / AKM2G

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [다나허 (Kollmorgen) / Danaher (Kollmorgen)](../companies/company_danaher.md) |
| **제품 카테고리** | 서보 모터 |
| **출시일** | 2018년 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [다나허 (Kollmorgen) 공식 사이트](https://www.danaher.com) |

## 제품 개요

Kollmorgen AKM2G는 다나허 산하 Kollmorgen이 출시한 차세대 동기 서보 모터로, 더 높은 토크 밀도와 다양한 구성 옵션을 제공합니다.

모터는 40mm ~ 180mm 프레임을 포함하며, 다양한 피드백 장치와 권선을 선택할 수 있고, AKD 서보 드라이브와 함께 사용하면 플러그 앤 플레이가 가능합니다. 로봇, 반도체 및 정밀 자동화 장비에 널리 사용됩니다.

## 제품 이미지

> Kollmorgen AKM2G 서보 모터: [공식 자료](https://www.danaher.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 제품 유형 | 동기 서보 모터 | 공식 자료 |
| 출력 범위 | 0.03 kW ~ 7.2 kW (구체적인 범위는 모델에 따름) | 공식 자료 |
| 최대 토크 | 0.16 Nm ~ 53 Nm | 공식 자료 |
| 최고 회전 속도 | 8,000 rpm | 공식 자료 |
| 프레임 크기 | 40 / 60 / 80 / 130 / 180 mm | 공식 자료 |
| 피드백 유형 | 리졸버 / 인크리멘탈 / 싱글턴 또는 멀티턴 앱솔루트 엔코더 | 공식 자료 |
| 보호 등급 | IP65 (선택적 샤프트 씰) | 공식 자료 |
| 가격 | 미공개 | 미공개 |

## 공급망 위치

- **제조사**: [다나허 (Kollmorgen) / Danaher (Kollmorgen)](../companies/company_danaher.md)
- **핵심 부품/기술 출처**: 자체 개발 모터 설계 및 자기 회로 최적화; 자성 재료, 베어링, 엔코더, 권선 절연 재료는 외부 조달.
- **하위 응용 분야/고객**: 산업용 로봇, 협동 로봇, 반도체 장비, 포장 기계, 휴머노이드 로봇 관절.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_danaher_kollmorgen_akm2g`
- 제조사 엔터티: `ent_company_danaher`
- 주요 관계:
  - `ent_company_danaher` → `manufactures` → `ent_product_danaher_kollmorgen_akm2g` (관계 파일: `rel_ent_company_danaher_manufactures_ent_product_danaher_kollmorgen_akm2g.md`)

## 응용 시나리오

- **산업용 로봇**: 관절 서보 및 외부 축.
- **협동 로봇**: 저관성, 고안전성 관절 동력.
- **반도체 장비**: 웨이퍼 핸들링 및 정밀 위치 결정.
- **휴머노이드 로봇**: 팔, 다리, 허리 관절 동력 유닛.

## 경쟁 비교

| 비교 항목 | Kollmorgen AKM2G 서보 모터 | Panasonic MINAS A6 | Yaskawa Σ-7 |
|--------|---------------|--------|--------|
| 프레임 크기 | 40–180 mm | 미공개 | 미공개 |
| 최대 토크 | 0.16–53 Nm | 미공개 | 미공개 |
| 최고 회전 속도 | 8,000 rpm | 미공개 | 미공개 |
| 가격 | 미공개 | 미공개 | 미공개 |

## 구매 및 배치 권장 사항

높은 토크 밀도와 맞춤형 권선이 필요한 로봇 관절 응용 분야에서는 AKM2G를 우선 고려할 수 있습니다. 선정 시 설치 플랜지, 피드백 유형 및 드라이브 호환성을 확인해야 합니다.

## 참고 자료

1. [다나허 (Kollmorgen) 공식 사이트](https://www.danaher.com)
2. [Kollmorgen AKM2G 서보 모터 제품 페이지](https://www.kollmorgen.com/en-us/products/motors/servo-motors/akm2g-servo-motors)
3. Kollmorgen AKM2G 서보 모터 데이터시트
