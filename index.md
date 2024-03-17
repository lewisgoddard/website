---
---

{% assign counter = '0' %}
{% for page in site.pages %}
{% if page.url contains '/recommendations/' %}
{% unless page.url == '/recommendations/' %}
{% increment counter %}
{% endunless %}
{% endif %}
{% endfor %}

## [{{ counter }} Recommendations]({{ '/recommendations/' | relative_url }})
