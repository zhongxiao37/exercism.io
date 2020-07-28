import re
def transpose(lines):
    lines = lines.split('\n')
    rows = len(lines)
    columns = max(len(lines[i]) for i in range(rows))

    data = []
    for c in range(columns):
        data.append(''.join([lines[r][c] if c < len(lines[r]) else '$' for r in range(rows)]))
    
    return '\n'.join([re.sub(r'\$', ' ', re.sub(r'\$+$', '', i)) for i in data])