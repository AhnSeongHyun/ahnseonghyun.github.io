#!/usr/bin/env python3
"""
Tag Consolidation Script

Consolidates duplicate tags across all markdown files.
- Korean → English for technical terms
- Case normalization
- Spacing normalization
"""

import re
from pathlib import Path
from collections import defaultdict


# Consolidation rules: target_tag ← [variants to replace]
CONSOLIDATION_RULES = {
    # Programming Languages (Korean → English)
    'Python': [
        'python', 'Python', 'PYTHON', 'python3', 'python2.7', 'python3.6', 'python2',
        '파이썬', '파이썬 코리아 격월 세미나', '파이썬 마을', '파이썬 이미지 라이브러리',
        'daum open api python', 'python nginx', 'python function argument type',
        'python get user home path', 'python shell', 'python celery settings',
        'sqlite3 python 연동하기', 'python performance tips', 'aws python',
        'python 2.7 centos', 'screenshot python'
    ],

    'Java': [
        'java', 'Java', 'JAVA',
        '자바', '자바 파일 인코딩', '자바 빌드', '자바 디렉토리 추출',
        '이펙티브 자바', '자바 라이브러리', '자바 스레드', '자바 컬렉션 계층구조',
        '자바 MD5 자릿수', 'java 인코딩', 'Effective Java',
        'java redis 연동하기', 'java thread runnable callback',
        'java rss parser rome', 'RSS JAVA Library'
    ],

    'JavaScript': [
        'javascript', 'JavaScript', 'JAVASCRIPT', 'JS', 'js',
        'Java Script', '자바스크립트', '3자리 금액 자바스크립트'
    ],

    'iOS': [
        'ios', 'iOS', 'IOS', 'i os', 'i OS',
        'iphone', 'iPhone', 'IPHONE', 'iPhone4', 'iPhone4S', 'iPhone5s',
        'iPhone dev', 'iphone UI', 'iPhone GUI', 'make iphone ui',
        'iphone directory', "iphone's disadvantages",
        '아이폰', '아이폰 음악재생', '아이폰 카메라', '아이폰 앱', '아이폰 터치의 귀찮음',
        '아이폰 바코드 인식', '아이폰 강의', '아이폰 고장', '아이폰앱', '아이폰 개발',
        '아이폰어플', '로딩화면 아이폰', '아이폰 OS', '아이폰 멀티태스킹',
        '아이폰 배경화면', '아이폰 탈옥', '아이폰 폴더', '아이폰 앱 개발',
        '아이폰 설정', '아이폰 앱 디자인', '아이폰 4s', '아이폰 음악 어플',
        'ZBAR iPhone5s', '~/Library/Application Support/iPhone Simulator/',
        'iPhone 시뮬레이터 경로', 'compare iphone to nexus one'
    ],

    'C#': [
        'c#', 'C#', 'csharp', 'CSharp', 'C sharp'
    ],

    'Objective-C': [
        'Objective-C', 'objective-c', 'Objective C', 'objective c'
    ],

    # Frameworks/Libraries
    'Flask': [
        'FLASK', 'flask', 'Flask', 'flask 웹서버'
    ],

    'Django': [
        'django', 'Django', 'DJANGO'
    ],

    'React': [
        'react', 'React', 'REACT', 'ReactJS'
    ],

    'jQuery': [
        'jquery', 'jQuery', 'JQUERY', 'JQuery',
        'jQuery Mobile', 'jquery mobile force reload current page'
    ],

    # Platforms/Tools
    'GitHub': [
        'github', 'Github', 'GitHub', 'GITHUB'
    ],

    'Git': [
        'git', 'Git', 'GIT'
    ],

    'MySQL': [
        'mysql', 'MySQL', 'MYSQL', 'MySql'
    ],

    'Docker': [
        'docker', 'Docker', 'DOCKER'
    ],

    'AWS': [
        'aws', 'AWS', 'Aws'
    ],

    'Xcode': [
        'xcode', 'Xcode', 'XCODE', 'XCode'
    ],

    # Technologies
    'API': [
        'api', 'Api', 'API', 'OpenAPI', 'Open API'
    ],

    'REST': [
        'rest', 'Rest', 'REST'
    ],

    'SQL': [
        'sql', 'Sql', 'SQL'
    ],

    # Categories
    'developer': [
        'developer', 'Developer', 'DEVELOPER',
        '개발자', '개발자모임', '개발자 회의', '모바일 개발자',
        '개발자 세미나', '다음 개발자 행사', '개발자 창업과 아이디어',
        '개발자를 위한 까페', 'Windows Phone Developer Tools CTP'
    ],

    'programming': [
        'programming', 'Programming', 'PROGRAMMING',
        '프로그래밍', '어떻게 프로그래밍하는가?', '차분하게 프로그래밍 하라'
    ],

    'mobile': [
        'mobile', 'Mobile', 'MOBILE',
        '모바일', '윈도우 모바일', '모바일헬스케어', 'SKTE 모바일 오픈마켓',
        '모바일 개발 교육', '모바일 개발자', '윈도우 모바일 5', '모바일 게이트웨이',
        '윈도우 모바일6.5', '모바일플랫폼', '바다 모바일플랫폼', '모바일 프로그램',
        '모바일 플랫폼', 'mobile gateway', 'Windows Mobile 6.0',
        'Windows Mobile 5.0', 'mobile platform'
    ],

    'server': [
        'server', 'Server', 'SERVER',
        '서버', '웹서버', '서버정보', '리눅스 서버정보', '서버구축',
        '웹서버 성능', 'Active Server Pages', 'SharePoint Server',
        'linux server info', 'Web Server', '윈도우 서버 2003'
    ],

    'algorithm': [
        'algorithm', 'Algorithm', 'ALGORITHM',
        '알고리즘', '정렬 알고리즘', '계산기 알고리즘',
        'algorithm bubble sort'
    ],

    'database': [
        'database', 'Database', 'DATABASE',
        '데이터베이스', '데이터베이스 학회', '데이터베이스 연동',
        'multiple database'
    ],

    'Android': [
        'android', 'Android', 'ANDROID',
        '안드로이드', '안드로이드 교육'
    ],

    # Spacing/Formatting variants
    'open-source': [
        'opensource', 'Opensource', 'Open Source', 'open source',
        'OpenSource', 'OPENSOURCE'
    ],

    'design-pattern': [
        '디자인패턴', '디자인 패턴', 'design pattern', 'Design Pattern',
        'DesignPattern'
    ],

    'clean-code': [
        'cleancode', 'Cleancode', 'clean code', 'Clean Code', 'CleanCode'
    ],

    'machine-learning': [
        'machine learning', 'Machine Learning', 'ML', 'ml',
        '머신러닝', '머신 러닝'
    ],

    'deep-learning': [
        'deep learning', 'Deep Learning', 'DL', 'dl',
        '딥러닝', '딥 러닝'
    ],

    # Additional technical terms (Korean → English)
    'programmer': [
        'programmer', '프로그래머', '프로그래머 열정을 말하다'
    ],

    'blog': [
        'blog', 'Blog', '블로그', '블로그에 코드입력하기'
    ],

    'app': [
        'app', 'App', '앱', '앱 개발'
    ],

    'bluetooth': [
        'bluetooth', 'Bluetooth', '블루투스'
    ],

    'search-engine': [
        'search engine', 'search-engine', '검색엔진'
    ],

    'maven': [
        'maven', 'Maven', '메이븐'
    ],

    'thread': [
        'thread', 'Thread', '스레드'
    ],

    'test': [
        'test', 'Test', 'testing', '테스트'
    ],

    'deploy': [
        'deploy', 'Deploy', 'deployment', '배포'
    ],

    'parsing': [
        'parsing', 'Parsing', '파싱', 'HTML 파싱', '문자열 파싱'
    ],

    'library': [
        'library', 'Library', '라이브러리', 'django 라이브러리'
    ],

    'healthcare': [
        'healthcare', 'Healthcare', 'Health Care', '헬스케어',
        '헬스케어 서비스', 'U-헬스케어 포괄 업무제휴'
    ],

    'medical-informatics': [
        'medical informatics', 'Medical Informatics',
        '의료정보', '의료정보학', '의공학', '대한의료정보학회'
    ],

    'stored-procedure': [
        'stored procedure', 'stored-procedure', '저장프로시저'
    ],

    'pycon': [
        'pycon', 'Pycon', 'PyCon', '파이콘'
    ],

    'weekly-dev': [
        'weekly-dev', '주간개발기'
    ],

    'code-input': [
        'code-input', '코드입력'
    ],

    'retrospective': [
        'retrospective', 'Retrospective', '회고'
    ],

    'startup': [
        'startup', 'Startup', 'startups', '스타트업'
    ],

    'DDD': [
        'DDD', 'domain-driven-design', '도메인주도의설계'
    ],

    # Personal branding - keep Korean
    '안성현': [
        '안성현', 'An Seong Hyun', 'Ahn Seong Hyun', 'AhnSeongHyun',
        '성현', '안성현.회고'
    ],

    # Korean-specific projects/topics
    '한우찾기': [
        '한우', '한우찾기', '한우어플', '한우찾기 어플',
        '한우찾기 2.4.0', '한우찾기 후기'
    ],

    # Additional technical tools
    'Hadoop': [
        'Hadoop', 'hadoop', '하둡', '하웁', '하둡설치'
    ],

    'kafka': [
        'kafka', 'Kafka', '카프카'
    ],

    'paul-smith': [
        'Paul Smith', 'paul smith', 'inside paul smith',
        '폴 스미스', '폴스미스'
    ],

    # Remove empty/problematic tags
    None: [' ', '', '  ', '   ', '태그를 입력해 주세요.', '황의건']
}

