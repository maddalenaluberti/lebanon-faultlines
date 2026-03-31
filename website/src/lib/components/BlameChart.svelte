<script lang="ts">
	import { onMount } from 'svelte';
	import * as d3 from 'd3';
	import blameData from '$lib/data/blame_crosstabs.json';

	interface Props {
		activeStep?: number;
	}

	let { activeStep = 0 }: Props = $props();

	let chartEl: SVGSVGElement;
	let containerEl: HTMLDivElement;
	let mounted = $state(false);
	let containerWidth = $state(0);

	const locationGroups = ['Diaspora (Arab)', 'Lebanon', 'Western'] as const;

	const targets = ['israel', 'iran', 'hezbollah', 'lebanese_government', 'sectarian_system'] as const;

	const targetLabels: Record<string, string> = {
		israel: 'Israel',
		iran: 'Iran',
		hezbollah: 'Hezbollah',
		lebanese_government: 'Lebanese Gov.',
		sectarian_system: 'Sectarian System'
	};

	const targetColors: Record<string, string> = {
		israel: '#5b8fb9',
		iran: '#c4836a',
		hezbollah: '#b8a47e',
		lebanese_government: '#6a9e96',
		sectarian_system: '#8b8db5'
	};

	const groupLabels: Record<string, string> = {
		'Diaspora (Arab)': 'Arab Countries',
		'Lebanon': 'Lebanon',
		'Western': 'Western Countries'
	};

	let tooltip = $state({ show: false, x: 0, y: 0, content: '', color: '' });

	function drawChart() {
		if (!chartEl || !containerEl) return;

		const svg = d3.select(chartEl);
		svg.selectAll('*').remove();

		const isMobile = containerWidth < 500;
		const margin = {
			top: 30,
			right: isMobile ? 50 : 65,
			bottom: 10,
			left: isMobile ? 100 : 140
		};
		const width = Math.min(containerWidth, 700) - margin.left - margin.right;
		const groupHeight = isMobile ? 190 : 210;
		const barHeight = isMobile ? 22 : 26;
		const barGap = isMobile ? 7 : 9;
		const totalHeight = locationGroups.length * groupHeight + margin.top + margin.bottom;

		svg
			.attr('width', width + margin.left + margin.right)
			.attr('height', totalHeight)
			.attr('viewBox', `0 0 ${width + margin.left + margin.right} ${totalHeight}`);

		const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

		const x = d3.scaleLinear().domain([0, 60]).range([0, width]);

		// Gridlines
		g.append('g')
			.attr('class', 'gridlines')
			.selectAll('line')
			.data([0, 10, 20, 30, 40, 50, 60])
			.enter()
			.append('line')
			.attr('x1', (d) => x(d))
			.attr('x2', (d) => x(d))
			.attr('y1', 0)
			.attr('y2', totalHeight - margin.top - margin.bottom)
			.attr('stroke', 'rgba(255,255,255,0.05)')
			.attr('stroke-width', 1);

		// Tick labels at top
		g.append('g')
			.attr('class', 'tick-labels')
			.selectAll('text')
			.data([0, 20, 40, 60])
			.enter()
			.append('text')
			.attr('x', (d) => x(d))
			.attr('y', -12)
			.attr('text-anchor', 'middle')
			.attr('fill', 'rgba(255,255,255,0.2)')
			.attr('font-size', '9px')
			.text((d) => `${d}%`);

		locationGroups.forEach((group, gi) => {
			const groupG = g.append('g').attr('transform', `translate(0, ${gi * groupHeight})`);

			// Group label
			groupG
				.append('text')
				.attr('x', -14)
				.attr('y', 18)
				.attr('text-anchor', 'end')
				.attr('fill', '#e8e6e3')
				.attr('font-size', isMobile ? '12px' : '13px')
				.attr('font-weight', '600')
				.text(groupLabels[group]);

			// n count
			const nVal = (blameData.blame_by_location as Record<string, Record<string, number>>)[group]['_n'];
			groupG
				.append('text')
				.attr('x', -14)
				.attr('y', 34)
				.attr('text-anchor', 'end')
				.attr('fill', 'rgba(255,255,255,0.22)')
				.attr('font-size', '9px')
				.attr('font-family', "'JetBrains Mono', monospace")
				.text(`n = ${nVal.toLocaleString()}`);

			// Bars
			targets.forEach((target, ti) => {
				const value = (blameData.blame_by_location as Record<string, Record<string, number>>)[group][target];
				const yPos = 50 + ti * (barHeight + barGap);
				const maxTarget = getMaxTarget(group);
				const isMax = target === maxTarget;

				// Target label
				groupG
					.append('text')
					.attr('x', -14)
					.attr('y', yPos + barHeight / 2 + 4)
					.attr('text-anchor', 'end')
					.attr('fill', isMax ? 'rgba(255,255,255,0.7)' : 'rgba(255,255,255,0.4)')
					.attr('font-size', isMobile ? '10px' : '11px')
					.attr('font-weight', isMax ? '500' : '400')
					.text(targetLabels[target]);

				// Bar background
				groupG
					.append('rect')
					.attr('x', 0)
					.attr('y', yPos)
					.attr('width', width)
					.attr('height', barHeight)
					.attr('fill', 'rgba(255,255,255,0.015)')
					.attr('rx', 3);

				// Interactive hit area (invisible, wider)
				const hitArea = groupG
					.append('rect')
					.attr('x', -margin.left + 10)
					.attr('y', yPos - 2)
					.attr('width', width + margin.left + margin.right - 20)
					.attr('height', barHeight + 4)
					.attr('fill', 'transparent')
					.attr('cursor', 'pointer');

				// Animated bar
				const bar = groupG
					.append('rect')
					.attr('x', 0)
					.attr('y', yPos)
					.attr('width', 0)
					.attr('height', barHeight)
					.attr('fill', targetColors[target])
					.attr('rx', 3)
					.attr('opacity', isMax ? 0.95 : 0.7)
					.attr('pointer-events', 'none');

				bar
					.transition()
					.duration(800)
					.delay(gi * 200 + ti * 80)
					.ease(d3.easeCubicOut)
					.attr('width', x(value));

				// Value label
				const label = groupG
					.append('text')
					.attr('x', x(value) + 8)
					.attr('y', yPos + barHeight / 2 + 4)
					.attr('fill', isMax ? targetColors[target] : 'rgba(255,255,255,0.55)')
					.attr('font-size', isMobile ? '10px' : '11px')
					.attr('font-weight', isMax ? '700' : '500')
					.attr('opacity', 0)
					.attr('pointer-events', 'none')
					.text(`${value}%`);

				label
					.transition()
					.duration(400)
					.delay(gi * 200 + ti * 80 + 600)
					.attr('opacity', 1);

				// Hover interactions
				hitArea
					.on('mouseenter', (event: MouseEvent) => {
						bar.transition().duration(150).attr('opacity', 1);
						label.transition().duration(150)
							.attr('fill', targetColors[target])
							.attr('font-weight', '700');

						const rect = containerEl.getBoundingClientRect();
						tooltip = {
							show: true,
							x: event.clientX - rect.left,
							y: event.clientY - rect.top - 10,
							content: `${targetLabels[target]}: ${value}% of ${groupLabels[group]} tweets`,
							color: targetColors[target]
						};
					})
					.on('mousemove', (event: MouseEvent) => {
						const rect = containerEl.getBoundingClientRect();
						tooltip.x = event.clientX - rect.left;
						tooltip.y = event.clientY - rect.top - 10;
					})
					.on('mouseleave', () => {
						bar.transition().duration(300).attr('opacity', isMax ? 0.95 : 0.7);
						if (!isMax) {
							label.transition().duration(300)
								.attr('fill', 'rgba(255,255,255,0.55)')
								.attr('font-weight', '500');
						} else {
							label.transition().duration(300)
								.attr('fill', targetColors[target])
								.attr('font-weight', '700');
						}
						tooltip.show = false;
					});
			});

			// Divider between groups
			if (gi < locationGroups.length - 1) {
				groupG
					.append('line')
					.attr('x1', -margin.left + 20)
					.attr('x2', width)
					.attr('y1', groupHeight - 10)
					.attr('y2', groupHeight - 10)
					.attr('stroke', 'rgba(255,255,255,0.05)')
					.attr('stroke-width', 1);
			}
		});
	}

	function getMaxTarget(group: string): string {
		const data = (blameData.blame_by_location as Record<string, Record<string, number>>)[group];
		let max = 0;
		let maxKey = '';
		for (const t of targets) {
			if (data[t] > max) {
				max = data[t];
				maxKey = t;
			}
		}
		return maxKey;
	}

	onMount(() => {
		mounted = true;
		if (containerEl) {
			containerWidth = containerEl.clientWidth;
		}

		const observer = new ResizeObserver((entries) => {
			for (const entry of entries) {
				containerWidth = entry.contentRect.width;
			}
		});

		if (containerEl) observer.observe(containerEl);

		return () => observer.disconnect();
	});

	$effect(() => {
		if (mounted && containerWidth > 0) {
			drawChart();
		}
	});
