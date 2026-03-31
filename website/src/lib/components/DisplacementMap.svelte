<script lang="ts">
	import { onMount } from 'svelte';
	import * as d3 from 'd3';
	import governorates from '$lib/data/lebanon_governorates.json';
	import litaniRiver from '$lib/data/litani_river.json';

	interface Props {
		activeStep?: number;
	}

	let { activeStep = 0 }: Props = $props();

	let mapContainer: HTMLDivElement;
	let visible = $state(false);

	onMount(() => {
		visible = true;
		drawMap();
	});

	// Key cities with real coordinates [lon, lat] and label offsets
	const cities: { name: string; coords: [number, number]; size: number; importance: string; labelX: number; labelY: number; anchor?: string }[] = [
		{ name: 'Beirut', coords: [35.5018, 33.8938], size: 5, importance: 'primary', labelX: 10, labelY: 4 },
		{ name: 'Tripoli', coords: [35.8498, 34.4332], size: 3, importance: 'secondary', labelX: 8, labelY: 4 },
		{ name: 'Sidon', coords: [35.3729, 33.5571], size: 3, importance: 'secondary', labelX: 8, labelY: 4 },
		{ name: 'Tyre', coords: [35.2038, 33.2705], size: 3, importance: 'secondary', labelX: 8, labelY: 4 },
		{ name: 'Nabatieh', coords: [35.4836, 33.3772], size: 2.5, importance: 'secondary', labelX: 8, labelY: 4 },
		{ name: 'Baalbek', coords: [36.2110, 34.0047], size: 2.5, importance: 'secondary', labelX: 8, labelY: 4 },
		{ name: 'Bint Jbeil', coords: [35.4339, 33.1214], size: 2, importance: 'tertiary', labelX: -8, labelY: 4, anchor: 'end' },
		{ name: 'Zahle', coords: [35.9024, 33.8467], size: 2.5, importance: 'secondary', labelX: 8, labelY: 4 },
	];

	// Strike/event markers (no labels — show on hover to avoid clutter)
	const strikes = [
		{ name: 'Dahiyeh', coords: [35.49, 33.86], type: 'evacuation', detail: '~700K evacuated, Mar 5–6' },
		{ name: 'Nabi Sheet', coords: [36.08, 34.08], type: 'strike', detail: 'Bekaa Valley strikes' },
	];

	const stats = [
		{ value: '816K+', label: 'People displaced', detail: 'By March 12 (Social Development Ministry)' },
		{ value: '1,001+', label: 'Killed in 19 days', detail: 'Health Ministry, as of March 20' },
		{ value: '700K', label: 'Evacuated in one day', detail: 'Dahiyeh suburbs, March 5–6' },
		{ value: '128+', label: 'Attacks on medical targets', detail: 'Since start of war (Health Ministry)' }
	];

	const timeline = [
		{ date: 'Mar 1', event: 'Hezbollah fires rockets after Khamenei assassination. Israeli airstrikes follow.', severity: 2 },
		{ date: 'Mar 3', event: 'Government bans Hezbollah military activity. 58,000 displaced. Over 80 killed.', severity: 2 },
		{ date: 'Mar 4–5', event: 'Israel launches ground invasion. Evacuation ordered south of the Litani River.', severity: 3 },
		{ date: 'Mar 5–6', event: 'Mass evacuation of southern Beirut suburbs (~700K). 123 killed, 638 injured.', severity: 4 },
		{ date: 'Mar 12', event: 'Drone strike kills 11 on Ramlet al-Baida corniche. 634+ killed, 816K displaced.', severity: 4 },
		{ date: 'Mar 18–19', event: 'Strikes devastate central Beirut (Bashoura, Zoqaq al-Blat, Basta). 968+ killed.', severity: 5 }
	];

	let evacGroup: d3.Selection<SVGGElement, unknown, null, undefined>;
	let strikeGroup: d3.Selection<SVGGElement, unknown, null, undefined>;

	function drawMap() {
		if (!mapContainer) return;

		const width = 400;
		const height = 600;

		d3.select(mapContainer).selectAll('svg').remove();

		const svg = d3.select(mapContainer)
			.append('svg')
			.attr('viewBox', `0 0 ${width} ${height}`)
			.attr('class', 'lebanon-map-svg');

		// Projection centered on Lebanon
		const projection = d3.geoMercator()
			.center([35.75, 33.75])
			.scale(11500)
			.translate([width / 2, height / 2]);

		const pathGen = d3.geoPath().projection(projection);

		// Draw governorate boundaries
		svg.append('g').attr('class', 'governorates')
			.selectAll('path')
			.data((governorates as any).features)
			.enter()
			.append('path')
			.attr('d', pathGen as any)
			.attr('fill', (d: any) => {
				const name = d.properties.name;
				if (['South', 'Nabatiyeh'].includes(name)) return 'rgba(196, 131, 106, 0.05)';
				return 'rgba(212, 208, 200, 0.02)';
			})
			.attr('stroke', 'rgba(212, 208, 200, 0.12)')
			.attr('stroke-width', 0.5);

		// Evacuation zone overlay
		const southGovs = (governorates as any).features.filter(
			(f: any) => ['South', 'Nabatiyeh'].includes(f.properties.name)
		);

		evacGroup = svg.append('g')
			.attr('class', 'evac-overlay')
			.style('opacity', 0);

		evacGroup.selectAll('path')
			.data(southGovs)
			.enter()
			.append('path')
			.attr('d', pathGen as any)
			.attr('fill', 'rgba(196, 131, 106, 0.15)')
			.attr('stroke', 'rgba(196, 131, 106, 0.4)')
			.attr('stroke-width', 1)
			.attr('stroke-dasharray', '4 2');

		// Evacuation zone label
		const evacLabelPos = projection([35.35, 33.30] as [number, number])!;
		evacGroup.append('text')
			.attr('x', evacLabelPos[0])
			.attr('y', evacLabelPos[1] + 16)
			.attr('fill', 'rgba(196, 131, 106, 0.5)')
			.attr('font-size', '7px')
			.attr('font-family', "'JetBrains Mono', monospace")
			.attr('text-anchor', 'middle')
			.attr('letter-spacing', '0.05em')
			.text('EVACUATION ZONE');

		// Litani River (real OSM data)
		const riverPath = d3.line<[number, number]>()
			.x(d => projection(d)![0])
			.y(d => projection(d)![1])
			.curve(d3.curveCatmullRom.alpha(0.5));

		svg.append('path')
			.attr('d', riverPath((litaniRiver as any).geometry.coordinates))
			.attr('fill', 'none')
			.attr('stroke', 'rgba(120, 165, 210, 0.45)')
			.attr('stroke-width', 1.3)
			.attr('stroke-linecap', 'round');

		// Litani label near the river's bend
		const riverCoords = (litaniRiver as any).geometry.coordinates;
		const midIdx = Math.floor(riverCoords.length * 0.6);
		const labelPoint = projection(riverCoords[midIdx])!;
		svg.append('text')
			.attr('x', labelPoint[0] + 6)
			.attr('y', labelPoint[1] - 4)
			.attr('fill', 'rgba(120, 165, 210, 0.45)')
			.attr('font-size', '6.5px')
			.attr('font-family', "'JetBrains Mono', monospace")
			.attr('font-style', 'italic')
			.text('Litani R.');

		// City markers
		const cityGroup = svg.append('g').attr('class', 'cities');

		cities.forEach(city => {
			const pos = projection(city.coords as [number, number])!;
			const color = city.importance === 'strike' ? '#c4836a' :
			              city.importance === 'primary' ? '#b8a47e' : 'rgba(184, 164, 126, 0.5)';

			// Hover ring (hidden by default)
			const hoverRing = cityGroup.append('circle')
				.attr('cx', pos[0])
				.attr('cy', pos[1])
				.attr('r', city.size + 4)
				.attr('fill', 'none')
				.attr('stroke', color)
				.attr('stroke-width', 0.5)
				.attr('opacity', 0);

			// City dot
			const dot = cityGroup.append('circle')
				.attr('cx', pos[0])
				.attr('cy', pos[1])
				.attr('r', city.size)
				.attr('fill', color)
				.attr('opacity', city.importance === 'primary' ? 0.9 : 0.6)
				.attr('cursor', 'pointer');

			const label = cityGroup.append('text')
				.attr('x', pos[0] + city.labelX)
				.attr('y', pos[1] + city.labelY)
				.attr('text-anchor', city.anchor || 'start')
				.attr('fill', city.importance === 'primary' ? 'rgba(212, 208, 200, 0.75)' :
				              'rgba(212, 208, 200, 0.45)')
				.attr('font-size', city.importance === 'primary' ? '10px' : '8px')
				.attr('font-weight', city.importance === 'primary' ? '500' : '400')
				.attr('font-family', "Verdana, Geneva, 'DejaVu Sans', sans-serif")
				.text(city.name);

			// Hover
			dot
				.on('mouseenter', () => {
					hoverRing.transition().duration(200).attr('opacity', 0.6);
					dot.transition().duration(200).attr('r', city.size + 1.5);
					label.transition().duration(200).attr('fill', 'rgba(232, 230, 227, 0.8)');
				})
				.on('mouseleave', () => {
					hoverRing.transition().duration(300).attr('opacity', 0);
					dot.transition().duration(300).attr('r', city.size);
					label.transition().duration(300).attr('fill',
						city.importance === 'primary' ? 'rgba(212, 208, 200, 0.7)' :
						city.importance === 'strike' ? 'rgba(196, 131, 106, 0.5)' :
						'rgba(212, 208, 200, 0.4)');
				});
		});

		// Strike markers (appear with scroll)
		strikeGroup = svg.append('g')
			.attr('class', 'strike-markers')
			.style('opacity', 0);

		strikes.forEach(strike => {
			const pos = projection(strike.coords as [number, number])!;

			if (strike.type === 'evacuation') {
				strikeGroup.append('circle')
					.attr('cx', pos[0]).attr('cy', pos[1]).attr('r', 14)
					.attr('fill', 'rgba(196, 131, 106, 0.1)')
					.attr('stroke', 'rgba(196, 131, 106, 0.3)')
					.attr('stroke-width', 0.8)
					.attr('stroke-dasharray', '3 2');

				// Pulse ring
				strikeGroup.append('circle')
					.attr('cx', pos[0]).attr('cy', pos[1]).attr('r', 14)
					.attr('fill', 'none')
					.attr('stroke', 'rgba(196, 131, 106, 0.2)')
					.attr('stroke-width', 1)
					.attr('class', 'pulse-ring');
			} else {
				// Inner dot
				strikeGroup.append('circle')
					.attr('cx', pos[0]).attr('cy', pos[1]).attr('r', 4)
					.attr('fill', 'rgba(196, 131, 106, 0.4)')
					.attr('stroke', 'rgba(196, 131, 106, 0.7)')
					.attr('stroke-width', 0.8);

				// Outer ring
				strikeGroup.append('circle')
					.attr('cx', pos[0]).attr('cy', pos[1]).attr('r', 9)
					.attr('fill', 'none')
					.attr('stroke', 'rgba(196, 131, 106, 0.15)')
					.attr('stroke-width', 0.5);

				// Pulse ring
				strikeGroup.append('circle')
					.attr('cx', pos[0]).attr('cy', pos[1]).attr('r', 9)
					.attr('fill', 'none')
					.attr('stroke', 'rgba(196, 131, 106, 0.15)')
					.attr('stroke-width', 0.5)
					.attr('class', 'pulse-ring');
			}

			});

	}

	// Animate on scroll step change
	$effect(() => {
		if (evacGroup) {
			evacGroup.transition().duration(800)
				.style('opacity', activeStep >= 0 ? 1 : 0);
		}
		if (strikeGroup) {
			strikeGroup.transition().duration(800)
				.style('opacity', activeStep >= 1 ? 1 : 0);
		}
	});
