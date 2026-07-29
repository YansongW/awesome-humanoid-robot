# Computing Platform Selection: Installing a "Layered Brain" for Your Robot

When building a humanoid robot, many people's first question is "Should I buy a Jetson or a NUC?" This is the wrong first question. The correct first question is: What types of computing tasks will your robot actually run, and what are the latency deadlines and failure consequences for each? The essence of platform selection is not comparing which board has higher TOPS, but rather layering the tasks and then assigning just enough computing power to each layer — too much wastes battery and budget, too little can cause gait instability at best or an immediate fall at worst. This page follows a four-step approach: Layering → Platform Selection → Real-time Solution Determination → Edge-side VLA Inference Evaluation. For theoretical background, see [Chapter 6: Computing, Power, and Thermal Management](/wiki/chapters/chapter-06/) and [Chapter 22: Software Middleware](/wiki/chapters/chapter-22/).

## Step 1: Divide Computing Requirements into Three Layers

**【What to do】** Take a piece of paper, list all the computing tasks in your plan, and categorize them into three layers based on "control cycle × failure consequence":

- **L0 Bottom Real-time Layer**: Joint servo loops, force control, safety monitoring. Joint current loops, force control, and balance control typically require a hard real-time cycle of 0.5–2 ms (see [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7), and exceeding this leads to instability. Safety-related functions (emergency stop, watchdog, overcurrent/overtemperature monitoring) must be placed on an independent [Safety MCU (Safety Microcontroller Unit)](/entry/ent_component_safety_mcu/) — it can cut power even when the main computing unit crashes.
- **L1 Middle Planning Layer**: State estimation, gait generation, MPC (Model Predictive Control), Whole-Body Control (WBC). Typical frequency is 50–500 Hz, allowing microsecond to millisecond jitter, but requiring stable average throughput.
- **L2 Upper Intelligence Layer**: Visual perception, SLAM, speech, VLA (Vision-Language-Action) model inference. A frequency of 1–30 Hz is sufficient; a larger single-frame delay only means "slower reaction," not an immediate fall.

**【Why】** The constraints of the three layers are completely different: L0 requires **determinism**, not computing power; L2 requires **peak throughput** (TOPS) and memory bandwidth, and does not need real-time guarantees at all. Using a non-real-time x86 host to directly run 1 kHz force control is like entrusting the robot's balance to the operating system's scheduling luck; conversely, paying for unused TOPS directly eats into the battery budget — ToddlerBot's endurance test lasted only 19 minutes during on-board inference "until thermal throttling" (source: [ToddlerBot Project Page](https://toddlerbot.github.io/)). The deep principle behind layering is the trend of heterogeneous computing: future main controllers will be heterogeneous combinations of CPU + GPU + NPU + functional safety MCU (see the trend summary in the [Safety MCU](/entry/ent_component_safety_mcu/) card).

**【How to analyze your situation】** The key depends on your actuator solution:

- **Using Dynamixel bus servos** (position loop in the servo firmware): L0 is already outsourced; the main controller only needs to send position commands at tens of Hz. ToddlerBot uses an off-the-shelf communication board to achieve 50 Hz feedback for all 30 motors at 2 Mbps baud rate (source: [ToddlerBot Paper](https://arxiv.org/html/2502.00893v2)). In this case, you almost don't need to buy dedicated hardware for the L0 layer.
- **Using self-developed Quasi-Direct Drive (QDD) actuators**: The current/torque loop is on the driver board, but the upper-layer force control loop still requires 250 Hz–1 kHz. Berkeley Humanoid Lite's approach is to use one CAN 2.0 bus (1 Mbps) per limb, communicating with actuators and IMU at 250 Hz (source: [Berkeley Humanoid Lite Paper](https://arxiv.org/html/2504.17249v1)), and a main controller running real-time Linux is sufficient.
- **Building a full-size model or requiring functional safety certification**: The safety MCU layer cannot be omitted, and functional safety standards such as ISO 13849, IEC 61508 must be considered (source: [Safety MCU](/entry/ent_component_safety_mcu/) card).

## Step 2: Candidate Platform Comparison and Real-World Cases

**【What to Do】** Based on the tiered results from Step 1, select the main controller for the L1+L2 layers (usually combined or split into two) from the four candidate categories below:

| Platform | AI Compute | Power Consumption | Price | Ecosystem | Real-Time Positioning |
|---|---|---|---|---|---|
| [NVIDIA Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) 64GB | Up to 275 TOPS (INT8) | 15–60 W configurable | Developer kit approx. 1,999 USD (third-party reference price) | Unified ecosystem with JetPack / Isaac ROS / Isaac Sim, 16-channel MIPI CSI-2 | Soft real-time (with PREEMPT_RT), covers L1+L2 |
| Jetson Orin NX 16GB | Up to 157 TOPS | 10–40 W | Requires confirmation from supplier | Same ecosystem as AGX Orin, smaller form factor | Soft real-time, primarily L2 with L1 support |
| [NVIDIA Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) | Blackwell architecture, designed for edge VLA/VLM; specific TOPS requires confirmation from supplier | 75–120 W class (source: [Safety MCU](/entry/ent_component_safety_mcu/) card) | Requires confirmation from supplier | Flagship ecosystem for "Physical AI" | Dedicated to L2; L0/L1 require separate configuration |
| Intel N95 Mini PC | No dedicated NPU, AI compute mainly via CPU/integrated GPU (specific TOPS requires confirmation from supplier) | Low-power x86 (specific TDP requires confirmation from supplier) | Approx. 129 USD (source: [EECS-2025-207 Technical Report BOM](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/Archive/EECS-2025-207.pdf)) | Standard x86 Linux/ROS ecosystem | Soft real-time, sufficient for L1, L2 limited to small models |
| Intel NUC (Core i3 class) | Same as above | Same as above | Full system price, requires confirmation from supplier | Mature ROS/ROS2 ecosystem | Soft real-time, teaching/development oriented |
| Raspberry Pi 4 | No AI accelerator, CPU only | Single-board low power (specific value requires confirmation from supplier) | Requires confirmation from supplier | Large community ecosystem, Python-friendly | Soft real-time, only for L1 lightweight control |

(Orin series compute/power/price sources: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) card and its competitive comparison table.)

Now look at how five real open-source projects made their choices (all sources from [public research archive](https://github.com/YansongW/awesome-humanoid-robot/tree/main/data/roadmap/research/)):

- **ToddlerBot (Stanford) → Jetson Orin NX 16GB**: To run a 300M parameter diffusion policy (approx. 100 ms inference latency) and 10 Hz stereo depth estimation onboard, an onboard GPU is necessary; Orin NX is the balance point between performance and size.
- **Berkeley Humanoid Lite → Intel N95 Mini PC (approx. $129)**: The RL walking policy network is very small; the N95 is sufficient for running both low-level control and policy deployment, allowing the entire budget to be allocated to 22 actuators.
- **Upkie → Raspberry Pi 4 + mjbots pi3hat (CAN expansion board)**: The PID/MPC/RL examples for wheel-legged balance control are all small models; the Raspberry Pi + CAN expansion board is the most hassle-free combination.
- **ROBOTIS OP3 → Intel NUC (Core i3 dual-core, 8GB DDR4, 250GB M.2 SSD) + OpenCR sub-controller**: A typical dual-board setup with L1/L2 on the x86 host and L0 on the microcontroller.
- **OpenLoong Qinglong → 400 TOPS high-compute controller + EtherCAT bus**: A full-size 43-DOF open-standard robot; upper-layer large model scheduling requires high compute power (as announced at 2024 WAIC; the primary source page could not be directly verified, so cite with caution).

**【Why】** The pattern is clear: **The "dumber" the actuators (servos) and the smaller the policy, the cheaper the main controller; Jetson only comes into play when running large models onboard.** The core selling point of the Orin series is not the TOPS number itself, but the "unified ecosystem"—JetPack SDK, Isaac ROS, and Isaac Sim allow policies trained in simulation to be deployed almost identically on the robot (source: [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/) card). The [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) goes a step further: the Blackwell architecture is specifically designed for running multimodal generative AI and VLA policies at the edge, but its 75–120 W power consumption means it's not a simple "board upgrade"—it's a generation of platform that requires redesigning the cooling, battery, and structure accordingly.

**【How to Analyze Your Situation】** Choose one of three based on budget and goals:

- **Budget < $500, goal is RL walking**: Copy the BHL recipe (N95-class mini PC), spending the money on actuators. The prerequisite is that your policy network is small (MLP-level) and vision requirements are low.
- **Budget $1,000–$2,000, need onboard perception/diffusion policy/VLA**: Orin NX or AGX Orin. First, calculate VRAM: model parameter count × quantization precision + activations. 16GB can fit a 300M-parameter diffusion policy (proven by ToddlerBot); larger VLA models require the 64GB version.
- **Targeting next-generation edge large models**: Keep an eye on Thor, but treat cooling (75–120 W class enters the realm of liquid cooling/phase change discussion, source: [Safety MCU](/entry/ent_component_safety_mcu/) card) and battery capacity as upfront design constraints, rather than figuring it out after purchase.

## Step 3: Determine the Real-Time Solution

**【What to Do】** Choose a real-time path for the L0/L1 layers. There are four mainstream options:

1.  **[Linux RT-PREEMPT](/entry/ent_software_rt_preempt_linux/)** : Apply real-time patches to mainline Linux, making most kernel code preemptible and interrupt threads threaded, providing scheduling latency in the tens of microseconds (Source: [QNX](/entry/ent_software_qnx/) card comparison section). Retains the full Linux ecosystem and is the default choice for individuals and labs. After patching, you must use `cyclictest` to measure the maximum latency under real load (see [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7).
2.  **[EtherCAT](/entry/ent_technology_ethercat_2024/) Master** : Real-time capability is pushed down to the bus. EtherCAT's "processing on the fly" allows slaves to read/write instantly as frames pass through. Combined with Distributed Clocks, it provides a unified time base for all joints (Source: EtherCAT card). The main controller runs PREEMPT_RT + the EtherCAT master protocol stack to drive a 1 ms joint loop. OpenLoong Qinglong uses the EtherCAT bus (Source: [OpenLoong-Dyn-Control](https://github.com/loongOpen/OpenLoong-Dyn-Control/blob/main/README-zh.md)).
3.  **Dual Kernel/Hard RTOS** : Xenomai runs an independent real-time core alongside Linux, achieving scheduling latency as low as microseconds but with complex configuration and maintenance; [QNX](/entry/ent_software_qnx/) is a commercial microkernel RTOS where the file system and network stack run as user-space services. It is widely used in automotive and medical fields, offering complete reliability and certification systems but requires a license fee (Source: QNX card).
4.  **MCU Hard Real-Time** : Offload current loops and safety logic entirely to a microcontroller (e.g., OP3's OpenCR sub-controller, Source: [ROBOTIS OP3 e-Manual](https://emanual.robotis.com/docs/en/platform/op3/introduction/)), leaving only soft real-time tasks for the main controller. Resource-constrained nodes can use open-source RTOS like Zephyr (Source: QNX card).

**【Why】** The kernel critical sections in standard Linux can cause high-priority tasks to wait for unpredictable durations. Jitter of tens to hundreds of microseconds is fatal for a 1 ms control loop (see [Chapter 6](/wiki/chapters/chapter-06/) Section 6.4.7 for details). Choosing a real-time solution essentially decides "where to place determinism": in the kernel (PREEMPT_RT), on the bus (EtherCAT), in a dedicated OS (QNX), or on a dedicated chip (MCU).

**【How to Analyze Your Situation】** Decision sequence:

*   Servo solution → No real-time patches needed; just get the robot running first.
*   Custom QDD + CAN bus (BHL route) → PREEMPT_RT is sufficient, low cost, abundant resources.
*   Custom QDD + High multi-joint synchronization requirements (>20 joints, 1 ms loop) → EtherCAT master. High initial investment, but this is an industry-proven path.
*   Future automotive/medical-grade certification → Start learning QNX concepts now, but no need to pay for it during the personal prototyping stage.

## Step 4: Evaluate On-Device VLA Inference Requirements

**【What to Do】** If your roadmap includes "robots understanding commands and working autonomously," you need a dedicated compute budget for [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/): list the target VLA model's parameter count, quantization scheme (INT8/FP16), required action output frequency, and back-calculate VRAM and TOPS requirements. See [Chapter 19](/wiki/chapters/chapter-19/) for VLA theory background.

**【Why】** Running VLA on-device instead of in the cloud is driven by three hard constraints: **Latency** (action commands cannot tolerate network round trips), **Connectivity** (the robot shouldn't become a brick without Wi-Fi), and **Privacy** (home scene images should not leave the premises) (Source: [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card). However, the cost of on-device deployment is that the model must fit into limited VRAM and power budgets, requiring compression techniques like quantization, pruning, and distillation (Source: [Safety MCU](/entry/ent_component_safety_mcu/) card trends section). An existing empirical anchor: A 300M parameter diffusion policy on Orin NX 16GB has ~100 ms latency (Source: [ToddlerBot paper](https://arxiv.org/html/2502.00893v2)) — 100 ms is usable for manipulation tasks but must be left to smaller L1 layer models for dynamic balance.

**【How to Analyze Your Situation】** Honestly answer three questions: How large is your VLA model (consider Orin NX/AGX Orin for <1B, look at Thor level or accept cloud-hybrid architecture for larger)? How high is the action output frequency requirement (5–10 Hz is usually sufficient for manipulation tasks; whole-body dynamic control cannot rely on direct VLA output)? What capabilities must the robot retain when offline (at least an on-device small policy for safety)? VLA inference performance is strongly correlated with the model and quantization configuration. For specific latency data, refer to benchmark papers like VLA-Perf (Source: [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card) and test on your target hardware.

## Acceptance Criteria

*   You have a task layering table: Each computing task is annotated with its target frequency, tolerable latency, and failure consequence. L0 tasks have independent fallback paths (safety MCU or drive local loop).
*   The main controller selection has a documented rationale: You can explain "why this board" and have at least one open-source project of a similar scale as a reference (e.g., "I chose N95 level for RL walking + small policy, referencing BHL").
*   If following the real-time Linux route: You have run `cyclictest` on the target hardware, recorded the maximum scheduling latency under idle and stressed loads, and ensured at least one order of magnitude margin over the control loop period.
*   If planning VLA: You have written down the target model's parameter count, quantization scheme, expected VRAM usage, and confirmed the selected platform's VRAM capacity has at least 30% headroom.
*   Power and thermal calculations are complete: The main controller's full-load power consumption (e.g., AGX Orin 60 W, Thor 75–120 W class) has been factored into the total system power budget and thermal design.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Robot is stable in simulation but shakes on the real robot | Control loop period not met, scheduling latency jitter | Use `cyclictest` to measure max latency; check if PREEMPT_RT patch is applied, CPU isolation and memory locking are configured |
| Performance drops sharply after a few minutes of inference | Thermal throttling (ToddlerBot measured throttling after 19 minutes, Source: its research archive) | Monitor chip temperature and frequency curve; improve airflow/add heat spreader; lower power mode and recalibrate |
| EtherCAT occasional frame loss, joint errors | Master scheduling timeout or DC sync not configured | Check Working Counter return values; confirm Distributed Clocks are enabled; run master on PREEMPT_RT + dedicated CPU core |
| VLA model doesn't fit in VRAM or inference is extremely slow | Model too large, not quantized | Quantize to INT8/FP16 first, then test; compare calculated VRAM requirements with platform specs; consider action chunking to reduce inference frequency |
| Occasional latency spikes in ROS nodes on NUC/Mini PC | Standard kernel scheduling jitter + USB device interrupt contention | Apply real-time patches; bind IRQ affinity to non-real-time cores; move CAN/IMU USB adapters to a separate USB controller |
| Robot loses control and falls after main controller crash | Missing independent safety layer | Add a safety MCU watchdog and emergency stop circuit so that drives automatically disable when the main controller loses power |

## Companion Reading

*   [Stage 2 · Biped Platform](../stage-2-biped.md) — Deployment of the main controller platform in walking control
*   [Stage 3 · Full Humanoid](../stage-3-humanoid.md) — Layered computing and on-device VLA inference
*   [Roadmap Overview](../index.md)
