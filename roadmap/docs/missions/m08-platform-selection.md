# M08 · 平台选型与采购：选对平台，成功一半

**全局位置**：这是 [阶段 2 双足平台](../stage-2-biped.md) 的第一个动手任务，承接 Stage 1 的关节级经验（M01–M07）。输入是 M01 的任务书与指标表 + 你的预算上限，输出是**一个选定的开源平台 + 一张核对过的 BOM 采购单**——下游 M09 整机装配直接按本任务的采购结果施工，选错平台的代价是数千美元与数月时间。

**前置条件**：[M01 · 需求场景数学化](m01-scenario-to-specs.md) 的指标表已填完；读过 [阶段 2 总览](../stage-2-biped.md) 的方案对比与决策树（本任务是它的手把手展开版）；预算有明确上限数字。

理论背景：[第 26 章 整机系统案例](/wiki/chapters/chapter-26/)、[第 4 章 执行器](/wiki/chapters/chapter-04/) 与 [第 7 章 供应商地图](/wiki/chapters/chapter-07/)。本页全部平台数据引自[公开调研档案](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/)（访问日期 2026-07-01），档案标"未知"的项如实保留。

## 步骤 1：候选平台全面对比

【做什么】把五个候选平台按十列指标过一遍，逐行核对（每个数字引自对应调研档案，未查到的标"未知"）：

| 平台 | 成本（BOM） | 身高/重量 | DoF | 执行器 | 主控 | 仿真栈 | 复刻难度 | 许可 | 文档完备度 |
|---|---|---|---|---|---|---|---|---|---|
| [ToddlerBot](/entry/ent_robot_system_toddlerbot/) | 约 $6,000（90% 花在电机与电脑） | 0.56 m / 3.4 kg | 30（臂 7×2、腿 6×2、颈 2、腰 2） | ROBOTIS Dynamixel 总线舵机 ×30（5 种型号） | Jetson Orin NX 16GB | MuJoCo/MJX + PPO | 低：纯 Python/pip 安装，无硬件经验者 3 天装完（论文验证） | 代码 MIT；设计文件非商业 CC | 文档站 + 装配手册/视频/治具齐全 |
| [Berkeley Humanoid Lite](/entry/ent_robot_system_berkeley_humanoid_lite/) | 美国 $4,312 / 中国 $3,236 | 0.8 m / 16 kg | 22（腿 6×2、臂 5×2） | 自研 6512/5010 准直驱 ×22（3D 打印摆线减速器） | Intel N95 迷你 PC（约 $129） | Isaac Lab（URDF/MJCF/USD 齐全） | 中：需自制 22 台执行器、焊 CAN、烧 FOC 固件 | 代码 MIT；CAD CC BY-SA 4.0 | GitBook + 技术报告完整 BOM |
| [Upkie](/entry/ent_robot_system_upkie/)（轮足） | 约 $3,000 + 60 小时打印 | 未知（因构型而异） | 6（每腿：髋、膝、轮） | mjbots qdd100 ×4 + moteus 驱动轮 | Raspberry Pi 4 + pi3hat | PyBullet（自带 PID/MPC/RL 三种平衡示例） | 低：轮足避开纯步行调参地狱 | Apache-2.0（轮胎网格 CC BY 4.0） | 逐步构建指南 + 活跃社区 |
| [BRUCE](/entry/ent_robot_system_bruce/) | 约 $6.5K（第三方论文口径，官方询价制） | 70 cm / 4.8 kg | 16（腿 5×2、臂 3×2） | Koala BEAR 准直驱（250 g、峰值 10.5 N·m、膝部液冷） | 6 TOPS 算力板 | 可变周期 MPC（模型被第三方论文当 benchmark） | 高：整机框架未公开，只能商务采购 | 组件级开源（PyBEAR 等），整机许可未能验证 | 面向专业用户，新手教程少 |
| [OpenLoong 青龙](/entry/ent_robot_system_openloong/) | 未知（公版机不自售） | 185 cm / 80 kg+ | 43（含五指灵巧手） | 旋转执行器为主（具体型号未知） | 400 TOPS 控制器 | MuJoCo 上 MPC+WBC 全栈开源（可零硬件学习） | 不适合个人复刻（机构级条件） | 代码 Apache-2.0；硬件许可标记 NOASSERTION | 中文工程文档，偏交付非教学 |

