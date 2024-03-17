---
---

## Recommendations

{% for page in site.pages %}
{% if page.url contains '/recommendations/' %}
{% unless page.url == '/recommendations/' %}

### [{{ page.title }}]({{ page.url | relative_url }})

{{ page.excerpt | markdownify }}

{% endunless %}
{% endif %}
{% endfor %}

{:.text-right}
