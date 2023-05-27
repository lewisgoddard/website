---
title: CPUs
breadcrumb: cpus
---

_This page is for Desktop and Server class CPUs. For mobile CPUs see [Laptops](../laptops) and [Tablets](../tablets)._

## Quick Look

_**Bold** for better value near prices shown._

- AMD X3D can perform below the cheaper non-X3D variants of the same CPUs in many situations, despite costing significantly more. It is an application-specific buy-in, only for high end machines.
- AMD 7000 is difficult to recommend due to only supporting DDR5 memory, a substantial additional expense outside of the highest end machines.
- AMD 5000 was a good all rounder, but is at the end of its platform, offering no upgrade path.
- AMD 4000 is generally poor for gaming due to the exclusive use of PCIe 3.0, but offers good value for bargain-grade productivity.
- AMD 3000 can still offer good gaming performance, and bought used sits on a platform with a known-good upgrade path at excellent value for money.
- Intel 13 improves on Intel 12 mostly by adding more efficency cores, and moving them further down the stack where they add even more relative benefit. This does come at a cost (the cost is money).
- Intel 12 added big.LITTLE core architecture to their 10nm process, and shows the first real re-think of Intel for several years.
- Anything prior to Intel 12 is a member of a platform with a known-bad last release (Intel 11) and is lacking substantial improvements made recently.

### Productivity

- Basic: Web Browsing, light office Work.
- Medium: Substantial multi-tasking, photo-editing, larger excel sheets.
- High: Video Editing, light CAD work, massive excel sheets.

| Family   | Basic Productivity | Medium Productivity | High Productivity  |
|----------|--------------------|---------------------|--------------------|
| Intel 13 | i5 13400 ~£210     | i5 13600K ~£300     | i9 13900 ~£550     |
|          | i3 13100 ~£140     | i5 13500 ~£240      | i7 13700 ~£380     |
| Intel 12 | **i5 12400 ~£175** | i5 12600K ~£230     |
|          | **i3 12100 ~£120** |
| AMD 7000 |                    | R7 7700 ~£300       | R9 7950X ~£530     |
|          |                    | R5 7600 ~£220       | R9 7900 ~£400      |
| AMD 5000 | **R5 5600G ~£110** | **R7 5700G ~£170**  |
| AMD 4000 | **R5 4600G ~£90**  |

### Gaming

- Low: Pair with Nvidia GeForce RTX 3060 / 3060 Ti / 3070 / 4060 / 4060 Ti or AMD Radeon RX 6600 / 6600 XT / 6650 XT / 6700
- Medium: Pair with Nvidia GeForce RTX 3070 Ti / 3080 / 3080 Ti / 4070 or AMD Radeon RX 6700 XT / 6750 XT / 6800 / 6800 XT / 6900 XT / 6950 XT
- High: Pair with Nvidia GeForce RTX 4070 Ti / 4080 / 4090 or AMD Radeon RX 7900 XT / 7900 XTX

| Family   | Low Gaming          | Medium Gaming        | High Gaming          | 
|----------|---------------------|----------------------|----------------------|
| Intel 13 | i5 13400F ~£190     | i5 13600KF ~£280     | i9 13900KF ~£520     |
|          | **i3 13100F ~£110** | **i5 13500 ~£240**   | i7 13700KF ~£380     |
| Intel 12 | i5 12400F ~£150     | i5 12600KF ~£220     |
|          | **i3 12100F ~£90**  |
| AMD 7000 |                     | R7 7700X ~£300       | R9 7950X ~£530       |
|          |                     | **R5 7600X ~£230**   | R9 7900X ~£400       |
| AMD 5000 |  **R5 5600 ~£125**  | **R7 5800X ~£200**   |
|          |                     | **R7 5700X ~£170**   |
| AMD 3000 | **R5 3600 ~£40^**   |

### Comparison Table

