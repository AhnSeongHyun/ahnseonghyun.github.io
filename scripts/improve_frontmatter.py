#!/usr/bin/env python3
"""
Frontmatter Auto-Improvement Script

Automatically improves frontmatter quality in markdown blog posts:
1. Auto-generates descriptions from first 200 chars of content
2. Removes markdown/HTML syntax from descriptions
3. Ensures minimum 50 character descriptions
4. Adds missing tags
5. Always creates backup files (filename_bak.md)
"""

import os
import re
import shutil
from pathlib import Path

import yaml


class FrontmatterImprover:
    def __init__(self, dry_run=False):
        self.dry_run = dry_run
        self.min_description_length = 50
        self.auto_description_length = 200

    def parse_frontmatter(self, content: str) -> tuple[dict | None, str, str | None]:
        """
        Parse frontmatter and body

        Returns:
            (frontmatter_dict, body, raw_frontmatter_text) tuple
        """
        pattern = r"^---\s*\n(.*?)\n---\s*\n(.*)$"
        match = re.match(pattern, content, re.DOTALL)

        if match:
            raw_frontmatter = match.group(1)
            body = match.group(2)
            try:
                frontmatter = yaml.safe_load(raw_frontmatter)
                return frontmatter, body, raw_frontmatter
            except yaml.YAMLError as e:
                print(f"  ⚠️  YAML 파싱 오류: {e}")
                return None, content, None
        else:
            return None, content, None

    def clean_text_for_description(self, text: str) -> str:
        """Remove markdown/HTML and clean text for description"""
        # Remove markdown headers
        text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)

        # Remove markdown bold/italic
        text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
        text = re.sub(r"\*(.+?)\*", r"\1", text)
        text = re.sub(r"__(.+?)__", r"\1", text)
        text = re.sub(r"_(.+?)_", r"\1", text)

        # Remove HTML tags
        text = re.sub(r"<[^>]+>", "", text)

        # Remove markdown links [text](url)
        text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)

        # Remove markdown images
        text = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", r"\1", text)

        # Remove code blocks
        text = re.sub(r"```[\s\S]*?```", "", text)
        text = re.sub(r"`([^`]+)`", r"\1", text)

        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text)
        text = text.strip()

        return text

    def generate_description(self, body: str, current_description: str = "") -> str:
        """Generate description from body content"""
        # Clean current description if it exists and is decent
        if current_description:
            cleaned = self.clean_text_for_description(current_description)
            if len(cleaned) >= self.min_description_length:
                return cleaned

        # Generate from body
        cleaned_body = self.clean_text_for_description(body)

        # Take first N characters
        if len(cleaned_body) >= self.auto_description_length:
            description = cleaned_body[: self.auto_description_length].rsplit(" ", 1)[0] + "..."
        else:
            description = cleaned_body

        return description

    def extract_tags_from_content(self, title: str, body: str) -> list[str]:
        """Extract potential tags from title and body"""
        tags = []

        # Common tech keywords to look for
        tech_keywords = [
            "python",
            "javascript",
            "typescript",
            "react",
            "vue",
            "node",
            "django",
            "flask",
            "fastapi",
            "docker",
            "kubernetes",
            "aws",
            "gcp",
            "azure",
            "git",
            "github",
            "ci/cd",
            "testing",
            "tdd",
            "api",
            "rest",
            "graphql",
            "database",
            "sql",
            "nosql",
            "mongodb",
            "postgresql",
            "redis",
            "nginx",
            "linux",
            "devops",
            "agile",
            "scrum",
            "retrospective",
            "cto",
            "leadership",
            "startup",
            "mvp",
            "product",
            "engineering",
            "architecture",
            "design",
        ]

        content_lower = (title + " " + body).lower()

        for keyword in tech_keywords:
            if keyword in content_lower:
                tags.append(keyword)
                if len(tags) >= 5:  # Limit to 5 auto-generated tags
                    break

        return tags

    def backup_file(self, filepath: Path) -> Path:
        """Create backup file"""
        backup_path = filepath.parent / f"{filepath.stem}_bak.md"

        if backup_path.exists():
            # Backup already exists, don't overwrite
            return backup_path

        shutil.copy2(filepath, backup_path)
        print(f"  ✅ 백업 생성: {backup_path.name}")
        return backup_path

    def improve_frontmatter(self, filepath: Path) -> bool:
        """
        Improve frontmatter in a single file

        Returns:
            True if changes were made, False otherwise
        """
        try:
            with open(filepath, encoding="utf-8") as f:
                content = f.read()

            frontmatter, body, raw_frontmatter = self.parse_frontmatter(content)

            if frontmatter is None:
                print(f"⏭️  건너뛰기: {filepath.name} (Frontmatter 없음)")
                return False

            changes = []
            modified = False

            # Check and improve description
            current_desc = frontmatter.get("description", "")
            if (
                not current_desc
                or len(current_desc) < self.min_description_length
                or "<" in current_desc
                or "**" in current_desc
            ):
                new_desc = self.generate_description(body, current_desc)
                if new_desc != current_desc:
                    frontmatter["description"] = new_desc
                    modified = True
                    changes.append(f"설명 개선 ({len(current_desc)} → {len(new_desc)} chars)")

            # Check and add tags
            current_tags = frontmatter.get("tags", [])
            if isinstance(current_tags, str):
                current_tags = [current_tags]

            if len(current_tags) <= 1:
                title = frontmatter.get("title", "")
                auto_tags = self.extract_tags_from_content(title, body)

                # Merge with existing tags
                all_tags = list(set(current_tags + auto_tags))

                if len(all_tags) > len(current_tags):
                    frontmatter["tags"] = all_tags
                    modified = True
                    changes.append(f"태그 추가 ({len(current_tags)} → {len(all_tags)})")

            if not modified:
                return False

            print(f"\n📝 개선 중: {filepath.name}")
            for change in changes:
                print(f"  • {change}")

            if self.dry_run:
                print("  🔍 [DRY RUN] 변경사항 미저장")
                return True

            # Backup original file
            self.backup_file(filepath)

            # Reconstruct file with improved frontmatter
            new_frontmatter_yaml = yaml.dump(
                frontmatter, allow_unicode=True, default_flow_style=False, sort_keys=False
            )

            new_content = f"---\n{new_frontmatter_yaml}---\n\n{body}"

            # Save improved version
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)

            print("  ✅ 저장 완료")
            return True

        except Exception as e:
            print(f"  ❌ 오류: {str(e)}")
            return False

    def improve_directory(
        self, directory: Path, year_filter: int = 2020, max_files: int | None = None
    ):
        """
        Improve frontmatter in all markdown files in directory

        Args:
            directory: Target directory
            year_filter: Only process files from this year onwards
            max_files: Maximum number of files to process
        """
        md_files = list(directory.glob("**/*.md"))

        # Exclude _bak.md files
        md_files = [f for f in md_files if not f.stem.endswith("_bak")]

        # Filter by year if pub_date is available
        if year_filter:
            filtered_files = []
            for filepath in md_files:
                try:
                    with open(filepath, encoding="utf-8") as f:
                        content = f.read()
                    frontmatter, _, _ = self.parse_frontmatter(content)
                    if frontmatter and "pub_date" in frontmatter:
                        pub_date = str(frontmatter["pub_date"])
                        year = int(pub_date.split("-")[0])
                        if year >= year_filter:
                            filtered_files.append(filepath)
                except Exception:
                    continue
            md_files = filtered_files

        print(f"\n{'=' * 60}")
        print("Frontmatter 자동 개선")
        print(f"{'=' * 60}")
        print(f"대상 디렉토리: {directory}")
        print(f"마크다운 파일: {len(md_files)}개")
        print(f"년도 필터: {year_filter}년 이후")
        if max_files:
            print(f"최대 처리 파일: {max_files}개")
        if self.dry_run:
            print("⚠️  DRY RUN 모드 (실제 저장 안함)")
        print(f"{'=' * 60}\n")

        improved = 0
        skipped = 0
        failed = 0

        for _i, filepath in enumerate(md_files, 1):
            if max_files and improved >= max_files:
                print(f"\n⏹️  최대 처리 파일 수({max_files})에 도달")
                break

            result = self.improve_frontmatter(filepath)

            if result is True:
                improved += 1
            elif result is False:
                skipped += 1
            else:
                failed += 1

        # Summary
        print(f"\n{'=' * 60}")
        print("개선 완료")
        print(f"{'=' * 60}")
        print(f"✅ 개선 완료: {improved}개")
        print(f"⏭️  건너뛴 파일: {skipped}개")
        if failed > 0:
            print(f"❌ 실패: {failed}개")
        print(f"{'=' * 60}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Frontmatter 자동 개선")
    parser.add_argument(
        "--year", type=int, default=2020, help="이 년도 이후 파일만 처리 (기본: 2020)"
    )
    parser.add_argument("--max-files", type=int, default=None, help="최대 처리 파일 수")
    parser.add_argument("--dry-run", action="store_true", help="실제 변환하지 않고 테스트만")
    parser.add_argument(
        "--directory", type=str, default="contents", help="대상 디렉토리 (기본: contents)"
    )

    args = parser.parse_args()

    try:
        import yaml  # noqa: F401
    except ImportError:
        print("❌ PyYAML not installed. Installing...")
        os.system("uv pip install pyyaml")

    improver = FrontmatterImprover(dry_run=args.dry_run)
    improver.improve_directory(
        directory=Path(args.directory), year_filter=args.year, max_files=args.max_files
    )


if __name__ == "__main__":
    main()
