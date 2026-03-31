<script lang="ts">
	import ScrollySection from '$lib/components/ScrollySection.svelte';
	import DisplacementMap from '$lib/components/DisplacementMap.svelte';
	import BlameChart from '$lib/components/BlameChart.svelte';
	import TimelineChart from '$lib/components/TimelineChart.svelte';
	import blameData from '$lib/data/blame_crosstabs.json';

	let s1Step = $state(0);
	let s2Step = $state(0);
	let s3Step = $state(0);
	let s4Step = $state(0);
</script>

<main>
	<!-- ============================================ -->
	<!-- HEADER                                       -->
	<!-- ============================================ -->
	<header class="report-header">
		<div class="header-inner">
			<h1 class="report-title">Fault Lines: <span class="title-subtitle">Blame Attribution in Online Discourse During the 2026 Lebanon Conflict</span></h1>
				<div class="scroll-hint">
				<div class="scroll-arrow"></div>
			</div>
		</div>
	</header>

	<!-- ============================================ -->
	<!-- SECTION 1: INTRODUCTION & METHODOLOGY        -->
	<!-- ============================================ -->
	<ScrollySection id="section1" onStepEnter={(i) => (s1Step = i)}>
		<div class="section-header">
			<span class="section-number">01</span>
			<h2 class="section-title">Introduction</h2>
		</div>

		<div class="scroll-step prose-block">
			<p>
				On 28 February 2026, a joint United States&ndash;Israeli operation targeting Iran's
				Supreme Leader, Ayatollah Ali Khamenei, triggered a rapid escalation across the
				Israel&ndash;Lebanon conflict. Subsequent exchanges between Israel and Hezbollah led
				to major civilian displacement and casualties within Lebanon.
			</p>
			<p>
				This escalation occurred in the context of a fragile post-2024 ceasefire and an
				incomplete process of Hezbollah disarmament within Lebanon. Ongoing Israeli strikes
				during the ceasefire period and the partial implementation of disarmament measures
				contributed to a highly unstable equilibrium prior to March 2026.
			</p>
			<p>
				This report analyses how responsibility for the escalation was attributed in online
				discourse, with particular attention to variation across geographic contexts. It
				examines how blame attribution patterns correspond to political and sectarian
				alignments and proximity to the conflict.
			</p>
		</div>

		<div class="scroll-step prose-block">
			<div class="method-box">
				<h3 class="method-heading">Data & Methodology</h3>
				<p>
					This study draws on a dataset of <strong>48,407 tweets</strong> collected via the
					X (Twitter) API using Lebanon conflict-related keywords in Arabic and English,
					covering the period <strong>12&ndash;19 March 2026</strong>. The dataset spans
					150 countries and two languages (69.4% English, 30.6% Arabic).
				</p>
				<p>
					Tweets were classified along two dimensions: (1) <strong>blame attribution</strong>,
					identifying which actors were held responsible (Israel, Iran, Hezbollah, the
					Lebanese government, the sectarian system, or the international community), and
					(2) <strong>discursive stance</strong> (analytical, anti-war, pro-resistance,
					pro-Israel or unclear). Classification was conducted using the Qwen2.5-7B-Instruct
					language model. Blame attribution categories were non-mutually exclusive, allowing
					individual tweets to assign responsibility to multiple actors.
				</p>
				<p>
					Geographic location was inferred from user profile data. A country of origin was
					identifiable for 44.9% of tweets. For analytical purposes, tweets were grouped
					into three categories: <strong>accounts based in Lebanon</strong> (n&nbsp;=&nbsp;4,013),
					<strong>accounts in Arab-majority countries</strong> (n&nbsp;=&nbsp;7,123), and
					<strong>accounts in Western countries</strong> (n&nbsp;=&nbsp;7,334). Within these
					groups, activity is unevenly distributed: Saudi Arabia accounts for 42% of tweets
					in the Arab-majority group, while the United States (33%) and United Kingdom (22%)
					dominate the Western group.
				</p>
				<div class="disclaimer">
					Several limitations should be noted. Firstly, X/Twitter users are not representative
					of the general population and tend to skew younger and more urban. Secondly, 55%
					of tweets lack identifiable geographic data which may introduce selection bias.
					Lastly, &ldquo;country of account&rdquo; reflects self-reported profile location
					rather than nationality or identity. This is particularly relevant in countries with
					large Arab diaspora populations (e.g. 65% of tweets from Germany are in Arabic),
					where geographic classification may not align with the political or cultural context
					of the speaker.
				</div>
				<p class="disclaimer-note">
					Accordingly, the findings should be interpreted as an analysis of online discourse
					within a specific platform and time period rather than as a measure of public opinion.
				</p>
			</div>
		</div>
	</ScrollySection>

	<!-- ============================================ -->
	<!-- SECTION 2: DISPLACEMENT AND ESCALATION       -->
	<!-- ============================================ -->
	<ScrollySection id="section2" onStepEnter={(i) => (s2Step = i)}>
		<div class="section-header">
			<span class="section-number">02</span>
			<h2 class="section-title">Displacement and Escalation</h2>
		</div>

		<div class="scroll-step prose-block">
			<p>
				The escalation in early March 2026 resulted in large-scale internal displacement
				across Lebanon. On 5 March, evacuation orders were issued for all areas south of the
				Litani River, affecting more than 100 villages. On 6 March, these orders were extended
				to Beirut's southern suburbs, leading to the rapid displacement of approximately
				700,000 residents within a 24-hour period.
			</p>
			<p>
				By 12 March, over 816,000 people had been displaced, according to the Ministry of
				Social Development. Displacement was geographically concentrated in predominantly
				Shia areas, with affected populations relocating to Sunni, Christian, and
				Druze-majority regions, placing significant pressure on shelter capacity nationwide.
			</p>
			<p>
				Casualty figures also increased rapidly during this period. By 20 March, over 1,000
				fatalities had been reported, alongside more than 128 recorded attacks on medical
				facilities (Health Ministry).
			</p>
		</div>

		<div class="scroll-step">
			<div class="sticky-visual">
				<DisplacementMap activeStep={s2Step} />
			</div>
		</div>

		<div class="scroll-step prose-block">
			<div class="callout-box">
				<div class="callout-number">82%</div>
				<div class="callout-text">
					of spike-period tweets were in English &mdash; up from 46% in the early days.
				</div>
			</div>
			<p>
				Between 12 and 19 March, the dataset records 48,407 tweets in Arabic and English from
				accounts across 150 countries. During the early phase (12&ndash;17 March), discourse
				was relatively balanced between Arabic (54%) and English (46%). By 18&ndash;19 March,
				English-language tweets accounted for 82% of the sample.
			</p>
			<p>
				This shift suggests a transition from primarily regional discourse to increased
				international attention as the escalation intensified. The change in language
				distribution is consistent with a broader expansion of the audience engaging with
				the conflict online.
			</p>
			<p>
				The following sections examine how this expansion in attention is reflected in patterns
				of blame attribution: which actors are held responsible, how this varies across
				geographic contexts and time.
			</p>
		</div>
	</ScrollySection>

	<!-- ============================================ -->
	<!-- SECTION 3: GEOGRAPHIC VARIATION               -->
	<!-- ============================================ -->
	<ScrollySection id="section3" onStepEnter={(i) => (s3Step = i)}>
		<div class="section-header">
			<span class="section-number">03</span>
			<h2 class="section-title">Geographic Variation in Blame Attribution</h2>
		</div>

		<div class="scroll-step prose-block">
			<p>
				Blame attribution was analysed across three geographic groupings: accounts based
				in Lebanon (n&nbsp;=&nbsp;4,013), accounts in Arab-majority countries
				(n&nbsp;=&nbsp;7,123), and accounts in Western countries (n&nbsp;=&nbsp;7,334).
			</p>
			<p>
				The distribution of blame varies systematically across these groups, indicating that
				attribution patterns are shaped by regional political contexts and discursive
				environments.
			</p>
		</div>

		<div class="scroll-step">
			<div class="chart-section">
				<h3 class="chart-title">Blame attribution by geographic group</h3>
				<p class="chart-desc">
					Percentage of tweets mentioning each blame target. Tweets can attribute blame
					to multiple actors, so percentages do not sum to 100%.
				</p>
				<BlameChart activeStep={s3Step} />
			</div>
		</div>

		<div class="scroll-step">
			<div class="findings-grid">
				<div class="finding-card">
					<div class="finding-stat" style="color: #c4836a">55%</div>
					<div class="finding-body">
						of tweets from <strong>Arab-majority countries</strong> attribute blame
						to Iran. The highest rates are in the Gulf states: Kuwait (70%),
						Saudi Arabia (69%), Yemen (68%), and Oman (68%). These tweets are
						overwhelmingly in Arabic (97&ndash;100%). Qatar is an outlier,
						blaming Israel (44%) more than Iran (37%).
					</div>
				</div>
				<div class="finding-card">
					<div class="finding-stat" style="color: #5b8fb9">49%</div>
					<div class="finding-body">
						of tweets from <strong>Western countries</strong> attribute blame to Israel.
						This group is dominated by the US (33%) and UK (22%). However, several
						European countries (Germany, France, Sweden) have high Arabic-language
						shares, suggesting Arab diaspora voices are present in this group.
					</div>
				</div>
				<div class="finding-card">
					<div class="finding-stat" style="color: #6a9e96">23%</div>
					<div class="finding-body">
						of tweets from <strong>Lebanese accounts</strong> blame the Lebanese
						government &mdash; the highest rate of any group. Lebanese accounts also
						show the most distributed blame pattern, with no single target exceeding 35%.
					</div>
				</div>
			</div>
		</div>

		<div class="scroll-step prose-block">
			<h3 class="subsection-heading">Variation Within Geographic Groups</h3>
			<p>
				The aggregate geographic categories reveal important country-level differences.
			</p>
			<p>
				In the Arab-majority group, Saudi Arabia alone accounts for 42% of tweets, and the
				Gulf states collectively comprise 72% of the sample. The high level of Iran-directed
				blame in this category therefore reflects a concentration within Gulf discourse rather
				than a uniform Arab pattern. Egypt and Qatar depart from this trend, with both
				attributing more blame to Israel than to Iran.
			</p>
			<p>
				Within the Western group, the United States shows the highest pro-Israel stance (16%)
				of any non-Israel country, while Ireland records the highest anti-war share (41%).
				Outside the three primary groupings, India and Pakistan are distinguished by a
				predominantly analytical stance (61&ndash;63%).
			</p>
		</div>

		<div class="scroll-step prose-block">
			<h3 class="subsection-heading">Interpreting Iran-Directed Blame</h3>
			<div class="indent-block">
				<p>
					Iran-directed blame is concentrated primarily in Arab-majority contexts,
					particularly in Gulf states, and is expressed almost entirely in Arabic. The
					dataset contains no Farsi-language tweets and only 13 tweets from accounts based
					in Iran, indicating that this pattern is not driven by Iranian domestic discourse.
				</p>
				<p>
					Within Europe, a similar pattern emerges in countries with large Arab diaspora
					populations (e.g. Germany, Sweden, France, Denmark, and Belgium). In these
					contexts, Iran-directed blame is disproportionately expressed in Arabic (e.g.
					78% of such tweets in Germany, 94% in Denmark, and 68% in Sweden).
				</p>
				<p>
					Taken together, these patterns suggest that what appears as &ldquo;Western&rdquo;
					attribution of blame to Iran partly reflects transnational Arabic-language
					discourse rather than geographically bounded public opinion. In this sense,
					language functions as a more reliable indicator of discursive alignment than
					country-level classification alone.
				</p>
			</div>
		</div>

		<div class="scroll-step prose-block">
			<p class="example-intro">
				The following examples are selected to illustrate how the dominant patterns identified
				in the dataset are expressed at the individual level. These tweets are not
				representative of the full sample but provide qualitative insight into different
				discursive framings:
			</p>
		</div>

		<div class="scroll-step">
			<div class="quote-section">
				<blockquote class="tweet-quote">
					<p class="quote-text-ar" dir="rtl" lang="ar">اقسم بمن احل القسم الي يحصل بين اسرائيل وامريكا من حربهم على ايران ومليشياتها في سوريا والعراق ولبنان تدخل الهي من رب العالمين قصاص وعقوبة لما فعلوه من جرائم ضد اهل السنة</p>
					<p class="quote-text">"I swear by God, what is happening between Israel and America in their war against Iran and its militias in Syria, Iraq and Lebanon is divine intervention &mdash; punishment for the crimes they committed against the Sunnis."</p>
					<footer class="quote-footer">
						<span class="quote-source">@NaseerSourani &middot; Arabic &middot; Finland &middot; Military background &middot; 49.7K followers &middot; <a href="https://x.com/NaseerSourani/status/2034043037630771436" target="_blank" rel="noopener">View tweet</a></span>
					</footer>
					<p class="quote-context">This example illustrates a form of sectarian and geopolitical framing observed in Arabic-language tweets, particularly in Gulf-aligned and diaspora contexts. Responsibility is attributed primarily to Iran and its regional network, and the conflict is interpreted through a religious lens. The account's location outside the region also reflects the role of transnational discourse networks in shaping geographically dispersed narratives.</p>
				</blockquote>

				<blockquote class="tweet-quote">
					<p class="quote-text">"I'm a Druze born, raised, and living in Lebanon, son of a former PSP militant who fought alongside the PLO during the Israeli siege of Beirut in 1982. Today, my old man and I both agree that we have nothing to do with Islam's holy war against the Jews. We want to live in peace."</p>
					<footer class="quote-footer">
						<span class="quote-source">@seasidedruze &middot; English &middot; Lebanon &middot; 636 followers &middot; <a href="https://x.com/seasidedruze/status/2033256746618077445" target="_blank" rel="noopener">View tweet</a></span>
					</footer>
					<p class="quote-context">This example illustrates a pattern more common among Lebanon-based accounts, where blame attribution is less concentrated on a single external actor and more reflective of internal political and sectarian dynamics. The emphasis on personal and historical context is consistent with the higher prevalence of analytical and less partisan discourse observed in this group.</p>
				</blockquote>

				<blockquote class="tweet-quote">
					<p class="quote-text">"The moment Israel targeted British journalist Steve Sweeney in Lebanon."</p>
					<footer class="quote-footer">
						<span class="quote-source">@ShaykhSulaiman &middot; English &middot; United Kingdom &middot; 822K followers &middot; <a href="https://x.com/ShaykhSulaiman/status/2034638686881464579" target="_blank" rel="noopener">View tweet</a></span>
					</footer>
					<p class="quote-context">Posted March 19 by a major UK-based account. This example reflects a form of event-driven framing observed in English-language tweets during the later stages of escalation, where attention is directed toward specific high-visibility incidents. Such moments were associated with increased attribution of responsibility to identifiable actors in Western-based discourse.</p>
				</blockquote>

				<blockquote class="tweet-quote">
					<p class="quote-text-ar" dir="rtl" lang="ar">هيدا لبنان لما كان المسيحيين والسنّة يشكلون الأغلبية. قبل عبد الناصر ومشاريعه مع المخيمات الفلسطينية. وقبل ثورة الخميني والعمائم الإيرانية. هيدا لبنان الحياد، وسويسرا الشرق.</p>
					<p class="quote-text">"This is Lebanon when Christians and Sunnis were the majority. Before Nasser and his projects with Palestinian camps. Before Khomeini's revolution and Iranian turbans. This was neutral Lebanon, the Switzerland of the East."</p>
					<footer class="quote-footer">
						<span class="quote-source">@RaymondFHakim &middot; Arabic &middot; Lebanon &middot; 183K followers &middot; 386,821 views &middot; <a href="https://x.com/RaymondFHakim/status/2034413577369465151" target="_blank" rel="noopener">View tweet</a></span>
					</footer>
					<p class="quote-context">Posted March 18 by a Lebanese Christian account with a large following. This type of narrative reflects a form of retrospective framing that emphasises a pre-conflict political order. Such framings attribute responsibility to later regional and ideological developments, while downplaying or selectively interpreting the structural conditions that contributed to Lebanon's earlier conflicts.</p>
				</blockquote>
			</div>
		</div>

		<div class="scroll-step prose-block">
			<h3 class="subsection-heading">Stance Analysis</h3>
			<p>
				In addition to blame attribution, tweets were classified by discursive stance.
				Accounts based in Lebanon show the highest proportion of analytical content (54%)
				and the lowest levels of explicitly partisan positioning among all groups.
			</p>
			<p>
				By contrast, pro-resistance sentiment is more prevalent in several Arab-majority
				contexts, including Tunisia (48%), Yemen (27%), and Iraq (24%). Notably, this stance
				is also more common among Arab diaspora accounts (17%) than among Lebanon-based
				accounts (10%).
			</p>
			<p>
				This distribution suggests that proximity to the conflict may be associated with more
				analytical and less polarised forms of discourse, while more distant or diaspora
				contexts exhibit higher levels of explicitly partisan framing. This relationship is
				descriptive and does not imply causation, but it is consistent across the dataset.
			</p>
			<div class="stance-comparison">
				<div class="stance-row">
					<span class="stance-label">Pro-resistance</span>
					<div class="stance-bars">
						<div class="stance-bar-group">
							<span class="stance-bar-label">Arab countries</span>
							<div class="stance-bar-track">
								<div class="stance-bar-fill diaspora" style="width: {17}%"></div>
							</div>
							<span class="stance-bar-value">17%</span>
						</div>
						<div class="stance-bar-group">
							<span class="stance-bar-label">Lebanon</span>
							<div class="stance-bar-track">
								<div class="stance-bar-fill lebanon" style="width: {10}%"></div>
							</div>
							<span class="stance-bar-value">10%</span>
						</div>
					</div>
				</div>
				<div class="stance-row">
					<span class="stance-label">Analytical</span>
					<div class="stance-bars">
						<div class="stance-bar-group">
							<span class="stance-bar-label">Arab countries</span>
							<div class="stance-bar-track">
								<div class="stance-bar-fill diaspora" style="width: {29}%"></div>
							</div>
							<span class="stance-bar-value">29%</span>
						</div>
						<div class="stance-bar-group">
							<span class="stance-bar-label">Lebanon</span>
							<div class="stance-bar-track">
								<div class="stance-bar-fill lebanon" style="width: {54}%"></div>
							</div>
							<span class="stance-bar-value">54%</span>
						</div>
					</div>
				</div>
			</div>
			<p class="aside">
				Proximity to conflict correlates with a more analytical, less partisan stance.
			</p>
		</div>
	</ScrollySection>

	<!-- ============================================ -->
	<!-- SECTION 4: TEMPORAL SHIFTS                   -->
	<!-- ============================================ -->
	<ScrollySection id="section4" onStepEnter={(i) => (s4Step = i)}>
		<div class="section-header">
			<span class="section-number">04</span>
			<h2 class="section-title">Temporal Shifts During Escalation</h2>
		</div>

		<div class="scroll-step prose-block">
			<p>
				The dataset spans eight days and is divided into an early period (12&ndash;17 March)
				and a spike period (18&ndash;19 March), during which the intensity of military
				activity and international media attention increased. The shift in discourse between
				these periods is measurable.
			</p>
		</div>

		<div class="scroll-step">
			<div class="chart-section">
				<h3 class="chart-title">Changes in Blame Attribution</h3>
				<p class="chart-desc">
					Each pair shows how blame attribution changed between the early period
					and the spike. The delta measures the shift in percentage points.
				</p>
				<TimelineChart activeStep={s4Step} />
			</div>
		</div>

		<div class="scroll-step">
			<div class="collapse-callout">
				<div class="collapse-visual">
					<div class="collapse-before">
						<span class="collapse-number">20%</span>
						<span class="collapse-period">Early</span>
					</div>
					<div class="collapse-arrow">
						<svg width="60" height="24" viewBox="0 0 60 24">
							<line x1="0" y1="12" x2="50" y2="12" stroke="rgba(212, 208, 200, 0.3)" stroke-width="2" />
							<polygon points="50,6 60,12 50,18" fill="rgba(212, 208, 200, 0.3)" />
						</svg>
					</div>
					<div class="collapse-after">
						<span class="collapse-number faded">7%</span>
						<span class="collapse-period">Spike</span>
					</div>
				</div>
				<p class="collapse-label">
					Blame attributed to the <strong>sectarian system</strong> falls from 19.9% to
					7.1% (&ndash;12.8 percentage points), representing the largest shift in the dataset.
					Attribution to the Lebanese government (&ndash;5.2pp) and Iran (&ndash;5.8pp) also
					declines. By contrast, attribution to proximate conflict actors increases, with
					Israel rising from 37.4% to 42.2% (+4.8pp) and Hezbollah from 24% to 30.3% (+6.3pp).
				</p>
			</div>
		</div>

		<div class="scroll-step prose-block">
			<h3 class="subsection-heading">From Structural to Event-Driven Framing</h3>
			<div class="indent-block">
				<p>
					During the early period, blame attribution&mdash;particularly among Lebanon-based
					accounts&mdash;was relatively distributed across multiple actors, including the
					Lebanese government (28%), the sectarian system (24%), and Israel (27%). This
					pattern reflects a more structural interpretation of the crisis, emphasising
					governance failures and longer-term political arrangements.
				</p>
				<p>
					During the spike period, this distribution narrows. References to systemic and
					institutional actors decline, while attribution increasingly concentrates on those
					directly engaged in military activity. This shift is consistent with a move from
					structural to event-driven framing, in which immediate developments take precedence
					over broader explanatory narratives.
				</p>
			</div>
		</div>

		<div class="scroll-step prose-block">
			<div class="language-shift-box">
				<h4 class="shift-heading">Language Shift</h4>
				<div class="lang-bars">
					<div class="lang-row">
						<span class="lang-label">Mar 12&ndash;17</span>
						<div class="lang-bar-track">
							<div class="lang-segment arabic" style="width: 54%">
								<span>Arabic 54%</span>
							</div>
							<div class="lang-segment english" style="width: 46%">
								<span>English 46%</span>
							</div>
						</div>
					</div>
					<div class="lang-row">
						<span class="lang-label">Mar 18&ndash;19</span>
						<div class="lang-bar-track">
							<div class="lang-segment arabic" style="width: 18%">
								<span>18%</span>
							</div>
							<div class="lang-segment english" style="width: 82%">
								<span>English 82%</span>
							</div>
						</div>
					</div>
				</div>
				<p class="shift-note">
					The temporal shift in attribution is accompanied by a change in language
					distribution. During 12&ndash;17 March, tweets are relatively balanced between
					Arabic (54%) and English (46%). By 18&ndash;19 March, English-language tweets
					account for 82% of the sample. This change suggests an expansion from primarily
					regional to more international discourse. Arabic-language tweets are more likely
					to include structural or system-level critique, whereas English-language tweets
					more frequently focus on identifiable state and non-state actors. The shift in
					language therefore corresponds with the observed movement from structural to
					actor-focused attribution.
				</p>
			</div>
		</div>
	</ScrollySection>

	<!-- ============================================ -->
	<!-- SECTION 5: DISCUSSION                        -->
	<!-- ============================================ -->
	<section class="coda">
		<div class="coda-inner">
			<div class="section-header" style="padding-top: 0;">
				<span class="section-number">05</span>
				<h2 class="section-title">Discussion</h2>
			</div>

			<h3 class="discussion-heading">Key Findings</h3>
			<div class="indent-block">
				<p class="coda-text">
					The analysis indicates that geographic location is closely associated with patterns
					of blame attribution in online discourse. Accounts based in Lebanon distribute blame
					across a wider range of actors and exhibit the highest proportion of analytical
					content. In contrast, accounts in Gulf states show a higher concentration of
					Iran-directed blame, consistent with prevailing regional political narratives.
					Accounts in Anglophone Western countries are more likely to attribute responsibility
					to Israel, reflecting a focus on observable state military action in English-language
					discourse.
				</p>
				<p class="coda-text">
					The temporal analysis further suggests that escalation is associated with a narrowing
					of discourse. As the intensity of violence increases, attention shifts away from
					systemic and institutional factors toward immediate actors directly involved in the
					conflict. This is reflected in the decline of references to the sectarian system and
					domestic governance during the spike period, alongside increased attribution to
					Israel and Hezbollah.
				</p>
			</div>

			<p class="coda-text coda-transition">
				Beyond shifts in blame attribution, the displacement itself also emerged as a distinct
				focus of online discourse.
			</p>

			<h3 class="discussion-heading">Displacement and Inter-Communal Tension</h3>
			<div class="indent-block">
				<p class="coda-text">
					A supplementary analysis of 12,338 displacement-related tweets suggests that the
					large-scale movement of populations from southern Lebanon and Beirut's southern
					suburbs was framed less in material than in political and sectarian terms. Sectarian
					framing was the most common category (53%), followed by securitisation (39%) and
					exclusionary rhetoric (31%), while references to economic or service burden were
					comparatively rare (3.6%). This indicates that displacement was discussed primarily
					as a question of identity, security, and communal balance rather than humanitarian
					management or state capacity.
				</p>
				<p class="coda-text">
					Geographic variation within this subset is also notable. Lebanon-based accounts show
					the lowest level of exclusionary rhetoric (20%) and the highest level of solidarity
					framing (27%), whereas accounts in Arab-majority countries&mdash;particularly in the
					Gulf&mdash;display substantially higher rates of exclusionary language (43%). This
					pattern is consistent with the broader finding that proximity to conflict is
					associated with less polarised and less exclusionary forms of discourse.
				</p>
				<p class="coda-text">
					Within Lebanon, language also appears to shape framing. English-language tweets show
					higher levels of sectarian framing than Arabic-language tweets, while Arabic posts
					are more likely to adopt practical or informational tones. This may reflect
					differences in audience orientation, with English-language discourse more focused
					on external explanation and political framing.
				</p>
			</div>

			<h3 class="discussion-heading">Interpretation</h3>
			<div class="indent-block">
				<p class="coda-text">
					Taken together, these findings suggest that online discourse during conflict is
					shaped by a combination of geographic context, linguistic community, and proximity
					to events. In particular, proximity to the conflict appears to be associated with
					more distributed and analytical forms of attribution, while more distant or
					diasporic contexts exhibit more concentrated and partisan framings.
				</p>
				<p class="coda-text">
					The observed shift from structural to event-driven attribution during escalation
					highlights a potential constraint for policy communication. Narratives that
					emphasise institutional reform or long-term structural factors may become less
					salient during periods of acute violence, when attention is focused on immediate
					actions and responsibility.
				</p>
			</div>

			<h3 class="discussion-heading">Limitations</h3>
			<div class="indent-block">
				<p class="coda-text">
					These findings are descriptive and do not establish causal relationships between
					geographic location and patterns of discourse. The dataset reflects activity on a
					single platform over a limited time period and is subject to selection bias,
					including incomplete geographic data and the demographic skew of X/Twitter users.
				</p>
				<p class="coda-text">
					Accordingly, the analysis should be interpreted as an account of observable
					discourse within a specific digital environment, rather than as a measure of
					broader public opinion.
				</p>
			</div>

			<div class="coda-stats">
				<div class="coda-stat">
					<span class="coda-stat-value">{blameData.metadata.valid_tweets.toLocaleString()}</span>
					<span class="coda-stat-label">tweets analysed</span>
				</div>
				<div class="coda-stat">
					<span class="coda-stat-value">150</span>
					<span class="coda-stat-label">countries</span>
				</div>
				<div class="coda-stat">
					<span class="coda-stat-value">2</span>
					<span class="coda-stat-label">languages</span>
				</div>
			</div>
		</div>
	</section>
