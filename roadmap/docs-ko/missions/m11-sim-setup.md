# M11 · 시뮬레이션 환경과 모델 변환: 디지털 세계에서 먼저 만 번 넘어지기

**전체 위치**: [M10의 URDF 모델 패키지](m10-urdf-modeling.md) 바로 다음에 위치하며, Stage 2 시뮬레이션의 첫 단계입니다. 입력은 M10에서 전달된 모델 패키지이며, 출력은 **실행 가능한 시뮬레이션 프로젝트**입니다——모델 로딩 시 경고 없음, 접촉 동작 합리적, 액추에이터/센서 모델링 완료, 기본 검사 모두 통과. [M12](m12-sim-walking.md)에서 이를 사용하여 서고 걷고, [M13](m13-rl-training.md)에서 이를 사용하여 정책을 훈련합니다.

**전제 조건**: M10 검사 모두 통과(모델 패키지入库, 관성 매개변수 확인 완료); [Stage 0](../stage-0-foundations.md) 단계 4의 PD 서기 감각 유지.

이론적 배경: [제23장 시뮬레이션과 물리 엔진](/wiki/chapters/chapter-23/), [제22장 소프트웨어 미들웨어](/wiki/chapters/chapter-22/), [부록 C 소프트웨어 및 시뮬레이션 플랫폼 목록](/wiki/appendices/appendix-c/); 엔진 선택 총괄표는 [시뮬레이션 환경 구축 매뉴얼](../playbooks/sim-setup.md) 첫 번째 단계 참조.

## 단계 1: 엔진 설치 및 공식 기준 검증

【무엇을 할까】두 가지 주 경로 중 하나 선택(또는 둘 다 설치):

- **[MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/)** : `pip install mujoco`, CPU만으로 실행 가능;
- **[Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/)** ([Isaac Sim](/entry/ent_software_nvidia_isaac_sim_2024/) 위에서 실행): NVIDIA GPU 필요, conda 환경, Isaac Lab과 Isaac Sim 버전 엄격히 일치——조합은 릴리스에 따라 변하므로, 공식 설치 문서를 기준으로 선택한 버전에 맞게 직접 확인.

설치 후 먼저 공식 예제 실행(MuJoCo 내장 humanoid 모델 / Isaac Lab의 H1 휴머노이드 예제), 그다음 자체 모델 테스트:

```bash
# MuJoCo: CPU면 충분; 공식 내장 휴머노이드 모델 로딩하여 검증(모델 경로는 버전에 따라 변하므로, 선택한 버전에 맞게 확인)
pip install mujoco
python -m mujoco.viewer --mjcf=$(python -c "import mujoco, os; print(os.path.join(os.path.dirname(mujoco.__file__), 'model', 'humanoid', 'humanoid.xml'))")
# Isaac Lab: conda 환경 + 공식 H1 예제(설치 단계와 작업 이름은 공식 문서 기준)
conda create -n isaaclab python=3.10 -y && conda activate isaaclab
git clone https://github.com/isaac-sim/IsaacLab.git
```

【왜 하는가】공식 예제는 "환경 문제"와 "모델 문제"를 분리하는 데 도움을 줍니다——예제가 실행되지 않으면 설치가 잘못된 것이고, 예제는 실행되는데 내 모델이 실행되지 않으면 모델이 잘못된 것입니다. 선택 논리(자세한 내용은 [시뮬레이션 매뉴얼](../playbooks/sim-setup.md) 참조): MuJoCo는 접촉 품질이 높아 다리 제어 연구의 사실상 표준; Isaac Lab GPU 대규모 병렬 처리로 RL 훈련을 위해 설계됨. 오픈소스 기준: ToddlerBot은 MuJoCo/MJX 사용, Berkeley Humanoid Lite는 Isaac Lab 기반, OpenLoong의 MPC+WBC는 MuJoCo에 배포(`data/roadmap/research/` 각 아카이브).

【상황 분석】NVIDIA GPU 없음: MuJoCo만 사용, 제어 연구와 CPU 소규모 RL에 충분; RTX 카드 있고 RL 경로: 둘 다 설치, MuJoCo로 모델 조정, Isaac Lab으로 정책 훈련(Berkeley가 이 조합); ROS 전체 스택 통합 테스트 필요: [Gazebo](/entry/ent_software_gazebo/) 추가, 물리 정밀도에 집착하지 말 것.

## 단계 2: URDF → MJCF/USD 변환 및 재확인

【무엇을 할까】[URDF](/entry/ent_technology_urdf_robot_description_format_2024/)를 대상 형식으로 변환: MuJoCo는 URDF를 직접 컴파일하고 [MJCF](/entry/ent_technology_mjcf_simulation_format_2024/)로 저장 가능, Isaac에 들어가려면 공식 URDF Importer를 사용하여 USD로 변환:

