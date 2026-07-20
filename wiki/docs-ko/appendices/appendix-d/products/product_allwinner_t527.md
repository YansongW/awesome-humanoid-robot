# Allwinner T527 AIoT 애플리케이션 프로세서

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [올위너 테크놀로지 / Allwinner Technology](../companies/company_allwinner.md) |
| **제품 카테고리** | AIoT / 로봇 SoC / 엣지 AI 애플리케이션 프로세서 |
| **출시일** | 2024년 출시 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Allwinner T527 제품 정보](https://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-4A.html) |

## 제품 개요

Allwinner T527은 올위너가 AIoT 및 로봇을 위해 설계한 고성능 대비 저렴한 애플리케이션 프로세서로, 옥타코어 Cortex-A55와 RISC-V 코프로세서 아키텍처를 채택하고 2 TOPS NPU, Mali-G57 GPU 및 4K 비디오 코덱을 통합했습니다. 칩은 USB 3.0, PCIe 2.1, 기가비트 이더넷, MIPI CSI/DSI, HDMI, CAN 및 RS485 등 다양한 인터페이스를 제공하며, 로봇, 산업용 게이트웨이, 스마트 상업용 디스플레이 및 엣지 AI 기기에 널리 사용됩니다.

## 제품 이미지

> Allwinner T527 AIoT 애플리케이션 프로세서: [공식 자료](https://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-4A.html)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 미공개 | 올위너/파트너 공개 자료 |
| CPU | 옥타코어 Arm Cortex-A55 (4× @ 최대 1.8 GHz + 4× @ 1.42 GHz) | 올위너/파트너 공개 자료 |
| 코프로세서 | XuanTie E906 RISC-V @ 200 MHz + HiFi4 DSP @ 600 MHz | 올위너/파트너 공개 자료 |
| GPU | Arm Mali-G57 MC1 | 올위너/파트너 공개 자료 |
| NPU | 통합 AI 가속기 | 올위너/파트너 공개 자료 |
| AI 연산 성능 | 최대 2 TOPS INT8/INT16/FP16 | 올위너/파트너 공개 자료 |
| 비디오 | 4K@60fps H.265/H.264 디코딩, 4K@25fps H.264 인코딩 | 올위너/파트너 공개 자료 |
| ISP | 다중 MIPI CSI 지원, 최대 8 MP@30fps | 올위너/파트너 공개 자료 |
| 메모리 | LPDDR4/LPDDR4X 지원, 일반 2–4 GB | 올위너/파트너 공개 자료 |
| 인터페이스 | USB 3.0/2.0, PCIe 2.1, GbE, MIPI CSI/DSI, HDMI 2.0, LVDS/eDP, CAN, RS485, ADC | 올위너/파트너 공개 자료 |
| 전력 소비 | 일반 약 3–7 W (전체 보드) | 올위너/파트너 공개 자료 |
| 가격 | 개발 보드 약 50–100 USD (참고 가격) | 올위너/파트너 공개 자료 |

## 공급망 위치

- **제조사**: [올위너 테크놀로지 / Allwinner Technology](../companies/company_allwinner.md)
- **핵심 부품/기술 출처**: 올위너 자체 개발 시스템 및 NPU IP, ARM CPU/GPU IP, XuanTie RISC-V IP, LPDDR4, PMIC, 패키징/테스트, 캐리어 보드
- **하위 응용/고객**: 로봇 및 교육 기기 OEM, 산업용 게이트웨이/상업용 디스플레이 고객, 개발자 커뮤니티, 차량용 애프터마켓 제조사

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_allwinner_t527`
- 부품 엔터티: `ent_component_allwinner_t527_soc`
- 제조사 엔터티: `ent_company_allwinner`
- 주요 관계:
  - `rel_ent_company_allwinner_manufactures_ent_product_allwinner_t527` (`ent_company_allwinner` → `manufactures` --> `ent_product_allwinner_t527`)
  - `rel_ent_company_allwinner_manufactures_ent_component_allwinner_t527_soc` (`ent_company_allwinner` → `manufactures` --> `ent_component_allwinner_t527_soc`)
  - `ent_product_allwinner_t527` -- `uses` --> `ent_component_allwinner_t527_soc`

## 응용 시나리오

- **로봇 및 AMR**: 저비용 메인 컨트롤러, 시각 인식 및 모션 제어, ROS 및 Linux 지원
- **스마트 상업용 디스플레이 및 셀프 서비스 단말기**: 4K 재생, 터치 인터랙션 및 원격 장치 관리
- **산업용 게이트웨이 및 엣지 AI**: 프로토콜 변환, 데이터 수집 및 로컬 2 TOPS AI 추론

## 경쟁 비교

| 비교 항목 | Allwinner T527 | Rockchip RK3568 | Rockchip RK3588 |
|---|---|---|---|
| AI 연산 성능 | 2 TOPS | 1 TOPS | 6 TOPS |
| CPU | 옥타코어 A55 | 쿼드코어 A55 | 4×A76 + 4×A55 |
| 비디오 | 4K@60 디코딩 | 4K@60 디코딩 | 8K@60 디코딩 |

## 구매 및 배포 권장 사항

올위너/파트너 SDK 및 BSP를 사용하여 NPU 모델 지원을 검증하세요. T527의 서로 다른 하위 모델 간 인터페이스 차이에 주의하세요. 저비용 시나리오에서는 코어 보드 솔루션을 우선 채택할 수 있습니다.

## 관련 항목

- [제조사: 올위너 테크놀로지 / Allwinner Technology](../companies/company_allwinner.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [올위너 테크놀로지 공식 사이트](https://www.allwinnertech.com)
2. [Orange Pi 4A 제품 페이지](https://www.orangepi.org/html/hardWare/computerAndMicrocontrollers/details/Orange-Pi-4A.html)
3. [linux-sunxi T527 자료](https://linux-sunxi.org/T527)
