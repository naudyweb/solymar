import os
import re

def fix_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix duplicated content (truncate after first </html>)
    if '</html>' in content:
        parts = content.split('</html>')
        content = parts[0] + '</html>'

    # 2. Standardize Header
    # Ensure header__cta is a direct child of header__container and outside header__nav
    # Pattern to find header__container and its contents
    container_match = re.search(r'(<div class="header__container">)(.*?)(</div>\s*</nav>)', content, re.DOTALL)
    if container_match:
        prefix = container_match.group(1)
        inner = container_match.group(2)
        suffix = container_match.group(3)

        # Find CTA if it's inside header__nav
        nav_match = re.search(r'(<div class="header__nav">)(.*?)(</div>)', inner, re.DOTALL)
        if nav_match:
            nav_inner = nav_match.group(2)
            cta_match = re.search(r'<a[^>]+class="header__cta"[^>]*>.*?</a>', nav_inner, re.DOTALL)
            if cta_match:
                cta_html = cta_match.group(0)
                # Remove from nav
                new_nav_inner = nav_inner.replace(cta_html, '')
                # Reconstruct inner with CTA outside
                new_inner = inner.replace(nav_inner, new_nav_inner)
                if cta_html not in new_inner: # If it was already outside, it stays
                    new_inner += '\n            ' + cta_html
                
                # Check if it's already there but we want it at the end of container
                # (Actualy the user just wants it NOT in header__nav)
                content = content.replace(container_match.group(0), prefix + new_inner + suffix)

    # 3. Verify Gallery Sections
    # Find <section class="gallery"> and ensure it has <div class="gallery__container">
    def fix_gallery(match):
        section_open = match.group(1)
        inner_content = match.group(2)
        section_close = match.group(3)
        
        if 'gallery__container' not in inner_content:
            # Wrap inner content with gallery__container
            # But wait, maybe the title is outside?
            # Standard: <section class="gallery"><div class="gallery__container">...</div></section>
            return f'{section_open}\n        <div class="gallery__container">{inner_content}</div>\n    {section_close}'
        return match.group(0)

    content = re.sub(r'(<section class="gallery"[^>]*>)(.*?)(</section>)', fix_gallery, content, flags=re.DOTALL)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# List all HTML files
html_files = [f for f in os.listdir('.') if f.endswith('.html')]
en_html_files = [os.path.join('en', f) for f in os.listdir('en') if f.endswith('.html')]

for f in html_files + en_html_files:
    print(f"Fixing {f}...")
    fix_html(f)