（数据来源：toddlerbot.md、berkeley-humanoid-lite.md、upkie.md、bruce-westwood.md、openloong-qinglong.md。）

【为什么】十列里真正决定成败的是四列：**成本**（能不能买得起）、**复刻难度**（能不能装得出来）、**执行器方案**（要不要碰烙铁与 FOC，物理背景见[准直驱执行器](/entry/ent_technology_quasi_direct_drive_actuator_2024/)卡片）、**仿真栈**（决定 M11–M13 顺不顺——[MuJoCo](/entry/ent_software_mujoco_physics_engine_2022/) 轻量免费，[Isaac Lab](/entry/ent_software_nvidia_isaac_lab_2024/) 需 NVIDIA 显卡）。BRUCE 与青龙放在表里是当参照系：一个告诉你"高动态要付出什么"，一个告诉你"全尺寸为什么不能在家复刻"。

【你的情况怎么分析】把上表抄进自己的对比表，加两列：**我的到手价**（含税含运）与**我的能力匹配度**。匹配度按执行器方案自评：没碰过焊接与固件烧录，"自研 QDD"一行直接标红；没有 NVIDIA 显卡，Isaac Lab 一栏直接标红。

## 步骤 2：决策树——预算 → 动手能力 → 目标

【做什么】三级决策，逐层收敛：

```
第 1 级（预算）：
  < $3.5k  → Upkie（约 $3,000，upkie.md），摔机代价最小，先学平衡控制
  $3.5–7k  → 进第 2 级
  机构级预算 → 才考虑 BRUCE（询价制）或成品整机 ROBOTIS OP3（$13,764.35，robotis-op3-darwin-op.md）
第 2 级（动手能力）：
  零基础/纯软件背景 → ToddlerBot：舵机总线免调 FOC，拧螺丝插线为主
  有 3D 打印 + 焊接 + 嵌入式经验 → Berkeley：中国口径 $3,236 拿到 22 DoF，代价是自造 22 台执行器
第 3 级（目标）：
  快速正反馈、学平衡控制/RL 部署 → Upkie
  行走 + loco-manipulation 数据采集 → ToddlerBot
  RL 运动控制研究 → Berkeley（Isaac Lab 管线现成）
  高动态（跑/跳）研究 → BRUCE（机构采购，软件授权需向供应商确认）
  全尺寸控制栈学习 → OpenLoong-Dyn-Control（MuJoCo 零硬件，不花钱买整机）
```

再用**五项自检清单**对号入座：

| 自检项 | 你的答案 | 指向 |
|---|---|---|
| 预算上限 | < $3.5k | Upkie |
| 预算上限 | $3.5–7k | ToddlerBot 或 Berkeley（按下四行分） |
| 每周可投入小时数 | < 5 h | ToddlerBot（文档最保姆）；Berkeley 打印约 1 周 + 组装约 3 天（berkeley-humanoid-lite.md） |
| 3D 打印机 | 无 | 在线打印服务补位；注意 Upkie 需 60+ 小时打印（upkie.md） |
| GPU | 无 NVIDIA 显卡 | MuJoCo 路线（ToddlerBot / OpenLoong 示例）；Isaac Lab 路线需 RTX 级显卡 |
| 烙铁经验 | 无 | 舵机总线平台（ToddlerBot）；Berkeley 要焊 CAN、烧固件 |

【为什么】第一台双足的核心 KPI 是"走起来"，不是一步到位。决策树的顺序有讲究：预算是硬约束先砍，动手能力是失败率主因其次，目标只在剩余选项里做排序——倒过来选（先看目标）的人，大多卡在"买得起装不出"。

