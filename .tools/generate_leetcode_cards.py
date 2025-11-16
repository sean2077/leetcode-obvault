#!/usr/bin/env python3
"""
LeetCode Problem Metadata to Obsidian Notes Converter

Generate Markdown notes from LeetCode.com and LeetCode.cn JSON metadata files
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Annotated, Dict, List, Optional

import typer
from natsort import natsorted
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.table import Table

# Create Rich Console instance
console = Console()
app = typer.Typer(help="Convert LeetCode problem metadata to Obsidian notes")


def parse_similar_questions(
    en_similar: str, cn_similar: str, slug_to_id: Dict[str, int] = None
) -> List[str]:
    """Parse similar questions JSON string, merge English and Chinese data"""
    if not en_similar:
        return []

    if slug_to_id is None:
        slug_to_id = {}

    try:
        en_questions = json.loads(en_similar)
        cn_questions = {}

        # Parse Chinese version, build titleSlug to translated title mapping
        if cn_similar:
            try:
                cn_list = json.loads(cn_similar)
                cn_questions = {
                    q.get("titleSlug"): q.get("translatedTitle")
                    for q in cn_list
                    if q.get("titleSlug")
                }
            except json.JSONDecodeError:
                pass

        results = []
        for q in en_questions:
            title_slug = q.get("titleSlug", "")
            if not title_slug:
                continue

            # Prefer Chinese translated title, fallback to English title
            translated_title = cn_questions.get(title_slug, q.get("title", ""))

            # Look up question ID from mapping
            question_id = slug_to_id.get(title_slug)
            if question_id:
                results.append(
                    f"[[{question_id}.{title_slug}|{question_id}.{translated_title}]]"
                )

        return results
    except json.JSONDecodeError:
        return []


def parse_topics(topics: List[Dict]) -> List[str]:
    """Parse problem tags/topics"""
    if not topics:
        return []

    return [f"[[{topic.get('slug', '')}]]" for topic in topics if topic.get("slug")]


def parse_code_snippets(snippets: List[Dict]) -> str:
    """Parse code snippets and generate tabs format"""
    if not snippets:
        return ""

    tabs_content = ["```tabs"]

    # Define language mapping
    lang_map = {
        "cpp": ("C++", "cpp"),
        "java": ("Java", "java"),
        "python": ("Python", "python"),
        "python3": ("Python3", "python"),
        "c": ("C", "c"),
        "csharp": ("C#", "csharp"),
        "javascript": ("JavaScript", "javascript"),
        "typescript": ("TypeScript", "typescript"),
        "php": ("PHP", "php"),
        "swift": ("Swift", "swift"),
        "kotlin": ("Kotlin", "kotlin"),
        "dart": ("Dart", "dart"),
        "golang": ("Go", "go"),
        "ruby": ("Ruby", "ruby"),
        "scala": ("Scala", "scala"),
        "rust": ("Rust", "rust"),
        "racket": ("Racket", "racket"),
        "erlang": ("Erlang", "erlang"),
        "elixir": ("Elixir", "elixir"),
        "mysql": ("MySQL", "sql"),
        "mssql": ("MS SQL Server", "sql"),
        "oraclesql": ("Oracle", "sql"),
        "postgresql": ("PostgreSQL", "sql"),
        "bash": ("Bash", "bash"),
    }

    for snippet in snippets:
        lang = snippet.get("lang", "")
        lang_slug = snippet.get("langSlug", lang)
        code = snippet.get("code", "")

        display_name, code_lang = lang_map.get(lang_slug, (lang, lang_slug))

        tabs_content.append(f"tab: {display_name}")
        tabs_content.append("")
        tabs_content.append(f"```{code_lang}")
        tabs_content.append(code)
        tabs_content.append("```")
        tabs_content.append("")

    tabs_content.append("```")
    return "\n".join(tabs_content)


def clean_html_content(html: str) -> str:
    """Clean HTML content, preserve basic formatting"""
    if not html:
        return ""

    # Return as-is since Obsidian can render HTML
    return html


def generate_frontmatter(
    en_data: Dict, cn_data: Dict, slug_to_id: Dict[str, int] = None
) -> str:
    """Generate YAML frontmatter"""
    question_en = en_data.get("data", {}).get("question", {}) if en_data else {}
    question_cn = cn_data.get("data", {}).get("question", {}) if cn_data else {}

    # Prefer English data, use Chinese as fallback
    question_id = question_en.get("questionFrontendId", "") or question_cn.get(
        "questionFrontendId", ""
    )
    title = question_en.get("title", "") or question_cn.get("translatedTitle", "")
    translated_title = question_cn.get("translatedTitle", "") or title
    title_slug = question_en.get("titleSlug", "") or question_cn.get("titleSlug", "")
    difficulty = question_en.get("difficulty", "") or question_cn.get("difficulty", "")

    # Parse statistics
    stats_en = json.loads(question_en.get("stats", "{}")) if question_en else {}
    stats_cn = json.loads(question_cn.get("stats", "{}")) if question_cn else {}
    ac_rate = stats_en.get("acRate", "") or stats_cn.get("acRate", "0%")

    # Merge likes/dislikes (take maximum from both sources)
    likes_en = question_en.get("likes", 0) if question_en else 0
    dislikes_en = question_en.get("dislikes", 0) if question_en else 0
    likes_cn = question_cn.get("likes", 0) if question_cn else 0
    dislikes_cn = question_cn.get("dislikes", 0) if question_cn else 0

    likes = max(likes_en, likes_cn)
    dislikes = max(dislikes_en, dislikes_cn)

    # Parse topic tags
    topics = parse_topics(question_en.get("topicTags", []))

    # Parse similar questions
    similar_questions = parse_similar_questions(
        question_en.get("similarQuestions", ""),
        question_cn.get("similarQuestions", ""),
        slug_to_id,
    )

    # Rating (based on like ratio)
    total_votes = likes + dislikes
    grade = ""
    if total_votes > 0:
        like_ratio = likes / total_votes
        if like_ratio >= 0.95:
            grade = "⭐⭐⭐⭐⭐"
        elif like_ratio >= 0.85:
            grade = "⭐⭐⭐⭐"
        elif like_ratio >= 0.70:
            grade = "⭐⭐⭐"
        elif like_ratio >= 0.50:
            grade = "⭐⭐"
        else:
            grade = "⭐"

    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    frontmatter = f"""---
