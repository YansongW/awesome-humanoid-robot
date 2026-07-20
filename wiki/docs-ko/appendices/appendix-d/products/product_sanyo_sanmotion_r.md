# 산요 SANMOTION R 시리즈 서보 모터 / Sanyo Denki SANMOTION R Series Servo Motor

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [산요 전기 / Sanyo Denki](../companies/company_sanyo_denki.md) |
| **제품 카테고리** | 서보 모터 / 정밀 운동 핵심 부품 |
| **출시 시기** | 2010년대 지속적 업데이트 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [https://www.sanyodenki.com](https://www.sanyodenki.com) |

## 제품 개요

산요 SANMOTION R 시리즈는 반도체, 의료, 로봇 및 정밀 자동화 장비를 위한 고성능 AC 서보 모터로, 출력 범위는 10W ~ 5kW입니다.

소형화, 고응답성, 낮은 코깅 토크 및 고분해능 엔코더를 특징으로 하며, 공간 제약이 있고 고정밀 및 고동적 응답이 필요한 애플리케이션에 적합합니다. SANMOTION R 시리즈는 산요 R ADVANCED 서보 드라이브와 함께 사용되어 휴머노이드 로봇의 손가락, 손목 등 정밀 관절에 신뢰할 수 있는 정밀 운동 솔루션을 제공합니다.

## 제품 이미지

> Sanyo SANMOTION R: [공식 자료](https://www.sanyodenki.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| 제품 형태 | AC 서보 모터 | 산요 공식 사이트 |
| 프레임 사이즈 | 20–130 mm (모델에 따라 다름) | 제품 매뉴얼 |
| 정격 출력 | 10 W – 5 kW | 제품 매뉴얼 |
| 정격 속도 | 1000–6000 rpm | 제품 매뉴얼 |
| 최대 토크 | 미공개 (모델에 따라 다름) | 제품 매뉴얼 |
| 엔코더 | 20비트 앱솔루트 (참고) | 제품 매뉴얼 |
| 보호 등급 | IP65 (일부 모델) | 제품 매뉴얼 |
| 절연 등급 | Class F (참고) | 제품 매뉴얼 |
| 가격 | 미공개 | 문의 필요 |

## 공급망 위치

- **제조사**: [산요 전기 / Sanyo Denki](../companies/company_sanyo_denki.md)
- **핵심 부품/기술 출처**: 자체 개발 모터 설계 및 제조 공정; 희토류 자석, 베어링, 엔코더 칩, 동선, 절연 재료는 외부 조달.
- **하위 응용/고객**: 반도체 장비 업체, 의료 로봇 제조사, 휴머노이드 로봇 완성체 업체, 협동 로봇, 정밀 위치 결정 플랫폼.

## 지식 그래프 노드 및 관계

- 부품 엔터티: `ent_component_sanyo_sanmotion_r_motor`
- 제조사 엔터티: `ent_company_sanyo_denki`
- 주요 관계:
  - `rel_ent_company_sanyo_denki_manufactures_ent_component_sanyo_sanmotion_r_motor` (`ent_company_sanyo_denki` → `manufactures` → `ent_component_sanyo_sanmotion_r_motor`)
  - `ent_component_sanyo_sanmotion_r_drive` -- `uses` --> `ent_component_sanyo_sanmotion_r_motor`

## 응용 시나리오

- **반도체 장비**: 웨이퍼 이송, 정밀 위치 결정, 칩 마운터.
- **의료 로봇**: 수술 로봇, 재활 로봇의 정밀 관절.
- **휴머노이드 로봇**: 손가락, 손목, 머리 등 공간 제약이 있는 관절.
- **협동 로봇**: 경량 관절 모듈.

## 경쟁 비교

| 비교 항목 | 산요 SANMOTION R | 야스카와 Σ-7 | 파나소닉 A6 |
|-----------|------------------|-------------|------------|
| 포지셔닝 | 소형화 고정밀 서보 모터 | 고급 범용 서보 | 고속 응답 서보 |
| 프레임 사이즈 | 20–130 mm | 20–180 mm | 20–180 mm |
| 엔코더 | 20비트 앱솔루트 (참고) | 24비트 앱솔루트 | 23비트 앱솔루트 |
| 핵심 장점 | 소형화, 저소음, 고신뢰성 | 고급 정밀도 및 신뢰성 | 고속 고응답성 |

## 구매 및 배치 권장 사항

- 설치 공간, 부하 관성 및 동적 응답 요구 사항에 따라 프레임 사이즈와 속도를 선택하십시오.
- 최적의 성능을 위해 산요 R ADVANCED 시리즈 드라이브와 함께 사용하는 것을 권장합니다.
- 휴머노이드 로봇 손가락 등의 응용 분야에서는 저속 안정성과 엔코더 분해능을 중점적으로 평가해야 합니다.

## 관련 항목

- [제조사: 산요 전기 / Sanyo Denki](../companies/company_sanyo_denki.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [산요 전기 공식 사이트](https://www.sanyodenki.com)
2. 산요 SANMOTION R 시리즈 제품 매뉴얼
3. [WAIC 2026 참가 보도](https://www.worldrobotconference.com)
