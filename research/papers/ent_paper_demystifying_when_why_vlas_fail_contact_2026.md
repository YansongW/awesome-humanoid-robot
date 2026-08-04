---
$id: ent_paper_demystifying_when_why_vlas_fail_contact_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them
  zh: Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them
  ko: Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them
summary:
  en: We address the problem of understanding when and why Vision-Language-Action models struggle with contact-rich manipulation
    tasks that require precise physical interaction. Prior work has primarily focused on addressing contact failures through
    force-augmented architectures and training-time regularizers, yet the root causes of these failures remain underexplored.
    We identify two distinct failure.
  zh: 本文系统剖析了VLA模型在接触丰富操作中的失败根源，识别出精度失败（流匹配训练不匹配）与力失败（力信号结构未被有效利用）两种模式，并提出FACT方法：以Logit-Normal噪声调度修复精度问题，以时间感知力注入（接触状态、历史、门控）修复力感知问题。在Franka
    Research 3上的五个真实任务中，FACT将平均成功率从39.0%提升至66.0%，并验证了力注入机制真正利用了力信息（噪声替换消融显著下降）。
  ko: We address the problem of understanding when and why Vision-Language-Action models struggle with contact-rich manipulation
    tasks that require precise physical interaction. Prior work has primarily focused on addressing contact failures through
    force-augmented architectures and training-time regularizers, yet the root causes of these failures remain underexplored.
    We identify two distinct failure.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- demystifying
- when
- why
- vlas
- fail
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2608.01402 Demystifying When and Why VLAs Fail in Contact-Rich Tasks and How to Fix Them
  url: https://arxiv.org/abs/2608.01402
  date: '2026-08-02'
  accessed_at: '2026-08-05'
---

## 概述

本文系统剖析了VLA模型在接触丰富操作中的失败根源，识别出精度失败（流匹配训练不匹配）与力失败（力信号结构未被有效利用）两种模式，并提出FACT方法：以Logit-Normal噪声调度修复精度问题，以时间感知力注入（接触状态、历史、门控）修复力感知问题。在Franka Research 3上的五个真实任务中，FACT将平均成功率从39.0%提升至66.0%，并验证了力注入机制真正利用了力信息（噪声替换消融显著下降）。

## 它改变了什么

此前力增强VLA的工作（如ForceVLA、TA-VLA）多将力作为辅助输入或正则化信号，但从未系统回答“力信号在何时、为何未被利用”这一根本问题。本文的关键改变在于：将失败归因从“架构不够强”转向“训练信号分配不当”与“力信号结构未被匹配”两个可诊断的机制层面。这改变了社区对接触失败的理解——不是加更多力编码器就能解决，而是需要针对流匹配训练的时间步调度和力信号的时间结构做专门设计。尤其值得注意的是，噪声替换消融揭示ForceVLA和TA-VLA的增益主要来自正则化而非真正利用力信息，这一发现对后续工作具有方法论上的警示意义。

## 方法拆解

### 精度失败修复：Logit-Normal噪声调度
- 将π₀.₅默认的Beta噪声调度替换为Logit-Normal分布：\( f_{\mathcal{T}}(\tau) = \frac{1}{s\sqrt{2\pi}}\frac{1}{\tau(1-\tau)}\exp{\left(-\frac{\left(\text{logit}(\tau)+m\right)^{2}}{2s^{2}}\right)} \)
- 重参数化采样：\(\tau = \sigma(s\cdot z - m), z \sim \mathcal{N}(0,1)\)，位置参数\(m=1.5\)（而非\(m=0\)）将训练信号偏向低噪声（接触校正）区域
- 效果：LN在\(\tau < 0.2\)区域分配的梯度信号比Beta调度多**6×**，无需改架构、加数据或增参数

### 力失败修复：时间感知力注入
- **接触状态**：当前力读数\(\mathbf{f}_t \in \mathbb{R}^{H_w \times 6}\)（\(H_w=27\)，400Hz采样对应15Hz策略）均值池化为6维摘要\(\bar{f}_t\)，经两层MLP和投影生成逐层缩放调制\(\Delta\gamma(\bar{f}_t) = W_\gamma \phi_{\mathrm{force}}(\bar{f}_t) \in \mathbb{R}^d\)，加到每层AdaRMS缩放上：\( h_l = (\gamma_l(\tau) + \Delta\gamma(\bar{f}_t)) \cdot \mathrm{RMSNorm}(h_{l-1}) + \beta_l(\tau) + h_{l-1} g_l(\tau) \)
- **接触历史**：前\(H=30\)步（2秒）力/力矩读数由共享因果TCN（约0.2M参数，4个膨胀块，隐藏宽度64）独立编码，token前置到动作生成模块
- **接触门控**：梯度阈值\(\delta=0.5\)N，未检测到接触时阻断力编码组件梯度，防止拟合无信息的近零读数
- 总新增参数约2.2M，远低于ForceVLA的45M

