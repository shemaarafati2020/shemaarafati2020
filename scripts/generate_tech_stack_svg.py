#!/usr/bin/env python3
import os
import re
import urllib.request
import xml.etree.ElementTree as ET

ICONS_DIR = "assets/icons"
OUTPUT_SVG = "assets/tech-stack.svg"
os.makedirs(ICONS_DIR, exist_ok=True)

tech_items = [
    # Row 1: Core Languages & Fundamentals
    {'name': 'TypeScript', 'key': 'typescript', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg'},
    {'name': 'JavaScript', 'key': 'javascript', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg'},
    {'name': 'Python', 'key': 'python', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg'},
    {'name': 'Java', 'key': 'java', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg'},
    {'name': 'C++', 'key': 'cplusplus', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg'},
    {'name': 'C#', 'key': 'csharp', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg'},
    {'name': 'Go', 'key': 'go', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/go/go-original.svg'},
    {'name': 'PHP', 'key': 'php', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/php/php-original.svg'},
    {'name': 'Bash', 'key': 'bash', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg'},

    # Row 2: Frontend & Modern Web
    {'name': 'React', 'key': 'react', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg'},
    {'name': 'Next.js', 'key': 'nextjs', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nextjs/nextjs-original.svg'},
    {'name': 'Tailwind', 'key': 'tailwind', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg'},
    {'name': 'Redux', 'key': 'redux', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg'},
    {'name': 'HTML5', 'key': 'html5', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg'},
    {'name': 'CSS3', 'key': 'css3', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg'},
    {'name': 'Vue.js', 'key': 'vuejs', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vuejs/vuejs-original.svg'},
    {'name': 'Vite', 'key': 'vitejs', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vitejs/vitejs-original.svg'},
    {'name': 'GraphQL', 'key': 'graphql', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/graphql/graphql-plain.svg'},

    # Row 3: Backend & Databases
    {'name': 'Node.js', 'key': 'nodejs', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg'},
    {'name': 'Express', 'key': 'express', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original.svg'},
    {'name': 'Spring Boot', 'key': 'spring', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg'},
    {'name': 'NestJS', 'key': 'nestjs', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nestjs/nestjs-original.svg'},
    {'name': 'FastAPI', 'key': 'fastapi', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg'},
    {'name': 'PostgreSQL', 'key': 'postgresql', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg'},
    {'name': 'MySQL', 'key': 'mysql', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg'},
    {'name': 'MongoDB', 'key': 'mongodb', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg'},
    {'name': 'Redis', 'key': 'redis', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg'},

    # Row 4: Cloud & DevOps
    {'name': 'Docker', 'key': 'docker', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg'},
    {'name': 'Kubernetes', 'key': 'kubernetes', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/kubernetes/kubernetes-plain.svg'},
    {'name': 'AWS', 'key': 'aws', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-plain-wordmark.svg'},
    {'name': 'GCP', 'key': 'googlecloud', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg'},
    {'name': 'Azure', 'key': 'azure', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/azure/azure-original.svg'},
    {'name': 'Linux', 'key': 'linux', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg'},
    {'name': 'Nginx', 'key': 'nginx', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nginx/nginx-original.svg'},
    {'name': 'GitHub Actions', 'key': 'githubactions', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/githubactions/githubactions-original.svg'},
    {'name': 'Vercel', 'key': 'vercel', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vercel/vercel-original.svg'},

    # Row 5: Development & ORM Tools
    {'name': 'Git', 'key': 'git', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg'},
    {'name': 'GitHub', 'key': 'github', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg'},
    {'name': 'GitLab', 'key': 'gitlab', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gitlab/gitlab-original.svg'},
    {'name': 'Prisma', 'key': 'prisma', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/prisma/prisma-original.svg'},
    {'name': 'Firebase', 'key': 'firebase', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/firebase/firebase-plain.svg'},
    {'name': 'Supabase', 'key': 'supabase', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/supabase/supabase-original.svg'},
    {'name': 'Jest', 'key': 'jest', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jest/jest-plain.svg'},
    {'name': 'Postman', 'key': 'postman', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postman/postman-original.svg'},
    {'name': 'VS Code', 'key': 'vscode', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg'},

    # Row 6: AI, ML & Hardware
    {'name': 'OpenAI', 'key': 'openai', 'url': 'https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/openai.svg', 'color': '#10A37F'},
    {'name': 'TensorFlow', 'key': 'tensorflow', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original.svg'},
    {'name': 'PyTorch', 'key': 'pytorch', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pytorch/pytorch-original.svg'},
    {'name': 'Pandas', 'key': 'pandas', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg'},
    {'name': 'NumPy', 'key': 'numpy', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg'},
    {'name': 'Scikit-learn', 'key': 'scikitlearn', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/scikitlearn/scikitlearn-original.svg'},
    {'name': 'Android', 'key': 'android', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/android/android-original.svg'},
    {'name': 'Figma', 'key': 'figma', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg'},
    {'name': 'Arduino', 'key': 'arduino', 'url': 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/arduino/arduino-original.svg'}
]

def download_and_sanitize(item):
    key = item['key']
    local_path = os.path.join(ICONS_DIR, f"{key}.svg")
    
    if not os.path.exists(local_path):
        print(f"Downloading {item['name']}...")
        req = urllib.request.Request(item['url'], headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw_data = resp.read().decode('utf-8')
        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(raw_data)
    else:
        with open(local_path, 'r', encoding='utf-8') as f:
            raw_data = f.read()

    # Clean XML declaration, doctype, comments
    raw_data = re.sub(r'<\?xml.*?\?>', '', raw_data, flags=re.DOTALL)
    raw_data = re.sub(r'<!DOCTYPE.*?>', '', raw_data, flags=re.DOTALL)
    raw_data = re.sub(r'<!--.*?-->', '', raw_data, flags=re.DOTALL)
    
    # Extract viewBox
    vb_match = re.search(r'viewBox=[\"\']([^\"\']+)[\"\']', raw_data)
    if vb_match:
        viewBox = vb_match.group(1)
    else:
        w_match = re.search(r'width=[\"\']([0-9\.]+)px?[\"\']', raw_data)
        h_match = re.search(r'height=[\"\']([0-9\.]+)px?[\"\']', raw_data)
        if w_match and h_match:
            viewBox = f"0 0 {w_match.group(1)} {h_match.group(1)}"
        else:
            viewBox = "0 0 128 128"

    # Extract inner SVG contents
    inner_match = re.search(r'<svg[^>]*>(.*)</svg>', raw_data, re.DOTALL)
    if inner_match:
        inner = inner_match.group(1).strip()
    else:
        inner = raw_data.strip()

    # Remove redundant xmlns declarations on child tags
    inner = re.sub(r'\s+xmlns(:\w+)?=[\"\'][^\"\']*[\"\']', '', inner)
    # Clean xlink:href to href
    inner = re.sub(r'xlink:href=', 'href=', inner)
    # Clean xml:space
    inner = re.sub(r'xml:space=[\"\'][^\"\']*[\"\']', '', inner)

    # Prefix IDs to avoid collisions
    prefix = f"ic_{key}_"
    ids = set(re.findall(r'id=[\"\']([^\"\']+)[\"\']', inner))
    for old_id in ids:
        new_id = prefix + old_id
        inner = re.sub(r'id=[\"\']' + re.escape(old_id) + r'[\"\']', f'id="{new_id}"', inner)
        inner = re.sub(r'url\(#' + re.escape(old_id) + r'\)', f'url(#{new_id})', inner)
        inner = re.sub(r'href=[\"\']#' + re.escape(old_id) + r'[\"\']', f'href="#{new_id}"', inner)

    # Special handling for simple-icons monochrome like OpenAI
    if 'color' in item:
        inner = f'<g fill="{item["color"]}">{inner}</g>'

    return viewBox, inner

def build_svg():
    width = 880
    cols = 9
    col_width = 88
    row_height = 96
    start_x = (width - (cols * col_width)) // 2  # 44px
    start_y = 74
    card_w = 56
    card_h = 56
    icon_size = 32
    icon_pad = (card_w - icon_size) // 2  # 12px

    total_rows = (len(tech_items) + cols - 1) // cols
    total_height = start_y + (total_rows * row_height) + 20

    items_svg = []

    for idx, item in enumerate(tech_items):
        r = idx // cols
        c = idx % cols
        cell_x = start_x + (c * col_width)
        cell_y = start_y + (r * row_height)

        card_x = cell_x + (col_width - card_w) // 2
        card_y = cell_y

        viewBox, inner_content = download_and_sanitize(item)

        item_xml = f'''    <!-- {item['name']} -->
    <g class="tech-card" transform="translate({card_x}, {card_y})">
      <rect width="{card_w}" height="{card_h}" rx="13" fill="url(#cardBg)" stroke="#223044" stroke-width="1.2" />
      <svg x="{icon_pad}" y="{icon_pad}" width="{icon_size}" height="{icon_size}" viewBox="{viewBox}" preserveAspectRatio="xMidYMid meet">
        {inner_content}
      </svg>
      <text x="{card_w // 2}" y="{card_h + 17}" text-anchor="middle" class="label">{item['name']}</text>
    </g>'''
        items_svg.append(item_xml)

    all_items_str = "\n".join(items_svg)

    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {width} {total_height}" width="100%" height="100%">
  <defs>
    <!-- Background Gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0b0f17" />
      <stop offset="100%" stop-color="#080c14" />
    </linearGradient>

    <!-- Card Background Gradient -->
    <linearGradient id="cardBg" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#141c2b" />
      <stop offset="100%" stop-color="#0d1420" />
    </linearGradient>

    <!-- Header Subtle Glow -->
    <linearGradient id="headerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8" />
      <stop offset="100%" stop-color="#818cf8" />
    </linearGradient>
  </defs>

  <style>
    .header-text {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      font-size: 21px;
      font-weight: 700;
      fill: #FFFFFF;
      letter-spacing: -0.2px;
    }}
    .label {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
      font-size: 11.5px;
      font-weight: 500;
      fill: #CBD5E1;
      letter-spacing: 0.1px;
    }}
    .outer-box {{
      fill: url(#bgGrad);
      stroke: #1E293B;
      stroke-width: 1.5;
      rx: 14px;
    }}
    .tech-card rect {{
      transition: all 0.2s ease;
    }}
  </style>

  <!-- Container Box -->
  <rect x="2" y="2" width="{width - 4}" height="{total_height - 4}" class="outer-box" />

  <!-- Section Header -->
  <g transform="translate(32, 42)">
    <text class="header-text" x="0" y="0">💻 My favorite tools and technologies</text>
  </g>

  <!-- Divider Line -->
  <line x1="32" y1="56" x2="{width - 32}" y2="56" stroke="#1E293B" stroke-width="1" opacity="0.6" />

  <!-- Technology Cards Grid -->
  <g>
{all_items_str}
  </g>
</svg>
'''

    with open(OUTPUT_SVG, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    print(f"Successfully generated {OUTPUT_SVG} ({len(svg_content)} bytes)")

    # Verify XML validity
    try:
        ET.parse(OUTPUT_SVG)
        print("XML validation PASSED!")
    except Exception as e:
        print("XML validation FAILED:", e)

if __name__ == "__main__":
    build_svg()
