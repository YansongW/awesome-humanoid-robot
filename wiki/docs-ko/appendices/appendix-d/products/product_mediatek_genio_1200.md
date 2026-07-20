# MediaTek Genio 1200 엣지 AI 플랫폼

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료 기준이며, 누락된 항목은 "미공개"로 표기합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [MediaTek](../companies/company_mediatek.md) |
| **제품 카테고리** | AIoT 엣지 AI SoC / 로봇 및 산업용 비전 플랫폼 |
| **출시일** | 2022년 출시 |
| **상태** | 양산/상용 |
| **공식 홈페이지/출처** | [MediaTek Genio 1200 제품 페이지](https://genio.mediatek.com/genio-1200) |

## 제품 개요

MediaTek Genio 1200은 고급 AIoT 및 엣지 AI를 위한 6nm 플랫폼으로, 옥타코어 CPU, Mali-G57 MC5 GPU, 4.8 TOPS APU 및 듀얼 ISP를 통합합니다. 멀티미디어 성능은 트리플 4K 디스플레이와 4K90 비디오 코덱을 지원하며, 고속 인터페이스로 PCIe 3.0, USB 3.2, 기가비트 TSN 이더넷 및 다중 MIPI CSI/DSI를 포함하고, ROS, Yocto, Ubuntu 등의 시스템을 지원하여 로봇, 스마트 카메라 및 산업용 게이트웨이의 주류 선택입니다.

## 제품 이미지

> MediaTek Genio 1200 엣지 AI 플랫폼: [공식 자료](https://genio.mediatek.com/genio-1200)를 방문하여 확인하십시오.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 6 nm | MediaTek 공개 자료 |
| CPU | 옥타코어 (4× Cortex-A78 @ 최대 2.2 GHz + 4× Cortex-A55) | MediaTek 공개 자료 |
| GPU | Arm Mali-G57 MC5 | MediaTek 공개 자료 |
| AI 가속기 | MediaTek 멀티코어 APU | MediaTek 공개 자료 |
| AI 연산 성능 | 최대 4.8 TOPS INT8 | MediaTek 공개 자료 |
| 비전 | 듀얼 ISP, 최대 48 MP 단일 카메라 / 16 MP+16 MP 듀얼 카메라, 4K90 디코딩 | MediaTek 공개 자료 |
| DSP | 듀얼 Cadence Tensilica VP6 + HiFi 4 오디오 DSP | MediaTek 공개 자료 |
| 메모리 | LPDDR4X 지원, 최대 16 GB | MediaTek 공개 자료 |
| 인터페이스 | PCIe 3.0, USB 3.2 Gen1, GbE (TSN), MIPI CSI/DSI, HDMI, UART/I2C/SPI | MediaTek 공개 자료 |
| 전력 소비 | 일반 약 6–10 W (전체 보드/모듈) | MediaTek 공개 자료 |
| 가격 | 개발 키트 약 200–400 USD (참고 가격) | MediaTek 공개 자료 |

## 공급망 위치

- **제조사**: [MediaTek](../companies/company_mediatek.md)
- **핵심 부품/기술 출처**: TSMC 6nm 파운드리, ARM CPU/GPU IP, MediaTek 자체 개발 APU, LPDDR4X, UFS, PMIC, 캐리어 보드
- **하위 응용/고객**: AIoT 및 로봇 OEM/ODM, 스마트 카메라 제조사, 디지털 사이니지 및 산업용 HMI 고객, 엣지 게이트웨이 통합업체

## 지식 그래프 노드 및 관계

- 제품 엔티티: `ent_product_mediatek_genio_1200`
- 부품 엔티티: `ent_component_mediatek_genio_1200_soc`
- 제조사 엔티티: `ent_company_mediatek`
- 주요 관계:
  - `rel_ent_company_mediatek_manufactures_ent_product_mediatek_genio_1200` (`ent_company_mediatek` → `manufactures` --> `ent_product_mediatek_genio_1200`)
  - `rel_ent_company_mediatek_manufactures_ent_component_mediatek_genio_1200_soc` (`ent_company_mediatek` → `manufactures` --> `ent_component_mediatek_genio_1200_soc`)
  - `ent_product_mediatek_genio_1200` -- `uses` --> `ent_component_mediatek_genio_1200_soc`

## 응용 시나리오

- **산업용 로봇 및 AMR**: 다중 경로 시각 인식, SLAM, 경로 계획 및 로봇 팔 제어
- **스마트 카메라 및 보안**: 4K 실시간 객체 감지, 얼굴 인식 및 행동 분석
- **엣지 AI 게이트웨이 및 HMI**: 다중 화면 디스플레이, 장치 간 연결 및 로컬 AI 추론

## 경쟁 비교

| 비교 항목 | Genio 1200 | Rockchip RK3588 | Qualcomm QCS8550 |
|---|---|---|---|
| 공정 | 6 nm | 8 nm | 4 nm |
| AI 연산 성능 | 4.8 TOPS | 6 TOPS | 약 15 TOPS |
| CPU | 4×A78 + 4×A55 | 4×A76 + 4×A55 | 8×Kryo |

## 구매 및 배포 권장 사항

MediaTek NeuroPilot SDK를 사용하여 APU 성능을 평가하십시오. I/O 요구 사항에 따라 코어 보드 또는 SMARC/OSM 모듈을 선택하십시오. Yocto/Ubuntu 드라이버 및 ROS 패키지 지원을 확인하십시오.

## 관련 항목

- [제조사: MediaTek](../companies/company_mediatek.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [MediaTek Genio 1200](https://genio.mediatek.com/genio-1200)
2. [MediaTek Genio 플랫폼](https://www.mediatek.com/products/iot/genio)
3. [MediaTek NeuroPilot SDK](https://www.mediatek.com/products/iot/neuropilot)