### 控制器设计
- 双速率架构：15Hz策略更新与1kHz关节力矩控制解耦
- 策略输出笛卡尔末端位移\(\Delta x\in\mathbb{R}^3\)和角度位移\(\Delta\alpha\in\mathbb{R}^3\)
- 阻抗控制：\(a_u = a_{des} - k_p(x - x_{des}) - k_v(v - v_{des})\)，操作空间力矩：\(\tau_u = J^T(q)\cdot\Lambda(q)\cdot a_u\)

## 关键创新

1. **失败模式分解**：首次将VLA接触失败明确分为精度失败（训练信号分配）与力失败（感知结构不匹配），并分别给出针对性修复。这一诊断框架比“加力就完事”的朴素思路更具解释力和可迁移性。
2. **LN调度的理论动机**：将噪声调度从Beta换为Logit-Normal并偏移位置参数\(m=1.5\)，本质上是重新分配训练信号到接触校正最需要的低噪声区间。这是一个零成本、即插即用的修复，且实验证明在按钮按压上带来+45pp的提升（p<.001）。
3. **时间感知力注入+接触门控**：共享因果TCN编码2秒力历史、逐层AdaRMS调制、以及梯度门控防止无接触时力编码器退化——三者协同使FACT在噪声替换消融中显著下降（钥匙插入60%→5%，p<.001），证明真正利用了力信息，而对比方法ForceVLA和TA-VLA并未做到。

## 实验与结果

| 方法 | 插头插入 | USB插入 | 按钮按压 | 板擦除 | 钥匙插入 | 平均 |
|---|---|---|---|---|---|---|
| π₀.₅ | 30.0 | 37.5 | 12.5 | 100.0 | 15.0 | 39.0 |
| π₀.₅+LN | 50.0 | 47.5 | 57.5 | 87.5 | 37.5 | 56.0 |
| **FACT** | **57.5** | **47.5** | **75.0** | **90.0** | **60.0** | **66.0** |
| ForceVLA | 32.5 | 37.5 | 12.5 | 77.5 | 42.5 | 40.5 |
| TA-VLA | 30.0 | 25.0 | 20.0 | 97.5 | 15.0 | 37.5 |

- LN单独贡献：插头+20pp（p=.055）、按钮+45pp（p<.001）、钥匙+22.5pp（p=.020）
- 力注入额外贡献：按钮+17.5pp、钥匙+22.5pp（均p<.001）
- 消融显示力历史最重要（按钮-62.5pp、钥匙-40pp），瞬时读数在钥匙上-25pp，梯度门控在插头上-15pp
- 噪声替换消融：FACT在插头57.5→40.0、钥匙60.0→5.0、按钮75.0→17.5（均p<.001），确认真正利用力；ForceVLA仅钥匙显著（42.5→15.0），TA-VLA无显著依赖
- π₀骨干上FACT同样优于对比方法（插头70.0 vs ForceVLA 55.0 vs TA-VLA 30.0）
- 评估规模：每方法每任务40次rollout，总计近2,500次真实世界试验，Fisher精确检验

## 边界与局限

- 仅在单一平台（Franka Research 3）和腕装Bota SensONE传感器上验证，未测试其他运动学结构或传感器位置
- LN特定于流匹配动作头，不适用于自回归或扩散策略
- 时间感知力注入设计用于AdaRMS调制的transformer层，其他架构需重新适配
- 任务集仅五个场景，更广泛的几何/材料属性评估会增强普适性
- 插头插入和按钮按压上，FACT增益部分归因于额外输入的正则化（噪声替换无显著变化），说明力注入在这些任务上未完全发挥潜力
- 推理频率未明确提及（策略更新15Hz，但端到端延迟未报告）

## 工程启示

