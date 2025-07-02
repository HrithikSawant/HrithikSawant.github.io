import markdown
from pathlib import Path

template = Path("templates/post.html").read_text()

for post_path in Path("posts").glob("*.md"):
    md_content = post_path.read_text()
    html_content = markdown.markdown(md_content)
    final_html = template.replace("{{ title }}", post_path.stem).replace("{{ content }}", html_content)

    output_path = Path("site") / f"{post_path.stem}.html"
    output_path.write_text(final_html)
