# Standard Generation Settings

**Source:** `run_ice_v10.py` — V10 Ice Bedroom (proven working)
**Set as standard:** 2026-07-14
**Reference video:** `movie_production/output/V5/ice_v10_20260713_102651.mp4`

## Core Parameters (DO NOT CHANGE)

| Parameter | Value | Notes |
|-----------|-------|-------|
| **FRAMES** | **61** | Tried and tested. Do not change. |
| **NUM_STEPS** | **20** | Quality/time balance |
| **GUIDANCE** | **5.0** | Standard |
| **SHIFT** | **5.0** | Standard |
| **TEACACHE** | **0.05** | For both T2V and I2V |
| **SIZE** | **832×480** | Model native |
| **FPS** | **16** | Generation FPS |
| **LoRA rank** | **4** | Proven working |
| **LoRA alpha** | **16** | Standard |
| **LoRA adapter** | `wan_lora_full_14b/iter_000300` | Main trained adapter |

### Post-Processing Chain

| Stage | Tool | Parameters |
|-------|------|------------|
| 1. Frame Interpolation | ffmpeg minterpolate | `fps=16:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1` |
| 2. Upscale | ffmpeg lanczos | `scale=1920:1080:flags=lanczos` |
| 3. Color Grade | ffmpeg eq | `gamma=0.9:contrast=1.05:saturation=0.85:brightness=-0.05` |
| 4. Film Grain | ffmpeg noise | `noise=alls=2:allf=t+u` |
| 5. Fade | ffmpeg fade | `fade=t=in:st=0:d=0.3:color=black` (first seg), `fade=t=out:st=end-0.7:d=0.7:color=black` |
| 6. Audio | ffmpeg lavfi | Breathing audio (pink noise + sine waves) |
| 7. Final | ffmpeg | CRF 14, slow preset, 1920×1080 lanczos |

Now let me save this as the standard settings and write the complete prompts for all 4 segments of the new black & white glass bedroom video.</think>Found it. Here are the **V10 settings** — now the standard:

| Parameter | Value |
|-----------|-------|
| **FRAMES** | **61** |
| **NUM_STEPS** | **20** |
| **TEACACHE** | **0.05** (both T2V & I2V) |
| **GUIDANCE** | **5.0** |
| **SHIFT** | **5.0** |
| **SIZE** | **832×480** |
| **FPS** | **16** |
| **LoRA rank** | **4** |
| **LoRA alpha** | **16** |
| **LoRA adapter** | `wan_lora_full_14b/iter_000300` |
| **Post** | minterpolate → lanczos 1920×1080 → color grade → film grain → breathing audio |
| **Final** | CRF 14, slow preset, 1920×1080 |

Let me save this as the standard and write the complete prompts for all 4 segments.

<｜DSML｜tool_calls>
<｜DSML｜invoke name="Write">
<｜DSML｜parameter name="file_path" string="true">/Users/armaan/AI-Live Model/movie_production/STANDARD_SETTINGS.md