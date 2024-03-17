---
---

{% assign counter = '0' %}
{% for page in site.pages %}
{% if page.url contains '/recommendations/' %}
{% unless page.url == '/recommendations/' %}
{{ counter | plus:'1' }}
{% endunless %}
{% endif %}
{% endfor %}

## [{{ counter }} Recommendations]({{ '/recommendations/' | relative_url }})