```bash
# MuJoCo Python API로 URDF 컴파일 및 MJCF 내보내기(API 세부 사항은 선택한 버전에 맞게 확인)
python -c "import mujoco; m = mujoco.MjModel.from_xml_path('robot.urdf'); mujoco.mj_saveLastXML('robot_mjcf.xml', m); print('converted OK')"
```

네 가지 고전적인 변환 오류를 하나씩 확인:

| 오류 | 증상 | 수정 방법 |
|---|---|---|
| 관성 텐서 비정부호 | 컴파일 오류/모델 떨림 | M10 단계 3으로 돌아가 CAD로 다시 내보내기, ixx/iyy/izz 삼각 부등식 확인 |
| mesh 단위 mm를 m으로 착각 | 모델이 1000배 크거나 작음 | ×0.001 스케일링 또는 내보낼 때 미터로 통일 |
| mesh 경로 대소문자 | Linux에서 파일을 찾을 수 없음 | 경로와 파일명을 모두 소문자로 정규화 |
| 관절 축 방향 규약 차이 | 운동 방향이 모두 반대 | viewer에서 관절별로 구동하여 확인(M10에서 이미 초기 검증, 여기서 시뮬레이션 내 재확인) |

변환 후 수동으로 MJCF 패치: `<compiler angle="radian" .../>` 각도 단위 통일, 변환 중 손실된 관절 제한 복원, 좌표계 규약 확인.

【왜 하는가】URDF는 시각화와 ROS 도구 체인을 위해 설계되어 트리 구조만 지원하고 액추에이터 모델이 약함; MJCF는 시뮬레이션과 제어를 위해 설계됨——컴파일 시 관성을 자동으로 계산하고, 액추에이터와 센서는 일급 시민(제23장 23.4절). 변환할 때마다 정보 손실이 있으며, 작은 오류는 물리 엔진에 의해 증폭되어 "실행하자마자 날아감"이 됩니다.

【상황 분석】오픈소스 플랫폼 복제: 공식 유지 관리 MJCF/USD 사용(Berkeley는 세 가지 형식 모두 제공, 아카이브), 이 단계에서는 관절별로 재확인만 수행; 자체 개발 모델: 변환 결과물과 패치 기록을 함께 버전 관리에 포함, M13에서 모델을 수정할 때 무엇을 변경했는지 알 수 있음.

## 단계 3: 액추에이터 모델링——제한값 부풀리기 = sim-to-real 자살 행위

【무엇을 할까】MJCF에서 각 제어 가능한 관절에 액추에이터 할당: 힘 제어는 `motor`, 위치 제어는 `position` 사용; 세 가지 규칙:

1. **토크 제한** = M01 사양표의 피크 토크(M10 단계 4에서 effort에 이미 기록, 변환 후 손실되지 않았는지 확인);
2. **속도 제한**은 M01 정격 속도 환산값 사용;
3. **액추에이터 동특성**은 1차 저역 통과 필터로 실제 응답 근사, 시정수는 먼저 5–20 ms로 추정(공학 권장값, [M14](m14-sim-to-real.md)에서 [시스템 식별](/entry/ent_method_system_identification/)로 측정하여 역입력).

```xml
<actuator>
  <!-- ctrlrange는 M01 사양표 피크 토크 입력, 절대 부풀리지 말 것 -->
  <position joint="l_knee_pitch" kp="40" forcerange="-33 33" ctrllimited="true" ctrlrange="-1.2 1.2"/>
  <!-- 1차 저역 통과 필터로 액추에이터 동특성 근사: dynprm은 시정수(초), 5–20 ms 공학 권장값 시작 -->
  <general joint="l_hip_pitch" dyntype="filter" dynprm="0.01" gaintype="fixed" gainprm="1" ctrllimited="true" ctrlrange="-20 20"/>
</actuator>
```

【왜 하는가】RL은 제한값 내의 동작을 학습합니다: 제한값을 부풀리면, 정책은 실제 기계가 실행할 수 없는 동작을 학습하게 되어 sim-to-real이 직접 실패합니다(M10 단계 4의 규칙). 실제 액추에이터는 이상적인 토크 소스가 아닙니다——전류 루프 응답과 통신 지연으로 인해 1차 관성 요소에 가깝습니다; 이 동특성을 모델링하지 않으면, 시뮬레이션에서 사용 가능한 게인이 실제 기계에서는 진동이 됩니다.

