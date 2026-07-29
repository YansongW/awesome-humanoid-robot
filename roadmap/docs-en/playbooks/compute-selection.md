# Computing Platform Selection: Installing a "Layered Brain" for Your Robot

When many people start building a humanoid robot, their first question is "Should I buy a Jetson or a NUC?" This is the wrong first question. The correct first question is: What types of computing tasks will your robot actually run, and what are the latency deadlines and failure consequences for each? The essence of platform selection is not comparing which board has higher TOPS, but rather layering the tasks and then equipping each layer with just the right amount of computing power—too much wastes battery and budget, too little can cause gait instability at best or an immediate fall at worst. This page follows a four-step approach: Layering → Platform Selection → Real-time Solution Determination → On-device VLA Inference Evaluation. For theoretical background, see [Chapter 6: Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/) and [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/).

## Step 1: Divide Computing Requirements into Three Layers

**【What to Do】** Take a piece of paper, list all the computing tasks in your plan, and categorize them into three layers based on "control cycle × failure consequences":

- **L0 Low-level Real-time Layer**: Joint servo loops, force control, safety monitoring. Joint current loops, force control, and balance control typically require a hard real-time cycle of 0.5–2 ms (see [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7); exceeding this leads to instability. Safety-related functions (emergency stop, watchdog, overcurrent/overtemperature monitoring) must be placed on an independent [Safety MCU (Safety Microcontroller Unit)](/entry/ent_component_safety_mcu/)—it can cut power even when the main computing unit crashes.
- **L1 Mid-level Planning Layer**: State estimation, gait generation, MPC (Model Predictive Control), Whole-Body Control (WBC). Typical frequency is 50–500 Hz, allowing microsecond to millisecond jitter, but requiring stable average throughput.
- **L2 High-level Intelligence Layer**: Visual perception, SLAM, speech, VLA (Vision-Language-Action) model inference. A frequency of 1–30 Hz is sufficient; a larger single-frame delay only means "slower reaction" and will not directly cause a fall.

**【Why】** The constraints of the three layers are completely different: L0 requires **determinism**, not raw computing power; L2 requires **peak throughput** (TOPS) and memory bandwidth, and does not need real-time guarantees. Using a non-real-time x86 host to directly run 1 kHz force control is like entrusting the robot's balance to the operating system's scheduling luck. Conversely, paying for unused TOPS directly eats into the battery budget—ToddlerBot's endurance test showed it only lasted 19 minutes before "overheating and throttling" during on-device inference (source: data/roadmap/research/toddlerbot.md). The deep principle behind layering is the trend toward heterogeneous computing: future main controllers will be a heterogeneous combination of CPU + GPU + NPU + functional safety MCU (see the trend summary in the [Safety MCU](/entry/ent_component_safety_mcu/) card).

**【How to Analyze Your Situation】** The key depends on your actuator solution:

- **Using Dynamixel bus servos** (position loop in the servo firmware): L0 is already outsourced; the main controller only needs to send position commands at tens of Hz. ToddlerBot uses an off-the-shelf communication board to achieve 50 Hz feedback for all 30 motors at 2 Mbps baud rate (source: data/roadmap/research/toddlerbot.md). In this case, you can almost skip dedicated hardware for the L0 layer.
- **Using self-developed Quasi-Direct Drive (QDD) actuators**: The current/torque loop is on the driver board, but the upper-level force control loop still requires 250 Hz–1 kHz. Berkeley Humanoid Lite's approach is to use one CAN 2.0 bus per limb (1 Mbps), with actuators and IMU communicating at 250 Hz (source: data/roadmap/research/berkeley-humanoid-lite.md); a main controller running real-time Linux is sufficient.
- **Building a full-size model or requiring functional safety certification**: The safety MCU layer cannot be omitted, and functional safety standards such as ISO 13849, IEC 61508 must be considered (source: [Safety MCU](/entry/ent_component_safety_mcu/) card).

## Step 2: Candidate Platform Comparison and Real-World Cases

**【What to Do】** Based on the hierarchical results from Step 1, select the main controller for the L1+L2 layers (usually combined or split into two) from the following four categories of candidates:

| Platform | AI Compute | Power Consumption | Price | Ecosystem | Real-Time Positioning |
|---|---|---|---|---|---|
| [NVIDIA Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) 64GB | Up to 275 TOPS (INT8) | 15–60 W configurable | Developer kit approx. 1,999 USD (third-party reference price) | Unified ecosystem with JetPack / Isaac ROS / Isaac Sim, 16-channel MIPI CSI-2 | Soft real-time (with PREEMPT_RT), handles L1+L2 |
| Jetson Orin NX 16GB | Up to 157 TOPS | 10–40 W | Must confirm with supplier | Same ecosystem as AGX Orin, smaller form factor | Soft real-time, primarily L2, also handles L1 |
| [NVIDIA Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) | Blackwell architecture, designed for edge VLA/VLM; specific TOPS must be confirmed with supplier | 75–120 W class (source: [Safety MCU](/entry/ent_component_safety_mcu/) card) | Must confirm with supplier | Flagship ecosystem for "Physical AI" | Dedicated to L2, L0/L1 require separate configuration |
| Intel N95 Mini PC | No dedicated NPU, AI compute primarily via CPU/integrated graphics (specific TOPS must be confirmed with supplier) | Low-power x86 (specific TDP must be confirmed with supplier) | Approx. 129 USD (source: data/roadmap/research/berkeley-humanoid-lite.md) | Standard x86 Linux/ROS ecosystem | Soft real-time, sufficient for L1, L2 only runs small models |
| Intel NUC (Core i3 class) | Same as above | Same as above | Full system price, must confirm with supplier | Mature ROS/ROS2 ecosystem | Soft real-time, teaching/development positioning |
| Raspberry Pi 4 | No AI accelerator, only CPU | Single-board low power (specific value must be confirmed with supplier) | Must confirm with supplier | Large community ecosystem, Python-friendly | Soft real-time, only for L1 lightweight control |

(Orin series compute/power/price sources: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) card and its competitive comparison table.)

