# M18 · Imitation Learning Training and Deployment: 50 Demonstrations Yield a Cup-Grasping Policy

**Global Position**: After the M17 teleoperation dataset is built and before M19 end-to-end task integration. Input is ≥50 demonstration episodes collected under a unified protocol (multi-view images + joint states + actions + timestamps, Stage 3 criteria), output is a **grasping policy with ≥70% success rate under a fixed real-robot protocol** (weights + model card + measured deployment latency), which M19 integrates as a "grasping skill" into the end-to-end task chain.

**Prerequisites**: [M17 · Teleoperation and Data Collection](m17-teleop-data.md) completed (episode format frozen, training/validation split done, data quality spot checks passed); perception calibration meets standards (Stage 3 criteria: cup 3D positioning error ≤1 cm); a GPU capable of training vision policies (VRAM requirements verified against the chosen official repository documentation).

Theoretical background: [Behavior Cloning](/entry/ent_method_behavior_cloning/), [ACT](/entry/ent_method_action_chunking_transformer/), [Diffusion Policy](/entry/ent_method_diffusion_policy/) are the three core cards for this task; systematic discussion is in [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/), data format and ecosystem in [Chapter 21 Data Infrastructure](/wiki/chapters/chapter-21/) and [Appendix B Datasets](/wiki/appendices/appendix-b/).

## Step 1: Baseline First—Run the Training Pipeline with Behavior Cloning

