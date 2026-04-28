---
title: Hardware
---

{% assign current_depth = page.url | split: '/' | size %}
{% assign child_depth = current_depth | plus: 1 %}

{% for p in site.pages %}
{% if p.url contains page.url and p.url != page.url %}
{% assign p_depth = p.url | split: '/' | size %}
{% if p_depth == child_depth %}

### [{{ p.title }}]({{ p.url | relative_url }})

{{ p.excerpt | markdownify }}

{% endif %}
{% endif %}
{% endfor %}
