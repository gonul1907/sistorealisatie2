from pathlib import Path

replacements = {
    'â˜Ž': '☎',
    'âœ†': '✆',
    'â†’': '→',
    'âœ“': '✓',
    'Â©': '©',
    'â€™': '’',
}

base = Path(r'C:\Users\gonul\source\repos\sisto-clone')
for p in base.glob('*.html'):
    text = p.read_text(encoding='utf-8', errors='surrogateescape')
    for old, new in replacements.items():
        text = text.replace(old, new)
    p.write_text(text, encoding='utf-8')
    print(f'fixed {p.name}')
