---
---

## Hardware

{% for page in site.pages %}
{% if page.url contains '/hardware/' %}
{% unless page.url contains page.url == '/hardware/' %}

### [{{ page.title }}]({{ page.url | relative_url }})

{{ page.excerpt | markdownify }}

{% endunless %}
{% endif %}
{% endfor %}

### [Continue &raquo;]({{ '/hardware/' | relative_url }})
{:.text-right}
