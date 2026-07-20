# Computing Platform Selection: Equipping a Robot with a "Layered Brain"

> ⚠️ This roadmap content is compiled based on public information and theoretical knowledge, and has not been verified on actual hardware; please verify safety specifications yourself when involving electrical and mechanical operations.

When many people build a humanoid robot, their first question is "Should I buy a Jetson or a NUC?" This is the wrong first question. The correct first question is: What types of computing tasks will your robot actually run, and what are the latency limits and failure consequences for each? The essence of platform selection is not comparing which board has higher TOPS, but rather layering the tasks and then allocating just enough computing power for each layer—too much wastes battery and budget, too little can cause gait instability at best or an immediate fall at worst. This page follows four steps: Layering → Platform Selection → Determining Real-Time Solutions → Evaluating On-Device VLA Inference. For theoretical background, see [Chapter 6: Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/) and [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/).

## Step 1: Divide Computing Demands into Three Layers

**【What to Do】** Take a piece of paper, list all the computing tasks in your plan, and categorize them into three layers based on "control cycle × failure consequence":

- **L0 Bottom Real-Time Layer**: Joint servo loops, force control, safety monitoring. Joint current loops, force control, and balance control typically require a hard real-time cycle of 0.5–2 ms (see [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7); timeout leads to instability. Safety-related functions (emergency stop, watchdog, overcurrent/overtemperature monitoring) must be placed on an independent [Safety MCU (Safety Microcontroller Unit)](/entry/ent_component_safety_mcu/) separate from the main controller—it can cut power even when the main computing unit crashes.
- **L1 Middle Planning Layer**: State estimation, gait generation, MPC (Model Predictive Control), Whole-Body Control (WBC). Typical frequency is 50–500 Hz, allowing microsecond to millisecond jitter, but requiring stable average throughput.
- **L2 Top Intelligence Layer**: Visual perception, SLAM, voice, VLA (Vision-Language-Action) model inference. A frequency of 1–30 Hz is sufficient; a slightly higher single-frame latency only results in "slower reaction" and will not directly cause a fall.

**【Why】** The constraints for the three layers are completely different: L0 requires **determinism**, not computing power; L2 requires **peak throughput** (TOPS) and memory bandwidth, and precisely does not need real-time guarantees. Running a 1 kHz force control loop directly on an x86 host that does not guarantee real-time performance is equivalent to entrusting the robot's balance to the operating system's scheduling luck. Conversely, paying for unused TOPS directly eats into the battery budget—ToddlerBot's endurance test lasted only 19 minutes during on-device inference until "overheating and throttling" (source: data/roadmap/research/toddlerbot.md). The underlying principle of layering is the trend toward heterogeneous computing: future main controllers will be a heterogeneous combination of CPU + GPU + NPU + functional safety MCU (see the trend summary in the [Safety MCU](/entry/ent_component_safety_mcu/) card).

**【How to Analyze Your Situation】** The key depends on your actuator solution:

- Using **Dynamixel bus servos** (position loop in the servo firmware): L0 is already outsourced; the main controller only needs to send position commands at tens of Hz. ToddlerBot uses an off-the-shelf communication board to achieve 50 Hz feedback for all 30 motors at 2 Mbps baud rate (source: data/roadmap/research/toddlerbot.md). In this case, you almost don't need dedicated hardware for the L0 layer.
- Using **self-developed Quasi-Direct Drive (QDD) actuators**: The current/torque loop is on the driver board, but the upper-level force control loop still requires 250 Hz–1 kHz. The Berkeley Humanoid Lite approach uses one CAN 2.0 bus (1 Mbps) per limb, with actuators and IMU communicating at 250 Hz (source: data/roadmap/research/berkeley-humanoid-lite.md); the main controller running a real-time Linux is sufficient.
- Building a **full-size model or requiring functional safety certification**: The safety MCU layer cannot be omitted, and functional safety standards such as ISO 13849, IEC 61508 must be considered (source: [Safety MCU](/entry/ent_component_safety_mcu/) card).

## Step 2: Candidate Platform Comparison and Real-World Cases

**【What to Do】** Based on the layered results from Step 1, select the main controller for the L1+L2 layers (usually combined or split into two) from the four candidate categories below:

| Platform | AI Compute | Power Consumption | Price | Ecosystem | Real-time Positioning |
|---|---|---|---|---|---|
| [NVIDIA Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) 64GB | Up to 275 TOPS (INT8) | 15–60 W configurable | Developer kit approx. 1,999 USD (third-party reference price) | Unified ecosystem: JetPack / Isaac ROS / Isaac Sim, 16-channel MIPI CSI-2 | Soft real-time (with PREEMPT_RT), handles L1+L2 |
| Jetson Orin NX 16GB | Up to 157 TOPS | 10–40 W | Must confirm with supplier | Same ecosystem as AGX Orin, smaller form factor | Soft real-time, primarily L2, also handles L1 |
| [NVIDIA Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) | Blackwell architecture, designed for edge VLA/VLM; specific TOPS must be confirmed with supplier | 75–120 W class (source: [Safety MCU](/entry/ent_component_safety_mcu/) card) | Must confirm with supplier | Flagship ecosystem for "Physical AI" | Dedicated to L2; L0/L1 require separate configuration |
| Intel N95 Mini PC | No dedicated NPU, AI compute primarily via CPU/integrated GPU (specific TOPS must be confirmed with supplier) | Low-power x86 (specific TDP must be confirmed with supplier) | Approx. 129 USD (source: data/roadmap/research/berkeley-humanoid-lite.md) | Standard x86 Linux/ROS ecosystem | Soft real-time, sufficient for L1, L2 limited to small models |
| Intel NUC (Core i3 class) | Same as above | Same as above | Full system price, must confirm with supplier | Mature ROS/ROS2 ecosystem | Soft real-time, teaching/development oriented |
| Raspberry Pi 4 | No AI accelerator, CPU only | Single-board low power (specific value must be confirmed with supplier) | Must confirm with supplier | Large community ecosystem, Python-friendly | Soft real-time, only for L1 lightweight control |

(Orin series compute/power/price sources: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) card and its competitive comparison table.)