</main>

<style>
	/* ============================
	   HEADER
	   ============================ */
	.report-header {
		min-height: 100vh;
		min-height: 100dvh;
		display: flex;
		align-items: center;
		justify-content: center;
		text-align: center;
		padding: 2rem;
		position: relative;
	}

	.header-inner {
		max-width: 750px;
	}

	.report-title {
		font-size: clamp(2rem, 6vw, 3.25rem);
		font-weight: 700;
		line-height: 1.2;
		margin-bottom: 2rem;
		color: #d4d0c8;
		letter-spacing: -0.01em;
	}

	.title-subtitle {
		font-weight: 300;
		font-size: clamp(0.95rem, 2.2vw, 1.15rem);
		display: block;
		margin-top: 0.75rem;
		color: rgba(212, 208, 200, 0.55);
		line-height: 1.6;
		letter-spacing: 0;
		font-style: italic;
	}

	.scroll-hint {
		display: flex;
		justify-content: center;
	}

	.scroll-arrow {
		width: 16px;
		height: 16px;
		border-right: 1.5px solid rgba(212, 208, 200, 0.2);
		border-bottom: 1.5px solid rgba(212, 208, 200, 0.2);
		transform: rotate(45deg);
		animation: bounce 2.5s ease-in-out infinite;
	}

	@keyframes bounce {
		0%, 100% { transform: rotate(45deg) translateY(-2px); opacity: 0.2; }
		50% { transform: rotate(45deg) translateY(2px); opacity: 0.4; }
	}

	/* ============================
	   SECTION HEADERS
	   ============================ */
	.section-header {
		text-align: center;
		padding: 4rem 2rem 2rem;
	}

	.section-number {
		display: block;
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.65rem;
		letter-spacing: 0.2em;
		color: rgba(212, 208, 200, 0.3);
		margin-bottom: 0.75rem;
		font-weight: 400;
	}

	.section-title {
		font-size: clamp(1.4rem, 3.5vw, 2rem);
		font-weight: 600;
		line-height: 1.2;
		color: #d4d0c8;
		letter-spacing: -0.01em;
	}

	/* ============================
	   SCROLL STEPS & PROSE
	   ============================ */
	.scroll-step {
		min-height: 40vh;
		display: flex;
		align-items: center;
		justify-content: center;
		padding: 3rem 1.5rem;
	}

	.prose-block {
		flex-direction: column;
		max-width: 640px;
		margin: 0 auto;
	}

	.prose-block p {
		font-size: clamp(0.88rem, 1.8vw, 0.95rem);
		line-height: 1.85;
		color: rgba(212, 208, 200, 0.75);
		margin-bottom: 1.25rem;
	}

	.prose-block p strong {
		color: #d4d0c8;
		font-weight: 600;
	}

	.example-intro {
		font-size: clamp(0.85rem, 1.6vw, 0.9rem) !important;
		color: rgba(212, 208, 200, 0.5) !important;
		font-style: italic;
	}

	.aside {
		font-style: italic;
		color: rgba(212, 208, 200, 0.4) !important;
		text-align: center;
		font-size: 0.85rem !important;
	}

	.subsection-heading {
		font-size: clamp(0.95rem, 2vw, 1.1rem);
		font-weight: 600;
		color: #d4d0c8;
		margin-bottom: 1rem;
	}

	.indent-block {
		padding-left: 1.5rem;
		border-left: 2px solid rgba(212, 208, 200, 0.06);
	}

	.indent-block p {
		font-size: clamp(0.85rem, 1.7vw, 0.92rem);
		line-height: 1.85;
		color: rgba(212, 208, 200, 0.7);
		margin-bottom: 1.25rem;
	}

	/* ============================
	   METHOD BOX
	   ============================ */
	.method-box {
		padding: 2rem;
		border: 1px solid rgba(212, 208, 200, 0.08);
		border-radius: 3px;
		background: rgba(212, 208, 200, 0.02);
		max-width: 640px;
	}

	.method-heading {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.75rem;
		font-weight: 500;
		color: rgba(212, 208, 200, 0.55);
		text-transform: uppercase;
		letter-spacing: 0.1em;
		margin-bottom: 1.25rem;
	}

	.method-box p {
		font-size: 0.85rem !important;
		line-height: 1.8;
		color: rgba(212, 208, 200, 0.6);
		margin-bottom: 1rem;
	}

	.disclaimer {
		margin-top: 1.25rem;
		padding-top: 1.25rem;
		border-top: 1px solid rgba(212, 208, 200, 0.06);
		font-size: 0.8rem;
		line-height: 1.75;
		color: rgba(212, 208, 200, 0.4);
	}

	.disclaimer-note {
		margin-top: 0.75rem;
		font-size: 0.8rem !important;
		color: rgba(212, 208, 200, 0.4) !important;
		font-style: italic;
	}

	/* ============================
	   CALLOUT BOX
	   ============================ */
	.callout-box {
		display: flex;
		gap: 1.5rem;
		align-items: center;
		padding: 1.5rem 2rem;
		border: 1px solid rgba(212, 208, 200, 0.08);
		border-radius: 3px;
		background: rgba(212, 208, 200, 0.02);
		margin-bottom: 2rem;
	}

	.callout-number {
		font-family: 'JetBrains Mono', monospace;
		font-size: 2rem;
		font-weight: 500;
		color: #b8a47e;
		flex-shrink: 0;
		line-height: 1;
	}

	.callout-text {
		font-size: 0.85rem;
		color: rgba(212, 208, 200, 0.6);
		line-height: 1.6;
	}

	@media (max-width: 500px) {
		.callout-box {
			flex-direction: column;
			text-align: center;
			gap: 0.75rem;
			padding: 1.25rem;
		}
	}

	/* ============================
	   STICKY VISUAL
	   ============================ */
	.sticky-visual {
		width: 100%;
		max-width: 800px;
	}

	/* ============================
	   CHART SECTIONS
	   ============================ */
	.chart-section {
		width: 100%;
		max-width: 750px;
		padding: 0 1rem;
	}

	.chart-title {
		font-size: clamp(0.95rem, 2vw, 1.1rem);
		font-weight: 600;
		color: #d4d0c8;
		text-align: center;
		margin-bottom: 0.5rem;
	}

	.chart-desc {
		font-size: 0.72rem;
		color: rgba(212, 208, 200, 0.35);
		text-align: center;
		max-width: 500px;
		margin: 0 auto 2rem;
		line-height: 1.5;
	}

	/* ============================
	   FINDINGS GRID
	   ============================ */
	.findings-grid {
		display: grid;
		grid-template-columns: 1fr;
		gap: 1.25rem;
		max-width: 700px;
		padding: 0 1rem;
	}

	@media (min-width: 640px) {
		.findings-grid {
			grid-template-columns: repeat(3, 1fr);
		}
	}

	.finding-card {
		padding: 1.5rem;
		border-radius: 3px;
		border: 1px solid rgba(212, 208, 200, 0.06);
		background: rgba(212, 208, 200, 0.02);
	}

	.finding-stat {
		font-family: 'JetBrains Mono', monospace;
		font-size: 2rem;
		font-weight: 500;
		line-height: 1;
		margin-bottom: 0.75rem;
	}

	.finding-body {
		font-size: 0.78rem;
		color: rgba(212, 208, 200, 0.55);
		line-height: 1.7;
	}

	.finding-body strong {
		color: #d4d0c8;
	}

	/* ============================
	   QUOTES
	   ============================ */
	.quote-section {
		display: flex;
		flex-direction: column;
		gap: 2rem;
		max-width: 620px;
		padding: 0 1rem;
	}

	.tweet-quote {
		padding: 1.5rem 2rem;
		border-left: 2px solid rgba(212, 208, 200, 0.1);
		background: rgba(212, 208, 200, 0.015);
		border-radius: 0 3px 3px 0;
	}

	.quote-text-ar {
		font-size: 0.82rem;
		line-height: 1.8;
		color: rgba(212, 208, 200, 0.4);
		margin-bottom: 0.75rem;
		font-style: italic;
	}

	.quote-text {
		font-size: 0.88rem;
		line-height: 1.7;
		color: rgba(212, 208, 200, 0.7);
		margin-bottom: 0.75rem;
		font-style: italic;
	}

	.quote-footer {
		margin-bottom: 0.5rem;
	}

	.quote-source {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.6rem;
		color: rgba(212, 208, 200, 0.3);
		font-weight: 400;
	}

	.quote-source a {
		color: rgba(212, 208, 200, 0.4);
		text-decoration: underline;
		text-underline-offset: 2px;
	}

	.quote-source a:hover {
		color: rgba(212, 208, 200, 0.6);
	}

	.quote-context {
		font-size: 0.75rem;
		color: rgba(212, 208, 200, 0.45);
		line-height: 1.7;
		font-style: normal;
	}

	/* ============================
	   STANCE COMPARISON
	   ============================ */
	.stance-comparison {
		display: flex;
		flex-direction: column;
		gap: 2rem;
		margin: 2.5rem 0;
		width: 100%;
	}

	.stance-row {
		display: flex;
		flex-direction: column;
		gap: 0.6rem;
		width: 100%;
	}

	.stance-label {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.72rem;
		font-weight: 600;
		color: rgba(212, 208, 200, 0.55);
		text-transform: uppercase;
		letter-spacing: 0.06em;
	}

	.stance-bars {
		display: flex;
		flex-direction: column;
		gap: 0.4rem;
		width: 100%;
	}

	.stance-bar-group {
		display: flex;
		align-items: center;
		gap: 0.75rem;
	}

	.stance-bar-label {
		font-size: 0.72rem;
		color: rgba(212, 208, 200, 0.45);
		width: 100px;
		flex-shrink: 0;
		text-align: right;
	}

	.stance-bar-track {
		flex: 1;
		height: 24px;
		background: rgba(212, 208, 200, 0.04);
		border-radius: 3px;
		overflow: hidden;
	}

	.stance-bar-fill {
		height: 100%;
		border-radius: 3px;
		transition: width 0.6s ease, filter 0.2s ease;
	}

	.stance-bar-value {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.72rem;
		font-weight: 600;
		color: rgba(212, 208, 200, 0.6);
		flex-shrink: 0;
		width: 36px;
	}

	.stance-bar-group:hover .stance-bar-fill {
		filter: brightness(1.15);
	}

	.stance-bar-group:hover .stance-bar-value {
		color: rgba(212, 208, 200, 0.85);
	}

	.stance-bar-fill.diaspora {
		background: #c4836a;
	}

	.stance-bar-fill.lebanon {
		background: #5b8fb9;
	}

	/* ============================
	   COLLAPSE CALLOUT
	   ============================ */
	.collapse-callout {
		text-align: center;
		max-width: 560px;
		padding: 2.5rem 2rem;
		border: 1px solid rgba(212, 208, 200, 0.08);
		border-radius: 3px;
		background: rgba(212, 208, 200, 0.02);
	}

	.collapse-visual {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 1.5rem;
		margin-bottom: 1.5rem;
	}

	.collapse-before,
	.collapse-after {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.25rem;
	}

	.collapse-number {
		font-family: 'JetBrains Mono', monospace;
		font-size: 2rem;
		font-weight: 500;
		color: rgba(212, 208, 200, 0.6);
		line-height: 1;
	}

	.collapse-number.faded {
		opacity: 0.35;
	}

	.collapse-period {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.6rem;
		color: rgba(212, 208, 200, 0.3);
		text-transform: uppercase;
		letter-spacing: 0.1em;
	}

	.collapse-arrow {
		flex-shrink: 0;
	}

	.collapse-label {
		font-size: 0.82rem;
		color: rgba(212, 208, 200, 0.55);
		line-height: 1.7;
		text-align: left;
	}

	/* ============================
	   LANGUAGE SHIFT BOX
	   ============================ */
	.language-shift-box {
		padding: 2rem;
		border: 1px solid rgba(212, 208, 200, 0.06);
		border-radius: 3px;
		background: rgba(212, 208, 200, 0.015);
		max-width: 640px;
	}

	.shift-heading {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.72rem;
		font-weight: 500;
		color: rgba(212, 208, 200, 0.5);
		text-transform: uppercase;
		letter-spacing: 0.1em;
		margin-bottom: 1.25rem;
	}

	.lang-bars {
		display: flex;
		flex-direction: column;
		gap: 0.75rem;
		margin-bottom: 1rem;
	}

	.lang-row {
		display: flex;
		align-items: center;
		gap: 0.75rem;
	}

	.lang-label {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.62rem;
		color: rgba(212, 208, 200, 0.35);
		width: 70px;
		flex-shrink: 0;
		text-align: right;
		font-weight: 400;
	}

	.lang-bar-track {
		flex: 1;
		display: flex;
		height: 26px;
		border-radius: 3px;
		overflow: hidden;
		gap: 2px;
	}

	.lang-segment {
		display: flex;
		align-items: center;
		justify-content: center;
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.56rem;
		font-weight: 500;
		color: rgba(255, 255, 255, 0.85);
		transition: width 0.6s ease, filter 0.2s ease;
		cursor: default;
	}

	.lang-segment:hover {
		filter: brightness(1.15);
	}

	.lang-segment span {
		white-space: nowrap;
		overflow: hidden;
		text-overflow: ellipsis;
		padding: 0 6px;
	}

	.lang-segment.arabic {
		background: #c4836a;
	}

	.lang-segment.english {
		background: #5b8fb9;
	}

	.shift-note {
		font-size: 0.78rem;
		color: rgba(212, 208, 200, 0.4);
		line-height: 1.7;
	}

	/* ============================
	   CODA / DISCUSSION
	   ============================ */
	.coda {
		padding: 6rem 2rem 8rem;
	}

	.coda-inner {
		max-width: 640px;
		margin: 0 auto;
	}

	.discussion-heading {
		font-size: clamp(0.95rem, 2vw, 1.1rem);
		font-weight: 600;
		color: #d4d0c8;
		margin-bottom: 1rem;
		margin-top: 2.5rem;
	}

	.coda-text {
		font-size: clamp(0.85rem, 1.8vw, 0.92rem);
		color: rgba(212, 208, 200, 0.65);
		line-height: 1.85;
		margin-bottom: 1.25rem;
		text-align: left;
	}

	.coda-transition {
		margin-top: 2rem;
		font-style: italic;
		color: rgba(212, 208, 200, 0.5);
	}

	.coda-inner .indent-block {
		margin-bottom: 0.5rem;
	}

	.coda-inner .indent-block .coda-text {
		font-size: clamp(0.83rem, 1.7vw, 0.9rem);
		color: rgba(212, 208, 200, 0.6);
	}

	.coda-stats {
		display: flex;
		gap: 2.5rem;
		justify-content: center;
		flex-wrap: wrap;
		margin: 4rem 0 0;
		padding: 2rem 0;
		border-top: 1px solid rgba(212, 208, 200, 0.06);
	}

	.coda-stat {
		display: flex;
		flex-direction: column;
		align-items: center;
		gap: 0.25rem;
	}

	.coda-stat-value {
		font-family: 'JetBrains Mono', monospace;
		font-size: 1.35rem;
		font-weight: 500;
		color: #b8a47e;
	}

	.coda-stat-label {
		font-family: 'JetBrains Mono', monospace;
		font-size: 0.58rem;
		color: rgba(212, 208, 200, 0.3);
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	/* ============================
	   RESPONSIVE
	   ============================ */
	@media (max-width: 640px) {
		.scroll-step {
			padding: 3rem 1rem;
			min-height: 50vh;
		}

		.section-header {
			padding: 4rem 1rem 1.5rem;
		}

		.tweet-quote {
			padding: 1rem 1.25rem;
		}

		.coda {
			padding: 4rem 1.5rem 6rem;
		}

		.coda-stats {
			gap: 1.5rem;
		}

		.indent-block {
			padding-left: 1rem;
		}
	}
</style>