tags:
  - leetcode/problem
questionId: "{question_id}"
title: {title}
translatedTitle: {translated_title}
titleSlug: {title_slug}
aliases:
  - {title}
  - {title_slug}
  - {translated_title}
lcLinks:
  - https://leetcode.com/problems/{title_slug}/
  - https://leetcode.cn/problems/{title_slug}/
lcTopics:"""

    for topic in topics:
        frontmatter += f'\n  - "{topic}"'

    frontmatter += f"""
lcDifficulty: {difficulty}
lcAcRate: {ac_rate}
similarQuestions:"""

    for sq in similar_questions:
        frontmatter += f'\n  - "{sq}"'

    frontmatter += f"""
grade: {grade}
likes: {likes}
dislikes: {dislikes}
favorites: []
created: {current_date}
updated: {current_date}
---"""

    return frontmatter


def generate_description(
    en_data: Dict, cn_data: Dict, prev_link: str = "-", next_link: str = "-"
) -> str:
    """Generate problem description section"""
    question_en = en_data.get("data", {}).get("question", {}) if en_data else {}
    question_cn = cn_data.get("data", {}).get("question", {}) if cn_data else {}

    title_slug = question_en.get("titleSlug", "") or question_cn.get("titleSlug", "")
    question_id = question_en.get("questionFrontendId", "") or question_cn.get(
        "questionFrontendId", ""
    )

    content_cn = (
        clean_html_content(question_cn.get("translatedContent", ""))
        if question_cn
        else ""
    )
    content_en = (
        clean_html_content(question_en.get("content", "")) if question_en else ""
    )

    # Parse hints
    hints = (
        question_en.get("hints", [])
        if question_en
        else (question_cn.get("hints", []) if question_cn else [])
    )
    hints_section_cn = ""
    hints_section_en = ""
    if hints:
        hints_section_cn = "\n"
        hints_section_en = "\n"
        for i, hint in enumerate(hints, 1):
            hints_section_cn += f"\n> [!tip]- 提示 {i}\n> {hint}\n"
            hints_section_en += f"\n> [!tip]- Hint {i}\n> {hint}\n"

    # Determine whether to generate single language or bilingual tabs
    has_en = bool(content_en)
    has_cn = bool(content_cn)

    if has_en and has_cn:
        # Bilingual tabs
        description = f"""