Now look at how five real open-source projects chose (all sources from data/roadmap/research/ survey files):

- **ToddlerBot (Stanford) → Jetson Orin NX 16GB**: To run a 300M parameter diffusion policy (approx. 100 ms inference latency) and 10 Hz stereo depth estimation on board, an onboard GPU is necessary. Orin NX is the balance point between performance and size.
- **Berkeley Humanoid Lite → Intel N95 Mini PC (approx. $129)**: The RL walking policy network is very small. The N95 is sufficient for running both low-level control and policy deployment, allocating the entire budget to 22 actuators.
- **Upkie → Raspberry Pi 4 + mjbots pi3hat (CAN expansion board)**: The PID/MPC/RL examples for wheeled-legged balance control are all small models. Raspberry Pi + CAN expansion board is the most hassle-free combination.
- **ROBOTIS OP3 → Intel NUC (Core i3 dual-core, 8GB DDR4, 250GB M.2 SSD) + OpenCR sub-controller**: A typical dual-board division where L1/L2 runs on the x86 host and L0 runs on the microcontroller.
- **OpenLoong Qinglong → 400 TOPS high-compute controller + EtherCAT bus**: A full-size 43-DOF reference platform. The upper-layer large model scheduling requires high compute power (announced at 2024 WAIC; the primary page could not be directly verified, cite with caution).

**【Why】** The pattern is clear: **The "dumber" the actuators (servos) and the smaller the policy, the cheaper the main controller; only when running large models on board does Jetson come into play.** The core selling point of the Orin series is not the TOPS number itself, but the "unified ecosystem"—JetPack SDK, Isaac ROS, and Isaac Sim allow policies trained in simulation to be deployed almost identically on the robot (source: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) card). The [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) goes a step further: the Blackwell architecture is specifically designed for running multimodal generative AI and VLA policies on the device, but the 75–120 W class power consumption means it's not simply a "board upgrade"; it's a generation of platform requiring redesign of cooling, battery, and structure.