【你的情况怎么分析】五项全打勾的那行就是你的平台；有两项以上不满足就降一档，不要硬上。尤其别把"顺便学焊接"当成选 Berkeley 的理由——学习成本会叠加在装配风险上，两台机器的教训（ToddlerBot 论文的可复现性实验、Berkeley 的新手友好度 3.5/5 自评）都指向同一结论：第一台选保守的。

## 步骤 3：许可与合规核查

【做什么】分清两种许可，逐平台核查（均引档案原文口径）：

- **代码许可 vs 设计文件许可**是两回事。[ToddlerBot](/entry/ent_robot_system_toddlerbot/)：代码与文档 MIT，设计文件（Onshape、STL）为**非商业** CC 许可（toddlerbot.md）——复刻自用没问题，卖整机/套件越界。
- [Berkeley Humanoid Lite](/entry/ent_robot_system_berkeley_humanoid_lite/)：代码 MIT，CAD 等资产 CC BY-SA 4.0（berkeley-humanoid-lite.md）——可改可商用，但要署名 + 衍生作品相同方式共享。
- [Upkie](/entry/ent_robot_system_upkie/)：Apache-2.0（upkie.md）；[ODRI Bolt](/entry/ent_robot_system_odri_bolt/)：BSD-3-Clause（open-dynamic-robot-initiative.md）——最宽松的一档。
- [InMoov](/entry/ent_robot_system_inmoov/)：打印件 CC BY-NC 3.0（非商业）（inmoov.md）；[Poppy Humanoid](/entry/ent_robot_system_poppy_humanoid/)：硬件 CC BY-SA 4.0、软件 GPLv3（poppy-humanoid.md）。
- [OpenLoong 青龙](/entry/ent_robot_system_openloong/)：代码 Apache-2.0，但硬件仓库许可证被 GitHub 标记为 NOASSERTION（条款不明确）（openloong-qinglong.md）——用其硬件图纸前先向社区问清。

【为什么】"开源"不等于"可商用"：NC（非商业）条款挡的是一切收费场景，SA（相同方式共享）要求你的改型继续开放，GPLv3 会传染到配套软件。有商用意图（哪怕只是接单帮人装）必须先把许可证读一遍；产品化路上的认证与合规框架见 [第 12 章 认证合规与质量标准](/wiki/chapters/chapter-12/)。

【你的情况怎么分析】纯学习自用：五个平台全绿灯；做课程/收费演示：避开 NC 条款（ToddlerBot 设计文件、InMoov）；计划产品化：优先 BSD/Apache 类（Upkie、ODRI）。核查结论写成一页文档存档——日期、许可证名称、你的用途、结论四行就够。

## 步骤 4：BOM 核对与下单

【做什么】从官方 BOM 逐项核对，建四列台账：**规格 / 数量 / 到手价（含税含运）/ 货期**。四条规则：

1. **钱花在刀刃认知**：电机与电脑占成本大头——ToddlerBot 的 BOM 约 90% 花在电机与电脑上（toddlerbot.md）；Berkeley 单台 6512 执行器 BOM $157（中国）–$188（美国），仅 10 台 6512 就是 $1,570–1,880（berkeley-humanoid-lite.md）。砍预算先砍对地方，别在紧固件上抠。
2. **缺货替代件校核流程**：列关键参数逐项对比——电机看 KV 值/尺寸/额定扭矩，舵机看扭矩/电压/通信协议，电池看串数/容量/放电倍率；任何一项对不上，标"**需自行向供应商确认**"，不许想当然下单。
3. **机电件与结构件分开下单**：电机/主控/电池货期长先锁单；打印件/轴承/紧固件可边看装配文档边补。
4. **总价 +15% 损耗余量**（M01 规则，工程建议值）：打印失败件、压坏的端子、摔坏的舵机都从这里出。

【为什么】BOM 是论文里的理想清单，你下单时一定有缺货与涨价；四列台账让"超支"在下单前暴露，而不是装到一半才发现。货期是第一隐性成本——THORMANG3 经销商口径交货期 12 周（thormang3.md），个人平台的热门电机缺货等一个月也常见。

