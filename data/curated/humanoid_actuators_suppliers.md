# 人形机器人执行器/关节/供应商数据收集策略

## 数据来源

1. **整机厂官方规格页**
   - Unitree: https://www.unitree.com/products/h1, /g1
   - Tesla Optimus: https://www.tesla.com/optimus
   - Figure AI: https://www.figure.ai/
   - Agility Robotics: https://www.agilityrobotics.com/
   - Boston Dynamics Atlas: https://bostondynamics.com/atlas
   - 1X Technologies: https://www.1x.tech/
   - Apptronik: https://www.apptronik.com/
   - Fourier Intelligence: https://www.fourierintelligence.com/
   - UBTECH: https://www.ubtrobot.com/
   - AgiBot: https://www.agibot.com/

2. **核心零部件供应商**
   - 减速器：Harmonic Drive, Nabtesco, Leaderdrive, Wittenstein, Bonfiglioli
   - 电机：Maxon, Kollmorgen, Moog, Inovance, Mingzhi
   - 执行器总成：Sanhua, Tuopu, CubeMars, ZeroErr, Techrobots

3. **拆解与行业报告**
   - iFixit / TechInsights teardowns
   - 券商研报（雪球、搜狐、微信公众号）
   - 展会资料（CES, Automate, ICRA, IROS）

## 扩展计划

- 继续补充电机、编码器、力传感器、丝杠供应商
- 为每个整机产品补充关节数量、扭矩、减速器类型、电机类型
- 建立 `component_manufacturer` → `component` → `robot_system` 的关系链