Now, look at how five real open-source projects made their choices (all sources from data/roadmap/research/ survey files):

- **ToddlerBot (Stanford) → Jetson Orin NX 16GB**: To run a 300M parameter diffusion policy (approx. 100 ms inference latency) and 10 Hz stereo depth estimation on-board, an on-board GPU is necessary. Orin NX is the balance point between performance and size.
- **Berkeley Humanoid Lite → Intel N95 Mini PC (approx. $129)**: The RL walking policy network is very small; the N95 is sufficient to run both low-level control and the policy, allocating the entire budget to 22 actuators.
- **Upkie → Raspberry Pi 4 + mjbots pi3hat (CAN expansion board)**: The PID/MPC/RL examples for wheel-legged balance control are all small models. Raspberry Pi + CAN expansion board is the most hassle-free combination.
- **ROBOTIS OP3 → Intel NUC (Core i3 dual-core, 8GB DDR4, 250GB M.2 SSD) + OpenCR sub-controller**: A typical dual-board division where L1/L2 run on the x86 host and L0 runs on the microcontroller.
- **OpenLoong Qinglong → 400 TOPS high-compute controller + EtherCAT bus**: A full-size 43-DOF reference platform. The upper-layer large model scheduling requires high compute power (announced at WAIC 2024; the primary page could not be directly verified, cite with caution).

**【Why】** The pattern is clear: **The "dumber" the actuator (servo) and the smaller the policy, the cheaper the main controller; only when running large models on-board does the Jetson come into play.** The core selling point of the Orin series is not the TOPS number itself, but the "unified ecosystem"—JetPack SDK, Isaac ROS, and Isaac Sim allow policies trained in simulation to be deployed almost identically on the robot (source: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) card). The [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) goes a step further: its Blackwell architecture is specifically designed for running multimodal generative AI and VLA policies on-device, but its 75–120 W class power consumption means it's not a simple "board upgrade"; it's a platform generation requiring redesign of cooling, battery, and structure.