【What to do】First, use the simplest [Behavior Cloning](/entry/ent_method_behavior_cloning/) (BC) to run through the complete pipeline: data loading → image + state encoding → per-frame action regression → training → validation loss → **open-loop playback evaluation** (plot the model's predicted action sequence against the ground truth on the same graph, comparing joint by joint). Keep the configuration simple: lightweight visual backbone + regression head. The goal is to get the pipeline running, not to achieve high metrics.

【Why】BC has two irreplaceable values. First, **pipeline validation**: any bug in data loading, temporal alignment, normalization, or evaluation scripts is cheapest to expose with BC—if you go straight to ACT and something goes wrong, you won't know if the method or the pipeline is at fault. Second, **baseline**: BC's numbers are the foundation for all subsequent methods. How much better ACT/Diffusion Policy is than BC must be evaluated on the same data and with the same protocol. BC's theoretical weakness is compounding error: during per-frame regression, small errors at each frame push the robot out of the training distribution, and errors accumulate like a snowball—this is exactly what the next two steps aim to suppress, see [Chapter 18](/wiki/chapters/chapter-18/).

【How to analyze your situation】If BC validation loss decreases but open-loop playback clearly deviates: first check temporal alignment (a 1–2 frame misalignment between image frames and action frames is the most common hidden issue in collected data), then check if action normalization is reversed. BC's real-robot success rate is usually low, so don't dwell on it—once the pipeline works and numbers are recorded, move to Step 2.

## Step 2: ACT—Action Chunking to Suppress Compounding Error

【What to do】Switch to [ACT (Action Chunking Transformer)](/entry/ent_method_action_chunking_transformer/): the model predicts an action chunk of ~100 steps at once, and during execution, temporal ensemble applies weighted smoothing to overlapping chunks. Training configuration **starts with the official repository defaults** (learning rate, epochs, chunk length, backbone all left unchanged); if M17 data is organized according to the [ALOHA](/entry/ent_technology_aloha_teleoperation_system_2023/) data format, its data pipeline can be reused directly. During training, monitor the validation curve: if training loss decreases while validation loss increases, it's overfitting—stop early.

【Why】Action chunking is the first mainstream approach to counter compounding error: looking at a future segment instead of a single frame absorbs per-frame jitter through intra-chunk averaging, significantly reducing out-of-distribution drift. ACT card claim: reports 80%–90% success rate on fine-grained bimanual tasks (source: ACT card; task and data scale differ from your scenario, use only as an order-of-magnitude reference). Temporal ensemble uses "multiple prediction votes" for execution smoothing, at the cost of reduced inference frequency.

【How to analyze your situation】With 50–100 demonstrations: start with the official default chunk length; don't increase it immediately—longer chunks require more data. When wrist/first-person views are missing, ACT's performance on fine alignment degrades noticeably; revisit M17's view coverage. Three strategies for overfitting: early stopping, image data augmentation (translation/color jitter), and targeted data collection in Step 6.

## Step 3: Diffusion Policy—When Multiple Valid Solutions Exist for the Same Situation

【What to do】Run [Diffusion Policy](/entry/ent_method_diffusion_policy/): model the **distribution** of action sequences using a denoising diffusion process instead of point regression, iteratively sampling a segment of actions from noise. Again, start with the official repository defaults and perform a comparative experiment with ACT using **the same data and the same split**, recording validation loss, open-loop playback error, and real-robot results in three columns.

【Why】Regression methods inherently struggle with multimodal actions: if half the demonstrations go "around the left" and half "around the right," regression learns an average "straight through the middle" action; diffusion modeling directly represents multimodal distributions, and sampling any mode yields a valid solution (see the card). The cost is higher training and inference overhead: multi-step denoising means higher on-robot inference latency, which must be measured during deployment (Step 5). Empirical anchor: ToddlerBot runs a 300M parameter diffusion policy on Jetson Orin NX 16GB with ~100 ms on-robot inference (source: [ToddlerBot paper](https://arxiv.org/html/2502.00893v2)).

Quick comparison of the two methods (details in their respective cards):

| Dimension | ACT | Diffusion Policy |
|---|---|---|
| Action modeling | Chunked regression + temporal ensemble smoothing | Denoising diffusion modeling of action distribution |
| Multimodal actions | Weak (regression tends to average) | Strong (samples from distribution) |
| On-robot inference | Single forward pass, low latency | Multi-step denoising, high latency (needs measurement) |
| Preferred scenario | Single solution, quick start | Multiple valid solutions for the same situation |

【How to analyze your situation】If the task has a single solution (grasping a fixed cup at a fixed position): ACT is usually sufficient; the benefit of diffusion is small and the cost is high, so this step can be skipped, but it's recommended to run it at least once as a comparison. If the task has multiple grasping methods/paths: perform a thorough comparative experiment. When real-robot results are similar between the two methods, choose the faster inference one—on-robot frequency equals stability.

## Step 4: Evaluation Protocol—Offline Screening, Closed-Loop Decides

【What to do】Establish a two-level evaluation and solidify it into scripts:

1. **Offline**: Validation loss is only a coarse filter; **open-loop playback** is mandatory—for each candidate model, pick 5–10 validation episodes, overlay predicted actions with ground truth on plots, render videos, and inspect each one manually;
2. **Closed-loop**: Fixed real-robot protocol—fixed object, fixed position grid (e.g., 3×3, 5 cm spacing, engineering suggestion, verify against your task), repeat at each grid point, total 20 trials recording success/failure; Stage 3 criteria: success rate ≥70%;
3. **Failure taxonomy**: Classify each failure into one of four categories and count—perception error (detection/segmentation error), localization error (pose deviation), grasp slip (contact but no grip), trajectory collision (knocking over object or hitting table).

Each closed-loop trial is recorded as one row, with a script for automatic aggregation (fields can be added/deleted as needed):

```
trial_id,grid,success,failure_class,infer_ms,notes
007,(2,1),fail,slip,96, Cup slipped at the moment of closure
```

【Why】Between "loss decreased" and "robot can grasp" lie three major obstacles: distribution shift, temporal alignment, and execution latency. Only a closed-loop real-robot protocol is the final judge; the value of a fixed protocol is reproducibility and horizontal comparability—without it, the effect of each change is a mystery. The failure taxonomy determines what to fix next: perception errors → add view/lighting data; localization errors → recheck calibration; slip → modify gripper or add approach segment data; collision → add obstacle scenarios. Evaluation methodology is detailed in [Chapter 25 Robot Evaluation Systems](/wiki/chapters/chapter-25/).

【How to analyze your situation】20 trials is the minimum for a "publishable" result: a denser grid would take too long, and fewer trials would introduce too much statistical noise (one more success out of 20 is 5 percentage points). On evaluation day, record lighting, ambient temperature, and battery level—each of these three variables can individually account for a few percentage points of fluctuation.

## Step 5: Edge Deployment – Strategy on Jetson, Limiting for Safety

[What to do] Deploy the policy to the onboard computing platform (typically [Jetson AGX Orin](/entry/ent_component_nvidia_jetson_agx_orin_2024/), see [Compute Platform Selection Playbook](../playbooks/compute-selection.md) for tiered selection rationale), and reduce latency using methods from the [On-Device VLA Inference](/entry/ent_tech_on_device_vla_inference/) card: quantization (FP16/INT8), inference engine optimization, and lowering input resolution. Then complete four tasks:

1. **Frequency Matching**: Measure end-to-end inference latency and determine the policy frequency (5–10 Hz is usually sufficient for manipulation tasks, source: Compute Platform Selection Playbook); policy output is handed off to the low-level high-frequency loop for tracking (proprietary QDD force control closed-loop at 250 Hz–1 kHz, same source);
2. **Action Limiting**: Policy output is sent only after passing through workspace soft limits (5–10° smaller than mechanical hard limits, M10 rule) and velocity limits;
3. **Degradation Strategy**: Inference timeout (e.g., >2x control cycle, engineering recommended value) → maintain current pose; consecutive timeouts → release force and enter damping (M14 [m14-sim-to-real.md](m14-sim-to-real.md) tiered);
4. **Baseline Regression**: Write the measured latency and closed-loop success rate from this deployment into the model card; any subsequent changes to limits, frequency, or quantization configuration must re-run the closed-loop protocol from Step 4 to take effect.

[Why] Onboard inference cannot assume network availability: cloud inference with Wi-Fi jitter equals loss of control—latency, connectivity, and privacy are the three hard constraints for edge deployment (On-Device VLA Inference card). The policy is a "fallible black box"; limiting and degradation are the final line of defense to contain it, sharing the same safety logic as M20's protection mechanism checklist.

[How to analyze your situation] ACT-level small models can usually run at sufficient frequency directly on Orin; for diffusion policies, quantize first then test. ToddlerBot's 300M diffusion policy runs at approximately 100 ms on Orin NX 16GB (toddlerbot.md archive), which can serve as an order-of-magnitude anchor. If latency is insufficient, cut in order: quantize → reduce resolution → reduce denoising steps/action chunk length; if still insufficient, evaluate a [Jetson Thor](/entry/ent_component_nvidia_jetson_thor/) level platform. Configure CPU affinity and priority for the inference process separately to avoid competing for cores with the control process.

## Step 6: Iterative Closed-Loop – Where It Fails, Add Data There

[What to do] Establish a fixed iteration cadence: change only **one variable** per round (add one data type / tune one hyperparameter / swap one backbone), run the full "train → offline evaluation → 20 closed-loop trials" pipeline, and log it in the table:

| Model Version | Data Version | Change | Validation Loss | Closed-Loop Success Rate | Failure Category Count |
|---|---|---|---|---|---|
| v1.0 | d1.0 (50 demos) | BC baseline | … | … | … |
| v1.1 | d1.1 (+8 slip scenarios) | Targeted data collection | … | … | … |

Use the DAgger approach for targeted data collection: reproduce the scenarios where the policy failed (e.g., slip in the top-right grid), teleoperate to collect 5–10 additional demonstrations for that scenario, and add them to the training set. Optional: use [LIBERO](/entry/ent_benchmark_libero/) (short-horizon desktop benchmark with task suites + procedural scene variations) for simulation regression; test each change in simulation before deploying on the real robot.

Synchronize the output of each iteration round to update the **model card**: data version, training configuration (code commit + key hyperparameters), offline/closed-loop metrics, measured deployment latency, and known failure scenarios—M19 integration and M20 change management both rely on the model card.

[Why] The performance bottleneck in imitation learning is almost always data distribution, not model capacity: failure taxonomy tells you where the holes in the distribution are, and targeted data collection is the change with the highest return per unit time. Changing only one variable at a time + a version correspondence table is the only way to answer "why did the success rate drop from 75% to 60%" three months later. LIBERO's procedural scene variations can expose overfitting, and simulation regression keeps most "changes that make things worse" off the real robot (see [Chapter 25](/wiki/chapters/chapter-25/)).

[How to analyze your situation] Control targeted data collection to 10–20% of the total per round: too much dilutes the original distribution, too little has no effect. If the success rate stagnates for two rounds: review the failure category count—if perception errors account for more than half, the problem is in the data or calibration, not the policy; fixing the data is cheaper than continuing to tune parameters.

## Acceptance Criteria

- [ ] BC baseline runs successfully; pipeline (loading/alignment/normalization/replay) verification is documented, with numbers kept as a control group.
- [ ] At least one version each of ACT and Diffusion Policy is trained; comparison table with same data and same split is archived.
- [ ] Real-robot fixed protocol (fixed objects + position grid + 20 trials) success rate ≥70%; raw records of success/failure and failure categories for each trial are complete.
- [ ] Failure taxonomy counts for all four categories are complete, with at least one round of "targeted data collection → retest" closed-loop record.
- [ ] Model card is documented: data version, training configuration, evaluation metrics, measured deployment latency.
- [ ] Training and evaluation scripts, along with configuration, are committed to the repository (reproducible with the same data version); closed-loop raw records are archived with the version.
- [ ] Edge deployment meets standards: measured inference latency satisfies policy frequency; action limiting and timeout degradation are verified via real-robot triggering.

## Common Pitfalls and Troubleshooting

| Symptom | Possible Cause | Troubleshooting Action |
|---|---|---|
| Training loss decreases, but real robot fails completely | Distribution shift / misaligned image and action timestamps | Open-loop replay, check timestamps frame by frame; verify clock synchronization during collection |
| Jitter or jerkiness at action chunk boundaries | Temporal ensemble not enabled or improper weighting / inference frequency too low | Confirm temporal ensemble is active; measure end-to-end latency; increase chunk overlap |
| Overfitting on small data (val loss rises early) | Too little data / too many epochs | Early stopping; image augmentation; go back to Step 6 for targeted data collection |
| Real robot always off by a few centimeters | Image compression/downsampling loses key details / extrinsic calibration drift | Check data pipeline image transforms; recalibrate hand-eye |
| Inference latency exceeds limit, control feels floaty | Not quantized / input resolution too high / inference and control competing for CPU | Quantize + inference engine optimization; reduce resolution; bind cores and set process priorities |
| Success rate crashes after camera/lighting change | Data distribution overfits to viewpoint/lighting | Introduce viewpoint and lighting variations during collection; use LIBERO simulation regression first to expose issues |

## Companion Reading

- Previous task: [M17 · Teleoperation and Data Collection](m17-teleop-data.md)
- Next task: [M19 · End-to-End Task Integration](m19-e2e-task.md)
- Theoretical background: [Chapter 18 Imitation Learning and Policy Learning](/wiki/chapters/chapter-18/), [Chapter 21 Data Infrastructure](/wiki/chapters/chapter-21/), [Chapter 25 Robot Evaluation Systems](/wiki/chapters/chapter-25/)
- [Compute Platform Selection Playbook](../playbooks/compute-selection.md) · [Stage 3 Overview](../stage-3-humanoid.md) · [Roadmap Overview](../index.md)
