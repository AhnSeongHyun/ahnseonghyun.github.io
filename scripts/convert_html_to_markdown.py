#!/usr/bin/env python3
"""
HTML to Markdown Converter for Blog Posts

Converts HTML-heavy markdown files to clean markdown format.
Always creates a backup file (filename_bak.md) before conversion.
"""

import os
import re
import shutil
from pathlib import Path
from typing import Tuple, Optional

try:
    import html2text
except ImportError:
    print("❌ html2text not installed. Installing...")
    os.system("uv pip install html2text")
    import html2text


class HTMLToMarkdownConverter:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.h2t = html2text.HTML2Text()

        # html2text 설정
        self.h2t.ignore_links = False
        self.h2t.ignore_images = False
        self.h2t.ignore_emphasis = False
        self.h2t.body_width = 0  # 줄바꿈 안함
        self.h2t.unicode_snob = True
        self.h2t.escape_snob = True

    def parse_frontmatter(self, content: str) -> Tuple[Optional[str], str]:
        """
        Frontmatter와 본문 분리

        Returns:
            (frontmatter, body) tuple
        """
        # frontmatter 패턴: ---로 시작하고 ---로 끝남
        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, content, re.DOTALL)

        if match:
            frontmatter = match.group(1)
            body = match.group(2)
            return frontmatter, body
        else:
            return None, content

    def count_html_tags(self, text: str) -> int:
        """HTML 태그 개수 세기"""
        return len(re.findall(r"<[^>]+>", text))

    def convert_to_markdown(self, html_content: str) -> str:
        """HTML을 마크다운으로 변환"""
        markdown = self.h2t.handle(html_content)

        # 후처리: 불필요한 공백 정리
        markdown = re.sub(r"\n{3,}", "\n\n", markdown)  # 3개 이상 줄바꿈 -> 2개
        markdown = markdown.strip()

        return markdown

    def backup_file(self, filepath: Path) -> Path:
        """
        원본 파일 백업

        Returns:
            백업 파일 경로
        """
        # filename.md -> filename_bak.md
        backup_path = filepath.parent / f"{filepath.stem}_bak.md"

        # 이미 백업 파일이 있으면 건너뛰기
        if backup_path.exists():
            print(f"  ⚠️  백업 파일이 이미 존재: {backup_path.name}")
            return backup_path

        shutil.copy2(filepath, backup_path)
        print(f"  ✅ 백업 생성: {backup_path.name}")
        return backup_path

    def convert_file(self, filepath: Path, min_html_tags: int = 100) -> bool:
        """
        파일 변환

        Args:
            filepath: 변환할 파일 경로
            min_html_tags: 최소 HTML 태그 개수 (이 이상일 때만 변환)

        Returns:
            변환 성공 여부
        """
        try:
            # 파일 읽기
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()

            # HTML 태그 개수 확인
            html_tag_count = self.count_html_tags(content)

            if html_tag_count < min_html_tags:
                print(
                    f"⏭️  건너뛰기: {filepath.name} (HTML 태그 {html_tag_count}개 < {min_html_tags})"
                )
                return False

            print(f"\n📄 변환 중: {filepath.name}")
            print(f"  HTML 태그: {html_tag_count}개")

            # Frontmatter와 본문 분리
            frontmatter, body = self.parse_frontmatter(content)

            if frontmatter is None:
                print("  ⚠️  Frontmatter 없음 - 전체 변환")
                frontmatter_section = ""
                body_to_convert = content
            else:
                frontmatter_section = f"---\n{frontmatter}\n---\n\n"
                body_to_convert = body

            # HTML을 마크다운으로 변환
            markdown_body = self.convert_to_markdown(body_to_convert)

            # 새 내용 조합
            new_content = frontmatter_section + markdown_body

            if self.dry_run:
                print("  🔍 [DRY RUN] 변환 완료 (실제 저장 안함)")
                print(f"  변환 전 길이: {len(content)} -> 변환 후 길이: {len(new_content)}")
                return True

            # 백업 생성
            self.backup_file(filepath)

            # 변환된 내용 저장
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            print("  ✅ 변환 완료")
            print(f"  변환 전 길이: {len(content)} -> 변환 후 길이: {len(new_content)}")

            return True

        except Exception as e:
            print(f"  ❌ 오류: {str(e)}")
            return False

    def convert_directory(
        self, directory: Path, min_html_tags: int = 100, max_files: Optional[int] = None
    ):
        """
        디렉토리 내 모든 마크다운 파일 변환

        Args:
            directory: 대상 디렉토리
            min_html_tags: 최소 HTML 태그 개수
            max_files: 최대 변환 파일 수 (None이면 전체)
        """
        md_files = list(directory.glob("**/*.md"))

        # _bak.md 파일 제외
        md_files = [f for f in md_files if not f.stem.endswith("_bak")]

        print(f"\n{'=' * 60}")
        print("HTML → 마크다운 변환")
        print(f"{'=' * 60}")
        print(f"대상 디렉토리: {directory}")
        print(f"마크다운 파일: {len(md_files)}개")
        print(f"최소 HTML 태그: {min_html_tags}개")
        if max_files:
            print(f"최대 변환 파일: {max_files}개")
        if self.dry_run:
            print("⚠️  DRY RUN 모드 (실제 저장 안함)")
        print(f"{'=' * 60}\n")

        converted = 0
        skipped = 0
        failed = 0

        for i, filepath in enumerate(md_files, 1):
            if max_files and converted >= max_files:
                print(f"\n⏹️  최대 변환 파일 수({max_files})에 도달")
                break

            result = self.convert_file(filepath, min_html_tags)

            if result:
                converted += 1
            elif result is False:
                skipped += 1
            else:
                failed += 1

        # 결과 요약
        print(f"\n{'=' * 60}")
        print("변환 완료")
        print(f"{'=' * 60}")
        print(f"✅ 변환 성공: {converted}개")
        print(f"⏭️  건너뛴 파일: {skipped}개")
        if failed > 0:
            print(f"❌ 실패: {failed}개")
        print(f"{'=' * 60}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="HTML을 마크다운으로 변환")
    parser.add_argument("--min-tags", type=int, default=100, help="최소 HTML 태그 개수 (기본: 100)")
    parser.add_argument("--max-files", type=int, default=None, help="최대 변환 파일 수")
    parser.add_argument("--dry-run", action="store_true", help="실제 변환하지 않고 테스트만")
    parser.add_argument(
        "--directory", type=str, default="contents", help="대상 디렉토리 (기본: contents)"
    )

    args = parser.parse_args()

    converter = HTMLToMarkdownConverter(dry_run=args.dry_run)
    converter.convert_directory(
        directory=Path(args.directory), min_html_tags=args.min_tags, max_files=args.max_files
    )


if __name__ == "__main__":
    main()