</script>

<div class="displacement-container" class:visible>
	<div class="map-visual">
		<div class="map-frame" bind:this={mapContainer}></div>
	</div>

	<div class="stats-grid" class:active={activeStep >= 0}>
		{#each stats as stat, i}
			<div class="stat-card" style="transition-delay: {i * 100 + 200}ms">
				<div class="stat-value">{stat.value}</div>
				<div class="stat-label">{stat.label}</div>
				<div class="stat-detail">{stat.detail}</div>
			</div>
		{/each}
	</div>

	<div class="mini-timeline" class:active={activeStep >= 1}>
		{#each timeline as item, i}
			<div class="timeline-item" style="transition-delay: {i * 80}ms">
				<div class="timeline-date">{item.date}</div>
				<div class="timeline-bar-track">
					<div
						class="timeline-bar-fill"
						style="width: {item.severity * 20}%; background: {item.severity >= 4
							? '#c4836a'
							: item.severity >= 3
								? '#b8a47e'
								: 'rgba(212, 208, 200, 0.25)'}"
					></div>
				</div>
				<div class="timeline-event">{item.event}</div>
			</div>
		{/each}
	</div>
</div>

<style>
	.displacement-container {
		width: 100%;
		max-width: 800px;
		margin: 0 auto;
		padding: 2rem 1rem;
		opacity: 0;
		transform: translateY(20px);
		transition: opacity 0.8s ease, transform 0.8s ease;
	}

	.displacement-container.visible {
		opacity: 1;
		transform: translateY(0);
	}

	.map-visual {
		display: flex;
		justify-content: center;
		margin-bottom: 3rem;
	}

	.map-frame {
		position: relative;
		width: 280px;
	}

	.map-frame :global(.lebanon-map-svg) {
		width: 100%;
		height: auto;
	}

	/* Pulse animation for strike markers */
	.map-frame :global(.pulse-ring) {
		animation: pulse 3s ease-in-out infinite;
	}

	@keyframes pulse {
		0%, 100% { opacity: 0; transform-origin: center; }
		50% { opacity: 0.4; }
	}

	/* Stats */
	.stats-grid {
		display: grid;
		grid-template-columns: repeat(2, 1fr);
		gap: 0.75rem;
		margin-bottom: 3rem;
	}

	@media (min-width: 600px) {
		.stats-grid {
			grid-template-columns: repeat(4, 1fr);
		}
	}

	.stats-grid .stat-card {
		opacity: 0;
		transform: translateY(16px);
		transition: opacity 0.6s ease, transform 0.6s ease;
	}

	.stats-grid.active .stat-card {
		opacity: 1;
		transform: translateY(0);
	}

	.stat-card {
		text-align: center;
		padding: 1.25rem 0.75rem;
		border: 1px solid rgba(212, 208, 200, 0.06);
		border-radius: 4px;
		background: rgba(212, 208, 200, 0.02);
		transition: border-color 0.3s ease, background 0.3s ease;
	}

	.stat-card:hover {
		border-color: rgba(212, 208, 200, 0.12);
		background: rgba(212, 208, 200, 0.04);
	}

	.stat-value {
		font-family: 'JetBrains Mono', monospace;
		font-size: 1.5rem;
		font-weight: 500;
		color: #b8a47e;
		line-height: 1.1;
		margin-bottom: 0.3rem;
	}

	.stat-label {
		font-size: 0.75rem;
		font-weight: 500;
		color: rgba(212, 208, 200, 0.7);
		margin-bottom: 0.3rem;
	}

	.stat-detail {
		font-size: 0.6rem;
		color: rgba(212, 208, 200, 0.3);
		line-height: 1.3;
	}

	/* Mini timeline */
	.mini-timeline {
		display: flex;
		flex-direction: column;
		gap: 0.35rem;
	}

	.mini-timeline .timeline-item {
		opacity: 0;
		transform: translateX(-10px);
		transition: opacity 0.5s ease, transform 0.5s ease;
	}

	.mini-timeline.active .timeline-item {
		opacity: 1;
		transform: translateX(0);
	}

	.timeline-item {
		display: grid;
		grid-template-columns: 70px 80px 1fr;
		gap: 0.75rem;
		align-items: center;
		padding: 0.5rem 0.5rem;
		border-radius: 3px;
		transition: background 0.2s ease;
	}

	.timeline-item:hover {
		background: rgba(212, 208, 200, 0.03);
	}

	@media (max-width: 500px) {
		.timeline-item {
			grid-template-columns: 60px 60px 1fr;
			gap: 0.5rem;
		}
	}

	.timeline-date {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.62rem;
		font-weight: 400;
		color: rgba(212, 208, 200, 0.4);
		text-align: right;
	}

	.timeline-bar-track {
		height: 4px;
		background: rgba(212, 208, 200, 0.04);
		border-radius: 2px;
		overflow: hidden;
	}

	.timeline-bar-fill {
		height: 100%;
		border-radius: 2px;
		transition: width 0.8s ease;
	}

	.timeline-event {
		font-size: 0.66rem;
		color: rgba(212, 208, 200, 0.5);
		line-height: 1.45;
	}

	.timeline-item:hover .timeline-event {
		color: rgba(212, 208, 200, 0.7);
	}

	.timeline-item:hover .timeline-date {
		color: rgba(212, 208, 200, 0.6);
	}
</style>
