---
layout: home
redirect_from:
  - /altruist
  - /altruist.php
  - /teacher
  - /teacher.php
  - /student
  - /student.php
  - /writer
  - /writer.php
---

<section class="support-row" aria-label="Support my work">
	<a class="card card--quarter card--support" href="https://paypal.me/goddardlewis">
		<span class="card-label">Pay me</span>
		<span class="card-icon">{% include icons/brands/paypal.svg.html %}</span>
		<span class="card-detail">One-off via PayPal.</span>
	</a>
	<a class="card card--quarter card--support card--support-sponsor" href="https://github.com/sponsors/lewisgoddard">
		<span class="card-label">Sponsor</span>
		<span class="card-icon">{% include icons/brands/github-sponsors.svg.html %}</span>
		<span class="card-detail">Support open&#8209;source development.</span>
	</a>
	<a class="card card--half card--hire" href="&#109;&#097;&#105;&#108;&#116;&#111;:&#103;&#111;&#100;&#100;&#97;&#114;&#100;&#46;&#108;&#101;&#119;&#105;&#115;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;?subject=Freelance%20enquiry">
		<span class="card-label">Hire me</span>
		<span class="card-detail">Available for infrastructure and network enginner — contracts, advisory, permanent roles.</span>
		<span class="card-cta">Get in touch &rarr;</span>
	</a>
</section>

<section class="orgs-row" aria-label="Where I&apos;ve worked">
	<a class="card card--third card--org" href="https://eustasy.org">
		<span class="stat">30M</span>
		<span class="stat-label">users served</span>
		<span class="card-detail"><strong>eustasy</strong> since 2007.</span>
	</a>
	<a class="card card--third card--org" href="https://elementary.io">
		<span class="stat">14.4&#8239;PB</span>
		<span class="stat-label">delivered</span>
		<span class="card-detail"><strong>elementary</strong> since 2014.</span>
	</a>
	<a class="card card--third card--org" href="https://www.linkedin.com/in/lewisgoddard/">
		<span class="stat">16&#8239;yrs</span>
		<span class="stat-label">in the field</span>
		<span class="card-detail">Infrastructure / Network Engineer &dash; Manufacturing and Healthcare.</span>
	</a>
</section>

{% assign counter_recommendations = '-1' %}
{% for page in site.pages %}{% if page.url contains '/recommendations/' %}{% assign counter_recommendations = counter_recommendations | plus: 1 %}{% endif %}{% endfor %}

<section class="recs-row" aria-label="Recommendations">
	<a class="card card--full card--recs" href="{{ '/recommendations/' | relative_url }}">
		<span class="card-label">Recommendations</span>
		<span class="card-icon">{% include icons/crown.svg.html %}</span>
		<span class="card-count">{{ counter_recommendations }}</span>
		<span class="card-detail">Hardware and software I&rsquo;d actually buy or install today.</span>
	</a>
</section>
