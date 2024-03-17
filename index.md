---
---

{% assign counter_recommendations = '-1' %}
{% for page in site.pages %}
{% if page.url contains '/recommendations/' %}
{% assign counter_recommendations = counter_recommendations | plus: 1 %}
{% endif %}
{% endfor %}

## [{{ counter_recommendations }} Recommendations]({{ '/recommendations/' | relative_url }})

{% assign counter_comparisons = '-1' %}
{% for page in site.pages %}
{% if page.url contains '/comparisons/' %}
{% assign counter_comparisons = counter_comparisons | plus: 1 %}
{% endif %}
{% endfor %}

## [{{ counter_comparisons }} Comparisons]({{ '/comparisons/' | relative_url }})
