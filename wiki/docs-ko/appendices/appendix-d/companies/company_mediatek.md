# MediaTek / MediaTek

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 '미공개'로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한국어명** | 미디어텍 |
| **영문명** | MediaTek |
| **본사** | 대만 신주 |
| **설립 연도** | 1997년 |
| **공식 사이트** | [https://www.mediatek.com](https://www.mediatek.com) |
| **공급망 단계** | 엣지 AI SoC, AIoT, 모바일/컴퓨팅 플랫폼, 로봇 메인 컨트롤러 |
| **기업 속성** | 상장 기업 (TWSE: 2454) |
| **모회사/소속 그룹** | 없음 (MediaTek이 상장 주체) |
| **데이터 출처** | MediaTek 공식 사이트, Genio 제품 자료, 공개 보도자료, 업계 보고서 |

## 회사 소개

MediaTek(미디어텍)은 세계적인 반도체 설계 회사로, 스마트폰, 태블릿, TV, 웨어러블 기기, 자동차 및 AIoT 분야의 제품을 포괄합니다. Genio 시리즈 엣지 AI 플랫폼은 산업용 IoT, 로봇 및 스마트 기기를 대상으로 하며, 멀티코어 CPU, GPU, APU(AI 프로세서) 및 다양한 멀티미디어 인터페이스를 통합하고, 첨단 6nm 공정을 통해 고성능과 저전력의 균형을 이루며, NeuroPilot SDK 및 Yocto/Ubuntu를 지원합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| Genio 시리즈 | AIoT 엣지 AI 플랫폼 | Genio 1200 / 700 / 510 | 산업용 IoT, 로봇, 스마트 리테일, 디지털 사이니지, 엣지 게이트웨이 |
| Filogic / Pentonic | 연결 및 디스플레이 플랫폼 | Filogic 880 | Wi-Fi 7 라우터, 스마트 TV, AIoT 게이트웨이 |

## 대표 제품

### MediaTek Genio 1200

> MediaTek Genio 1200: [공식 자료](https://www.mediatek.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 6 nm | MediaTek 공개 자료 |
| CPU | 옥타코어 (4× Cortex-A78 @ 최대 2.2 GHz + 4× Cortex-A55) | MediaTek 공개 자료 |
| GPU | Arm Mali-G57 MC5 | MediaTek 공개 자료 |
| AI 가속기 | MediaTek 멀티코어 APU | MediaTek 공개 자료 |
| AI 연산 성능 | 최대 4.8 TOPS INT8 | MediaTek 공개 자료 |
| 비전 | 듀얼 ISP, 최대 48 MP 싱글 카메라 / 16 MP+16 MP 듀얼 카메라, 4K90 디코딩 | MediaTek 공개 자료 |
| DSP | 듀얼 Cadence Tensilica VP6 + HiFi 4 Audio DSP | MediaTek 공개 자료 |
| 메모리 | LPDDR4X 지원, 최대 16 GB | MediaTek 공개 자료 |
| 인터페이스 | PCIe 3.0, USB 3.2 Gen1, GbE(TSN), MIPI CSI/DSI, HDMI, UART/I2C/SPI | MediaTek 공개 자료 |
| 전력 소비 | 일반 약 6–10 W (전체 보드/모듈) | MediaTek 공개 자료 |
| 가격 | 개발 키트 약 200–400 USD (참고 가격) | MediaTek 공개 자료 |

**기술 하이라이트**: 6nm 플래그십 AIoT SoC, 4.8 TOPS APU, 트리플 4K 디스플레이, 듀얼 ISP, 다양한 고속 인터페이스, Android/Yocto/Ubuntu 및 ROS 지원.

**적용 시나리오**: **산업용 로봇 및 AMR**: 다중 경로 시각 인식, SLAM, 경로 계획 및 로봇 팔 제어; **스마트 카메라 및 보안**: 4K 실시간 객체 감지, 얼굴 인식 및 행동 분석; **엣지 AI 게이트웨이 및 HMI**: 다중 화면 디스플레이, 기기 간 연결 및 로컬 AI 추론

### MediaTek Genio 700

> MediaTek Genio 700: [공식 자료](https://www.mediatek.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 6 nm | MediaTek 공개 자료 |
| CPU | 옥타코어 (4× Cortex-A78 + 4× Cortex-A55) | MediaTek 공개 자료 |
| GPU | Arm Mali-G57 MC3 | MediaTek 공개 자료 |
| AI 연산 성능 | 약 4 TOPS | MediaTek 공개 자료 |
| 비디오 | 4K60 인코딩/디코딩 | MediaTek 공개 자료 |
| 인터페이스 | PCIe, USB 3.0, GbE, MIPI CSI/DSI | MediaTek 공개 자료 |
| 전력 소비 | 약 4–8 W | MediaTek 공개 자료 |
| 가격 | 미공개 | MediaTek 공개 자료 |

**기술 하이라이트**: 중고급 AIoT 플랫폼, 6nm 에너지 효율, 다양한 멀티미디어 및 연결 기능.

**적용 시나리오**: 스마트 리테일, 산업용 HMI, 스마트 카메라, 엣지 게이트웨이.

## 공급망 위치

- **상류 핵심 부품/소재**: TSMC 6nm 파운드리, ARM CPU/GPU IP, 자체 APU, LPDDR5, UFS, 패키징/테스트, 기판
- **하류 고객/적용 시나리오**: AIoT 기기 제조사, 로봇 완제품 업체, 스마트 리테일 및 디지털 사이니지 제조사, 산업용 게이트웨이 고객
- **주요 경쟁사/대상**: Qualcomm QCS, NVIDIA Jetson, Rockchip RK3588, Allwinner T527, Amlogic

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_mediatek`
- 제품 엔터티: `ent_product_mediatek_genio_1200`, `ent_product_mediatek_genio_700`
- 부품 엔터티: `ent_component_mediatek_genio_1200_soc`, `ent_component_mediatek_genio_700_soc`
- 주요 관계:
  - `ent_company_mediatek` -- `manufactures` --> `ent_product_mediatek_genio_1200`
  - `ent_company_mediatek` -- `manufactures` --> `ent_product_mediatek_genio_700`
  - `ent_company_mediatek` -- `manufactures` --> `ent_component_mediatek_genio_1200_soc`
  - `ent_company_mediatek` -- `manufactures` --> `ent_component_mediatek_genio_700_soc`
  - `ent_product_mediatek_genio_1200` -- `uses` --> `ent_component_mediatek_genio_1200_soc`
  - `ent_product_mediatek_genio_700` -- `uses` --> `ent_component_mediatek_genio_700_soc`

## 참고 자료

1. [MediaTek 공식 사이트](https://www.mediatek.com)
2. [MediaTek Genio 1200](https://genio.mediatek.com/genio-1200)
3. [MediaTek Genio 플랫폼](https://www.mediatek.com/products/iot/genio)
