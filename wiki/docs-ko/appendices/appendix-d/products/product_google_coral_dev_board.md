# Google Coral Dev Board

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트: 2026-07-01. 모든 매개변수는 공식 공개 자료 기준이며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Google Coral / Google Coral](../companies/company_google_coral.md) |
| **제품 카테고리** | 엣지 AI 개발 보드 / Edge TPU 평가 플랫폼 |
| **출시일** | 2019년 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Coral Dev Board Product Page](https://coral.ai/products/dev-board/) |

## 제품 개요

Google Coral Dev Board는 Edge TPU를 통합한 AI 개발 보드로, 분리형 SoM 설계를 채택했습니다. Edge TPU는 4 TOPS INT8 연산 성능을 제공하며, 일반적인 소비 전력은 약 2W에 불과하여 MobileNet, EfficientDet-Lite 등 양자화 모델을 로컬에서 효율적으로 실행할 수 있습니다. 개발 보드는 Raspberry Pi와 호환되는 40핀 GPIO, MIPI CSI/DSI, HDMI, USB 3.0 및 기가비트 이더넷을 제공하여 로봇 인식, 스마트 카메라 및 산업용 비전 프로토타입의 신속한 검증에 적합합니다.

## 제품 이미지

> Google Coral Dev Board: [공식 자료](https://coral.ai/products/dev-board/)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|-----------|------|-----------|
| SoC | NXP i.MX 8M (쿼드 코어 Cortex-A53 + Cortex-M4F) | Coral 공개 자료 |
| AI 가속기 | Google Edge TPU | Coral 공개 자료 |
| AI 연산 성능 | 최대 4 TOPS INT8 | Coral 공개 자료 |
| 에너지 효율 | 약 2 TOPS/W | Coral 공개 자료 |
| 메모리 | 1 GB / 4 GB LPDDR4 (버전에 따라 다름) | Coral 공개 자료 |
| 저장 공간 | 8 GB / 16 GB / 64 GB eMMC + MicroSD | Coral 공개 자료 |
| 공정 | Edge TPU 미공개; i.MX 8M 14 nm | Coral 공개 자료 |
| 인터페이스 | USB 3.0, GbE, HDMI 2.0, MIPI CSI/DSI, 40핀 GPIO, PCIe (SoM) | Coral 공개 자료 |
| 소비 전력 | 약 5 W 일반 (전체 보드) | Coral 공개 자료 |
| 크기 | 약 88 mm × 60 mm (방열판 포함) | Coral 공개 자료 |
| 가격 | Dev Board 약 150 USD (참고 가격) | Coral 공개 자료 |

## 공급망 위치

- **제조사**: [Google Coral / Google Coral](../companies/company_google_coral.md)
- **핵심 부품/기술 출처**: Google 자체 개발 Edge TPU, NXP i.MX 8M SoC, LPDDR4/eMMC, PMIC, 캐리어 보드/방열판
- **하위 응용/고객**: 로봇 완제품 제조사, AIoT 솔루션 업체, 스마트 카메라 제조사, 대학 및 개발자 커뮤니티

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_google_coral_dev_board`
- 부품 엔터티: `ent_component_google_coral_edge_tpu`
- 제조사 엔터티: `ent_company_google_coral`
- 주요 관계:
  - `rel_ent_company_google_coral_manufactures_ent_product_google_coral_dev_board` (`ent_company_google_coral` → `manufactures` --> `ent_product_google_coral_dev_board`)
  - `rel_ent_company_google_coral_manufactures_ent_component_google_coral_edge_tpu` (`ent_company_google_coral` → `manufactures` --> `ent_component_google_coral_edge_tpu`)
  - `ent_product_google_coral_dev_board` -- `uses` --> `ent_component_google_coral_edge_tpu`

## 응용 시나리오

- **로봇 엣지 인식**: 실시간 객체 감지, 의미론적 분할 및 내비게이션 지원, 클라우드 의존도 감소
- **스마트 카메라 프로토타입**: 로컬 이벤트 감지 및 얼굴 인식, 개인정보 보호 및 응답 속도 향상
- **산업용 비전 검사**: 불량 분류, 바코드/QR 코드 인식 및 생산 라인 품질 검사

## 경쟁 비교

| 비교 항목 | Coral Dev Board | NVIDIA Jetson Nano | Raspberry Pi 5 + AI HAT |
|---|---|---|---|
| 연산 성능 | 4 TOPS | 0.5 TFLOPS | 13 TOPS |
| 소비 전력 | 약 5 W | 5–10 W | 약 7 W |
| 생태계 | TensorFlow Lite | JetPack / CUDA | Raspberry Pi / Hailo |

## 구매 및 배포 권장 사항

Edge TPU Compiler를 우선 사용하여 TensorFlow Lite 모델을 양자화 및 컴파일하세요. 호스트 인터페이스와 드라이버 버전을 확인하세요. 양산 시 BOM 최적화를 위해 Coral SoM 맞춤형 캐리어 보드를 사용하는 것을 권장합니다.

## 관련 항목

- [제조사: Google Coral / Google Coral](../companies/company_google_coral.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Coral Dev Board 제품 페이지](https://coral.ai/products/dev-board/)
2. [Coral 공식 문서](https://coral.ai/docs/)
3. [Coral Dev Board 데이터 시트](https://coral.ai/docs/dev-board/datasheet/)