| SKU | Cores | Threads | TDP | Single Core | Multi Core | Price | Rating |
|-----|-------|---------|-----|-------------|------------|-------|--------|
| 12100   | 4+0 | 8 | {% assign cpu = site.data.cpus['13100'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12100F  | 4+0 | 8 | {% assign cpu = site.data.cpus['12100F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12400   | 6+0 | 12 | {% assign cpu = site.data.cpus['12400'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12400F  | 6+0 | 12 | {% assign cpu = site.data.cpus['12400F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12500   | 6+0 | 12 | {% assign cpu = site.data.cpus['12500'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12600   | 6+0 | 12 | {% assign cpu = site.data.cpus['12600'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12600K  | 6+4 | 16 | {% assign cpu = site.data.cpus['12600K'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12600KF | 6+4 | 16 | {% assign cpu = site.data.cpus['12600KF'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12700   | 8+4 | 20 | {% assign cpu = site.data.cpus['12700'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12700F  | 8+4 | 20 | {% assign cpu = site.data.cpus['12700F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12700K  | 8+4 | 20 | {% assign cpu = site.data.cpus['12700K'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12700KF | 8+4 | 20 | {% assign cpu = site.data.cpus['12700KF'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12900   | 8+8 | 24 | {% assign cpu = site.data.cpus['12900'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12900F  | 8+8 | 24 | {% assign cpu = site.data.cpus['12900F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12900K  | 8+8 | 24 | {% assign cpu = site.data.cpus['12900K'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12900KF | 8+8 | 24 | {% assign cpu = site.data.cpus['12900KF'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 12900KS | 8+8 | 24 | {% assign cpu = site.data.cpus['12900KS'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13100   | 4+0 | 8 | {% assign cpu = site.data.cpus['13100'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13100F  | 4+0 | 8 | {% assign cpu = site.data.cpus['13100F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13400   | 6+4 | 16 | {% assign cpu = site.data.cpus['13400'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13400F  | 6+4 | 16 | {% assign cpu = site.data.cpus['13400F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13500   | 6+8 | 20 | {% assign cpu = site.data.cpus['13500'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13600K  | 6+8 | 20 | {% assign cpu = site.data.cpus['13600K'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13600KF | 6+8 | 20 | {% assign cpu = site.data.cpus['13600KF'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13700   | 8+8 | 24 | {% assign cpu = site.data.cpus['13700'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13700F  | 8+8 | 24 | {% assign cpu = site.data.cpus['13700F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13700K  | 8+8 | 24 | {% assign cpu = site.data.cpus['13700K'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13700KF | 8+8 | 24 | {% assign cpu = site.data.cpus['13700KF'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13900   | 8+16 | 32 | {% assign cpu = site.data.cpus['13900'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13900F  | 8+16 | 32 | {% assign cpu = site.data.cpus['13900F'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13900K  | 8+16 | 32 | {% assign cpu = site.data.cpus['13900K'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13900KF | 8+16 | 32 | {% assign cpu = site.data.cpus['13900KF'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 13900KS | 8+16 | 32 | {% assign cpu = site.data.cpus['13900KS'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3100 | 4 | 8 | {% assign cpu = site.data.cpus['3100'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3300X | 4 | 8 | {% assign cpu = site.data.cpus['3300X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3600 | 6 | 12 | {% assign cpu = site.data.cpus['3600'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3600X | 6 | 12 | {% assign cpu = site.data.cpus['3600'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3600XT | 6 | 12 | {% assign cpu = site.data.cpus['3600XT'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3700X | 8 | 16 | {% assign cpu = site.data.cpus['3700X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3800X | 8 | 16 | {% assign cpu = site.data.cpus['3800X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3800XT | 8 | 16 | {% assign cpu = site.data.cpus['3800XT'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3900X | 12 | 24 | {% assign cpu = site.data.cpus['3900X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3900XT | 12 | 24 | {% assign cpu = site.data.cpus['3900XT'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 3950X | 16 | 32 | {% assign cpu = site.data.cpus['3950X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 4100* | 4 | 8 | {% assign cpu = site.data.cpus['4100'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 4500* | 6 | 12 | {% assign cpu = site.data.cpus['4500'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 4600G* | 6 | 12 | {% assign cpu = site.data.cpus['4600G'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5500* | 6 | 12 | {% assign cpu = site.data.cpus['5500'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5600 | 6 | 12 | {% assign cpu = site.data.cpus['5600'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5600G* | 6 | 12 | {% assign cpu = site.data.cpus['5600G'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5600X | 6 | 12 | {% assign cpu = site.data.cpus['5600X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5700G* | 8 | 16 | {% assign cpu = site.data.cpus['5700G'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5700X | 8 | 16 | {% assign cpu = site.data.cpus['5700X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5800X | 8 | 16 | {% assign cpu = site.data.cpus['5800X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5800X3D | 8 | 16 | {% assign cpu = site.data.cpus['5800X3D'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5900X | 12 | 24 | {% assign cpu = site.data.cpus['5900X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 5950X | 16 | 32 | {% assign cpu = site.data.cpus['5950X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7600 | 6 | 12 | {% assign cpu = site.data.cpus['7600'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7600X | 6 | 12 | {% assign cpu = site.data.cpus['7600X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7700 | 8 | 16 | {% assign cpu = site.data.cpus['7700'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7700X | 8 | 16 | {% assign cpu = site.data.cpus['7700X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7800X3D | 8 | 16 | {% assign cpu = site.data.cpus['7800X3D'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7900 | 12 | 24 | {% assign cpu = site.data.cpus['7900'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7900X | 12 | 24 | {% assign cpu = site.data.cpus['7900X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7900X3D | 12 | 24 | {% assign cpu = site.data.cpus['7900X3D'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7950X | 16 | 32 | {% assign cpu = site.data.cpus['7950X'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |
| 7950X3D | 16 | 32 | {% assign cpu = site.data.cpus['7950X3D'] %}{{ cpu.tdp }} | {{ cpu.thread }} | {{ cpu.score }} | {{ cpu.price }} | {{ cpu.rating }} |


_* Uses PCIe gen 3.0, restrictive as to which GPUs perform appropriately._

_**IMPORTANT:** Rating does not account for Motherboard / RAM affordability, differing types of usability and existence of integrated graphics, or available upgrade paths. It is only based on a performance to price ratio that may be heavily outdated._

_Note: Does not include Intel T-type SKUs or models below i3, like Pentium or Celeron, or workstation-socket CPUs like Xeon._

_Note: Does not include AMD GE-type SKUs or models below Ryzen 3, like Athlon, or workstation-socket CPUs like Threadripper._

<script>
var el = document.getElementsByTagName("td")
for (var i = 0; i < el.length; i++) {
  if (el[i].innerHTML == "S") {
    el[i].className += " " + "color-elementary-grape-500"
  } else if (el[i].innerHTML == "A") {
    el[i].className += " " + "color-elementary-blueberry-500"
  } else if (el[i].innerHTML == "B") {
    el[i].className += " " + "color-elementary-mint-500"
  } else if (el[i].innerHTML == "C") {
    el[i].className += " " + "color-elementary-lime-500"
  } else if (el[i].innerHTML == "D") {
    el[i].className += " " + "color-elementary-banana-500"
  } else if (el[i].innerHTML == "E") {
    el[i].className += " " + "color-elementary-orange-500"
  } else if (el[i].innerHTML == "F") {
    el[i].className += " " + "color-elementary-strawberry-500"
  } 
}
</script>

## Intel

I have heard that generational improvement of Intel silicon is largely down to pushing more power for diminishing returns. While this adage may have been true for a time (14nm was almost exclusively in use from 5th gen / 2014 - 10th gen 2019) it no longer holds true. 12th gen Intel brought with them a new 10nm process and a move to a new naming scheme for such processes in line with AMDs naming, thus "Intel 7". It also brought a bit.LITTLE style core arrangement, with single-thread efficiency cores coupled with the existing dual-thread performance cores and continued DDR4 support throwing a substantial wrench in AMDs move towards price parity as a true competitor.

### Modifiers

####  F SKUs
- Lack Intel integrated graphics, either UHD or Xe, neither of which generally perform well. If you have a dedicated GPU, an F SKU will save you a little money, but be aware that Intel Quicksync can noticeably speed up any video transcode you might do.
- For: Gamers that do not stream or encode video.
- Not For: People without a dedicated GPU, streamers or video editors.

#### K SKUs 
- Unlocked for overclocking only on the top chipset motherboards available. Outside of that they typically only add a small amount of additional boost, the exception being the 12600K which adds 4 efficiency cores.
- For: Gamers on the highest motherboard chipset, or people with good cooling who want a little more performance.
- Not For: Everyone else.

#### S SKUs
- Slightly higher clocks at a much higher price.
- For: Top-teir builds that have nowhere else to upgrade to.
- Not For: Everyone else.

#### T SKUs
- Much lower TDP with most of the performance.
- For: Extreamly small builds that are not too concerned with performance.
- Not For: Everyone else.

### 12th gen (Alder Lake)

### 13th gen (Raptor Lake)

## AMD

### Modifiers

#### G SKUs
- 5000 series and earlier only: Includes integrated graphics.
- For: Productivity users lacking dedicated graphics.
- Not For: Everyone else.

#### GE SKUs

#### X SKUs
- Slightly higher clocks, sometimes with no non-X variant available.

#### XT SKUs

#### X3D SKUs

## ARM

## Apple
