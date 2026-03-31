<script lang="ts">
	let { children } = $props();
</script>

<svelte:head>
	<title>Fault Lines: Blame Attribution in Online Discourse During the 2026 Lebanon Conflict</title>
	<meta name="description" content="An analysis of 48,407 tweets examining how geographic location shapes blame attribution in the 2026 Lebanon conflict." />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
</svelte:head>

{@render children()}

<style>
	:global(*) {
		margin: 0;
		padding: 0;
		box-sizing: border-box;
	}

	:global(html) {
		scroll-behavior: smooth;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
	}

	:global(body) {
		font-family: Verdana, Geneva, 'DejaVu Sans', sans-serif;
		background: #0c0c0e;
		color: #d4d0c8;
		line-height: 1.7;
		overflow-x: hidden;
	}

	:global(::selection) {
		background: rgba(180, 160, 120, 0.3);
		color: #fff;
	}
</style>
