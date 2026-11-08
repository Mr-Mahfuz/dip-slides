"""Build the two standalone study entry points from editable sources."""
import json
from pathlib import Path
from study_data import lessons, quiz

root = Path(__file__).resolve().parent
html = (root / 'study_shell.html').read_text(encoding='utf-8')
for marker, value in {
    '__CSS__': (root / 'study.css').read_text(encoding='utf-8'),
    '__LESSONS__': json.dumps(lessons, ensure_ascii=False).replace('</', '<\\/'),
    '__QUIZ__': json.dumps(quiz, ensure_ascii=False).replace('</', '<\\/'),
    '__JS__': (root / 'study.js').read_text(encoding='utf-8'),
}.items():
    html = html.replace(marker, value)
for name in ('index.html', 'dip_mastery_guide.html'):
    (root / name).write_text(html, encoding='utf-8')
print(f'Built {len(lessons)} lessons, {len(quiz)} questions; {sum(l["minutes"] for l in lessons)} minutes.')