【상황 분석】버스 서보/QDD 준직구동: `position` + 토크 제한이 실제 기계 작동 방식에 가장 가깝습니다; 순수 힘 제어 계획: `motor` + 저역 통과 필터. 시정수를 모르겠다면 먼저 10 ms 정도로 시작하고, M14에서 다시 확인. PD 게인을 모델(kp/kv)에 쓸지, 컨트롤러 코드에 쓸지: 모델에 쓰면 컨트롤러를 바꿔도 재조정 불필요, 코드에 쓰면 온라인 튜닝에 용이——하나를 선택하고 전체적으로 통일.

## 4단계: 접촉 및 마찰 – 이족보행의 모든 것은 발바닥에서 일어난다

【수행할 작업】네 가지 동작:

1. **발바닥 마찰 계수**: 고무/PLA와 바닥의 크기는 먼저 0.6–1.0 범위로 시도(구체적인 값은 재료에 따라 직접 확인 필요);
2. **접촉 해석 파라미터**: `solref`(시간 상수, 감쇠비)로 접촉의 강성 조절 – 너무 부드러우면 발이 바닥에 파묻히고, 너무 딱딱하면 수치적 진동 발생; `solimp`는 구속 조건 임피던스 곡선을 제어하며, 먼저 기본값 근처 값 사용;
3. **자체 충돌 쌍 정리**: `exclude`를 사용하여 필요한 접촉 쌍만 남기고, 접촉 쌍의 수가 시뮬레이션 속도를 직접 결정;
4. **바닥 및 외란 인터페이스**: 바닥 geom을 파라미터화하고, 외부 힘 외란 입력 지점을预留 – M13의 [도메인 무작위화](/entry/ent_method_domain_randomization/)는 마찰을 무작위화하고 로봇을 밀어야 함.

```xml
<default>
  <!-- solref=(시간 상수, 감쇠비): 일반적으로 2–10×timestep, 작을수록 접촉이 더 딱딱함 -->
  <geom solref="0.01 1" solimp="0.9 0.95 0.001" friction="0.8 0.005 0.0001"/>
</default>
<contact><exclude body1="l_thigh" body2="l_shank"/></contact>  <!-- 충돌 가능성이 없는 링크 쌍 제외 -->
```

【이유】접촉 파라미터는 sim-to-real 격차의 주요 원인이며, 반드시 "발바닥 재료-바닥 재료" 쌍으로 보정하고 이후 도메인 무작위화 범위(23장 23.4.4절)에 포함시켜야 함. 먼저 명목 값을 합리적으로 조정한 후 무작위화를 논의.

【상황 분석 방법】마찰이 확실하지 않음: 발바닥 재료 샘플을 대상 바닥에 놓고 스프링 저울로 슬라이더를 당겨 크기를 추정. PLA로 출력한 발바닥과 고무 밑창은 차이가 크므로 다른 사람의 값을 그대로 사용하지 말 것.

## 5단계: 센서 시뮬레이션 및 관측 파이프라인

【수행할 작업】실기 BOM에 따라 관측 파이프라인 구축: [IMU](/entry/ent_component_imu_2024/)(자세/각속도 + 노이즈 모델), 관절 엔코더(위치/속도, 양자화 가능), 발바닥 접촉력; 주파수 계층 결정:

```xml
<sensor>
  <framequat objtype="site" objname="imu_site" noise="0.001"/>
  <gyro site="imu_site" noise="0.005"/>
  <jointpos joint="l_knee_pitch"/>  <jointvel joint="l_knee_pitch"/>
</sensor>
```

```python
# 물리 1 kHz, 제어 100 Hz (엔지니어링 권장값, 컨트롤러 대역폭 및 버스 속도에 따라 확인)
model.opt.timestep = 0.001   # 물리 스텝 크기
decimation = 10              # 물리 10 스텝마다 제어 1회 발행 → 100 Hz
```

**철칙: 관측 인터페이스는 실기 센서와 일대일 대응 – 실기에서 얻을 수 없는 관측은 정책에 입력하지 않음**(M13/M14의 공통 규율). 제어 주파수 기준점: ToddlerBot 전상태 피드백 50 Hz, Berkeley CAN 버스 250 Hz (각 조사 파일 참조).

【이유】관측은 sim-to-real에서 가장 쉽게 부정행위를 할 수 있는 부분: 시뮬레이션에서 쉽게 읽을 수 있는 실제 값(베이스 선속도, 질량 중심 위치)은 실기에는 존재하지 않음. 지금 실기 센서 목록에 따라 파이프라인을 구축하면 M13 훈련 시 재작업이 없음; 노이즈를 추가하는 것은 자신을 괴롭히는 것이 아니라 정책이 실제 센서에 미리 적응하도록 하는 것.

