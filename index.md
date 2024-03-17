---
---

{% assign counter_recommendations = '-1' %}
{% for page in site.pages %}
{% if page.url contains '/recommendations/' %}
{% assign counter_recommendations = counter_recommendations | plus: 1 %}
{% endif %}
{% endfor %}

{% assign counter_comparisons = '-1' %}
{% for page in site.pages %}
{% if page.url contains '/comparisons/' %}
{% assign counter_comparisons = counter_comparisons | plus: 1 %}
{% endif %}
{% endfor %}

<style>
  .grid-item {
    padding: 2rem;
    width: 25rem;
    border-radius: 0.5rem;
    background: #eee;
    height: 10rem;
    position: relative;
  }
.grid-title {
    position: absolute;
    top: 1rem;
    left: 1rem;
}
.grid-icon {
    position: absolute;
    right: 1rem;
    top: 1rem;
}
.grid-count {
    position: absolute;
    left: 1rem;
    bottom: 1rem;
}
</style>

<div style="display: flex; flex-flow: row wrap; justify-content: sapce-between;">
<a class="grid-item" href="{{ '/recommendations/' | relative_url }}">
  <span class="grid-title">Recommendations</span>
  <span class="grid-icon">{% include icons/crown.svg.html %}</span>
  <span class="grid-count">{{ counter_recommendations }}</span>
</a>
<a class="grid-item" href="{{ '/comparisons/' | relative_url }}">
  <span class="grid-title">Comparisons</span>
  <span class="grid-icon">{% include icons/ranking.svg.html %}</span>
  <span class="grid-count">{{ counter_comparisons }}</span>
</a>
</div>
