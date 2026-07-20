# 캄브리콘 사위안 370 / Cambricon MLU370

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [캄브리콘 / Cambricon](../companies/company_cambricon.md) |
| **제품 카테고리** | AI 추론/훈련 가속 칩 및 가속 카드 |
| **출시일** | 2021년 사위안 370 시리즈 출시 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | 캄브리콘 공식 홈페이지, 제품 매뉴얼 |

## 제품 개요

캄브리콘 사위안 370(MLU370)은 캄브리콘의 3세대 클라우드 AI 칩으로, 자체 개발한 MLUarch03 아키텍처를 기반으로 하며 클라우드 추론, 훈련 및 대규모 모델 배포를 위한 국산 컴퓨팅 성능을 지원합니다.

사위안 370 시리즈는 MLU370-X8, MLU370-S4, MLU370-X4 등 다양한 폼팩터를 포함하며, PCIe 가속 카드, OAM 모듈 및 통합 시스템 솔루션을 포괄합니다. 칩은 INT8/INT16/FP16/BF16 등 다중 정밀도 연산을 지원하고, 고대역폭 메모리와 MLU-Link 칩 간 상호 연결을 통합하며, Neuware 소프트웨어 스택과 함께 제공되어 CV, NLP, 추천 및 생성형 AI 워크로드를 실행할 수 있습니다.

## 제품 이미지

> 캄브리콘 사위안 370: [공식 자료](https://www.cambricon.com)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| AI 프로세서 | 사위안 370(MLU370) | 캄브리콘 공식 홈페이지 |
| 아키텍처 | 자체 개발 MLUarch03 | 캄브리콘 공개 자료 |
| 공정 | 7 nm | 공개 보도 |
| AI 연산 성능 | INT8 최대 약 256 TOPS; FP16 약 128 TFLOPS | 캄브리콘 공개 자료 |
| 메모리 | 48 GB LPDDR4X / HBM2e(모델에 따라 다름) | 공개 보도 |
| 메모리 대역폭 | 미공개 | - |
| 칩 간 상호 연결 | MLU-Link | 캄브리콘 공개 자료 |
| 인터페이스 | PCIe Gen4 / OAM | 캄브리콘 공개 자료 |
| 전력 소비 | 약 75–250 W(폼팩터에 따라 다름) | 공개 보도 |
| 소프트웨어 스택 | Neuware, PyTorch/TensorFlow 어댑테이션 | 캄브리콘 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [캄브리콘 / Cambricon](../companies/company_cambricon.md)
- **핵심 부품/기술 출처**: 자체 개발 MLU 아키텍처, 웨이퍼 파운드리, LPDDR/HBM 스토리지, 패키징 및 테스트, PCB, 방열.
- **하위 응용/고객**: 클라우드 컴퓨팅 업체, 인터넷 기업, 지능형 컴퓨팅 센터, AI 기업, 연구 기관, 로봇 완제품 제조사.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_cambricon_mlu370`
- 부품 엔터티: `ent_component_cambricon_mlu370_chip`
- 제조사 엔터티: `ent_company_cambricon`
- 주요 관계:
  - `rel_ent_company_cambricon_manufactures_ent_product_cambricon_mlu370`(`ent_company_cambricon` → `manufactures` → `ent_product_cambricon_mlu370`)
  - `rel_ent_company_cambricon_manufactures_ent_component_cambricon_mlu370_chip`(`ent_company_cambricon` → `manufactures` → `ent_component_cambricon_mlu370_chip`)
  - `ent_product_cambricon_mlu370` -- `uses` --> `ent_component_cambricon_mlu370_chip`

## 응용 시나리오

- **클라우드 대규모 모델 추론**: LLM, VLM 등 생성형 모델을 배포하여 텍스트/멀티모달 추론 서비스 제공.
- **지능형 컴퓨팅 센터**: 국산 AI 가속 노드로서 훈련 및 추론 혼합 워크로드 지원.
- **로봇 두뇌**: 휴머노이드 로봇에 클라우드/엣지 인지, 계획 및 의사 결정 컴퓨팅 성능 제공.

## 경쟁 비교

| 비교 항목 | 캄브리콘 사위안 370 | NVIDIA A10/L4 | 화웨이 어센드 310/910 |
|-----------|------|------|------|
| 아키텍처 | 자체 개발 MLU | NVIDIA Ampere/Ada | 다빈치 |
| 생태계 | Neuware + 국산 프레임워크 | CUDA + PyTorch | CANN + MindSpore |
| 국산화 | 자주 제어 가능 | 수출 통제 영향 | 자주 제어 가능 |

## 구매 및 배포 권장 사항

- 모델 유형 및 정밀도 요구 사항에 따라 X8/S4 등 폼팩터를 선택하고, 우선적으로 Neuware가 대상 모델을 지원하는지 확인하십시오.
- 배포 전 전원 공급, 방열 및 PCIe 토폴로지가 다중 카드 상호 연결 요구 사항을 충족하는지 평가하십시오.
- 캄브리콘 공식 채널 또는 공인 대리점을 통해 최신 펌웨어 및 SDK를 확보하는 것을 권장합니다.

## 관련 항목

- [제조사: 캄브리콘 / Cambricon](../companies/company_cambricon.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [캄브리콘 공식 홈페이지](https://www.cambricon.com)
2. [캄브리콘 사위안 370 제품 페이지](https://www.cambricon.com/index.php?m=content&c=index&a=lists&catid=75)
3. 캄브리콘 제품 매뉴얼 및 백서
