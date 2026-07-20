# Rokoko / Rokoko

> 이 항목은 [부록 D 기업/제품 Wiki](../../appendix-d.md)에 속합니다.
> 데이터 업데이트 시간: 2026-07-01. 모든 매개변수는 공식 공개 자료를 기준으로 하며, 누락된 항목은 "미공개"로 표시합니다.

---

## 회사 정보 카드

| 항목 | 내용 |
|------|------|
| **한글명** | Rokoko |
| **영문명** | Rokoko |
| **본사** | 덴마크 코펜하겐 |
| **설립일** | 2014년 |
| **공식 사이트** | [https://rokoko.com](https://rokoko.com) |
| **공급망 단계** | 관성 모션 캡처, 애니메이션 데이터, 인간-기계 상호작용 데이터 수집 |
| **기업 속성** | 스타트업 |
| **모회사/소속 그룹** | 없음 |
| **데이터 출처** | Rokoko 공식 사이트, CGW 뉴스, Animation Xpress |

## 회사 소개

Rokoko는 독립 창작자, 게임, 영화, 스포츠 과학 및 로봇 분야를 대상으로 하는 관성 모션 캡처(mocap) 회사로, 높은 가성비, 사용 편의성 및 실시간 스트리밍 기능으로 유명합니다.

핵심 제품인 Smartsuit Pro II는 전신 관성 모션 캡처 슈트로, 17~19개의 9-DOF IMU 센서를 내장하고 있으며, Wi-Fi를 통해 무료 Rokoko Studio 소프트웨어와 연결하여 실시간으로 녹화, 정리, 편집 및 애니메이션을 Unreal Engine, Unity, Blender, Maya, MotionBuilder 등 주요 3D 도구로 스트리밍할 수 있습니다. Rokoko는 또한 Smartgloves 손 추적, Face Capture 얼굴 캡처 및 Video to Animation과 같은 AI 기반 애니메이션 도구를 제공합니다.

Rokoko의 모션 데이터는 로봇 분야에서도 점점 더 많이 사용되어, 휴머노이드 로봇, 디지털 휴먼 및 임베디드 지능형 모델에 자연스러운 동작 참조 및 훈련 데이터를 제공합니다.

## 제품 라인

| 제품 라인 | 포지셔닝 | 대표 제품 | 적용 분야 |
|--------|------|----------|----------|
| 전신 모션 캡처 | 관성 모션 캡처 슈트 | Smartsuit Pro II | 애니메이션, 게임, VFX |
| 손 모션 캡처 | 손가락 추적 장갑 | Smartgloves | 손 애니메이션, 로봇 손 |
| 소프트웨어 플랫폼 | 녹화, 편집, 스트리밍 | Rokoko Studio | 모션 캡처 후반 작업, 실시간 구동 |
| AI 애니메이션 도구 | 비디오/단일 카메라 구동 애니메이션 | Rokoko Video / Motion Library | 빠른 애니메이션 생성 |

## 대표 제품

### Rokoko Smartsuit Pro II

> Rokoko Smartsuit Pro II: [공식 자료](https://rokoko.com)를 방문하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 센서 개수 | 17× 또는 19× 9-DOF IMU | Rokoko 공식 사이트 |
| 3D 방향 정밀도 | ±1° | Rokoko 공개 사양 |
| 샘플링/스트리밍 | 200 fps | Rokoko 공개 사양 |
| 가속도계 범위 | 16 g | Rokoko 공개 사양 |
| 무선 연결 | Wi-Fi (최대 약 100 m) | Rokoko 공개 사양 |
| 배터리 지속 시간 | 약 6시간 | Rokoko 공개 사양 |
| 슈트 사이즈 | S / M / L / XL | Rokoko 공식 사이트 |
| 가격 | 약 2,745 USD부터 | 공개 견적 |

**기술적 특징**: Sensor Fusion 2.0 저드리프트 알고리즘, 다층 추적(계단/사다리), 고충격 동작 최적화, 세탁 가능한 원단, Smartgloves와의 기본 통합, 원클릭 실시간 스트리밍.

**적용 분야**: 영화 애니메이션, 게임 캐릭터, 가상 라이브/VTubing, 스포츠 생체역학 분석, 로봇/휴머노이드 로봇 동작 참조 데이터 수집.

### Rokoko Smartgloves

> Rokoko Smartgloves: [공식 자료](https://rokoko.com)를 방문하세요.

| 사양 항목 | 수치 | 비고/출처 |
|--------|------|-----------|
| 센서 개수 | 7× 6-DOF 손 추적기 | Rokoko 공개 사양 |
| 샘플링 속도 | 100 Hz | Rokoko 공개 사양 |
| 지연 시간 | 약 20 ms | Rokoko 공개 사양 |
| 무선 연결 | 2.4 / 5 GHz Wi-Fi | Rokoko 공개 사양 |
| 자기계 | 없음 (자기 간섭 방지) | Rokoko 공개 사양 |
| 3D 방향 정밀도 | ±1° | Rokoko 공개 사양 |
| 가격 | 약 995 USD | 공개 견적 |

**기술적 특징**: 자기계 없는 설계로 간섭 방지, 서브밀리미터 수준 손끝 추적, Smartsuit Pro II와 배터리 및 Wi-Fi 링크 공유, Rokoko Studio 기본 통합.

**적용 분야**: 손 애니메이션, 가상 캐릭터 라이브 방송, 로봇 손 조작 데이터 수집, 인간-기계 상호작용 연구.

## 공급망 위치

- **상류 핵심 부품/소재**: MEMS IMU 센서, Wi-Fi 모듈, 웨어러블 텍스타일, 리튬 배터리, 센서 융합 알고리즘 칩.
- **하류 고객/적용 분야**: 독립 애니메이터, 게임 스튜디오(Ubisoft, EA 등), 영화 VFX, 스포츠 과학 연구 기관, 로봇/휴머노이드 로봇 회사.
- **주요 경쟁사/대상**: Xsens / Movella, Noitom Perception Neuron, StretchSense, Manus, Vicon(광학 모션 캡처).

## 지식 그래프 노드 및 관계

- 회사 엔터티: `ent_company_rokoko`
- 제품/플랫폼 엔터티: `ent_product_rokoko_smartsuit_pro_ii`, `ent_product_rokoko_smartgloves`
- 주요 관계:
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartsuit_pro_ii` (`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartsuit_pro_ii`)
  - `rel_ent_company_rokoko_manufactures_ent_product_rokoko_smartgloves` (`ent_company_rokoko` → `manufactures` → `ent_product_rokoko_smartgloves`)

## 참고 자료

1. [Rokoko 공식 사이트](https://rokoko.com)
2. [CGW – Rokoko Smartsuit Pro II 출시](https://www.cgw.com/Press-Center/News/2021/Rokoko-Launches-the-Next-Gen-Smartsuit-Pro-II.aspx)
3. [Animation Xpress – Rokoko Smartsuit Pro II](https://www.animationxpress.com/latest-news/motion-capture-company-rokoko-launches-smartsuit-pro-ii/)
4. [Rokoko Studio 다운로드 페이지](https://rokoko.com/studio)
