# Hailo

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Hailo (이스라엘 엣지 AI 칩 회사) |
| **영문명** | Hailo Technologies |
| **본사** | 이스라엘 텔아비브 |
| **설립 시간** | 2017년 |
| **공식 웹사이트** | [https://hailo.ai](https://hailo.ai) |
| **공급망 단계** | 엣지 AI 프로세서, 엔드사이드 NPU, 로봇/자동차 비전 |
| **기업 속성** | 유니콘, 사기업 |
| **모회사/소속 그룹** | 없음 (독립 주체) |
| **데이터 출처** | Hailo 공식 웹사이트, 제품 매뉴얼, 공개 보도자료, 업계 보고서 |

## 회사 소개

Hailo는 이스라엘의 선도적인 엣지 AI 칩 회사로, 엣지 디바이스에 고성능, 저전력의 신경망 프로세서를 제공하는 데 특화되어 있습니다.

Hailo의 Hailo-8 AI 프로세서는 혁신적인 데이터 흐름 아키텍처(Dataflow Architecture)를 채택하여 일반적인 전력 소비에서 높은 TOPS 연산 성능을 제공하며, 자동차 ADAS, 스마트 카메라, 산업 검사, 로봇 및 드론에 널리 사용됩니다. Hailo-15는 ISP와 AI를 추가로 통합하여 스마트 카메라 SoC를 대상으로 합니다. Hailo는 완전한 SDK와 모델 최적화 도구를 제공하며, 주요 딥러닝 프레임워크를 지원합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| Hailo-8 | 엣지 AI 가속기 | Hailo-8 / Hailo-8L | 로봇, 자동차, 보안, 산업 |
| Hailo-15 | ISP 통합 비전 프로세서 | Hailo-15 | 스마트 카메라, AIoT |
| 개발 키트 | 평가 및 프로토타입 | Hailo-8 M.2 / PCIe 개발 키트 | 개발자, 솔루션 제공업체 |
| 소프트웨어 스택 | 모델 최적화 및 추론 | Hailo Dataflow Compiler / TAPPAS | 전체 칩 시리즈 |

## 대표 제품

### Hailo-8 AI 프로세서

> Hailo-8 AI 프로세서: [공식 자료](https://hailo.ai)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 아키텍처 | 데이터 흐름 아키텍처(Dataflow Architecture) | Hailo 공개 자료 |
| 연산 성능 | 최대 26 TOPS INT8 | Hailo 공개 자료 |
| 에너지 효율 | 약 3 TOPS/W 일반 | Hailo 공개 자료 |
| 공정 | 16 nm (공개 보도) | 공개 보도 |
| 인터페이스 | PCIe Gen3 / M.2 / BGA 패키징 | Hailo 공개 자료 |
| 크기 | 약 15 mm × 15 mm (BGA) | Hailo 공개 자료 |
| 전력 소비 | 약 2.5 W 일반 | Hailo 공개 자료 |
| 가격 | 미공개 | - |

**기술 하이라이트**: 데이터 흐름 아키텍처의 높은 활용률, 저전력 고연산 성능, 다중 정밀도 양자화 지원, 소형 크기로 통합 용이.

**응용 시나리오**: 로봇 엔드사이드 인식, ADAS, 스마트 카메라, 산업 품질 검사, 드론, AIoT.

### Hailo-15 비전 프로세서

> Hailo-15 비전 프로세서: [공식 자료](https://hailo.ai)를 방문하여 확인하세요.

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 포지셔닝 | ISP와 AI를 통합한 비전 프로세서 | Hailo 공개 자료 |
| AI 연산 성능 | 최대 20 TOPS INT8 | Hailo 공개 자료 |
| ISP | 고성능 ISP 통합 | Hailo 공개 자료 |
| 비디오 | 다중 고해상도 비디오 지원 | Hailo 공개 자료 |
| 인터페이스 | MIPI, 이더넷, USB 등 | Hailo 공개 자료 |
| 전력 소비 | 미공개 | - |
| 응용 시나리오 | 스마트 카메라, 로봇 비전, AIoT | Hailo 공개 자료 |
| 가격 | 미공개 | - |

**기술 하이라이트**: ISP+AI 단일 칩, 엔드투엔드 비전 처리, 시스템 비용 및 전력 소비 절감.

**응용 시나리오**: 스마트 보안 카메라, 로봇 내비게이션, 얼굴 인식, 산업 비전 검사.

## 공급망 위치

- **상류 핵심 부품/재료**: 웨이퍼 파운드리, 패키징 및 테스트, 메모리, ISP IP, PCB/모듈.
- **하류 고객/응용 시나리오**: 자동차 Tier1/OEM, 보안 업체, 산업용 카메라 회사, 로봇 완제품 제조사, AIoT 장비 업체.
- **주요 경쟁사/대상**: Intel Movidius, Qualcomm QCS, Horizon Robotics Journey, Ambarella, Renesas R-Car.

## 지식 그래프 노드 및 관계

- 회사 엔티티: `ent_company_hailo`
- 제품 엔티티: `ent_product_hailo_8`
- 부품 엔티티: `ent_component_hailo_8_npu`
- 주요 관계:
  - `ent_company_hailo` -- `manufactures` --> `ent_product_hailo_8`
  - `ent_company_hailo` -- `manufactures` --> `ent_component_hailo_8_npu`
  - `ent_product_hailo_8` -- `uses` --> `ent_component_hailo_8_npu`

## 참고 자료

1. [Hailo 공식 웹사이트](https://hailo.ai)
2. [Hailo-8 제품 페이지](https://hailo.ai/products/hailo-8/)
3. [Hailo-15 제품 페이지](https://hailo.ai/products/hailo-15/)
