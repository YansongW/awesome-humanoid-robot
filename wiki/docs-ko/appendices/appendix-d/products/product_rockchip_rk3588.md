# Rockchip RK3588 AIoT SoC

> 이 항목은 [부록 D 주요 제품 Wiki](../../appendix-d.md)에 속합니다.
> 돌아가기: [부록 D.4 주요 제품 Wiki 목차](../index-products.md)
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 제품 정보 카드

| 항목 | 내용 |
|------|------|
| **제조사** | [Rockchip / Rockchip](../companies/company_rockchip.md) |
| **제품 카테고리** | 플래그십 AIoT SoC / 로봇 및 엣지 AI 메인 컨트롤러 |
| **출시일** | 2022년 출시, 2023년 양산 |
| **상태** | 양산/상용 |
| **공식 사이트/출처** | [Rockchip RK3588 Product Page](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html) |

## 제품 개요

Rockchip RK3588은 Rockchip의 플래그십 AIoT SoC로, 8 nm 공정을 채택하고 쿼드 코어 Cortex-A76과 쿼드 코어 Cortex-A55, Mali-G610 MC4 GPU 및 6 TOPS 트리플 코어 NPU를 통합했습니다. 멀티미디어 엔진은 8K@60fps 디코딩과 8K@30fps 인코딩을 지원하며, ISP는 32 MP 다중 카메라를 지원합니다. 인터페이스는 PCIe 3.0, USB 3.1, SATA, 기가비트 이더넷 및 다양한 디스플레이 출력을 포함하여 로봇, NVR, 엣지 AI 박스 및 스마트 상업용 디스플레이에 적합한 고성능 저가형 선택지입니다.

## 제품 이미지

> Rockchip RK3588 AIoT SoC: [공식 자료](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)를 방문하여 확인하세요.

## 사양 매개변수 표

| 사양 항목 | 값 | 비고/출처 |
|--------|------|-----------|
| 공정 | 8 nm LP | Rockchip 공개 자료 |
| CPU | 옥타코어 (4× Cortex-A76 @ 최대 2.4 GHz + 4× Cortex-A55) | Rockchip 공개 자료 |
| GPU | Arm Mali-G610 MC4 (약 450 GFLOPS) | Rockchip 공개 자료 |
| NPU | 자체 개발 트리플 코어 NPU | Rockchip 공개 자료 |
| AI 연산 성능 | 최대 6.0 TOPS INT8 | Rockchip 공개 자료 |
| 정밀도 지원 | INT4/INT8/INT16/FP16/BF16/TF32 | Rockchip 공개 자료 |
| 비디오 | 8K@60fps 디코딩, 8K@30fps 인코딩, H.265/VP9/AVS2 | Rockchip 공개 자료 |
| ISP | 듀얼 ISP, 32 MP, HDR & 3DNR 지원 | Rockchip 공개 자료 |
| 메모리 | LPDDR4/LPDDR4x/LPDDR5 지원, 최대 32 GB | Rockchip 공개 자료 |
| 인터페이스 | PCIe 3.0, USB 3.1, SATA 3.0, GbE, MIPI CSI/DSI, HDMI 2.1/DP/eDP | Rockchip 공개 자료 |
| 전력 소비 | 일반 약 5–15 W (전체 보드) | Rockchip 공개 자료 |
| 가격 | 개발 보드 약 100–200 USD (참고 가격) | Rockchip 공개 자료 |

## 공급망 위치

- **제조사**: [Rockchip / Rockchip](../companies/company_rockchip.md)
- **핵심 부품/기술 출처**: Rockchip 자체 개발 NPU 및 시스템 IP, ARM CPU/GPU IP, 8 nm 파운드리, LPDDR4x/5, eMMC, PMIC, 캐리어 보드
- **하위 응용/고객**: 로봇 및 드론 제조사, 산업용 NVR/보안 고객, 상업용 디스플레이 및 셀프 서비스 장비 업체, 개발 보드 커뮤니티

## 지식 그래프 노드 및 관계

- 제품 엔터티: `ent_product_rockchip_rk3588`
- 부품 엔터티: `ent_component_rockchip_rk3588_soc`
- 제조사 엔터티: `ent_company_rockchip`
- 주요 관계:
  - `rel_ent_company_rockchip_manufactures_ent_product_rockchip_rk3588` (`ent_company_rockchip` → `manufactures` --> `ent_product_rockchip_rk3588`)
  - `rel_ent_company_rockchip_manufactures_ent_component_rockchip_rk3588_soc` (`ent_company_rockchip` → `manufactures` --> `ent_component_rockchip_rk3588_soc`)
  - `ent_product_rockchip_rk3588` -- `uses` --> `ent_component_rockchip_rk3588_soc`

## 응용 시나리오

- **로봇 메인 컨트롤러**: 다중 카메라 인식, SLAM, 경로 계획 및 로봇 팔 제어
- **엣지 AI 박스 및 NVR**: 8K 디코딩, 다중 채널 비디오 분석 및 로컬 AI 추론
- **스마트 상업용 디스플레이 및 셀프 서비스 단말기**: 다중 화면 이기종 디스플레이, 터치 상호작용 및 광고 재생

## 경쟁 비교

| 비교 항목 | RK3588 | Allwinner T527 | MediaTek Genio 1200 |
|---|---|---|---|
| 공정 | 8 nm | 미공개 | 6 nm |
| AI 연산 성능 | 6 TOPS | 2 TOPS | 4.8 TOPS |
| 비디오 | 8K@60 디코딩 | 4K@60 디코딩 | 4K90 디코딩 |

## 구매 및 배포 권장 사항

RKNN-Toolkit2를 사용하여 모델을 INT8로 변환하고 NPU 활용도를 평가하세요. 방열 및 인터페이스 요구 사항에 따라 코어 보드 또는 SBC를 선택하세요. Linux/Android BSP 및 카메라 드라이버 버전을 확인하세요.

## 관련 항목

- [제조사: Rockchip / Rockchip](../companies/company_rockchip.md)
- [부록 D.4 주요 제품 Wiki](../index-products.md)

## 참고 자료

1. [Rockchip RK3588 제품 페이지](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)
2. [RKNN-Toolkit2 GitHub](https://github.com/rockchip-linux/rknpu2)
3. [Rockchip 공식 사이트](https://www.rock-chips.com)