- **先核对噪声调度**：若你的VLA基于流匹配，检查是否使用Beta调度——换成Logit-Normal并设\(m=1.5\)是零成本的第一步，按钮类任务可能直接获得数十个百分点的提升
- **力编码器设计优先级**：消融显示力历史（2秒窗口）比瞬时读数更重要，且梯度门控（δ=0.5N）能防止无接触阶段力编码器退化——这两点应优先于更复杂的MoE或注意力机制
- **警惕“伪力利用”**：用噪声替换消融验证你的力编码器是否真正利用力信息——ForceVLA和TA-VLA的增益主要来自正则化，若你的方法在噪声替换下无显著下降，说明力通路形同虚设
- **参数效率**：FACT仅新增2.2M参数即达66.0%平均成功率，而ForceVLA的45M参数仅40.5%——力注入应轻量、因果、带门控，而非堆参数
- **复现要点**：F/T数据400Hz采样、27样本窗口（⌈400/15⌉）、one-euro filter预处理、双速率控制（15Hz策略/1kHz阻抗）——这些细节直接影响力信号质量，建议严格复现

## Overview
We address the problem of understanding when and why Vision-Language-Action models struggle with contact-rich manipulation tasks that require precise physical interaction. Prior work has primarily focused on addressing contact failures through force-augmented architectures and training-time regularizers, yet the root causes of these failures remain underexplored. We identify two distinct failure modes underlying this gap. Precision failures are rooted in a flow-matching policy training mismatch, and force failures arise from the distinctive structure of force signals. We address each failure mode with a targeted mechanism and combine them into FACT, which achieves 66% average success rate across five contact-rich tasks against 41% for the best prior baseline, in an evaluation spanning almost 2,500 real-world rollouts.

## 参考
- https://arxiv.org/abs/2608.01402

## 개요

본 논문은 VLA 모델이 접촉이 풍부한 조작에서 실패하는 근본 원인을 체계적으로 분석하여, 정밀도 실패(흐름 매칭 훈련 불일치)와 힘 실패(힘 신호 구조가 효과적으로 활용되지 않음)라는 두 가지 패턴을 식별하고, FACT 방법을 제안한다: Logit-Normal 노이즈 스케줄링으로 정밀도 문제를 수리하고, 시간 인지 힘 주입(접촉 상태, 이력, 게이팅)으로 힘 인지 문제를 수리한다. Franka Research 3에서의 다섯 가지 실제 작업에서 FACT는 평균 성공률을 39.0%에서 66.0%로 향상시켰으며, 힘 주입 메커니즘이 실제로 힘 정보를 활용함을 검증했다(노이즈 대체 소거 실험에서 유의미한 감소).

## 무엇을 바꾸었는가

이전의 힘 강화 VLA 연구(ForceVLA, TA-VLA 등)는 대부분 힘을 보조 입력 또는 정규화 신호로 사용했지만, "힘 신호가 언제, 왜 활용되지 않는가"라는 근본적인 질문에 체계적으로 답한 적은 없었다. 본 논문의 핵심 변화는 실패 원인을 "아키텍처가 충분히 강하지 않음"에서 "훈련 신호 할당 부적절"과 "힘 신호 구조 미일치"라는 두 가지 진단 가능한 메커니즘 수준으로 전환한 것이다. 이는 커뮤니티의 접촉 실패에 대한 이해를 바꾼다—더 많은 힘 인코더를 추가하는 것으로 해결되는 것이 아니라, 흐름 매칭 훈련의 시간 단계 스케줄링과 힘 신호의 시간 구조에 대한 전용 설계가 필요하다. 특히 주목할 점은 노이즈 대체 소거 실험이 ForceVLA와 TA-VLA의 이득이 주로 정규화에서 비롯되었지 실제 힘 정보 활용이 아님을 밝혀냈다는 것으로, 이 발견은 후속 연구에 방법론적 경고 의미를 지닌다.

## 방법 분해

### 정밀도 실패 수리: Logit-Normal 노이즈 스케줄링
- π₀.₅ 기본 Beta 노이즈 스케줄링을 Logit-Normal 분포로 대체: \( f_{\mathcal{T}}(\tau) = \frac{1}{s\sqrt{2\pi}}\frac{1}{\tau(1-\tau)}\exp{\left(-\frac{\left(\text{logit}(\tau)+m\right)^{2}}{2s^{2}}\right)} \)
- 재매개변수화 샘플링: \(\tau = \sigma(s\cdot z - m), z \sim \mathcal{N}(0,1)\), 위치 매개변수 \(m=1.5\)(\(m=0\) 대신)가 훈련 신호를 저노이즈(접촉 보정) 영역으로 편향시킴
- 효과: LN은 \(\tau < 0.2\) 영역에서 Beta 스케줄링보다 **6×** 더 많은 그래디언트 신호를 할당하며, 아키텍처 변경, 데이터 추가, 매개변수 증가 없이 가능

