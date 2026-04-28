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

<section class="projects-row" aria-label="Open-source projects">
	<a class="card card--half card--projects" href="{{ '/projects/eustasy/' | relative_url }}">
		<span class="card-label">eustasy</span>
		<span class="card-icon">{% include icons/brands/github.svg.html %}</span>
		<span class="card-detail">Open-source code I&rsquo;ve built and maintain under the eustasy org &mdash; SSL tooling, 2FA, BitTorrent, colour systems.</span>
		<span class="card-cta">See projects &rarr;</span>
	</a>
	<a class="card card--half card--projects" href="{{ '/projects/elementary/' | relative_url }}">
		<span class="card-label">elementary</span>
		<span class="card-icon">{% include icons/brands/github.svg.html %}</span>
		<span class="card-detail">Long-running contributions to elementary OS &mdash; the website, the build system, icons, and the delivery network behind them.</span>
		<span class="card-cta">See projects &rarr;</span>
	</a>
</section>

<h2 class="row-header">Things I Use</h2>
<section class="uses-row" aria-label="Third-party tools and resources">
	<a class="card card--third card--use" href="https://grid.iamkate.com/">
		<span class="card-logo" style="background:#b3408e;">
			<img src="https://www.google.com/s2/favicons?domain=grid.iamkate.com&sz=64" alt="" loading="lazy" width="32" height="32">
		</span>
		<span class="card-label">National Grid Live</span>
		<span class="card-detail">Real-time monitoring of Great Britain&rsquo;s electricity grid &mdash; generation mix, demand, carbon intensity, and the ongoing shift from coal to renewables.</span>
	</a>
	<a class="card card--third card--use" href="https://www.uswitch.com/">
		<span class="card-logo" style="background:#00a651;">
			<img src="https://www.google.com/s2/favicons?domain=uswitch.com&sz=64" alt="" loading="lazy" width="32" height="32">
		</span>
		<span class="card-label">uswitch</span>
		<span class="card-detail">UK price comparison for energy, broadband, and insurance &mdash; saved me significant money when switching suppliers.</span>
	</a>
	<a class="card card--third card--use" href="https://elementary.io/">
		<span class="card-logo" style="background:#3689e6;">
			<img src="https://www.google.com/s2/favicons?domain=elementary.io&sz=64" alt="" loading="lazy" width="32" height="32">
		</span>
		<span class="card-label">elementary OS</span>
		<span class="card-detail">The Linux distribution I contribute to and daily-drive &mdash; beautifully designed and privacy-respecting.</span>
	</a>
</section>

{% assign counter_components = 0 %}{% assign counter_hardware = 0 %}{% assign counter_services = 0 %}{% assign counter_software = 0 %}
{% for p in site.pages %}
{% if p.url contains '/recommendations/components/' and p.url != '/recommendations/components/' %}{% assign counter_components = counter_components | plus: 1 %}{% endif %}
{% if p.url contains '/recommendations/hardware/' and p.url != '/recommendations/hardware/' %}{% assign counter_hardware = counter_hardware | plus: 1 %}{% endif %}
{% if p.url contains '/recommendations/services/' and p.url != '/recommendations/services/' %}{% assign counter_services = counter_services | plus: 1 %}{% endif %}
{% if p.url contains '/recommendations/software/' and p.url != '/recommendations/software/' %}{% assign counter_software = counter_software | plus: 1 %}{% endif %}
{% endfor %}

<h2 class="row-header">My Recommendations</h2>
<section class="recs-row recs-row--quad" aria-label="Recommendations">
	<a class="card card--quarter card--rec" href="{{ '/recommendations/components/' | relative_url }}">
		<span class="card-label">Components</span>
		<span class="card-icon">{% include icons/crown.svg.html %}</span>
		<span class="card-count">{{ counter_components }}</span>
		<span class="card-detail">CPUs, GPUs, RAM &mdash; the parts you pick first.</span>
	</a>
	<a class="card card--quarter card--rec" href="{{ '/recommendations/hardware/' | relative_url }}">
		<span class="card-label">Other Hardware</span>
		<span class="card-icon">{% include icons/crown.svg.html %}</span>
		<span class="card-count">{{ counter_hardware }}</span>
		<span class="card-detail">Laptops, peripherals, and the rest of the rack.</span>
	</a>
	<a class="card card--quarter card--rec" href="{{ '/recommendations/services/' | relative_url }}">
		<span class="card-label">Services</span>
		<span class="card-icon">{% include icons/crown.svg.html %}</span>
		<span class="card-count">{{ counter_services }}</span>
		<span class="card-detail">Hosts, registrars, SaaS &mdash; who I&rsquo;d actually pay.</span>
	</a>
	<a class="card card--quarter card--rec" href="{{ '/recommendations/software/' | relative_url }}">
		<span class="card-label">Software</span>
		<span class="card-icon">{% include icons/crown.svg.html %}</span>
		<span class="card-count">{{ counter_software }}</span>
		<span class="card-detail">Tools, libraries, and apps I&rsquo;d install today.</span>
	</a>
</section>
