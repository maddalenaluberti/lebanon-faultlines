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

	const timeData = blameData.blame_by_time;
	const earlyData = timeData['Early (Mar 12-17)'];
	const spikeData = timeData['Spike (Mar 18-19)'];

	interface ShiftItem {
		target: string;
		label: string;
		early: number;
		spike: number;
		delta: number;
		color: string;
	}

	const shifts: ShiftItem[] = [
		{ target: 'sectarian_system', label: 'Sectarian System', early: earlyData.sectarian_system, spike: spikeData.sectarian_system, delta: spikeData.sectarian_system - earlyData.sectarian_system, color: '#8b8db5' },
		{ target: 'lebanese_government', label: 'Lebanese Gov.', early: earlyData.lebanese_government, spike: spikeData.lebanese_government, delta: spikeData.lebanese_government - earlyData.lebanese_government, color: '#6a9e96' },
		{ target: 'iran', label: 'Iran', early: earlyData.iran, spike: spikeData.iran, delta: spikeData.iran - earlyData.iran, color: '#c4836a' },
		{ target: 'israel', label: 'Israel', early: earlyData.israel, spike: spikeData.israel, delta: spikeData.israel - earlyData.israel, color: '#5b8fb9' },
		{ target: 'hezbollah', label: 'Hezbollah', early: earlyData.hezbollah, spike: spikeData.hezbollah, delta: spikeData.hezbollah - earlyData.hezbollah, color: '#b8a47e' },
	];

	let tooltip = $state({ show: false, x: 0, y: 0, content: '', color: '' });

	function drawChart() {
		if (!chartEl || !containerEl) return;

		const svg = d3.select(chartEl);
		svg.selectAll('*').remove();

		const isMobile = containerWidth < 500;
		const margin = {
			top: 44,
			right: isMobile ? 55 : 70,
			bottom: 20,
			left: isMobile ? 100 : 130
		};
		const width = Math.min(containerWidth, 650) - margin.left - margin.right;
		const rowHeight = isMobile ? 54 : 60;
		const totalHeight = shifts.length * rowHeight + margin.top + margin.bottom;

		svg
			.attr('width', width + margin.left + margin.right)
			.attr('height', totalHeight)
			.attr('viewBox', `0 0 ${width + margin.left + margin.right} ${totalHeight}`);

		const g = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`);

		const x = d3.scaleLinear().domain([0, 50]).range([0, width]);

		// Subtle axis ticks
		g.append('g')
			.selectAll('line')
			.data([0, 10, 20, 30, 40, 50])
			.enter()
			.append('line')
			.attr('x1', (d) => x(d))
			.attr('x2', (d) => x(d))
			.attr('y1', -4)
			.attr('y2', shifts.length * rowHeight)
			.attr('stroke', 'rgba(255,255,255,0.04)')
			.attr('stroke-width', 1);

		// Column headers
		g.append('text')
			.attr('x', 0)
			.attr('y', -22)
			.attr('fill', 'rgba(255,255,255,0.3)')
			.attr('font-size', isMobile ? '9px' : '10px')
			.attr('font-weight', '500')
			.attr('font-family', "'JetBrains Mono', monospace")
			.text('Mar 12–17');

		g.append('text')
			.attr('x', 0)
			.attr('y', -12)
			.attr('fill', 'rgba(255,255,255,0.18)')
			.attr('font-size', '8px')
			.attr('font-family', "'JetBrains Mono', monospace")
			.text('Early period');

		g.append('text')
			.attr('x', width)
			.attr('y', -22)
			.attr('text-anchor', 'end')
			.attr('fill', 'rgba(255,255,255,0.3)')
			.attr('font-size', isMobile ? '9px' : '10px')
			.attr('font-weight', '500')
			.attr('font-family', "'JetBrains Mono', monospace")
			.text('Mar 18–19');

		g.append('text')
			.attr('x', width)
			.attr('y', -12)
			.attr('text-anchor', 'end')
			.attr('fill', 'rgba(255,255,255,0.18)')
			.attr('font-size', '8px')
			.attr('font-family', "'JetBrains Mono', monospace")
			.text('Spike period');

		// Header separator
		g.append('line')
			.attr('x1', -margin.left + 10)
			.attr('x2', width + margin.right - 10)
			.attr('y1', -6)
			.attr('y2', -6)
			.attr('stroke', 'rgba(255,255,255,0.06)')
			.attr('stroke-width', 1);

		shifts.forEach((item, i) => {
			const y = i * rowHeight + rowHeight / 2;

			// Row background (alternating)
			if (i % 2 === 0) {
				g.append('rect')
					.attr('x', -margin.left + 10)
					.attr('y', y - rowHeight / 2)
					.attr('width', width + margin.left + margin.right - 20)
					.attr('height', rowHeight)
					.attr('fill', 'rgba(255,255,255,0.012)')
					.attr('rx', 4);
			}

			// Interactive hit area
			const hitArea = g.append('rect')
				.attr('x', -margin.left + 10)
				.attr('y', y - rowHeight / 2)
				.attr('width', width + margin.left + margin.right - 20)
				.attr('height', rowHeight)
				.attr('fill', 'transparent')
				.attr('cursor', 'pointer');

			// Target label
			const targetLabel = g.append('text')
				.attr('x', -14)
				.attr('y', y + 4)
				.attr('text-anchor', 'end')
				.attr('fill', item.color)
				.attr('font-size', isMobile ? '11px' : '12px')
				.attr('font-weight', '600')
				.text(item.label);

			// "Early" dot
			const earlyDot = g.append('circle')
				.attr('cx', x(item.early))
				.attr('cy', y)
				.attr('r', 0)
				.attr('fill', item.color)
				.attr('opacity', 0.45)
				.attr('pointer-events', 'none');

			earlyDot
				.transition()
				.duration(600)
				.delay(i * 100)
				.attr('r', 5);

			// "Early" label
			const earlyLabel = g.append('text')
				.attr('x', x(item.early))
				.attr('y', y - 11)
				.attr('text-anchor', 'middle')
				.attr('fill', 'rgba(255,255,255,0.35)')
				.attr('font-size', '9px')
				.attr('font-family', "'JetBrains Mono', monospace")
				.attr('opacity', 0)
				.attr('pointer-events', 'none')
				.text(`${item.early}%`);

			earlyLabel
				.transition()
				.duration(400)
				.delay(i * 100 + 400)
				.attr('opacity', 1);

			// Connecting line (animated)
			const line = g.append('line')
				.attr('x1', x(item.early))
				.attr('y1', y)
				.attr('x2', x(item.early))
				.attr('y2', y)
				.attr('stroke', item.color)
				.attr('stroke-width', 2)
				.attr('opacity', 0.3)
				.attr('stroke-dasharray', '4 3')
				.attr('pointer-events', 'none');

			line
				.transition()
				.duration(800)
				.delay(i * 100 + 300)
				.attr('x2', x(item.spike));

			// Arrow head at spike end
			const arrowSize = 4;
			const direction = item.spike > item.early ? 1 : -1;
			const arrow = g.append('polygon')
				.attr('points', `0,${-arrowSize} ${arrowSize * direction * 1.5},0 0,${arrowSize}`)
				.attr('transform', `translate(${x(item.spike)}, ${y})`)
				.attr('fill', item.color)
				.attr('opacity', 0)
				.attr('pointer-events', 'none');

			arrow
				.transition()
				.duration(300)
				.delay(i * 100 + 900)
				.attr('opacity', 0.6);

			// "Spike" dot
			const spikeDot = g.append('circle')
				.attr('cx', x(item.spike))
				.attr('cy', y)
				.attr('r', 0)
				.attr('fill', item.color)
				.attr('opacity', 0.9)
				.attr('pointer-events', 'none');

			spikeDot
				.transition()
				.duration(600)
				.delay(i * 100 + 600)
				.attr('r', 6);

			// "Spike" label
			const spikeLabel = g.append('text')
				.attr('x', x(item.spike))
				.attr('y', y + 16)
				.attr('text-anchor', 'middle')
				.attr('fill', item.color)
				.attr('font-size', '9px')
				.attr('font-weight', '600')
				.attr('font-family', "'JetBrains Mono', monospace")
				.attr('opacity', 0)
				.attr('pointer-events', 'none')
				.text(`${item.spike}%`);

			spikeLabel
				.transition()
				.duration(400)
				.delay(i * 100 + 800)
				.attr('opacity', 1);

			// Delta annotation
			const deltaText = item.delta > 0 ? `+${item.delta.toFixed(1)}` : item.delta.toFixed(1);
			const deltaColor = item.delta < 0 ? '#c4836a' : '#6a9e96';

			const deltaLabel = g.append('text')
				.attr('x', width + (isMobile ? 10 : 15))
				.attr('y', y + 4)
				.attr('fill', deltaColor)
				.attr('font-size', isMobile ? '10px' : '11px')
				.attr('font-weight', '700')
				.attr('font-family', "'JetBrains Mono', monospace")
				.attr('opacity', 0)
				.attr('pointer-events', 'none')
				.text(`${deltaText}pp`);

			deltaLabel
				.transition()
				.duration(400)
				.delay(i * 100 + 1000)
				.attr('opacity', 1);

			// Hover interactions
			hitArea
				.on('mouseenter', (event: MouseEvent) => {
					// Highlight row
					earlyDot.transition().duration(150).attr('r', 7).attr('opacity', 0.7);
					spikeDot.transition().duration(150).attr('r', 8).attr('opacity', 1);
					line.transition().duration(150).attr('stroke-width', 3).attr('opacity', 0.5);
					arrow.transition().duration(150).attr('opacity', 0.9);
					targetLabel.transition().duration(150).attr('font-size', isMobile ? '12px' : '13px');
					deltaLabel.transition().duration(150).attr('font-size', isMobile ? '11px' : '13px');

					const rect = containerEl.getBoundingClientRect();
					const direction = item.delta > 0 ? '↑' : '↓';
					tooltip = {
						show: true,
						x: event.clientX - rect.left,
						y: event.clientY - rect.top - 10,
						content: `${item.label}: ${item.early}% → ${item.spike}% (${direction} ${Math.abs(item.delta).toFixed(1)}pp)`,
						color: item.color
					};
				})
				.on('mousemove', (event: MouseEvent) => {
					const rect = containerEl.getBoundingClientRect();
					tooltip.x = event.clientX - rect.left;
					tooltip.y = event.clientY - rect.top - 10;
				})
				.on('mouseleave', () => {
					earlyDot.transition().duration(300).attr('r', 5).attr('opacity', 0.45);
					spikeDot.transition().duration(300).attr('r', 6).attr('opacity', 0.9);
					line.transition().duration(300).attr('stroke-width', 2).attr('opacity', 0.3);
					arrow.transition().duration(300).attr('opacity', 0.6);
					targetLabel.transition().duration(300).attr('font-size', isMobile ? '11px' : '12px');
					deltaLabel.transition().duration(300).attr('font-size', isMobile ? '10px' : '11px');
					tooltip.show = false;
				});
		});
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

<div class="timeline-wrapper" bind:this={containerEl}>
	<svg bind:this={chartEl}></svg>

	{#if tooltip.show}
		<div
			class="tooltip"
			style="left: {tooltip.x}px; top: {tooltip.y}px; border-color: {tooltip.color}"
		>
			{tooltip.content}
		</div>
	{/if}
</div>

<style>
	.timeline-wrapper {
		width: 100%;
		max-width: 650px;
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
		font-family: 'JetBrains Mono', monospace;
	}
</style>