### 힘 실패 수리: 시간 인지 힘 주입
- **접촉 상태**: 현재 힘 판독값 \(\mathbf{f}_t \in \mathbb{R}^{H_w \times 6}\)(\(H_w=27\), 400Hz 샘플링이 15Hz 정책에 대응)을 평균 풀링하여 6차원 요약 \(\bar{f}_t\)로 축소, 2층 MLP와 프로젝션을 거쳐 층별 스케일링 변조 \(\Delta\gamma(\bar{f}_t) = W_\gamma \phi_{\mathrm{force}}(\bar{f}_t) \in \mathbb{R}^d\) 생성, 각 층 AdaRMS 스케일링에 추가: \( h_l = (\gamma_l(\tau) + \Delta\gamma(\bar{f}_t)) \cdot \mathrm{RMSNorm}(h_{l-1}) + \beta_l(\tau) + h_{l-1} g_l(\tau) \)
- **접촉 이력**: 이전 \(H=30\) 스텝(2초) 힘/토크 판독값을 공유 인과 TCN(약 0.2M 매개변수, 4개 팽창 블록, 은닉 너비 64)으로 독립 인코딩, 토큰을 동작 생성 모듈에 앞서 배치
- **접촉 게이팅**: 그래디언트 임계값 \(\delta=0.5\)N, 접촉 미감지 시 힘 인코딩 구성 요소의 그래디언트 차단, 무정보성의 0에 가까운 판독값 과적합 방지
- 총 신규 매개변수 약 2.2M, ForceVLA의 45M보다 훨씬 적음

### 컨트롤러 설계
- 이중 속도 아키텍처: 15Hz 정책 업데이트와 1kHz 관절 토크 제어 분리
- 정책 출력: 데카르트 끝단 변위 \(\Delta x\in\mathbb{R}^3\) 및 각도 변위 \(\Delta\alpha\in\mathbb{R}^3\)
- 임피던스 제어: \(a_u = a_{des} - k_p(x - x_{des}) - k_v(v - v_{des})\), 작업 공간 토크: \(\tau_u = J^T(q)\cdot\Lambda(q)\cdot a_u\)

## 핵심 혁신

1. **실패 모드 분해**: VLA 접촉 실패를 정밀도 실패(훈련 신호 할당)와 힘 실패(인지 구조 불일치)로 명확히 구분하고, 각각에 대한 맞춤형 수리를 제시한 최초의 연구. 이 진단 프레임워크는 "힘을 추가하면 끝"이라는 단순한 접근보다 설명력과 이식성이 뛰어나다.
2. **LN 스케줄링의 이론적 동기**: 노이즈 스케줄링을 Beta에서 Logit-Normal로 교체하고 위치 매개변수 \(m=1.5\)로 이동시키는 것은 본질적으로 훈련 신호를 접촉 보정이 가장 필요한 저노이즈 구간에 재할당하는 것이다. 이는 비용 제로, 플러그 앤 플레이 수리이며, 실험에서 버튼 누름에 +45pp 향상(p<.001)을 입증했다.
3. **시간 인지 힘 주입 + 접촉 게이팅**: 공유 인과 TCN의 2초 힘 이력 인코딩, 층별 AdaRMS 변조, 그리고 무접촉 시 힘 인코더 퇴화를 방지하는 그래디언트 게이팅—세 가지가 협력하여 FACT가 노이즈 대체 소거에서 유의미한 감소(키 삽입 60%→5%, p<.001)를 보여, 실제로 힘 정보를 활용함을 증명하며, 비교 방법인 ForceVLA와 TA-VLA는 그렇지 않았다.

## 실험 및 결과

