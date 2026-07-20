# SynTouch BioTac 생체모방 촉각 센서 / SynTouch BioTac Biomimetic Tactile Sensor

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [SynTouch](../companies/company_syntouch.md) |
| **제품 카테고리** | 생체모방 다중 모드 촉각 센서 |
| **출시 시간** | 2008년부터 지속적인 업데이트 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [SynTouch 공식 홈페이지](https://www.syntouchllc.com) |

## 제품 개요

SynTouch BioTac은 세계 최초이자 학계와 산업계에서 가장 널리 사용되는 생체모방 손끝 촉각 센서 중 하나입니다. 그 디자인은 인간 손끝의 기계적 구조와 지각 능력을 모방합니다: 단단한 뼈 모양의 코어 외부에 교체 가능한 탄성 피부가 덮여 있으며, 피부와 코어 사이에는 전도성 액체가 채워져 있습니다. 센서가 물체에 접촉하면 피부와 액체층의 변형이 코어 표면의 전극 배열 임피던스를 변화시키고, 동시에 압력 센서가 액체 진동을 감지하며, 열 감지 요소가 온도와 열 흐름을 인식합니다.

BioTac은 힘, 진동, 온도의 세 가지 촉각 정보를 동시에 출력할 수 있으며, 미끄러짐 감지, 접촉 위치 파악, 질감 인식, 경도 추정, 모서리/각도 인식 등의 기능을 지원합니다. 전자 부품은 모두 단단한 코어 내부에 내장되어 있고, 유연한 피부는 교체 가능하여 매우 높은 견고성과 유지보수성을 제공합니다.

## 제품 이미지

![SynTouch BioTac](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_485.jpg)

> 이미지 출처: SynTouch 공식 제품 자료. 교체가 필요한 경우 공식 공개 이미지 URL을 사용하십시오.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 감지 원리 | 유체 압력 + 전극 임피던스 + 열 전도 | 공식 홈페이지 공개 자료 |
| 감지 차원 | 힘, 진동, 온도, 열 흐름 | 공식 홈페이지 공개 자료 |
| 전극 수 | 19개 감지 전극 + 4개 여기 전극 | 학술 논문 |
| 크기 | 인간 손끝 크기 | 공식 홈페이지 공개 자료 |
| 무게 | 미공개 | - |
| 힘 범위 | 0 – 50 N | BioTac 매뉴얼 |
| 힘 분해능 | 10 mN | BioTac 매뉴얼 |
| 압력 범위 | 0 – 100 kPa | BioTac 매뉴얼 |
| 압력 분해능 | 37 Pa | BioTac 매뉴얼 |
| 진동 범위 | ±760 Pa | BioTac 매뉴얼 |
| 진동 분해능 | 0.4 Pa | BioTac 매뉴얼 |
| 온도 범위 | 0 – 75 ℃ | BioTac 매뉴얼 |
| 온도 분해능 | 0.1 ℃ | BioTac 매뉴얼 |
| 열 흐름 범위 | ±1 ℃/s | BioTac 매뉴얼 |
| 열 흐름 분해능 | 0.001 ℃/s | BioTac 매뉴얼 |
| 전극 임피던스 샘플링 속도 | 100 Hz | 학술 논문 |
| 진동 샘플링 속도 | 2200 Hz | 학술 논문 |
| 통신 인터페이스 | 통합 전자 모듈 + 호스트 통신 | 공식 홈페이지 공개 자료 |
| 통합 솔루션 | Shadow Hand / Allegro Hand / PR2 등 | 공식 홈페이지 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [SynTouch](../companies/company_syntouch.md)
- **핵심 부품/기술 출처**: 자체 개발 유연 피부, 전도성 액체, 전극 배열, 압력 센서, 열 감지 요소; 신호 처리 회로는 코어 내부에 통합됨.
- **하위 응용/고객**: 로봇 손, 의수, 연구 기관, 재료 특성 분석, 의료 재활.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_syntouch_biotac`
- 제조사 엔터티: `ent_company_syntouch`
- 부품 엔터티: `ent_component_syntouch_biotac_transducer`
- 주요 관계:
  - `rel_ent_company_syntouch_manufactures_ent_product_syntouch_biotac`（`ent_company_syntouch` → `manufactures` --> `ent_product_syntouch_biotac`）
  - `rel_ent_company_syntouch_manufactures_ent_component_syntouch_biotac_transducer`（`ent_company_syntouch` → `manufactures` --> `ent_component_syntouch_biotac_transducer`）
  - `rel_ent_product_syntouch_biotac_uses_ent_component_syntouch_biotac_transducer`（`ent_product_syntouch_biotac` → `uses` --> `ent_component_syntouch_biotac_transducer`）

## 응용 시나리오

- **로봇 정밀 조작**: 잡기, 돌리기, 누르기, 미끄러짐 감지 및 재질 인식.
- **의수 촉각 피드백**: 상지 의수에 인간 피부에 가까운 힘/온도 감각 제공.
- **재료 촉각 특성 분석**: 재료의 거칠기, 마찰, 유연성, 열 특성 등 촉각 차원 정량화.
- **연구 및 교육**: 촉각 인식 알고리즘, 생체모방 로봇, 인간-로봇 상호작용 연구의 표준 센서.

## 경쟁 비교

| 비교 항목 | SynTouch BioTac | 파시니 PX-6AX | XELA uSkin |
|--------|-----------------|---------------|------------|
| 감지 원리 | 유체/전극/열 전도 | 6D 홀 배열 | 자기저항식 3축 |
| 감지 모드 | 힘 + 진동 + 온도 | 15가지 촉각 정보 | 3축 힘 |
| 형태 | 생체모방 손끝 | 감지 유닛/로봇 손 | 유연 피부 패치 |
| 핵심 장점 | 생체모방, 견고함, 교체 가능 피부 | 고밀도, 국산화 | 부드러움, 쉬운 통합 |

## 구매 및 배포 제안

- 목표 로봇 손에 따라 해당 통합 키트(Shadow, Allegro, PR2 등)를 선택해야 합니다.
- 유연 피부는 소모품이므로 사용 빈도에 따라 예비 부품을 준비하여 교체하는 것이 좋습니다.
- 진동 및 온도 데이터는 표면 처리 알고리즘에 대한 요구 사항이 높으므로 SynTouch 소프트웨어 또는 자체 개발 캘리브레이션 프로세스를 함께 사용하는 것이 좋습니다.

## 참고 자료

1. [SynTouch 공식 홈페이지](https://www.syntouchllc.com)
2. [SynTouch BioTac 제품 페이지](https://www.syntouchllc.com/Products/BioTac/)
3. [BioTac 브로셔](https://www.syntouchllc.com/Products/BioTac/_media/BioTac_Brochure.pdf)
4. [Interpreting and Predicting Tactile Signals for the SynTouch BioTac（arXiv）](https://arxiv.org/pdf/2101.05452.pdf)
5. [부록 D 기업 목록](../index-companies.md)
