#!/usr/bin/env python3
"""Validate timeline bounds and entity references in a neutral motion brief."""
import argparse
import json
import math
from pathlib import Path


def finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def validate_brief(brief):
    errors = []
    if not isinstance(brief, dict):
        return ['Brief must be a JSON object.']
    output = brief.get('output')
    if not isinstance(output, dict):
        return ['output must be an object.']
    duration = output.get('duration')
    if not finite(duration) or duration <= 0:
        errors.append('output.duration must be positive and finite.')
        duration = None
    fps = output.get('fps')
    if not finite(fps) or fps <= 0:
        errors.append('output.fps must be positive and finite.')
    for field in ('width', 'height'):
        value = output.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            errors.append(f'output.{field} must be a positive integer.')
    entities = brief.get('entities')
    if not isinstance(entities, list) or not entities:
        errors.append('entities must be a nonempty array.')
        entities = []
    ids = set()
    parents = {}
    for index, entity in enumerate(entities):
        if not isinstance(entity, dict) or not isinstance(entity.get('id'), str) or not entity['id'].strip():
            errors.append(f'entities[{index}] needs a nonempty string id.')
            continue
        identity = entity['id']
        if identity in ids:
            errors.append(f'Duplicate entity id: {identity}.')
        ids.add(identity)
        parent = entity.get('parent')
        if parent is not None:
            if not isinstance(parent, str):
                errors.append(f'Entity {identity} parent must be a string id.')
            else:
                parents[identity] = parent
    for identity, parent in parents.items():
        if parent not in ids:
            errors.append(f'Entity {identity} references unknown parent: {parent}.')
        visited = set()
        current = identity
        while current in parents:
            if current in visited:
                errors.append(f'Parent cycle containing entity: {identity}.')
                break
            visited.add(current)
            current = parents[current]
    beats = brief.get('beats')
    if not isinstance(beats, list) or not beats:
        errors.append('beats must be a nonempty array.')
        beats = []
    for index, beat in enumerate(beats):
        label = f'beats[{index}]'
        if not isinstance(beat, dict):
            errors.append(f'{label} must be an object.')
            continue
        start, end = beat.get('start'), beat.get('end')
        bounds_valid = finite(start) and finite(end) and 0 <= start < end
        if not bounds_valid or (duration is not None and finite(end) and end > duration):
            errors.append(f'{label} must satisfy 0 <= start < end <= duration.')
        hold = beat.get('reading_hold', 0)
        if not finite(hold) or hold < 0 or (bounds_valid and hold > end - start + 1e-9):
            errors.append(f'{label}.reading_hold must fit inside the beat.')
        references = []
        for field in ('persistent_entities', 'entering_entities', 'leaving_entities'):
            values = beat.get(field, [])
            if not isinstance(values, list):
                errors.append(f'{label}.{field} must be an array of ids.')
            else:
                references.extend(values)
        focus = beat.get('focus_target')
        if focus is not None:
            references.append(focus)
        for identity in references:
            if not isinstance(identity, str) or identity not in ids:
                errors.append(f'{label} references unknown entity: {identity!r}.')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('brief', type=Path, nargs='+')
    arguments = parser.parse_args()
    results = []
    for file in arguments.brief:
        try:
            brief = json.loads(file.read_text(encoding='utf-8'))
            errors = validate_brief(brief)
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            errors = [str(error)]
        results.append({'file': str(file), 'valid': not errors, 'errors': errors})
    print(json.dumps(results, ensure_ascii=True, indent=2))
    return int(any(not result['valid'] for result in results))


if __name__ == '__main__':
    raise SystemExit(main())