# Create reverse lookup: variant → target
VARIANT_TO_TARGET = {}
for target, variants in CONSOLIDATION_RULES.items():
    for variant in variants:
        VARIANT_TO_TARGET[variant] = target


def extract_frontmatter(content):
    """Extract frontmatter from markdown content."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.match(pattern, content, re.DOTALL)
    if match:
        return match.group(1), match.end()
    return None, 0


def parse_tags_from_frontmatter(frontmatter_text):
    """Extract tags list from frontmatter."""
    for line in frontmatter_text.split('\n'):
        if line.strip().startswith('tags:'):
            # Extract tags array
            match = re.search(r'tags:\s*\[(.*?)\]', line)
            if match:
                tags_str = match.group(1)
                # Parse individual tags
                tags = [tag.strip().strip("'\"") for tag in tags_str.split(',')]
                return [tag for tag in tags if tag]  # Filter empty
    return []


def consolidate_tags(tags):
    """Consolidate tags based on rules."""
    consolidated = []
    for tag in tags:
        # Check if this tag should be consolidated
        target = VARIANT_TO_TARGET.get(tag)

        if target is None and tag in CONSOLIDATION_RULES.get(None, []):
            # Skip empty/problematic tags
            continue
        elif target:
            # Replace with target tag
            if target not in consolidated:
                consolidated.append(target)
        else:
            # Keep as-is if no rule
            if tag not in consolidated:
                consolidated.append(tag)

    return consolidated


def update_frontmatter_tags(frontmatter_text, new_tags):
    """Update tags in frontmatter."""
    # Format new tags
    tags_str = ', '.join(f"'{tag}'" for tag in new_tags)
    new_tags_line = f"tags: [{tags_str}]"

    # Replace tags line
    lines = frontmatter_text.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('tags:'):
            lines[i] = new_tags_line
            break

    return '\n'.join(lines)


def process_file(file_path):
    """Process a single markdown file."""
    try:
        content = file_path.read_text(encoding='utf-8')

        # Extract frontmatter
        frontmatter_text, frontmatter_end = extract_frontmatter(content)
        if not frontmatter_text:
            return None, None, None

        # Extract and consolidate tags
        original_tags = parse_tags_from_frontmatter(frontmatter_text)
        if not original_tags:
            return None, None, None

        consolidated_tags = consolidate_tags(original_tags)

        # Check if changed
        if original_tags == consolidated_tags:
            return None, None, None

        # Update frontmatter
        new_frontmatter = update_frontmatter_tags(frontmatter_text, consolidated_tags)

        # Reconstruct content
        rest_of_content = content[frontmatter_end:]
        new_content = f"---\n{new_frontmatter}\n---\n{rest_of_content}"

        return original_tags, consolidated_tags, new_content

    except Exception as e:
        print(f"  ⚠️  Error processing {file_path}: {e}")
        return None, None, None


def main():
    """Main consolidation function."""

    print("🔄 Starting Tag Consolidation...")
    print()

    contents_path = Path('contents')

    # Statistics
    files_processed = 0
    files_changed = 0
    tag_changes = defaultdict(int)

    # Process all markdown files
    for md_file in contents_path.rglob('*.md'):
        original_tags, new_tags, new_content = process_file(md_file)

        if new_content:
            # Write updated content
            md_file.write_text(new_content, encoding='utf-8')
            files_changed += 1

            # Track changes
            for orig_tag in original_tags:
                target = VARIANT_TO_TARGET.get(orig_tag)
                if target and target != orig_tag:
                    tag_changes[f"{orig_tag} → {target}"] += 1

            print(f"  ✓ Updated: {md_file.name}")
            print(f"    Before: {original_tags}")
            print(f"    After:  {new_tags}")
            print()

        files_processed += 1

    # Summary
    print("=" * 80)
    print("✅ Tag Consolidation Complete!")
    print()
    print(f"📊 Files processed: {files_processed}")
    print(f"📝 Files changed: {files_changed}")
    print()

    if tag_changes:
        print("🔀 Top Tag Changes:")
        print("-" * 80)
        for change, count in sorted(tag_changes.items(), key=lambda x: -x[1])[:20]:
            print(f"  {change:<50} {count:>4} times")
        print()

    print(f"💡 Next steps:")
    print(f"  1. Run: make build")
    print(f"  2. Check: docs/tags/")
    print(f"  3. Commit changes")


if __name__ == '__main__':
    main()