【상황 분석 방법】실기 센서가 아직 결정되지 않음: 먼저 [센서 선택 매뉴얼](../playbooks/sensor-selection.md)로 돌아가 BOM을 결정하고, 시뮬레이션 관측은 실기를 따르며, 반대로 하지 않음.

## 6단계: 기준 건강 검사 – M12의 입장권

【수행할 작업】네 가지 검사:

1. **제로 토크 해제**: 액추에이터를 끄고 자유 낙하/매달기 – 모델이 분해되지 않고, 관절에 댐핑이 있어 과도하게 흔들리지 않음;
2. **초기 keyframe**: 서 있는 자세에서 10초 동안 입력 없이 표류하지 않고, 질량 중심 투영이 지지 영역 내에 안정적으로 유지됨;
3. **접촉력 크기**: 서 있을 때 한 발의 법선 힘 ≈ 체중의 절반 정도, 너무 크거나 작지 않음;
4. **시뮬레이션 속도**: real-time factor(RTF) 기록, 목표 ≥ 1(RL 처리량은 별도 계산).

【이유】모델 수준 오류(관성 오류, 축 방향 반대, 리미트 누락)는 PD 서 있을 때 모두 드러나며, 수동 역학으로 확인하는 것이 가장 저렴함; RTF는 이후 MPC 실시간성과 RL 훈련 처리량의 상한선을 결정.

【상황 분석 방법】매달면 분해됨: 관성 또는 관절 정의 오류, M10 3단계로 돌아감; RTF < 0.5: 접촉 쌍 수, 충돌 메쉬 복잡도, 스텝 크기 확인, 무리하게 진행하지 말 것.

## 승인 기준

- [ ] 엔진 공식 예제 실행 성공(MuJoCo humanoid 또는 Isaac Lab H1), 화면 녹화/로그存档.
- [ ] 모델 로드 시 warning 없음; 관절별 구동 방향이 M10 규약과 일치하는지 재확인.
- [ ] 액추에이터 리미트(토크/속도/위치)가 M01 지표표와 항목별로 일치하며, 허위로 높은 값 없음.
- [ ] 제로 토크 매달기/자유 낙하 테스트 통과: 분해되지 않고, 댐핑 정상; keyframe 서 있는 자세 10초 표류 없음, 접촉력 크기 합리적.
- [ ] 관측 목록 문서화: 각 항목별 실기 출처(어떤 센서, 어떤 속도) 명시, 실기에서 얻을 수 없는 것은 "정책 입력 금지"로 표시.
- [ ] real-time factor 기록, 접촉 쌍 및 충돌체 정리 완료.

## 일반적인 문제 및 해결

| 증상 | 가능한 원인 | 해결 조치 |
|---|---|---|
| MJCF 컴파일 시 관성 텐서 양정부호 오류 | 수동 관성 행렬이 물리적 제약 조건을 만족하지 않음 | M10 3단계로 돌아가 CAD로 재추출; ixx/iyy/izz 삼각 부등식 확인 |
| 발이 바닥에 파묻히거나 빙판 위를 미끄러지는 듯한 현상 | solref 너무 부드러움 / 마찰 계수 너무 낮음 | 4단계로 돌아가 solref 시간 상수 및 friction 조정 |
| 시뮬레이션이 실시간보다 몇 배 느림 | 접촉 쌍 너무 많음 / 충돌 메쉬 너무 복잡함 | exclude로 접촉 쌍 정리; 충돌체는 M10 5단계로 돌아가 단순화 |
| 관절 운동 방향이 모두 반대 | 도/라디안 혼용 / 축 규약 차이 | compiler angle 확인; viewer에서 단일 관절별로 재확인 |
| URDF를 USD로 변환 후 리미트 누락 | Importer 옵션/버전 동작 차이 | 변환 후 항목별로 limit 확인, 누락 시 수동으로 추가(선택한 버전의 Importer 문서 확인) |

## 관련 자료

- 이전 작업: [M10 · URDF 모델링 및 내보내기](m10-urdf-modeling.md)
- 다음 작업: [M12 · 시뮬레이션 서기 및 걷기](m12-sim-walking.md)
- 이론 배경: [제22장 소프트웨어 미들웨어](/wiki/chapters/chapter-22/), [제23장 시뮬레이션 및 물리 엔진](/wiki/chapters/chapter-23/), [부록 C 소프트웨어 및 시뮬레이션 플랫폼 목록](/wiki/appendices/appendix-c/)
- [시뮬레이션 환경 구축 매뉴얼](../playbooks/sim-setup.md) · [2단계 개요](../stage-2-biped.md)