| 방법 | 플러그 삽입 | USB 삽입 | 버튼 누름 | 보드 지우기 | 키 삽입 | 평균 |
|---|---|---|---|---|---|---|
| π₀.₅ | 30.0 | 37.5 | 12.5 | 100.0 | 15.0 | 39.0 |
| π₀.₅+LN | 50.0 | 47.5 | 57.5 | 87.5 | 37.5 | 56.0 |
| **FACT** | **57.5** | **47.5** | **75.0** | **90.0** | **60.0** | **66.0** |
| ForceVLA | 32.5 | 37.5 | 12.5 | 77.5 | 42.5 | 40.5 |
| TA-VLA | 30.0 | 25.0 | 20.0 | 97.5 | 15.0 | 37.5 |

- LN 단독 기여: 플러그 +20pp(p=.055), 버튼 +45pp(p<.001), 키 +22.5pp(p=.020)
- 힘 주입 추가 기여: 버튼 +17.5pp, 키 +22.5pp(모두 p<.001)
- 소거 실험에서 힘 이력이 가장 중요(버튼 -62.5pp, 키 -40pp), 순간 판독값은 키에서 -25pp, 그래디언트 게이팅은 플러그에서 -15pp
- 노이즈 대체 소거: FACT는 플러그 57.5→40.0, 키 60.0→5.0, 버튼 75.0→17.5(모두 p<.001), 실제 힘 활용 확인; ForceVLA는 키만 유의미(42.5→15.0), TA-VLA는 유의미한 의존성 없음
- π₀ 백본에서도 FACT가 비교 방법보다 우수(플러그 70.0 vs ForceVLA 55.0 vs TA-VLA 30.0)
- 평가 규모: 방법당 작업당 40회 롤아웃, 총 약 2,500회 실제 세계 실험, Fisher 정확 검정

## 경계 및 한계

- 단일 플랫폼(Franka Research 3)과 손목 장착 Bota SensONE 센서에서만 검증, 다른 운동학 구조나 센서 위치는 테스트되지 않음
- LN은 흐름 매칭 동작 헤드에 특화, 자기회귀 또는 확산 정책에는 적용 불가
- 시간 인지 힘 주입은 AdaRMS 변조를 사용하는 transformer 층용으로 설계, 다른 아키텍처는 재적응 필요
- 작업 세트는 5개 시나리오에 불과, 더 넓은 기하/재료 속성 평가가 일반화를 강화할 것
- 플러그 삽입과 버튼 누름에서 FACT 이득은 일부 추가 입력의 정규화(노이즈 대체 시 유의미한 변화 없음)에 기인, 힘 주입이 이 작업들에서 완전한 잠재력을 발휘하지 못함을 시사
- 추론 빈도가 명시적으로 언급되지 않음(정책 업데이트 15Hz, 그러나 종단 간 지연 시간은 보고되지 않음)

## 공학적 시사점

- **먼저 노이즈 스케줄링 확인**: VLA가 흐름 매칭 기반이라면 Beta 스케줄링을 사용하는지 확인—Logit-Normal로 교체하고 \(m=1.5\)로 설정하는 것은 비용 제로의 첫 단계이며, 버튼류 작업에서 수십 퍼센트 포인트 향상을 직접 얻을 수 있음
- **힘 인코더 설계 우선순위**: 소거 실험에서 힘 이력(2초 창)이 순간 판독값보다 중요하며, 그래디언트 게이팅(δ=0.5N)이 무접촉 단계에서 힘 인코더 퇴화를 방지—이 두 가지가 더 복잡한 MoE나 어텐션 메커니즘보다 우선해야 함
- **"가짜 힘 활용" 경계**: 노이즈 대체 소거로 힘 인코더가 실제로 힘 정보를 활용하는지 검증—ForceVLA와 TA-VLA의 이득은 주로 정규화에서 비롯, 노이즈 대체 시 유의미한 감소가 없다면 힘 경로가 무의미함을 의미
- **매개변수 효율성**: FACT는 단 2.2M 매개변수 추가로 66.0% 평균 성공률을 달성, 반면 ForceVLA의 45M 매개변수는 40.5%에 불과—힘 주입은 가볍고, 인과적이며, 게이팅이 있어야 하며, 매개변수를 쌓는 것이 아님
- **재현 핵심 사항**: F/T 데이터 400Hz 샘플링, 27개 샘플 창(⌈400/15⌉), one-euro filter 전처리, 이중 속도 제어(15Hz 정책/1kHz 임피던스)—이러한 세부 사항이 힘 신호 품질에 직접 영향을 미치므로 엄격한 재현을 권장
