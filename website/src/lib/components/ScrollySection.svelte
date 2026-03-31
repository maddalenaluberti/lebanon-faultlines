<script lang="ts">
	import { onMount, onDestroy } from 'svelte';

	interface Props {
		id: string;
		onStepEnter?: (index: number) => void;
		children?: import('svelte').Snippet;
	}

	let { id, onStepEnter, children }: Props = $props();

	let container: HTMLElement;
	let scrollerInstance: any = null;

	onMount(async () => {
		const scrollama = (await import('scrollama')).default;
		scrollerInstance = scrollama();

		scrollerInstance
			.setup({
				step: `#${id} .scroll-step`,
				offset: 0.5,
				debug: false
			})
			.onStepEnter((response: { index: number }) => {
				onStepEnter?.(response.index);
			});
	});

	onDestroy(() => {
		if (scrollerInstance) {
			scrollerInstance.destroy();
		}
	});
</script>

<section {id} bind:this={container} class="scrolly-section">
	{#if children}
		{@render children()}
	{/if}
</section>

<style>
	.scrolly-section {
		position: relative;
		width: 100%;
	}
</style>