</script>

<div class="chart-wrapper" bind:this={containerEl}>
	<svg bind:this={chartEl}></svg>

	{#if tooltip.show}
		<div
			class="tooltip"
			style="left: {tooltip.x}px; top: {tooltip.y}px; border-color: {tooltip.color}"
		>
			{tooltip.content}
		</div>
	{/if}

	<!-- Legend -->
	<div class="legend">
		{#each targets as target}
			<span class="legend-item">
				<span class="legend-swatch" style="background: {targetColors[target]}"></span>
				{targetLabels[target]}
			</span>
		{/each}
	</div>
</div>

<style>
	.chart-wrapper {
		width: 100%;
		max-width: 700px;
		margin: 0 auto;
		padding: 1rem 0;
		position: relative;
	}

	svg {
		display: block;
		margin: 0 auto;
		overflow: visible;
		width: 100%;
		height: auto;
	}

	svg :global(text) {
		font-family: Verdana, Geneva, 'DejaVu Sans', sans-serif;
	}

	.tooltip {
		position: absolute;
		pointer-events: none;
		background: rgba(20, 20, 18, 0.92);
		border: 1px solid;
		border-radius: 4px;
		padding: 6px 10px;
		font-size: 0.68rem;
		color: rgba(232, 230, 227, 0.85);
		white-space: nowrap;
		transform: translate(-50%, -100%);
		z-index: 10;
		backdrop-filter: blur(8px);
	}

	.legend {
		display: flex;
		flex-wrap: wrap;
		gap: 1rem;
		justify-content: center;
		margin-top: 1.5rem;
		padding: 0 1rem;
	}

	.legend-item {
		display: flex;
		align-items: center;
		gap: 0.4rem;
		font-size: 0.68rem;
		color: rgba(255, 255, 255, 0.45);
	}

	.legend-swatch {
		width: 10px;
		height: 10px;
		border-radius: 2px;
		display: inline-block;
		flex-shrink: 0;
	}
</style>