【你的情况怎么分析】国内复刻 Berkeley 直接按技术报告的中国 BOM 口径（$3,236）采购（berkeley-humanoid-lite.md）；跨境件（Dynamixel、qdd100）把关税运费计入到手价。台账里任一货期 > 2 周的件，下单当天就锁，别等"想清楚再说"。

## 步骤 5：工具、耗材与场地准备

【做什么】

- **工具清单**：3D 打印机或在线打印服务（功能件材料/填充率与官方一致——Berkeley 摆线齿轮用普通桌面 FDM + PLA 即可，官方做过 60 小时耐久测试，berkeley-humanoid-lite.md；Upkie 需 60+ 小时打印，upkie.md）、恒温烙铁、万用表、压线钳、剥线钳、热熔胶枪、扭力螺丝刀；吊架预案（M09 首通电与站立行走验收都要用）。
- **耗材**：线材（硅胶线按电流选线径）、端子与接插件、轴承与紧固件包（M05 的规格经验直接复用）、热缩管、扎带、螺纹胶。小件宁多勿少。
- **工作场地与锂电存放**：独立工作台面；LiPo 用防爆袋/防火容器存放、充电有人值守，规范见[锂电池技术卡片](/entry/ent_tech_li_battery_humanoid/)——6S 4000 mAh 这类电池短路能量足以点燃桌面杂物（阶段 2 安全红线）。

【为什么】装配中断的头号原因不是技术，是"少一卷线、少一包端子"等三天快递；锂电存放是安全前置，不是锦上添花。

【你的情况怎么分析】没有打印机：先把打印文件发给在线打印服务打样一套（指定与官方一致的材料与填充率），比买打印机便宜；工具只买本任务用得上的，吊架先拿龙门架 + 绑带搭简易版。

## 验收标准

- [ ] 平台选定有书面理由：对照五步决策逐项打勾，能说清"为什么是它、为什么不是另外两个"。
- [ ] BOM 台账 100% 条目有货，或缺货替代件有参数对比记录（对不上项标"需自行向供应商确认"）。
- [ ] 总账 ≤ 预算上限，且含 +15% 损耗余量；电机与电脑成本占比已单独核算。
- [ ] 许可核查结论成文：代码许可与设计文件许可分别记录，商用意图有明确结论。
- [ ] 工具/耗材清单已清点，锂电存放容器到位。
- [ ] 关键长货期件已下单，到货计划与 M09 开工日期对齐。

## 常见坑与排查

| 症状 | 可能原因 | 排查动作 |
|---|---|---|
| 装到一半卡在缺件 | 低估货期，长货期件没先下单 | 台账按货期排序，> 2 周的当天锁定 |
| 替代电机装上带不动/烧板 | 替代件只对了价格没对参数 | 回步骤 4 做关键参数逐项对比；存疑标"需自行向供应商确认" |
| 反复补单端子/线材/轴承 | 只按 BOM 大件下单，漏了小件 | 按步骤 5 耗材清单一次性买齐，宁多勿少 |
| 准备商用被社区提醒侵权 | 只看了"开源"二字，没读许可证 | 回步骤 3：NC 条款平台不可商用；结论补写成文 |
| 选的平台装不下去 | 贪大求全，动手能力评估失真 | 回步骤 2 五项自检；两项不满足就降档 |
| 总账超预算 30%+ | 漏算关税/运费/损耗 | 到手价 = 含税含运；加 15% 余量后再对预算 |

## 配套阅读

- 上一任务：[M07 · 台架测试与验收](m07-bench-acceptance.md)
- 下一任务：[M09 · 整机装配、线束与电源](m09-mechanical-assembly.md)
- [阶段 2 总览](../stage-2-biped.md) · [计算平台选型手册](../playbooks/compute-selection.md)
- 理论背景：[第 7 章 供应商地图](/wiki/chapters/chapter-07/) 与 [附录 D 供应商名录](/wiki/appendices/appendix-d/)、[第 26 章 整机系统案例](/wiki/chapters/chapter-26/)、[第 12 章 认证合规与质量标准](/wiki/chapters/chapter-12/)