**【How to Analyze Your Situation】** Choose one of three based on budget and goals:

- **Budget < $500, Goal: RL Walking**: Copy the BHL recipe (N95-class mini PC), spend money on actuators. Prerequisite: your policy network is small (MLP-class) and vision requirements are low.
- **Budget $1,000–2,000, Need Onboard Perception/Diffusion Policy/VLA**: Orin NX or AGX Orin. First, calculate VRAM: model parameter count × quantization precision + activations. 16GB can fit a 300M parameter diffusion policy (ToddlerBot empirical evidence); larger VLA models require the 64GB version.
- **Aiming for Next-Gen Edge Large Models**: Focus on Thor, but treat cooling (75–120 W class enters liquid cooling/phase change discussion territory, source: [Safety MCU](/entry/ent_component_safety_mcu/) card) and battery capacity as upfront design constraints, not something to figure out after purchase.

## Step 3: Determine the Real-Time Solution

**【What to Do】** Choose a real-time path for the L0/L1 layers. There are four mainstream options:

1. **[Linux RT-PREEMPT](/entry/ent_software_rt_preempt_linux/)**: Apply a real-time patch to mainline Linux, making most kernel code preemptible and interrupt threads, providing tens of microseconds scheduling latency (source: [QNX](/entry/ent_software_qnx/) card comparison section). Retains the full Linux ecosystem, the default choice for individuals and labs. After patching, you must use `cyclictest` to measure maximum latency under real load (method in [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7).
2. **[EtherCAT](/entry/ent_technology_ethercat_2024/) Master**: Real-time capability is pushed down to the bus. EtherCAT's "processing on the fly" allows slaves to read/write instantly as frames pass through. Combined with Distributed Clocks, all joints share a unified time base (source: EtherCAT card). The main controller running PREEMPT_RT + EtherCAT master protocol stack can drive a 1 ms joint loop. OpenLoong Qinglong uses the EtherCAT bus (source: data/roadmap/research/openloong-qinglong.md).
3. **Dual Kernel/Hard RTOS**: Xenomai runs an independent real-time core alongside Linux, achieving scheduling latency as low as microseconds but with complex configuration and maintenance; [QNX](/entry/ent_software_qnx/) is a commercial microkernel RTOS where the file system and network stack run as user-space services, widely used in automotive and medical fields with complete reliability and certification systems, but requires licensing fees (source: QNX card).
4. **MCU Hard Real-Time**: Completely delegate current loops and safety logic to a microcontroller (e.g., OP3's OpenCR sub-controller, source: data/roadmap/research/robotis-op3-darwin-op.md), leaving only soft real-time tasks for the main controller. For resource-constrained nodes, open-source RTOS like Zephyr can be used (source: QNX card).

**【Why】** The kernel critical sections of standard Linux can cause high-priority tasks to wait for unpredictable times. Jitter of tens to hundreds of microseconds is fatal for a 1 ms control loop (see [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7 for details). The choice of real-time solution essentially answers "where to place determinism": in the kernel (PREEMPT_RT), in the bus (EtherCAT), in a dedicated OS (QNX), or in a dedicated chip (MCU).

**【How to Analyze Your Situation】** Decision order:

- Servo solution → You can skip any real-time patches; just get the robot running first.
- Custom QDD + CAN bus (BHL route) → PREEMPT_RT is sufficient, low cost, abundant resources.
- Custom QDD + High multi-joint synchronization requirements (>20 joints, 1 ms loop) → EtherCAT master. High initial investment, but this is an industry-validated path.
- Future automotive/medical grade certification required → Start learning about QNX concepts now, but no need to pay for licensing during the personal prototype stage.

## Step 4: Evaluate On-Device VLA Inference Requirements

**【What to Do】** If your roadmap says "the robot understands commands and works autonomously," you need to create a dedicated compute budget for [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/): list the target VLA model's parameter count, quantization scheme (INT8/FP16), required action output frequency, and then back-calculate the VRAM and TOPS requirements. For VLA theoretical background, see [Chapter 19](/wiki/chapters/chapter-19/).

**【Why】** Putting VLA on the device rather than in the cloud is driven by three hard constraints: **latency** (action commands cannot tolerate network round trips), **connectivity** (the robot must not become a brick without Wi-Fi), and **privacy** (images from home environments should not leave the premises) (source: [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card). However, the cost of on-device deployment is that the model must fit within limited VRAM and power budgets, requiring compression techniques such as quantization, pruning, and distillation (source: [Safety MCU](/entry/ent_component_safety_mcu/) card trend section). Existing empirical anchor: a 300M parameter diffusion policy achieves approximately 100 ms latency on Orin NX 16GB (source: data/roadmap/research/toddlerbot.md) — 100 ms is usable for manipulation tasks, but for dynamic balancing, it must be left to L1 layer small models.

**【How to Analyze Your Situation】** Honestly answer three questions: How large is your VLA model (below 1B can consider Orin NX/AGX Orin; larger models should directly look at Thor level or accept a cloud-hybrid architecture)? How high is the required action output frequency (5–10 Hz is usually sufficient for manipulation tasks; whole-body dynamic control should not rely on direct VLA output)? What capabilities must the robot retain when offline (at least a small on-device safety policy)? VLA inference performance is strongly correlated with the model and quantization configuration; for specific latency data, refer to benchmark papers like VLA-Perf (source: [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card) and test on the target hardware.

## Acceptance Criteria

- You have a task hierarchy table: each compute task is annotated with target frequency, tolerable latency, failure consequences, and all L0 tasks have independent fallback paths (safety MCU or local drive loop).
- The main controller selection has a documented rationale: you can explain "why this board" and use at least one open-source project of similar scale as a reference (e.g., "I do RL walking + small policies, choose N95 level, referencing BHL").
- If following the real-time Linux route: you have run `cyclictest` on the target hardware, recorded the maximum scheduling latency under idle and stressed loads, and ensured at least one order of magnitude margin relative to the control loop cycle.
- If planning VLA: you have written down the target model's parameter count, quantization scheme, expected VRAM usage, and confirmed that the selected platform's VRAM capacity has at least 30% headroom.
- Power and thermal calculations are complete: the main controller's full-load power consumption (e.g., AGX Orin 60 W, Thor 75–120 W level) has been included in the overall power budget and thermal design.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Robot is stable in simulation but shakes on real hardware | Control loop cycle not meeting target, scheduling latency jitter | Use `cyclictest` to measure maximum latency; check if PREEMPT_RT patch is applied, CPU isolation and memory locking are configured |
| Performance drops sharply after a few minutes of inference | Overheating causing frequency throttling (ToddlerBot measured throttling after 19 minutes, source: its research archive) | Monitor chip temperature and frequency curves; improve airflow/add heat spreader; lower power mode and recalibrate |
| EtherCAT occasional frame loss, joint errors | Master scheduling timeout or DC synchronization not configured | Check Working Counter return values; confirm distributed clock is enabled; run the master with PREEMPT_RT + dedicated CPU core |
| VLA model cannot fit into VRAM or inference is extremely slow | Model too large, not quantized | First quantize to INT8/FP16 and retest; compare VRAM requirements with platform specifications; consider action chunking to reduce inference frequency |
| Occasional latency spikes in ROS nodes on NUC/mini PC | Standard kernel scheduling jitter + USB device interrupt contention | Apply real-time patches; bind IRQ affinity to non-real-time cores; move CAN/IMU USB adapters to a separate USB controller |
| Robot loses control and falls after main controller crash | Missing independent safety layer | Add safety MCU watchdog and emergency stop circuit, ensuring drives automatically disable when the main controller loses power |

## Companion Reading

- [Stage 2 · Biped Platform](../stage-2-biped.md) — Deployment of main controller platform in walking control
- [Stage 3 · Full Humanoid](../stage-3-humanoid.md) — Hierarchical compute and on-device VLA inference
- [Roadmap Overview](../index.md)
