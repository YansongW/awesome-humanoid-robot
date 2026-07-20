# Google Coral / Google Coral

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | Google Coral |
| **영문명** | Google Coral |
| **본사** | 미국 캘리포니아주 마운틴뷰 |
| **설립 시간** | 2019년 (Coral 제품 라인 출시) |
| **공식 웹사이트** | [https://coral.ai](https://coral.ai) |
| **공급망 단계** | Edge TPU, 엣지 AI 가속기, AIoT/로봇 비전 |
| **기업 속성** | Google / Alphabet 산하 (상장사 NASDAQ: GOOGL) |
| **모회사/소속 그룹** | Alphabet / Google |
| **데이터 출처** | Coral 공식 웹사이트, Google 공식 문서, 공개 제품 자료 |

## 회사 소개

Google Coral은 Google이 출시한 엣지 AI 플랫폼으로, 핵심은 자체 개발한 Edge TPU로 극저전력에서 신경망 추론을 수행합니다. Coral은 Dev Board, USB Accelerator, PCIe/M.2 가속기 및 SoM 등 다양한 형태를 제공하며, 스마트 카메라, 로봇, 산업 검사 및 AIoT 기기를 대상으로 합니다. 소프트웨어 스택은 TensorFlow Lite를 기반으로 하며, Edge TPU Compiler를 통해 양자화된 모델을 엣지에 효율적으로 배포할 수 있습니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 응용 분야 |
|--------|------|----------|----------|
| Dev Board / SoM | SoM 통합 개발 보드 | Coral Dev Board | AIoT 프로토타입, 로봇 인식, 엣지 AI 개발 |
| USB / PCIe / M.2 가속기 | 외장형 Edge TPU 가속기 | Coral USB Accelerator | 기존 임베디드 플랫폼 AI 업그레이드, 산업 비전, 스마트 카메라 |

## 대표 제품

### Coral Dev Board

> Coral Dev Board: [공식 자료](https://coral.ai)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| SoC | NXP i.MX 8M (쿼드 Cortex-A53 + Cortex-M4F) | Coral 공개 자료 |
| AI 가속기 | Google Edge TPU | Coral 공개 자료 |
| AI 연산 성능 | 최대 4 TOPS INT8 | Coral 공개 자료 |
| 에너지 효율 | 약 2 TOPS/W | Coral 공개 자료 |
| 메모리 | 1 GB / 4 GB LPDDR4 (버전에 따라 다름) | Coral 공개 자료 |
| 저장 공간 | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral 공개 자료 |
| 공정 | Edge TPU 미공개; i.MX 8M 14 nm | Coral 공개 자료 |
| 인터페이스 | USB 3.0, GbE, HDMI 2.0, MIPI CSI/DSI, 40핀 GPIO, PCIe (SoM) | Coral 공개 자료 |
| 전력 소비 | 약 5 W 일반 (전체 보드) | Coral 공개 자료 |
| 크기 | 약 88 mm × 60 mm (방열판 포함) | Coral 공개 자료 |
| 가격 | Dev Board 약 150 USD (참고 가격) | Coral 공개 자료 |

**기술 하이라이트**: 분리형 Coral SoM, Edge TPU와 i.MX 8M 이종 통합, Mendel Linux, TensorFlow Lite 생태계, 프로토타입에서 맞춤형 캐리어 보드로 빠르게 전환 가능.

**응용 시나리오**: **로봇 엣지 인식**: 실시간 객체 탐지, 의미론적 분할 및 내비게이션 지원으로 클라우드 의존도 감소; **스마트 카메라 프로토타입**: 로컬 이벤트 감지 및 얼굴 인식으로 개인정보 보호 및 응답 속도 향상; **산업 비전 검사**: 결함 분류, 바코드/QR 코드 인식 및 생산 라인 품질 검사

### Coral USB Accelerator

> Coral USB Accelerator: [공식 자료](https://coral.ai)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| AI 가속기 | Google Edge TPU | Coral 공개 자료 |
| AI 연산 성능 | 최대 4 TOPS INT8 | Coral 공개 자료 |
| 인터페이스 | USB 3.0 Type-C | Coral 공개 자료 |
| 전력 소비 | 약 2 W | Coral 공개 자료 |
| 크기 | 약 65 mm × 30 mm | Coral 공개 자료 |
| 가격 | 약 75 USD (참고 가격) | Coral 공개 자료 |

**기술 하이라이트**: 플러그 앤 플레이, USB 전원 공급, 별도 방열판 불필요, 기존 장치에 AI 추론 기능 신속 추가.

**응용 시나리오**: PC/엣지 박스 AI 확장, 산업 비전, 스마트 카메라, 개발 및 검증.

## 공급망 위치

- **상류 핵심 부품/소재**: TSMC 웨이퍼 파운드리, NXP i.MX 8M SoC, LPDDR4/eMMC, 패키징 및 테스트, PCB/모듈
- **하류 고객/응용 시나리오**: AIoT 장비 업체, 로봇 완제품 제조사, 스마트 카메라 제조사, 산업 비전 솔루션 업체, 개발자
- **주요 경쟁사/대상**: Intel Movidius, Hailo, NVIDIA Jetson Nano, Qualcomm QCS, Horizon Robotics Journey

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_google_coral`
- 제품 엔터티: `ent_product_google_coral_dev_board`, `ent_product_google_coral_usb_accelerator`
- 부품 엔터티: `ent_component_google_coral_edge_tpu`, `ent_component_google_coral_edge_tpu_2`
- 주요 관계:
  - `ent_company_google_coral` -- `manufactures` --> `ent_product_google_coral_dev_board`
  - `ent_company_google_coral` -- `manufactures` --> `ent_product_google_coral_usb_accelerator`
  - `ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu`
  - `ent_company_google_coral` -- `manufactures` --> `ent_component_google_coral_edge_tpu_2`
  - `ent_product_google_coral_dev_board` -- `uses` --> `ent_component_google_coral_edge_tpu`
  - `ent_product_google_coral_usb_accelerator` -- `uses` --> `ent_component_google_coral_edge_tpu_2`

## 참고 자료

1. [Coral 공식 웹사이트](https://coral.ai)
2. [Coral Dev Board 제품 페이지](https://coral.ai/products/dev-board/)
3. [Coral 공식 문서](https://coral.ai/docs/)
