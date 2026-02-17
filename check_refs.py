import os, re

docs_dir = 'docs'
mit_dir = os.path.join(docs_dir, 'mitigations')
tech_dir = os.path.join(docs_dir, 'techniques')

mit_files = [f for f in os.listdir(mit_dir) if f.endswith('.md') and f != 'index.md']
tech_files = [f for f in os.listdir(tech_dir) if f.endswith('.md') and f != 'index.md']

print(f'Mitigation files: {len(mit_files)}')
print(f'Technique files: {len(tech_files)}')

def parse_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    heading_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    heading = heading_match.group(1).strip() if heading_match else None
    id_match = re.search(r'ID:\s*(MS-[A-Za-z0-9]+)', content)
    file_id = id_match.group(1).strip() if id_match else None
    cross_refs = []
    table_rows = re.findall(r'\|\s*(MS-[A-Za-z0-9]+)\s*\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|', content)
    for row in table_rows:
        ref_id, ref_name, ref_link = row
        cross_refs.append({
            'ref_id': ref_id.strip(),
            'ref_name': ref_name.strip(),
            'ref_link': ref_link.strip()
        })
    return {'heading': heading, 'id': file_id, 'cross_refs': cross_refs}

mitigations = {}
for f in mit_files:
    mitigations[f] = parse_file(os.path.join(mit_dir, f))

techniques = {}
for f in tech_files:
    techniques[f] = parse_file(os.path.join(tech_dir, f))

issues = []

# Check mitigation -> technique references
for mit_file, mit_data in sorted(mitigations.items()):
    for ref in mit_data['cross_refs']:
        ref_id = ref['ref_id']
        ref_name = ref['ref_name']
        ref_link = ref['ref_link']
        if not ref_id.startswith('MS-TA'):
            continue
        link_path = ref_link.replace('%20', ' ')
        resolved = os.path.normpath(os.path.join(mit_dir, link_path))
        if not os.path.exists(resolved):
            issues.append(
                'BROKEN LINK in mitigation [{}]: references [{}] but file does not exist'.format(
                    mit_file, ref_link))
            continue
        tech_filename = os.path.basename(resolved)
        if tech_filename in techniques:
            td = techniques[tech_filename]
            if td['id'] and ref_id != td['id']:
                issues.append(
                    'ID MISMATCH in mitigation [{}]: references technique [{}] with ID [{}], but technique file [{}] has ID [{}]'.format(
                        mit_file, ref_name, ref_id, tech_filename, td['id']))
            if td['heading'] and ref_name != td['heading']:
                issues.append(
                    'NAME MISMATCH in mitigation [{}]: references technique as [{}] but [{}] heading is [{}]'.format(
                        mit_file, ref_name, tech_filename, td['heading']))
        else:
            issues.append(
                'FILE NOT FOUND: mitigation [{}] links to [{}] which is not in techniques directory'.format(
                    mit_file, tech_filename))

# Check technique -> mitigation references
for tech_file, tech_data in sorted(techniques.items()):
    for ref in tech_data['cross_refs']:
        ref_id = ref['ref_id']
        ref_name = ref['ref_name']
        ref_link = ref['ref_link']
        if not ref_id.startswith('MS-M'):
            continue
        link_path = ref_link.replace('%20', ' ')
        resolved = os.path.normpath(os.path.join(tech_dir, link_path))
        if not os.path.exists(resolved):
            issues.append(
                'BROKEN LINK in technique [{}]: references [{}] but file does not exist'.format(
                    tech_file, ref_link))
            continue
        mit_filename = os.path.basename(resolved)
        if mit_filename in mitigations:
            md = mitigations[mit_filename]
            if md['id'] and ref_id != md['id']:
                issues.append(
                    'ID MISMATCH in technique [{}]: references mitigation [{}] with ID [{}], but mitigation file [{}] has ID [{}]'.format(
                        tech_file, ref_name, ref_id, mit_filename, md['id']))
            if md['heading'] and ref_name != md['heading']:
                issues.append(
                    'NAME MISMATCH in technique [{}]: references mitigation as [{}] but [{}] heading is [{}]'.format(
                        tech_file, ref_name, mit_filename, md['heading']))
        else:
            issues.append(
                'FILE NOT FOUND: technique [{}] links to [{}] which is not in mitigations directory'.format(
                    tech_file, mit_filename))

# Check bidirectional consistency
print('\n--- Checking bidirectional references ---')
bidi_issues = []

# For each mitigation that references a technique, check if that technique references back
for mit_file, mit_data in sorted(mitigations.items()):
    mit_id = mit_data['id']
    for ref in mit_data['cross_refs']:
        if not ref['ref_id'].startswith('MS-TA'):
            continue
        link_path = ref['ref_link'].replace('%20', ' ')
        resolved = os.path.normpath(os.path.join(mit_dir, link_path))
        tech_filename = os.path.basename(resolved)
        if tech_filename in techniques:
            td = techniques[tech_filename]
            # Check if this technique references back to this mitigation
            back_refs = [r for r in td['cross_refs'] if r['ref_id'] == mit_id]
            if not back_refs and mit_id:
                bidi_issues.append(
                    'MISSING BACK-REF: Mitigation [{}] (ID: {}) references technique [{}], but that technique does not reference back'.format(
                        mit_file, mit_id, tech_filename))

# For each technique that references a mitigation, check if that mitigation references back
for tech_file, tech_data in sorted(techniques.items()):
    tech_id = tech_data['id']
    for ref in tech_data['cross_refs']:
        if not ref['ref_id'].startswith('MS-M'):
            continue
        link_path = ref['ref_link'].replace('%20', ' ')
        resolved = os.path.normpath(os.path.join(tech_dir, link_path))
        mit_filename = os.path.basename(resolved)
        if mit_filename in mitigations:
            md = mitigations[mit_filename]
            back_refs = [r for r in md['cross_refs'] if r['ref_id'] == tech_id]
            if not back_refs and tech_id:
                bidi_issues.append(
                    'MISSING BACK-REF: Technique [{}] (ID: {}) references mitigation [{}], but that mitigation does not reference back'.format(
                        tech_file, tech_id, mit_filename))

print('\n========== RESULTS ==========')
print('\n--- Direct Reference Issues ---')
if issues:
    for i, issue in enumerate(issues, 1):
        print('{}. {}'.format(i, issue))
else:
    print('No direct reference issues found!')

print('\n--- Bidirectional Reference Issues ---')
if bidi_issues:
    for i, issue in enumerate(bidi_issues, 1):
        print('{}. {}'.format(i, issue))
else:
    print('No bidirectional reference issues found!')

print('\nTotal direct issues: {}'.format(len(issues)))
print('Total bidirectional issues: {}'.format(len(bidi_issues)))

# Also print all IDs for debugging
print('\n--- All Mitigation IDs ---')
for f, d in sorted(mitigations.items()):
    print('  {}: ID={}, Heading={}'.format(f, d['id'], d['heading']))

print('\n--- All Technique IDs ---')
for f, d in sorted(techniques.items()):
    print('  {}: ID={}, Heading={}'.format(f, d['id'], d['heading']))
