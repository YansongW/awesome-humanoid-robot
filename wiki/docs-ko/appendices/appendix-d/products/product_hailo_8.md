# Hailo-8 AI 프로세서

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Hailo](../companies/company_hailo.md) |
| **제품 카테고리** | 엣지 AI 가속기 / NPU |
| **출시일** | 2019년 Hailo-8 출시 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | Hailo 공식 사이트, 제품 매뉴얼 |

## 제품 개요

Hailo-8은 Hailo가 출시한 엣지 AI 프로세서로, 혁신적인 데이터 흐름 아키텍처(Dataflow Architecture)를 채택하여 저전력에서 높은 AI 연산 성능을 구현하며, 로봇, 자동차, 보안 및 산업용 비전 분야에 널리 사용됩니다.

Hailo-8은 BGA 패키지, M.2 모듈 또는 PCIe 카드 형태로 제공되어 기존 임베디드 플랫폼에 직접 통합할 수 있습니다. 데이터 흐름 아키텍처는 신경망 추론에 맞게 심층 최적화되어 있어, 연산 성능 활용률과 에너지 효율이 기존 SIMD/GPU 방식보다 우수하며, 다중 채널 영상 분석, 실시간 객체 탐지 및 로봇 엣지 인식에 적합합니다.

## 제품 이미지

> Hailo-8 AI 프로세서: [공식 자료](https://hailo.ai)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 프로세서 | Hailo-8 | Hailo 공식 사이트 |
| 아키텍처 | 데이터 흐름 아키텍처(Dataflow Architecture) | Hailo 공개 자료 |
| 공정 | 16 nm | 공개 보도 |
| AI 연산 성능 | 최대 26 TOPS INT8 | Hailo 공개 자료 |
| 에너지 효율 | 약 3 TOPS/W 일반 | Hailo 공개 자료 |
| 정밀도 지원 | INT8 / INT4 / FP16(일부) | Hailo 공개 자료 |
| 패키지 크기 | 약 15 mm × 15 mm(BGA) | Hailo 공개 자료 |
| 인터페이스 | PCIe Gen3 / M.2 / BGA | Hailo 공개 자료 |
| 전력 소비 | 약 2.5 W 일반 | Hailo 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [Hailo](../companies/company_hailo.md)
- **핵심 부품/기술 출처**: 자체 개발 데이터 흐름 아키텍처, 웨이퍼 파운드리, 패키징 및 테스트, 모듈/기판.
- **하위 응용/고객**: 자동차 Tier1/OEM, 보안 업체, 산업용 카메라 회사, 로봇 완제품 제조사, AIoT 장비 업체.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_hailo_8`
- 부품 엔터티: `ent_component_hailo_8_npu`
- 제조사 엔터티: `ent_company_hailo`
- 주요 관계:
  - `rel_ent_company_hailo_manufactures_ent_product_hailo_8` (`ent_company_hailo` → `manufactures` --> `ent_product_hailo_8`)
  - `rel_ent_company_hailo_manufactures_ent_component_hailo_8_npu` (`ent_company_hailo` → `manufactures` --> `ent_component_hailo_8_npu`)
  - `ent_product_hailo_8` -- `uses` --> `ent_component_hailo_8_npu`

## 응용 시나리오

- **로봇 엣지 인식**: 실시간 객체 탐지, 의미론적 분할, 자세 추정 및 내비게이션 보조.
- **스마트 보안 카메라**: 엣지 영상 분석 및 이벤트 탐지.
- **자동차 ADAS**: 전방/서라운드 뷰 인식, 차량 내 모니터링 및 저지연 추론.

## 경쟁 비교

| 비교 항목 | Hailo-8 | Intel Movidius VPU | Horizon Robotics Journey 3 |
|--------|------|------|------|
| 연산 성능 | 26 TOPS | 약 4 TOPS | 약 5 TOPS |
| 전력 소비 | 약 2.5 W | 약 1 W | 약 2.5 W |
| 아키텍처 | 데이터 흐름 | VPU / SHAVE | 자체 개발 BPU |
| 생태계 | Hailo SDK | OpenVINO | Horizon Robotics Tiangong Kaiwu |

## 구매 및 배포 권장 사항

- Hailo Dataflow Compiler를 우선 사용하여 대상 모델의 Hailo-8 성능 및 정밀도를 평가하세요.
- 호스트 인터페이스에 따라 M.2, PCIe 또는 BGA 형태를 선택하고, 드라이버 및 BSP 호환성을 확인하세요.
- Hailo 공식 채널을 통해 최신 SDK, 참조 설계 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: Hailo](../companies/company_hailo.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Hailo 공식 사이트](https://hailo.ai)
2. [Hailo-8 제품 페이지](https://hailo.ai/products/hailo-8/)
3. Hailo-8 데이터 시트 및 개발자 문서
