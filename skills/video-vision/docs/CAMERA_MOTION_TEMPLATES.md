# Camera Motion Templates — Settings Reference

## 1. Body Scan Pan (V9 Style)
**Camera pans up OR down the body** — T2V generates the movement.

### Prompt phrase:
```
"Camera slowly pans up from her [lower body] past her [hips], 
up across her [stomach] to her [upper body], then to her [neck and face]."
```

### Working example (v9_darker_night):
```python
PROMPT = (
    f"Full body shot of {BODY}. Completely topless with bare breasts, wearing tiny black lace thong. "
    f"In {ENV}. Very dim natural darkness surrounding her, deep dark shadows. "
    f"Camera slowly pans up from her thick thighs past her wide hips, "
    f"up across her stomach to her full bare breasts, then to her neck and face with beautiful lips. "
    f"Skin with few light sweat droplets. Dark night ambiance. "
    f"Cinematic smooth camera movement. Photorealistic. 8K."
)
```

### Settings:
| Param | Value |
|-------|-------|
| Model | T2V-14B (8-bit quantized) |
| Output | 1920×1080 (upscaled) |
| Seed | 801 |
| Frames | 61 |
| Steps | 20 |
| Teacache | 0.05 |
| LoRA | wan_lora_full_14b/iter_000300 |
| Post | fade=t=in + scale=1920:1080 + color grade + unsharp |
| Audio | Breathing (anoisesrc + sine tones) |

---

## 2. Walking + Camera Circle (Gallery Style)
**Subject walks, camera circles around** — T2V generates both.

### Prompt phrase:
```
"She walks slowly through the [scene], water/light around her.
Camera slowly circles around her full body capturing every angle 
[OR drifts / glides around her body]. She stops, turns her body."
```

### Working example (beach_sunset):
```python
"Full body shot of {BODY}, completely nude, standing at the edge of a quiet beach at sunset.
She walks slowly through the shallow water, waves lapping at her ankles and calves.
She stops, turns her body to face the sun, hands at her sides, 
head tilted back slightly, eyes closed, a single hand gliding down her stomach.
Camera slowly circles around her full body capturing every angle.
Water on skin glistening, cinematic wide shot."
```

### Settings:
| Param | Value |
|-------|-------|
| Model | T2V-14B (8-bit quantized) |
| Output | 1920×1080 (upscaled) |
| Seed | 803 (beach), 801-806 range |
| Frames | 61 |
| Steps | 20 |
| Teacache | 0.05 |
| LoRA | wan_lora_full_14b/iter_000300 |
| Post | fade=t=in upscale + color grade |
| Motion | Natural speed (NO slow-mo) |

---

## 3. Key Rules for Camera Movement in Prompts

1. **Describe the camera, not just the subject**
   - ✅ `"Camera slowly pans up from her thighs to her face"`
   - ❌ "She moves her body" (model doesn't understand this as camera movement)

2. **Use "slowly"** — Fast movement causes distortion
   - ✅ `"Camera slowly drifts"`
   - ✅ `"Camera slowly circles"`
   - ❌ "Camera quickly moves"

3. **Describe a clear path** — Start → Middle → End
   - ✅ `"pans up from thighs → hips → stomach → breasts → face"`
   - ✅ `"circles from front → side → back → front"`

4. **Keep generation at 61 frames** — Longer videos lose camera coherence

5. **No slow-mo** — Real-speed makes camera movement look natural

---

## 4. Camera Movement Templates

### Body Scan (face→body or body→face):
```
Camera slowly pans [up/down] from [starting point], 
past [body part], across [body part], to [ending point].
```

### Circle Around:
```
Camera slowly circles around her full body, 
drifting from [angle] to [angle].
```

### Drift Towards:
```
Camera slowly drifts closer to her, 
starting at [wide/medium/close] shot, 
moving to [medium/close] shot.
```

### Side to Side:
```
Camera slowly drifts [left/right], 
revealing her [body angle].
```