**Nav:** << previous: {prev_link} | next: {next_link} >>

---

## Description

```tabs
tab: English

{content_en}
{hints_section_en}

---

[submissions](https://leetcode.com/problems/{title_slug}/submissions/) | [solutions](https://leetcode.com/problems/{title_slug}/solutions/)


tab: 中文

{content_cn}
{hints_section_cn}

---

[提交记录](https://leetcode.cn/problems/{title_slug}/submissions/) | [题解](https://leetcode.cn/problems/{title_slug}/solution/)


```"""
    elif has_en:
        # English only
        description = f"""
**Nav:** << previous: {prev_link} | next: {next_link} >>

---

## Description

{content_en}
{hints_section_en}

---

[submissions](https://leetcode.com/problems/{title_slug}/submissions/) | [solutions](https://leetcode.com/problems/{title_slug}/solutions/)
"""
    elif has_cn:
        # Chinese only
        description = f"""
**Nav:** << previous: {prev_link} | next: {next_link} >>

---

## Description

{content_cn}
{hints_section_cn}

---

[提交记录](https://leetcode.cn/problems/{title_slug}/submissions/) | [题解](https://leetcode.cn/problems/{title_slug}/solution/)
"""
    else:
        # No content available
        description = f"""
**Nav:** << previous: {prev_link} | next: {next_link} >>

---

## Description

*No description available.*
"""

    return description


def generate_solutions_section() -> str:
    """Generate solutions and notes section"""
    return """
## Solutions & Notes

```base
properties:
  note.updated:
    displayName: Last Updated
  note.relative_links:
    displayName: Related Links
  note.desc:
    displayName: Description
  note.grade:
    displayName: Rating
  note.program_language:
    displayName: Language
  note.time_complexity:
    displayName: TC
  note.space_complexity:
    displayName: SC
views:
  - type: table
    name: Solutions & Notes
    filters:
      and:
        - file.hasLink(this.file)
        - file.tags.containsAny("leetcode/solution", "leetcode/note")
    order:
      - file.name
      - desc
      - program_language
      - time_complexity
      - space_complexity
      - grade
      - relative_links
      - updated
    sort:
      - property: grade
        direction: ASC
      - property: time_complexity
        direction: ASC
      - property: program_language
        direction: ASC
    columnSize:
      file.name: 104
      note.space_complexity: 65
      note.grade: 126

```"""


def generate_similar_problems_section() -> str:
    """Generate similar problems section"""
    return """
## Similar Problems

```base
properties:
  note.lcTopics:
    displayName: Topics
  note.lcAcRate:
    displayName: AC Rate
  note.favorites:
    displayName: Favorites
  note.grade:
    displayName: Rating
  note.translatedTitle:
    displayName: Title (CN)
  note.lcDifficulty:
    displayName: Difficulty
views:
  - type: table
    name: Table
    filters:
      and:
        - file.hasLink(this.file)
        - similarQuestions.contains(this.file)
    order:
      - file.name
      - translatedTitle
      - lcTopics
      - lcDifficulty
      - lcAcRate
      - grade
      - favorites
    sort:
      - property: file.name
        direction: ASC
      - property: lcTopics
        direction: DESC
    columnSize:
      note.translatedTitle: 240
      note.lcTopics: 347
      note.lcAcRate: 75
      note.grade: 122

```"""


def generate_markdown(
    en_json_path: str,
    cn_json_path: str,
    output_path: Optional[str] = None,
    prev_link: str = "-",
    next_link: str = "-",
    slug_to_id: Dict[str, int] = None,
) -> str:
    """Generate Markdown notes from two JSON files"""

    # Read JSON files
    en_data = None
    cn_data = None

    if en_json_path:
        with open(en_json_path, "r", encoding="utf-8") as f:
            en_data = json.load(f)

    if cn_json_path:
        with open(cn_json_path, "r", encoding="utf-8") as f:
            cn_data = json.load(f)

    # Generate content sections
    frontmatter = generate_frontmatter(en_data, cn_data, slug_to_id)
    description = generate_description(en_data, cn_data, prev_link, next_link)
    solutions = generate_solutions_section()
    similar_problems = generate_similar_problems_section()

    # Combine final content
    markdown_content = f"{frontmatter}\n{description}\n{solutions}\n{similar_problems}"

    # Write to file if output path is specified
    if output_path:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text(markdown_content, encoding="utf-8")
        console.print(f"[green]✅ Generated note:[/green] {output_path}")

    return markdown_content


def batch_generate(problems_dir: str, problems_cn_dir: str, output_base_dir: str):
    """Batch generate notes"""
    problems_path = Path(problems_dir)
    problems_cn_path = Path(problems_cn_dir)
    output_base = Path(output_base_dir)

    # Get all JSON files
    en_files = {f.stem: f for f in problems_path.glob("*.json")}
    cn_files = {f.stem: f for f in problems_cn_path.glob("*.json")}

    # Find all problems (merge English and Chinese)
    all_problems = set(en_files.keys()) | set(cn_files.keys())

    console.print(
        Panel.fit(
            f"[cyan]Found {len(all_problems)} problems[/cyan]\n"
            f"English: {len(en_files)} | Chinese: {len(cn_files)}",
            title="[bold]Scan Results[/bold]",
            border_style="cyan",
        )
    )

    # First collect all problem info and build titleSlug to ID mapping
    problem_info = {}
    slug_to_id = {}
    for problem_id in all_problems:
        try:
            en_file = en_files.get(problem_id)
            cn_file = cn_files.get(problem_id)

            title_slug = ""
            question_id = ""
            translated_title = ""
            en_title = ""

            # Read English data
            if en_file:
                with open(en_file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    question = data.get("data", {}).get("question", {})
                    title_slug = question.get("titleSlug", "")
                    question_id = str(question.get("questionFrontendId", ""))
                    en_title = question.get("title", "")

            # Read Chinese data
            if cn_file:
                with open(cn_file, "r", encoding="utf-8") as cf:
                    cn_data = json.load(cf)
                    cn_question = cn_data.get("data", {}).get("question", {})
                    translated_title = cn_question.get("translatedTitle", "")
                    # If English file doesn't exist, get basic info from Chinese
                    if not en_file:
                        title_slug = cn_question.get("titleSlug", "")
                        question_id = str(cn_question.get("questionFrontendId", ""))

            # Fallback: if no Chinese title, use English title
            if not translated_title:
                translated_title = en_title

            if title_slug and question_id:
                problem_info[question_id] = {
                    "title_slug": title_slug,
                    "translated_title": translated_title,
                    "en_file": en_file,
                    "cn_file": cn_file,
                }
                slug_to_id[title_slug] = question_id
        except Exception as e:
            console.print(f"[red]❌ Error reading {problem_id} info:[/red] {str(e)}")

    # Sort by question ID (natural sort)
    # Use natsort for natural sorting: "1" < "2" < "10" < "100" < "LCP 01" < "面试题 17.24"
    sorted_ids = natsorted(problem_info.keys())

    console.print("\n[bold cyan]Starting to generate notes...[/bold cyan]\n")

    # Generate each problem
    success_count = 0
    error_count = 0

    for idx, question_id in track(
        enumerate(sorted_ids),
        total=len(sorted_ids),
        description="[cyan]Generation Progress",
    ):
        try:
            info = problem_info[question_id]
            title_slug = info["title_slug"]
            translated_title = info["translated_title"]

            # Determine previous and next problem links
            prev_link = "-"
            next_link = "-"

            if idx > 0:
                prev_id = sorted_ids[idx - 1]
                prev_info = problem_info[prev_id]
                prev_title = prev_info["translated_title"] or prev_info["title_slug"]
                prev_link = (
                    f"[[{prev_id}.{prev_info['title_slug']}|{prev_id}.{prev_title}]]"
                )

            if idx < len(sorted_ids) - 1:
                next_id = sorted_ids[idx + 1]
                next_info = problem_info[next_id]
                next_title = next_info["translated_title"] or next_info["title_slug"]
                next_link = (
                    f"[[{next_id}.{next_info['title_slug']}|{next_id}.{next_title}]]"
                )

            # Generate output file path
            output_file = output_base / f"{question_id}.{title_slug}.md"

            generate_markdown(
                str(info["en_file"]) if info["en_file"] else None,
                str(info["cn_file"]) if info["cn_file"] else None,
                str(output_file),
                prev_link,
                next_link,
                slug_to_id,
            )
            success_count += 1

        except Exception as e:
            console.print(
                f"[red]❌ Error processing problem {question_id}:[/red] {str(e)}"
            )
            error_count += 1

    # Display statistics table
    table = Table(
        title="\nGeneration Statistics", show_header=True, header_style="bold magenta"
    )
    table.add_column("Status", style="cyan", width=12)
    table.add_column("Count", justify="right", style="green")

    table.add_row("✅ Success", str(success_count))
    table.add_row("❌ Failed", str(error_count))
    table.add_row("📊 Total", str(len(sorted_ids)))

    console.print(table)


@app.command("single")
def generate_single(
    en: Annotated[
        Optional[str], typer.Option("--en", help="English JSON file path")
    ] = None,
    cn: Annotated[
        Optional[str], typer.Option("--cn", help="Chinese JSON file path")
    ] = None,
    output: Annotated[
        Optional[str], typer.Option("--output", "-o", help="Output Markdown file path")
    ] = None,
):
    """Generate a single problem note"""
    if not en or not cn:
        console.print(
            "[red]Error: Both --en and --cn parameters must be provided[/red]"
        )
        raise typer.Exit(1)

    console.print(
        Panel.fit(
            f"[cyan]English file:[/cyan] {en}\n"
            f"[cyan]Chinese file:[/cyan] {cn}\n"
            f"[cyan]Output path:[/cyan] {output or '(output to console)'}",
            title="[bold]Single Problem Generation[/bold]",
            border_style="cyan",
        )
    )

    generate_markdown(en, cn, output)

    if output:
        console.print("\n[bold green]✨ Generation complete![/bold green]")


@app.command("batch")
def generate_batch(
    problems_dir: Annotated[
        str, typer.Option("--problems-dir", help="English problems JSON directory")
    ] = ".ref/leetcode-problems/problems",
    problems_cn_dir: Annotated[
        str, typer.Option("--problems-cn-dir", help="Chinese problems JSON directory")
    ] = ".ref/leetcode-problems/problems-cn",
    output_dir: Annotated[
        str, typer.Option("--output-dir", help="Output directory")
    ] = "leetcode/lc-problems",
):
    """Batch generate problem notes"""
    console.print(
        Panel.fit(
            f"[cyan]English directory:[/cyan] {problems_dir}\n"
            f"[cyan]Chinese directory:[/cyan] {problems_cn_dir}\n"
            f"[cyan]Output directory:[/cyan] {output_dir}",
            title="[bold]Batch Generation Configuration[/bold]",
            border_style="cyan",
        )
    )

    batch_generate(problems_dir, problems_cn_dir, output_dir)

    console.print("\n[bold green]✨ Batch generation complete![/bold green]")


if __name__ == "__main__":
    app()
