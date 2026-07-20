# 등림과학기술 Goldwasser X / Denglai Goldwasser X

> 본 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [등림과학기술 / Denglai Technology](../companies/company_denglai.md) |
| **제품 카테고리** | 범용 GPU+ AI 학습/추론 가속 카드 |
| **출시 시간** | Goldwasser 시리즈 지속적 반복 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | 등림과학기술 공식 사이트, 제품 매뉴얼 |

## 제품 개요

등림과학기술 Goldwasser X는 자체 개발 GPU+ 혁신 아키텍처 기반의 클라우드 AI 가속 카드로, GPGPU 범용 컴퓨팅과 AI 전용 가속 능력을 융합하여 대규모 모델 추론, 학습 및 범용 컴퓨팅에 고효율 국산 컴퓨팅 파워를 제공합니다.

Goldwasser X는 등림과학기술 GPU+ 아키텍처를 채택하여 단일 칩에 범용 컴퓨팅 유닛과 텐서 가속 유닛을 통합, CUDA 호환성과 AI 작업 효율을 모두 고려합니다. 제품은 다중 정밀도 추론, 다중 카드 상호 연결 및 주요 프레임워크 적응을 지원하며, 지능형 컴퓨팅 센터, 인터넷 및 AI 기업 등 시나리오에 적합합니다.

## 제품 이미지

> 등림과학기술 Goldwasser X: [공식 자료](https://www.denglai.com.cn)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 가속기 | Goldwasser X 시리즈 | 등림과학기술 공식 사이트 |
| 아키텍처 | GPU+ (GPGPU + AI 가속) | 등림과학기술 공개 자료 |
| 공정 | 7 nm | 공개 보도 |
| AI 컴퓨팅 성능 | INT8 / FP16 수백 TOPS급 | 등림과학기술 공개 자료 |
| 비디오 메모리 | 32 GB HBM2e (일부 모델) | 공개 보도 |
| 비디오 메모리 대역폭 | 미공개 | - |
| 상호 연결 | 다중 카드 상호 연결 지원 | 등림과학기술 공개 자료 |
| 인터페이스 | PCIe Gen4 / OAM | 공개 보도 |
| 전력 소비 | 약 150–300 W (모델에 따라 다름) | 공개 보도 |
| 소프트웨어 스택 | CUDA 호환 런타임, 등림 SDK | 등림과학기술 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [등림과학기술 / Denglai Technology](../companies/company_denglai.md)
- **핵심 부품/기술 출처**: 자체 개발 GPU+ 아키텍처, 웨이퍼 파운드리, HBM2e 비디오 메모리, 패키징 및 테스트, PCB, 방열.
- **하류 응용/고객**: 인터넷 기업, 클라우드 컴퓨팅 업체, 지능형 컴퓨팅 센터, AI 기업, 로봇 기업, 연구 기관.

## 지식 그래프 노드와 관계

- 제품 엔터티: `ent_product_denglai_goldwasser_x`
- 부품 엔터티: `ent_component_denglai_goldwasser_x_accelerator`
- 제조사 엔터티: `ent_company_denglai`
- 주요 관계:
  - `rel_ent_company_denglai_manufactures_ent_product_denglai_goldwasser_x` (`ent_company_denglai` → `manufactures` --> `ent_product_denglai_goldwasser_x`)
  - `rel_ent_company_denglai_manufactures_ent_component_denglai_goldwasser_x_accelerator` (`ent_company_denglai` → `manufactures` --> `ent_component_denglai_goldwasser_x_accelerator`)
  - `ent_product_denglai_goldwasser_x` -- `uses` --> `ent_component_denglai_goldwasser_x_accelerator`

## 응용 시나리오

- **대규모 모델 추론 및 배포**: LLM, VLM 등 생성형 모델의 높은 처리량 추론 지원.
- **클라우드 AI 학습**: 중소 규모 모델 학습 및 미세 조정 작업에 사용.
- **로봇 클라우드 두뇌**: 인간형 로봇에 원격 인식, 계획 및 모델 서비스 컴퓨팅 파워 제공.

## 경쟁 비교

| 비교 항목 | Goldwasser X | 한우지 MLU370 | NVIDIA T4/L4 |
|--------|------|------|------|
| 아키텍처 | GPU+ 융합 | 자체 개발 MLU | NVIDIA Tensor Core |
| 생태계 | CUDA 호환 | Neuware | CUDA |
| 포지셔닝 | 학습/추론 겸용 | 추론/학습 | 추론 위주 |
| 국산화 | 자주 제어 가능 | 자주 제어 가능 | 수출 통제 영향 |

## 구매 및 배포 제안

- 작업 부하에 따라 X/L/S 등 하위 모델을 선택하고, CUDA 호환 레이어의 대상 연산자 지원 여부를 확인하세요.
- 다중 카드 배포 시 상호 연결 방식, 드라이버 버전 및 클러스터 스케줄링 도구를 확인하세요.
- 등림과학기술 공식 채널을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 등림과학기술 / Denglai Technology](../companies/company_denglai.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [등림과학기술 공식 사이트](https://www.denglai.com.cn)
2. [등림과학기술 제품 페이지](https://www.denglai.com.cn/product/)
3. 등림과학기술 제품 발표회 자료
