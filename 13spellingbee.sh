gunzip -c dictionary.gz | grep "r" | grep -E "[azircon]{4,100}" | grep -v "[^azircon]"

gunzip -c dictionary.gz | grep "r" | grep -v "[bdefghjklmpqstuvwxy]" | grep -E ".{4,100}"