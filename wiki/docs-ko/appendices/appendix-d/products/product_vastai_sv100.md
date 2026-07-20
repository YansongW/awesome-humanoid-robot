# 瀚博 반도체 SV100 / Vastai SV100

> 이 항목은 [부록 D 핵심 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 핵심 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 '미공개'로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [瀚博 반도체 / Vastai Technologies](../companies/company_vastai.md) |
| **제품 카테고리** | 클라우드 AI 추론 및 비디오 처리 가속 카드 |
| **출시 시간** | SV100 시리즈는 회사 제품 업데이트에 따라 출시 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | 瀚博 반도체 공식 사이트, 제품 매뉴얼 |

## 제품 개요

瀚博 반도체 SV100은 클라우드 AI 추론 및 비디오 이해 시나리오를 위한 고성능 가속 카드로, AI 컴퓨팅과 비디오 코덱 기능을 통합하여 멀티모달 콘텐츠 처리에 적합합니다.

SV100은 瀚博 자체 개발 AI 및 비디오 처리 아키텍처를 기반으로 하며, INT8/FP16 등의 정밀도를 지원하고, 여러 개의 고화질 비디오 스트림을 동시에 처리하면서 딥러닝 모델을 실행할 수 있습니다. 비디오+AI 융합 특성으로 인해 라이브 트랜스코딩, 콘텐츠 심사, 스마트 보안 및 로봇 비디오 피드백 등의 시나리오에서 장점을 가지고 있습니다.

## 제품 이미지

> 瀚博 반도체 SV100: [공식 자료](https://www.vastai.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 가속기 | 瀚博 SV100 | 瀚博 반도체 공식 사이트 |
| 아키텍처 | 자체 개발 AI 추론 + 비디오 처리 아키텍처 | 瀚博 반도체 공개 자료 |
| 공정 | 7 nm | 공개 보도 |
| AI 연산 성능 | INT8 약 200 TOPS급 | 瀚博 반도체 공개 자료 |
| 비디오 메모리 | 32 GB LPDDR4X / HBM (모델에 따라 다름) | 공개 보도 |
| 비디오 기능 | 다중 4K/8K 비디오 코덱 | 瀚博 반도체 공개 자료 |
| 인터페이스 | PCIe Gen4 | 공개 보도 |
| 전력 소비 | 약 75–150 W | 공개 보도 |
| 소프트웨어 스택 | VastStream, SDK | 瀚博 반도체 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [瀚博 반도체 / Vastai Technologies](../companies/company_vastai.md)
- **핵심 부품/기술 출처**: 자체 개발 AI/비디오 아키텍처, 웨이퍼 파운드리, 메모리, 패키징 및 테스트, PCB, 방열.
- **하류 응용/고객**: 인터넷 비디오 플랫폼, 클라우드 컴퓨팅 업체, 통신 사업자, 스마트 시티, 로봇 회사.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_vastai_sv100`
- 부품 엔터티: `ent_component_vastai_sv100_accelerator`
- 제조사 엔터티: `ent_company_vastai`
- 주요 관계:
  - `rel_ent_company_vastai_manufactures_ent_product_vastai_sv100` (`ent_company_vastai` → `manufactures` --> `ent_product_vastai_sv100`)
  - `rel_ent_company_vastai_manufactures_ent_component_vastai_sv100_accelerator` (`ent_company_vastai` → `manufactures` --> `ent_component_vastai_sv100_accelerator`)
  - `ent_product_vastai_sv100` -- `uses` --> `ent_component_vastai_sv100_accelerator`

## 응용 시나리오

- **클라우드 비디오 이해**: 실시간 비디오 분석, 콘텐츠 심사, 스마트 추천.
- **라이브 방송 및 클라우드 게임**: 고밀도 비디오 트랜스코딩 및 저지연 스트리밍.
- **로봇 비디오 피드백**: 엣지/클라우드 협업을 통한 로봇 다중 비디오 데이터 처리.

## 경쟁 비교

| 비교 항목 | 瀚博 SV100 | 寒武纪 MLU370 | NVIDIA T4 |
|--------|------|------|------|
| 성능 | AI + 비디오 융합 | AI 추론/학습 | AI 추론 |
| 비디오 | 강함 | 약함 | 중간 |
| 생태계 | VastStream | Neuware | CUDA |
| 국산화 | 자체 제어 가능 | 자체 제어 가능 | 수출 통제 영향 |

## 구매 및 배포 제안

- 비디오 채널 수, 해상도 및 AI 모델 동시 요구 사항이 SV100의 성능과 일치하는지 우선 평가하세요.
- 배포 전에 VastStream이 대상 비디오 형식 및 모델 프레임워크를 지원하는지 확인하세요.
- 瀚博 반도체 공식 채널을 통해 최신 드라이버, SDK 및 참조 솔루션을 획득하는 것을 권장합니다.

## 관련 항목

- [제조사: 瀚博 반도체 / Vastai Technologies](../companies/company_vastai.md)
- [부록 D.4 핵심 제품 Wiki](../index-products.md)

## 참고 자료

1. [瀚博 반도체 공식 사이트](https://www.vastai.com)
2. [瀚博 반도체 제품 페이지](https://www.vastai.com/products.html)
3. 瀚博 반도체 제품 발표회 자료
