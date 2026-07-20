# 화웨이昇騰 / Atlas

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [화웨이 / Huawei](../companies/company_huawei.md) |
| **제품 카테고리** | AI 컴퓨팅 플랫폼/훈련 추론 칩 |
| **출시 시간** | 2018년 昇騰 910/310 출시, 지속적 업데이트 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | 본문 참고 자료 참조 |

## 제품 개요

화웨이昇騰은 화웨이가 인공지능 시나리오를 위해 출시한 컴퓨팅 플랫폼 및 프로세서 시리즈로, 昇騰 910 훈련 칩, 昇騰 310 추론 칩 및 Atlas 시리즈 컴퓨팅 하드웨어를 포함합니다. 昇騰은 CANN, MindSpore 및 盤古 대형 모델과 함께 국산 AI 소프트웨어 및 하드웨어 생태계를 구축하며, 구현 지능 및 휴머노이드 로봇의 두뇌를 위한 국산 컴퓨팅 파워 기반 중 하나입니다.

## 제품 이미지

> 화웨이昇騰 / Atlas: [공식 자료](https://www.hiascend.com)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 프로세서 | 昇騰 910 / 310 시리즈 | 화웨이 공식 사이트 |
| 컴퓨팅 파워 | 昇騰 910B FP16 약 320 TFLOPS / INT8 약 640 TOPS | 화웨이 공개 자료 |
| 메모리 | HBM2e / LPDDR4X (모델에 따라 다름) | 화웨이 공개 자료 |
| 공정 | 7 nm (공개 보도) | 공개 보도 |
| Atlas 형태 | Atlas 800 훈련 서버 / Atlas 300I 추론 카드 | 화웨이 공식 사이트 |
| 소프트웨어 스택 | CANN, MindSpore, MindIE | 화웨이昇騰 커뮤니티 |
| 전력 소비 | 약 310 W (昇騰 910 프로세서) | 공개 자료 |
| 가격 | 미공개 | - |

## 공급망 위치

- **제조사**: [화웨이 / Huawei](../companies/company_huawei.md)
- **핵심 부품/기술 출처**: 자체 개발 다빈치 아키텍처, 웨이퍼 파운드리, HBM 스토리지, 패키징 및 테스트, PCB, 방열.
- **하위 응용/고객**: 인터넷 대기업, 정부 및 기업 고객, 지능형 컴퓨팅 센터, 로봇 완제품 제조사, 연구 기관.

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_huawei_ascend`
- 제조사 엔터티: `ent_company_huawei`
- 주요 관계:
  - `rel_ent_company_huawei_manufactures_ent_product_huawei_ascend` (`ent_company_huawei` → `manufactures` → `ent_product_huawei_ascend`)
  - `ent_product_huawei_ascend` -- `uses` --> `ent_component_huawei_ascend_chip`
  - `ent_product_huawei_ascend` -- `runs` --> `ent_software_mindspore`

## 응용 시나리오

- **구현 지능 두뇌**: VLA/VLM 대형 모델을 실행하여 인식, 이해 및 작업 계획 구현.
- **대형 모델 훈련**: 盤古 및 타사 대형 모델 훈련.
- **엣지 추론**: Atlas 200I 등 엣지 장치를 로봇 측 추론에 사용.

## 경쟁 비교

| 비교 항목 | 昇騰 Atlas | NVIDIA Jetson/데이터 센터 | 寒武紀 思元 |
|--------|------|------|------|
| 생태계 | CANN + MindSpore + 盤古 | CUDA + PyTorch | Cambricon Neuware |
| 컴퓨팅 파워 | 고급 훈련/추론 | 글로벌 선도 | 훈련/추론 |
| 국산화 | 자체 통제 가능 | 수출 규제 영향 | 자체 통제 가능 |

## 구매 및 배포 권장 사항

- 컴퓨팅 파워/정밀도/시나리오 요구 사항에 따라 해당 모델을 선택하고, 공식 지원 도구 체인 및 생태계 호환성을 우선 고려하세요.
- 배포 전 전원 공급, 방열, 기계 인터페이스 및 통신 프로토콜이 전체 기기 요구 사항을 충족하는지 확인하세요.
- 공식 채널 또는 공인 대리점을 통해 최신 펌웨어, SDK 및 기술 지원을 받는 것을 권장합니다.

## 관련 항목

- [제조사: 화웨이 / Huawei](../companies/company_huawei.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [화웨이 / Huawei 공식 제품/회사 페이지](https://www.hiascend.com)
2. [화웨이昇騰 커뮤니티](https://www.hiascend.com)
3. 화웨이 Atlas 제품 매뉴얼
