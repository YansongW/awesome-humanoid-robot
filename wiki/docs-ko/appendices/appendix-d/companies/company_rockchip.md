# 瑞芯微 / Rockchip

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 일자: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **중문명** | 瑞芯微 |
| **영문명** | Rockchip |
| **본사** | 중국 푸젠성 푸저우 |
| **설립일** | 2001년 |
| **공식 사이트** | [https://www.rock-chips.com](https://www.rock-chips.com) |
| **공급망 단계** | AIoT SoC, 로봇 메인 컨트롤러, 산업용 태블릿, 엣지 AI, 멀티미디어 |
| **기업 속성** | 상장 기업 (선전 증권거래소: 603893) |
| **모회사/소속 그룹** | 없음 (Rockchip이 상장 주체) |
| **데이터 출처** | Rockchip 공식 사이트, RK3588 제품 자료, 공개 보도자료, 업계 보고서 |

## 회사 소개

瑞芯微(Rockchip)은 중국을 선도하는 AIoT 및 멀티미디어 SoC 설계 회사로, 제품은 태블릿 PC, 스마트 TV 박스, 산업 제어, 로봇 및 엣지 AI를 포괄합니다. RK3588은 플래그십 AIoT 칩으로, 6 TOPS NPU, 8K 비디오 코덱 및 다양한 인터페이스를 통합하여 로봇 메인 컨트롤러, 산업용 게이트웨이, NVR, 스마트 상업용 디스플레이 및 엣지 AI 박스에 널리 사용됩니다. Rockchip은 RKNN 툴체인과 Linux/Android SDK를 제공하여 빠른 모델 배포를 지원합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| RK3588 시리즈 | 플래그십 AIoT / 로봇 SoC | RK3588 / RK3588S | 로봇 메인 컨트롤러, 엣지 AI, NVR, 산업용 HMI, 8K 상업용 디스플레이 |
| RK3576 / RK3568 시리즈 | 중고급 AIoT SoC | RK3568 / RK3576 | 산업용 게이트웨이, 스마트 카메라, 교육용 로봇, AIoT 단말 |

## 대표 제품

### Rockchip RK3588

> Rockchip RK3588: [공식 자료](https://www.rock-chips.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
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

**기술 하이라이트**: 8 nm 플래그십 AIoT 칩, 6 TOPS NPU, 8K 멀티미디어, 멀티 채널 카메라, 풍부한 확장 인터페이스, RKNN 툴체인, Linux/Android 생태계 성숙.

**적용 시나리오**: **로봇 메인 컨트롤러**: 멀티 채널 카메라 인식, SLAM, 경로 계획 및 로봇 팔 제어; **엣지 AI 박스 및 NVR**: 8K 디코딩, 멀티 채널 비디오 분석 및 로컬 AI 추론; **스마트 상업용 디스플레이 및 셀프 서비스 단말**: 멀티 스크린 이기종 디스플레이, 터치 인터랙션 및 광고 재생

### Rockchip RK3576

> Rockchip RK3576: [공식 자료](https://www.rock-chips.com)를 방문하여 확인하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 공정 | 미공개 | Rockchip 공개 자료 |
| CPU | 옥타코어 Cortex-A72/A53 또는 최신 아키텍처 | Rockchip 공개 자료 |
| NPU | 약 6 TOPS | Rockchip 공개 자료 |
| 비디오 | 4K/8K 디코딩 | Rockchip 공개 자료 |
| 인터페이스 | PCIe, USB, GbE, MIPI CSI/DSI, HDMI | Rockchip 공개 자료 |
| 전력 소비 | 약 3–8 W | Rockchip 공개 자료 |
| 가격 | 미공개 | Rockchip 공개 자료 |

**기술 하이라이트**: 중고급 AIoT SoC, RK3588의 NPU 및 멀티미디어 기능을 계승하여 비용에 민감한 로봇 및 엣지 디바이스를 대상으로 함.

**적용 시나리오**: 산업용 게이트웨이, 교육용 로봇, 스마트 카메라, AIoT 단말.

## 공급망 위치

- **상류 핵심 부품/소재**: TSMC/SMIC 위탁 생산, ARM CPU/GPU IP, 자체 개발 NPU, LPDDR4x, eMMC, 패키징 및 테스트, 기판
- **하류 고객/적용 시나리오**: 로봇 완제품 제조사, 산업용 태블릿/게이트웨이 제조사, NVR/보안 고객, 상업용 디스플레이 및 교육 기기 제조사, 개발자
- **주요 경쟁사/대상**: Allwinner, MediaTek Genio, Qualcomm QCS, NVIDIA Jetson, Amlogic, HiSilicon

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_rockchip`
- 제품 엔터티: `ent_product_rockchip_rk3588`, `ent_product_rockchip_rk3576`
- 부품 엔터티: `ent_component_rockchip_rk3588_soc`, `ent_component_rockchip_rk3576_soc`
- 주요 관계:
  - `ent_company_rockchip` -- `manufactures` --> `ent_product_rockchip_rk3588`
  - `ent_company_rockchip` -- `manufactures` --> `ent_product_rockchip_rk3576`
  - `ent_company_rockchip` -- `manufactures` --> `ent_component_rockchip_rk3588_soc`
  - `ent_company_rockchip` -- `manufactures` --> `ent_component_rockchip_rk3576_soc`
  - `ent_product_rockchip_rk3588` -- `uses` --> `ent_component_rockchip_rk3588_soc`
  - `ent_product_rockchip_rk3576` -- `uses` --> `ent_component_rockchip_rk3576_soc`

## 참고 자료

1. [Rockchip 공식 사이트](https://www.rock-chips.com)
2. [RK3588 제품 페이지](https://www.rock-chips.com/a/en/products/RK35_Series/2022/0926/1660.html)
3. [Rockchip RKNN SDK](https://github.com/rockchip-linux/rknpu2)
