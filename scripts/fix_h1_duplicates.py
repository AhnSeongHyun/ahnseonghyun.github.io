#!/usr/bin/env python3
"""
H1 Duplicate Remover

Fixes files with multiple H1 headings by converting all H1s after the first one to H2s.
Always creates backup files (filename_bak.md) before modification.
"""

import re
import shutil
from pathlib import Path
from typing import Tuple, Optional


class H1DuplicateFixer:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run

    def parse_frontmatter(self, content: str) -> Tuple[Optional[str], str]:
        """
        Parse frontmatter and body

        Returns:
            (frontmatter, body) tuple
        """
        pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(pattern, content, re.DOTALL)

        if match:
            frontmatter = match.group(1)
            body = match.group(2)
            return f"---\n{frontmatter}\n---\n\n", body
        else:
            return None, content

    def count_h1_headings(self, text: str) -> int:
        """Count H1 headings in markdown text"""
        # Match lines that start with exactly one # followed by a space
        pattern = r'^# [^\n]+'
        matches = re.findall(pattern, text, re.MULTILINE)
        return len(matches)

    def fix_h1_duplicates(self, body: str) -> Tuple[str, int]:
        """
        Convert all H1 headings after the first one to H2

        Returns:
            (fixed_body, number_of_fixes)
        """
        lines = body.split('\n')
        fixed_lines = []
        h1_count = 0
        fixes = 0

        for line in lines:
            # Check if line is an H1 heading (starts with # but not ##)
            if re.match(r'^# [^\n]+', line):
                h1_count += 1

                if h1_count == 1:
                    # Keep first H1
                    fixed_lines.append(line)
                else:
                    # Convert to H2
                    fixed_lines.append('#' + line)
                    fixes += 1
            else:
                fixed_lines.append(line)

        return '\n'.join(fixed_lines), fixes

    def backup_file(self, filepath: Path) -> Path:
        """Create backup file"""
        backup_path = filepath.parent / f"{filepath.stem}_bak.md"

        if backup_path.exists():
            # Backup already exists
            return backup_path

        shutil.copy2(filepath, backup_path)
        print(f"  ✅ 백업 생성: {backup_path.name}")
        return backup_path

    def fix_file(self, filepath: Path, min_h1_count: int = 2) -> bool:
        """
        Fix H1 duplicates in a single file

        Args:
            filepath: File to fix
            min_h1_count: Minimum H1 count to trigger fixing (default: 2)

        Returns:
            True if changes were made, False otherwise
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            frontmatter_section, body = self.parse_frontmatter(content)

            # Count H1 headings
            h1_count = self.count_h1_headings(body)

            if h1_count < min_h1_count:
                return False

            print(f"\n📝 수정 중: {filepath.name}")
            print(f"  H1 개수: {h1_count}개")

            # Fix H1 duplicates
            fixed_body, fixes = self.fix_h1_duplicates(body)

            print(f"  변경: {fixes}개 H1 → H2 변환")

            if self.dry_run:
                print("  🔍 [DRY RUN] 변경사항 미저장")
                return True

            # Backup original file
            self.backup_file(filepath)

            # Reconstruct file
            if frontmatter_section:
                new_content = frontmatter_section + fixed_body
            else:
                new_content = fixed_body

            # Save fixed version
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print("  ✅ 저장 완료")
            return True

        except Exception as e:
            print(f"  ❌ 오류: {str(e)}")
            return False

    def fix_directory(self, directory: Path, year_filter: int = 2020,
                     max_files: Optional[int] = None):
        """
        Fix H1 duplicates in all markdown files in directory

        Args:
            directory: Target directory
            year_filter: Only process files from this year onwards
            max_files: Maximum number of files to process
        """
        md_files = list(directory.glob('**/*.md'))

        # Exclude _bak.md files
        md_files = [f for f in md_files if not f.stem.endswith('_bak')]

        # Filter by H1 count
        files_to_fix = []
        for filepath in md_files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                _, body = self.parse_frontmatter(content)
                h1_count = self.count_h1_headings(body)

                if h1_count >= 2:
                    files_to_fix.append((filepath, h1_count))
            except Exception:
                continue

        # Sort by H1 count (descending)
        files_to_fix.sort(key=lambda x: x[1], reverse=True)

        print(f"\n{'='*60}")
        print("H1 중복 제거")
        print(f"{'='*60}")
        print(f"대상 디렉토리: {directory}")
        print(f"H1 중복 파일: {len(files_to_fix)}개")
        if max_files:
            print(f"최대 처리 파일: {max_files}개")
        if self.dry_run:
            print("⚠️  DRY RUN 모드 (실제 저장 안함)")
        print(f"{'='*60}\n")

        if files_to_fix:
            print("파일 목록:")
            for filepath, h1_count in files_to_fix[:10]:  # Show first 10
                print(f"  • {filepath.name} ({h1_count}개 H1)")
            if len(files_to_fix) > 10:
                print(f"  ... 외 {len(files_to_fix) - 10}개")
            print()

        fixed = 0
        skipped = 0
        failed = 0

        for filepath, h1_count in files_to_fix:
            if max_files and fixed >= max_files:
                print(f"\n⏹️  최대 처리 파일 수({max_files})에 도달")
                break

            result = self.fix_file(filepath)

            if result is True:
                fixed += 1
            elif result is False:
                skipped += 1
            else:
                failed += 1

        # Summary
        print(f"\n{'='*60}")
        print("수정 완료")
        print(f"{'='*60}")
        print(f"✅ 수정 완료: {fixed}개")
        print(f"⏭️  건너뛴 파일: {skipped}개")
        if failed > 0:
            print(f"❌ 실패: {failed}개")
        print(f"{'='*60}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='H1 중복 제거')
    parser.add_argument('--year', type=int, default=2020,
                       help='이 년도 이후 파일만 처리 (기본: 2020)')
    parser.add_argument('--max-files', type=int, default=None,
                       help='최대 처리 파일 수')
    parser.add_argument('--dry-run', action='store_true',
                       help='실제 변환하지 않고 테스트만')
    parser.add_argument('--directory', type=str, default='contents',
                       help='대상 디렉토리 (기본: contents)')

    args = parser.parse_args()

    fixer = H1DuplicateFixer(dry_run=args.dry_run)
    fixer.fix_directory(
        directory=Path(args.directory),
        year_filter=args.year,
        max_files=args.max_files
    )


if __name__ == '__main__':
    main()