**【How to Analyze Your Situation】** Choose one of three based on budget and goals:

- **Budget < $500, Goal: RL walking**: Copy the BHL recipe (N95-class mini PC), spend the money on actuators. Prerequisite: your policy network is small (MLP-level) and vision requirements are low.
- **Budget $1,000–$2,000, Goal: On-board perception/diffusion policy/VLA**: Orin NX or AGX Orin. First, calculate VRAM: model parameters × quantization precision + activations. 16GB can fit a 300M parameter diffusion policy (proven by ToddlerBot); larger VLA models require the 64GB version.
- **Aiming for next-generation edge large models**: Focus on Thor, but treat cooling (75–120 W class enters the discussion range for liquid cooling/phase change, source: [Safety MCU](/entry/ent_component_safety_mcu/) card) and battery capacity as upfront design constraints, not problems to solve after purchase.

## Step 3: Determine the Real-time Solution

**【What to Do】** Choose a real-time path for the L0/L1 layers. There are four mainstream options:

1. **[Linux RT-PREEMPT](/entry/ent_software_rt_preempt_linux/)**: Apply real-time patches to mainline Linux, making most kernel code preemptible and interrupt threads threaded, providing tens of microseconds scheduling latency (source: [QNX](/entry/ent_software_qnx/) card comparison section). Retains the full Linux ecosystem; it's the default choice for individuals and labs. After patching, you must use `cyclictest` to measure maximum latency under real load (method in [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7).
2. **[EtherCAT](/entry/ent_technology_ethercat_2024/) Master**: Real-time capability is pushed down to the bus. EtherCAT's "processing on the fly" allows slaves to read/write instantly as frames pass, and Distributed Clocks give all joints a shared time base (source: EtherCAT card). The main controller runs PREEMPT_RT + EtherCAT master protocol stack to drive 1 ms joint loops. OpenLoong Qinglong uses the EtherCAT bus (source: data/roadmap/research/openloong-qinglong.md).
3. **Dual-kernel/Hard RTOS**: Xenomai runs an independent real-time core alongside Linux, achieving microsecond-level scheduling latency but with complex configuration and maintenance; [QNX](/entry/ent_software_qnx/) is a commercial microkernel RTOS where the filesystem and network stack run as user-space services, widely used in automotive and medical fields with complete reliability and certification systems, but requires licensing fees (source: QNX card).
4. **MCU Hard Real-time**: Offload current loops and safety logic entirely to a microcontroller (e.g., OP3's OpenCR sub-controller, source: data/roadmap/research/robotis-op3-darwin-op.md), leaving the main controller for soft real-time tasks. Resource-constrained nodes can use open-source RTOS like Zephyr (source: QNX card).

**【Why】** Standard Linux kernel critical sections can cause unpredictable delays for high-priority tasks. Jitter of tens to hundreds of microseconds is fatal for a 1 ms control loop (principle detailed in [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7). The choice of real-time solution essentially answers "where to place determinism": in the kernel (PREEMPT_RT), in the bus (EtherCAT), in a dedicated OS (QNX), or in a dedicated chip (MCU).

**【How to Analyze Your Situation】** Decision order:

- Servo solution → You can skip any real-time patches and just get the robot running first.
- Custom QDD + CAN bus (BHL route) → PREEMPT_RT is sufficient, low cost, abundant resources.
- Custom QDD + high multi-joint synchronization requirements (>20 joints, 1 ms loop) → EtherCAT master. Higher initial investment, but this is the industry-proven path.
- Future automotive/medical grade certification → Start learning about QNX concepts now, but no need to pay for licensing during the personal prototype stage.

## Step 4: Evaluate On-Device VLA Inference Requirements

**【What to Do】** If your roadmap states "robots understand commands and work autonomously," you must create a dedicated compute budget for [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/): list the target VLA model's parameter count, quantization scheme (INT8/FP16), required action output frequency, and back-calculate VRAM and TOPS requirements. For VLA theoretical background, see [Chapter 19](/wiki/chapters/chapter-19/).

**【Why】** Placing VLA on-device rather than in the cloud is driven by three hard constraints: **latency** (action commands cannot tolerate network round trips), **connectivity** (robots must not become bricks without Wi-Fi), and **privacy** (home scene images should not leave the premises) (source: [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card). However, the cost of on-device deployment is that the model must fit within limited VRAM and power budgets, requiring compression techniques such as quantization, pruning, and distillation (source: [Safety MCU](/entry/ent_component_safety_mcu/) card trend section). Existing empirical anchor: a 300M parameter diffusion policy achieves approximately 100 ms latency on Orin NX 16GB (source: data/roadmap/research/toddlerbot.md) — 100 ms is acceptable for manipulation tasks, but for dynamic balancing, it must be left to L1 layer small models.

**【How to Analyze Your Situation】** Honestly answer three questions: How large is your VLA model (below 1B parameters, consider Orin NX/AGX Orin; larger, directly look at Thor-class or accept a cloud-hybrid architecture)? What is the required action output frequency (5–10 Hz is typically sufficient for manipulation tasks; whole-body dynamic control cannot rely on direct VLA output)? What capabilities must the robot retain when offline (at least onboard safety small policies)? VLA inference performance is strongly correlated with model and quantization configuration; for specific latency data, refer to benchmark papers like VLA-Perf (source: [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card) and test on target hardware.

## Acceptance Criteria

- You have a task layering table: each computing task is annotated with target frequency, tolerable latency, failure consequences, and all L0 tasks have independent fallback paths (safety MCU or drive local loop).
- Main controller selection has documented rationale: you can state "why this board" and compare with at least one open-source project of similar scale (e.g., "I do RL walking + small policy, choose N95-class, referencing BHL").
- If following the real-time Linux route: you have run `cyclictest` on target hardware, recording maximum scheduling latency under idle and stressed loads, with at least one order of magnitude margin relative to the control loop period.
- If planning VLA: you have written down the target model's parameter count, quantization scheme, expected VRAM usage, and confirmed that the selected platform's VRAM capacity has at least 30% headroom.
- Power and thermal calculations completed: main controller full-load power (e.g., AGX Orin 60 W, Thor 75–120 W class) has been accounted for in the total system power budget and thermal design.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Robot stable in simulation but shakes on real hardware | Control loop period not met, scheduling latency jitter | `cyclictest` to measure maximum latency; check if PREEMPT_RT patch is applied, CPU isolation and memory locking are configured |
| Performance drops sharply after a few minutes of inference | Overheating throttling (ToddlerBot measured throttling after 19 minutes, source: its research archive) | Monitor chip temperature and frequency curves; improve airflow/add heat spreader; lower power mode and recalibrate |
| EtherCAT occasional frame loss, joint errors | Master scheduling timeout or DC synchronization not configured | Check Working Counter return values; confirm distributed clock is enabled; run master with PREEMPT_RT + dedicated CPU core |
| VLA model cannot fit in VRAM or inference extremely slow | Model too large, not quantized | Quantize to INT8/FP16 first, then test; compare VRAM requirements with platform specs; consider action chunking to reduce inference frequency |
| Occasional latency spikes in ROS nodes on NUC/mini PC | Standard kernel scheduling jitter + USB device interrupt contention | Apply real-time patch; bind IRQ affinity to non-real-time cores; move CAN/IMU USB adapters to a separate USB controller |
| Robot loses control and falls after main controller crash | Missing independent safety layer | Add safety MCU watchdog and emergency stop circuit, ensuring drives automatically disable when main controller loses power |

## Companion Reading

- [Stage 2 · Biped Platform](../stage-2-biped.md) — Main controller platform deployment in walking control
- [Stage 3 · Full Humanoid](../stage-3-humanoid.md) — Layered compute and on-device VLA inference
- [Roadmap Overview](../index.md)
