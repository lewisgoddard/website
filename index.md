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

<h2 class="row-header">Projects</h2>
<section class="projects-row" aria-label="Open-source projects">
	<div class="card card--half card--projects">
		<a class="card-label" href="https://github.com/eustasy">eustasy</a>
		<a class="card-icon" href="https://github.com/eustasy" aria-label="eustasy on GitHub">{% include icons/brands/github.svg.html %}</a>
		<span class="card-detail">Things I&rsquo;ve built and maintained under the eustasy org.</span>
		<ul class="project-list">
			<li><a href="https://github.com/eustasy/Bubbly"><strong>Bubbly</strong> <span class="project-stars">217&#9733;</span></a><span class="project-blurb">Better SSL in nginx in 10 minutes &mdash; Certbot configs and setup scripts.</span></li>
			<li><a href="https://github.com/eustasy/Phoenix"><strong>Phoenix</strong> <span class="project-stars">18&#9733;</span></a><span class="project-blurb">Lightweight BitTorrent tracker in PHP with an SQL backend.</span></li>
			<li><a href="https://github.com/eustasy/authenticatron"><strong>authenticatron</strong> <span class="project-stars">11&#9733;</span></a><span class="project-blurb">HOTP / TOTP secrets, QR provisioning, and code verification in a single PHP script.</span></li>
			<li><a href="https://github.com/eustasy/Colors.css"><strong>Colors.css</strong> <span class="project-stars">8&#9733;</span></a><span class="project-blurb">A colour-system stylesheet &mdash; backgrounds and fonts from named palettes.</span></li>
		</ul>
	</div>
	<div class="card card--half card--projects">
		<a class="card-label" href="https://github.com/elementary">elementary</a>
		<a class="card-icon" href="https://github.com/elementary" aria-label="elementary on GitHub">{% include icons/brands/github.svg.html %}</a>
		<span class="card-detail">Long-running contributions to elementary OS and its delivery.</span>
		<ul class="project-list">
			<li><a href="https://github.com/elementary/website"><strong>website</strong> <span class="project-stars">1.3k&#9733;</span></a><span class="project-blurb">elementary.io marketing site &mdash; copy, layout, and the CDN behind it.</span></li>
			<li><a href="https://github.com/elementary/os"><strong>os</strong> <span class="project-stars">1.1k&#9733;</span></a><span class="project-blurb">The elementary OS build system.</span></li>
			<li><a href="https://github.com/elementary/icons"><strong>icons</strong> <span class="project-stars">586&#9733;</span></a><span class="project-blurb">Named, vector icons used across elementary OS.</span></li>
			<li><a href="https://github.com/elementary/appcenter"><strong>appcenter</strong> <span class="project-stars">552&#9733;</span></a><span class="project-blurb">Pay-what-you-can app store for elementary OS.</span></li>
		</ul>
	</div>
</section>

{% assign counter_components = 0 %}{% assign counter_hardware = 0 %}{% assign counter_services = 0 %}{% assign counter_software = 0 %}
{% for p in site.pages %}
{% if p.url contains '/recommendations/components/' and p.url != '/recommendations/components/' %}{% assign counter_components = counter_components | plus: 1 %}{% endif %}
{% if p.url contains '/recommendations/hardware/' and p.url != '/recommendations/hardware/' %}{% assign counter_hardware = counter_hardware | plus: 1 %}{% endif %}
{% if p.url contains '/recommendations/services/' and p.url != '/recommendations/services/' %}{% assign counter_services = counter_services | plus: 1 %}{% endif %}
{% if p.url contains '/recommendations/software/' and p.url != '/recommendations/software/' %}{% assign counter_software = counter_software | plus: 1 %}{% endif %}
{% endfor %}

<h2 class="row-header">Recommendations</h2>
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
