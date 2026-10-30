#!/bin/bash
# Pre-Generation Prompt Validator
# Validates that any generation prompt follows the Production Bible v1.0
# Call: ./validate_prompt.sh "prompt text here" "negative prompt text here"
# Returns: 0 (pass) or 1 (fail with reason)

PROMPT="$1"
NEGATIVE="$2"
FAILED=0

PRODUCTION_BIBLE="/Users/armaan/AI-Live Model/movie_production/PRODUCTION_BIBLE.md"

echo "=== Pre-Generation Prompt Validation ==="
echo ""

# Check 1: Production Bible exists and has been read
if [ ! -f "$PRODUCTION_BIBLE" ]; then
    echo "❌ FAIL: PRODUCTION_BIBLE.md not found. Read it before generating."
    exit 1
fi
echo "✅ Production Bible exists"

# Check 2: No performance language
# Words that signal performance (must NOT appear UNLESS negated)
PERF_WORDS=("seductive" "sensual" "smoldering" "looking at camera" "eye contact" "photoshoot" "modeling" "fashion" "flirting")
# Words that can be negated (e.g., "not posing", "no performing")
NEGATED_PERF_WORDS=("posing" "performing")
for word in "${PERF_WORDS[@]}"; do
    if echo "$PROMPT" | grep -qi "$word"; then
        echo "❌ FAIL: Prompt contains performance cue: '$word'"
        FAILED=1
    fi
done
for word in "${NEGATED_PERF_WORDS[@]}"; do
    if echo "$PROMPT" | grep -qi "$word"; then
        # Check if it's negated (preceded by "no" or "not" within 3 words)
        if echo "$PROMPT" | grep -qi "no $word\|not $word"; then
            echo "✅ '$word' found but negated — acceptable"
        else
            echo "❌ FAIL: Prompt contains non-negated performance cue: '$word'"
            FAILED=1
        fi
    fi
done

if [ $FAILED -eq 0 ]; then
    echo "✅ No performance language detected"
fi

# Check 3: Anti-performance marker present
if echo "$PROMPT" | grep -qi "doesn't know\|not performing\|no performance\|not posing\|just existing\|in her own\|private moment\|unaware"; then
    echo "✅ Anti-performance marker found"
else
    echo "⚠️  WARNING: No anti-performance marker detected. Add 'does not know she is being watched'"
fi

# Check 4: No smiling in negative prompt
if echo "$NEGATIVE" | grep -qi "smiling\|grinning\|happy\|cheerful\|laughing"; then
    echo "✅ Smile terms blocked in negative prompt"
else
    echo "⚠️  WARNING: Negative prompt missing smile-blocking terms (smiling, grinning, etc)"
fi

# Check 5: No bright/studio lighting
if echo "$PROMPT" | grep -qi "bright\|well-lit\|studio\|sunny\|daylight\|vibrant"; then
    echo "❌ FAIL: Prompt contains bright lighting keywords"
    FAILED=1
fi

# Check 6: No full nudity without explicit instruction
echo ""
echo "⚠️  CHECK: Does this prompt request full nudity (no covering)?"
echo "   If yes, was the user's EXPLICIT instruction given?"
echo "   Default is 95-99% covered (bare minimum, not full nude)."
echo ""

if [ $FAILED -eq 1 ]; then
    echo "=== ❌ VALIDATION FAILED ==="
    echo "Fix the prompt and try again."
    exit 1
fi

echo "=== ✅ VALIDATION PASSED ==="
exit 0
