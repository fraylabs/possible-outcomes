# How AgentMail gets customers

**One-line verdict:** A developer-distribution machine: agents and coding tools are the channel. Their SDKs, MCP server, Claude Code plugin and llms.txt self-signup bring in installs [E13, E14, E18, E28, E29, E30]. A partner embed in Browser Use Cloud and a run of named YC-network customer stories add credibility [E16, E17]. A very high-volume content site captures search and AI-answer traffic [E10, E19, E20]. Funding and YC endorsement amplify all of it [E15].

## TL;DR
- **They distribute through the agent tools themselves.** There is an official Claude Code plugin (hosted MCP plus skills, one command), 12 `https://www.agentmail.to/build/{agent}` pages, "Install skill" tabs for six agents on the homepage, and 40 public repos [E13, E18, E19, E28]. The npm package `agentmail` had 989,332 downloads and PyPI `agentmail` 1,406,613 in the last month [E29, E30]. Likely most of that volume is CI and agent installs rather than unique developers, but it shows the SDK is where usage flows.
- **Agents can sign up without a human.** llms.txt opens with "If you are an AI agent and need email, follow these steps" and gives a one-call `POST https://api.agentmail.to/v0/agent/sign-up` [E14]. The seed post says "Autonomous agents have started signing up for AgentMail on their own, finding us through web search" [E15]. This works because their buyer's agent is literally the one reading the docs.
- **One partner embed turned into a reference customer.** "Every Browser Use Cloud session now ships with its own AgentMail inbox… Zero config, no API key" [E17]. Browser Use's CEO also appears as a homepage testimonial [E13]. AgentCard by Alchemy gives every agent an inbox by default [E16].
- **They publish content at industrial scale.** The sitemap has 592 URLs and 187 content updates in 90 days, with 127 blog posts in the last 30 days [E10]. There are 100 more question-shaped "solution-recommendation" pages [E20], at least 10 comparison posts against email APIs [E19], and llms.txt with all AI bots allowed [E11]. They also write about the topic next door: agent auth and identity, 2FA and OTP [E21, E24, E25].
- **The free tier is the front door.** "Start for free" with no card, 3 inboxes and 3,000 emails a month. Paid starts at $20/mo, and Startup at $200/mo comes with a SOC 2 report [E12, E1]. A contact-sales Enterprise tier sits on top [E6, E12].

## Channel scorecard
| Channel | Status | Strength (0–3) | What we saw | Evidence |
|---|---|---|---|---|
| Developer distribution (SDKs, MCP, plugins, skills) | active | 3 | 40 repos; Claude Code plugin; 6 agent install tabs; ~1M npm and ~1.4M PyPI monthly downloads | [E13, E18, E28, E29, E30] |
| Partner embeds | active | 3 | AgentMail inbox in every Browser Use Cloud session; AgentCard default inbox | [E16, E17] |
| SEO | active | 3 | 592 URLs, 187 updates/90d, 12 https://www.agentmail.to/build pages, 21 use-case pages, comparison posts | [E10, E19] |
| GEO / AI search | active | 3 | llms.txt with agent self-signup; AI bots allowed; 100 Q&A-shaped pages | [E11, E14, E20] |
| Launches (HN, PH) | active | 2 | Show HN 121 points / 70 comments (2025-07-31); PH 5.0, 5 reviews, 435 followers | [E8, E27, E31] |
| Sales-led | active | 1 | Enterprise "Contact sales"; SOC 2; EU region; white-label | [E6, E12] |
| Paid (Meta, Google, LinkedIn, Reddit, TikTok, X…) | likely | 1 | 10 ad pixels via GTM, incl. Google Ads AW-18175082927; no ad-library check | [E3] |
| Founder-led | unknown | 0 | Founders Haakam, Michael, Adi (Show HN); audience not checked | [E27, E15] |
| Affiliate | none | 0 | No affiliate program found | [E4] |
| App stores | none | 0 | No App Store / Play app | — |

## The engine
- **Entry:** a developer's coding agent installs the plugin or skill, or an agent reads llms.txt and signs itself up [E14, E18]. On the web, the homepage shows a live inbox created for the visitor and "Start for free" [E13].
- **Conversion:** a free org (3 inboxes) becomes Developer at $20/mo once usage passes 3 inboxes or 3,000 emails, or once custom domains or removing the "Sent via AgentMail" footer start to matter [E12]. Likely the footer on free-tier mail also works as a small viral loop [E12].
- **Upmarket:** Startup at $200/mo with a SOC 2 report, then Enterprise [E12]. Customer stories run from startups to Opendoor [E16].
- **Loop:** each integration (Browser Use, AgentCard) becomes a customer story and a testimonial. That feeds the homepage and blog, and the blog feeds search and AI answers that send agents back to llms.txt [E13, E16, E17, E20]. Likely the new products (AgentID, Agent Armor) extend the same funnel into identity and security [E21, E22].

## Paid
Ten ad and attribution pixels are installed through GTM-P4JSK69N: X, Meta, Google Ads (AW-18175082927), TikTok, LinkedIn, Reddit, Pinterest, Snap, Quora and Floodlight [E3]. A pixel shows intent or past use, not current ads. No ad library was checked: there was no Scrape Creators key, and the public libraries need a browser, which this run did not use. No volume, creatives, longevity or spend can be stated. Probably paid plays a small part next to developer distribution: the scorecard strength is 1 [E3].

## Organic social
X (@agentmail), LinkedIn (agentmailto) and Discord are linked from the site [E2]. None was measured (no Scrape Creators key, and no logins). Cadence, reach and top posts are unknown. The homepage offers a weekly newsletter [E13].

## SEO & AI search
- **Size:** 592 sitemap URLs: https://www.agentmail.to/docs 330, https://www.agentmail.to/blog 211, https://www.agentmail.to/use-case 21, https://www.agentmail.to/build 12 [E10]. A second sitemap adds 100 `https://www.agentmail.to/blog/info/blog/solution-recommendation/{question}` pages [E20].
- **Templates:** `https://www.agentmail.to/build/{agent}` covers Claude Code, Codex, Cursor, Devin, Lovable, Replit, Vercel and others. `https://www.agentmail.to/use-case/{job}` covers recruiting, support, sales, n8n and more. `agentmail-vs-{email API}` covers Mailgun, Postmark, SendGrid, Resend, SES, Gmail API, Nylas, plus "building yourself" [E19].
- **Cadence:** 127 blog posts in 30 days [E10]. Likely mostly AI-assisted, given the volume [E10].
- **Gaps they admit:** "AgentMail does not rank for its own alternatives query, which is part of why this page exists" [E26].
- **AI search:** llms.txt published and written to agents, with GPTBot, ClaudeBot, PerplexityBot and Google-Extended allowed [E11, E14].
- **Adjacent territory:** posts on agent authentication and identity compare Auth0, Entra, WorkOS, Arcade, Nango, Descope, Stytch and their own AgentID [E25]. The 2FA/OTP post covers emailed codes only. It has 0 mentions of authenticator/TOTP or vaults/password managers, and neither does the homepage or pricing page [E24].

## Founders & people
REM's founder hint "Browser Use (Co-founder and CEO)" is wrong: it comes from a testimonial by Magnus Muller of Browser Use [E7, E13]. The Show HN post names the team as "Haakam, Michael, and Adi" [E27], and the seed post is by Haakam Aujla [E15]. Their audience size and posting habits were not checked. Backers named in the seed post (General Catalyst, YC, Paul Graham, Dharmesh Shah, Paul Copplestone, Karim Atiyeh) [E15] and a Garry Tan quote on the homepage [E13] act as borrowed reach.

## Reddit
Not checked. Reddit search needs a key or a browser, and the Reddit pixel is the only signal [E3]. Whether they post or get recommended there is unknown.

## Community & launches
- Show HN, 2025-07-31: 121 points, 70 comments, with an origin story: "we were building on top of Gmail, which was a struggle" [E8, E27].
- Product Hunt: 5.0 from 5 reviews, 435 followers [E31].
- An owned Discord is linked as the support channel for the free tier [E2, E12].
- An evals leaderboard made with Scope ranks models and harnesses on their API. Likely it is a shareable asset that also teaches agents their API [E23].

## Funnel & monetization
Self-serve PLG with a sales tier on top [E6, E12]:
- **Tiers:** Free $0 (no card), Developer $20/mo, Startup $200/mo, Enterprise custom.
- **Add-ons:** $2/mo per inbox, domain or 1,000 emails; $5/mo per seat; 20% off yearly [E12].
- **Lifecycle:** no email tool visible client-side, so this is unknown, not none [E4].
- **Affiliate:** none found [E4].
- **Social proof:** 11 named testimonials, "100M+ emails delivered", CarEdge with 25,000+ inboxes, 13 customer stories, "Backed by Y Combinator", SOC 2 [E13, E16].

## Positioning over time
- **2025-03:** "The Email Provider for AI Agents", with "Join the waitlist" and Discord CTAs [E9].
- **2025-10:** "Get Started".
- **2026-04:** the headline becomes "Email Inbox API for AI Agents" with a single "Start for free" CTA.
- **2026-10:** adds "Free tier, no credit card required" and "Install skill" [E9].

Likely the move went from community waitlist to self-serve, and now to agent-installed distribution. AgentID ("A sign-in button for AI agents") puts them on the identity ground that ActAs claims [E13, E21].

## Them vs you
| | AgentMail | ActAs | Who's ahead |
|---|---|---|---|
| Positioning | "Email Inboxes for AI Agents": email infrastructure, now adding AgentID sign-in [E1, E21] | "Its own email, logins and 2FA codes": a full agent identity [E33] | ActAs has the broader promise for browser agents. AgentMail has the clearer one-word category ("email") |
| Problem framing | Browser agents stall at OTP/2FA; their fix is reading the email [E17, E24] | "Agents stall at 'check your email'", plus the password, 2FA seed and API key afterwards [E33] | **ActAs.** AgentMail's 2FA content never mentions authenticator codes or vaults [E24] |
| Pricing | Free, then $20 / $200 / custom, plus add-ons [E12] | One plan, US$12/mo or US$120/yr: 10 identities, 5,000 incoming emails/mo, 1 domain [E33] | ActAs is simpler and cheaper to start paying. AgentMail scales further |
| Free tier | Yes: 3 inboxes, no card [E12] | None found; creating anything needs Pro [E33, E34] | **AgentMail**, clearly |
| Custom domain | From Developer ($20) [E12] | Included in the $12 plan [E33] | ActAs |
| First run | Live inbox demo on the homepage; one-command plugin; an agent can sign itself up from llms.txt [E13, E14, E18] | Email-link sign-in, subscribe, connect a domain, create an agent, download a connection file, install the CLI from a downloaded .tgz [E33] | **AgentMail.** Theirs is seconds and agent-driven; ours is six human steps behind a paywall |
| Sending | Full two-way, threads, attachments [E1, E12] | Plain text or simple HTML, one recipient, verified SES domain only [E33, E34] | AgentMail. ActAs says plainly it's not for bulk email [E33] |
| Security / trust | SOC 2 on Startup and up; signed webhooks; MFA [E12] | Scoped, revocable connections; activity log; honest "Limits" section; not audited; no MFA sign-in [E33] | AgentMail on badges. ActAs on scoping and candour |
| Channels | Plugins, SDKs, partner embeds, 700+ SEO pages, HN/PH, pixels [E3, E10, E17, E20, E28] | 3-URL sitemap; JS-only page; no socials, analytics or HN posts found [E32, E35, E36] | AgentMail by a wide margin |
| Content | 127 posts/30d, comparisons, evals [E10, E19, E23] | llms.txt, openapi.json, a recorded PyPI signup replay [E33, E34, E35] | AgentMail on volume. **ActAs has the better single proof asset**: a real signup → verify → login run [E33] |
| Social proof | 11 named testimonials, 13 stories, YC, $6M seed [E13, E15, E16] | None on the site [E33] | AgentMail |

Note: ActAs's own llms.txt says it can read "retained AgentMail inboxes" [E34]. Likely the honest position is "complements" rather than "replaces": AgentMail for high-volume agent email, ActAs for the identity around it.

## Steal this playbook: your playbook for ActAs
Ranked by expected impact per unit of effort, for a team with no audience and almost no budget. Copy the first four first.

1. **Instrument the funnel before anything else.** ActAs has no analytics tag anywhere and only 3 sitemap URLs [E32, E35], so no move below can be measured. *First step:* add one cookieless analytics script and a "how did you hear about us / which agent" field at sign-up. *Watch:* weekly visitors → sign-ups → paid. *Rests on:* [E32, E35].
2. **Let a developer try one identity without paying.** AgentMail's front door is "Start for free, no credit card" [E12, E1]. ActAs requires Pro before creating anything [E34]. *First step:* propose a 1-identity, 14-day or 100-email free tier (a pricing decision for the owner), and make "Start free" the hero CTA. *Watch:* the share of sign-ups that create their first identity within 24h. *Rests on:* [E12, E33, E34].
3. **Ship the Claude Code / Codex install path and its page.** AgentMail's biggest channel is installs from inside the agent tools: a one-command plugin, skills repo, MCP, and https://www.agentmail.to/build pages per agent [E18, E19, E28, E29]. ActAs's CLI installs from a downloaded .tgz [E33]. *First step:* publish `actas` to npm, add a public skills/plugin repo for Claude Code, and write one `https://www.agentmail.to/build/claude-code` page with the copy-paste prompt. *Watch:* npm weekly downloads and plugin installs. *Rests on:* [E18, E28, E29, E33].
4. **Own "agent 2FA / TOTP / password vault": the ground AgentMail doesn't cover.** Their 2FA content stops at emailed codes, with 0 mentions of authenticator or vault [E24]. Their auth comparison leaves out ActAs and credential vaults [E25]. They admit the alternatives search results are thin [E26]. *First step:* write 3 pages: "How an AI agent handles authenticator (TOTP) 2FA", "ActAs vs AgentMail (honest, including when to use both)" [E34], and "Where should an AI agent keep its passwords?". Prerender them as static HTML, because today's JS-only page shows crawlers an empty root [E32]. *Watch:* Search Console impressions and clicks on those 3 URLs. *Rests on:* [E24, E25, E26, E32].
5. **Do a Show HN built around the recorded PyPI run.** AgentMail's Show HN reached 121 points with a plain origin story [E27]. ActAs has 0 HN submissions [E36] and already owns a rare proof asset: a real signup → email verify → fresh login [E33]. *First step:* post "Show HN: ActAs – give your browser agent its own email, passwords and 2FA codes", with the replay and the honest Limits list in the first comment [E33]. *Watch:* points, comments, and sign-ups in the 72h after. *Rests on:* [E8, E27, E33, E36].
6. **Make llms.txt an agent-first sign-up path.** AgentMail's llms.txt tells agents exactly how to sign up, and they report agents finding and joining on their own [E14, E15]. ActAs's llms.txt documents the API but has no sign-up route for an agent [E34]. *First step:* add a "If you are an AI agent and need an identity" block that starts a sign-up the human approves by email. *Watch:* sign-ups with an agent user-agent or the "agent" source tag. *Rests on:* [E14, E15, E34].
7. **Get one embed in an open-source browser-agent stack.** The Browser Use embed is AgentMail's flagship story and testimonial [E17, E13]. *First step:* publish an open example ("Browser Use / Stagehand agent signs up and logs in with ActAs") in a public repo, then offer it to one browser-agent framework's examples or docs. *Watch:* repo stars and sign-ups attributed to that source. *Rests on:* [E13, E17].
8. **Collect 3 named design-partner quotes.** AgentMail's homepage runs on 11 named testimonials and 13 stories [E13, E16]. ActAs shows none [E33]. *First step:* ask the first 3 paying users for one sentence and permission to use their name, and add a proof strip under the hero. *Watch:* hero-to-sign-up conversion before and after. *Rests on:* [E13, E16, E33].
9. **Build 10 answer pages, not 100.** AgentMail runs 100 question-shaped pages for AI search [E20] and allows every AI crawler [E11]. ActAs already allows all bots [E35]. *First step:* write 10 pages that answer exact builder questions ("How does a Claude Code agent log into a site with 2FA?"), each with a CLI snippet. *Watch:* AI-referrer visits (chatgpt.com, perplexity.ai) in analytics. *Rests on:* [E11, E20, E35].

**Don't copy yet:** paid pixels [E3] (no confirmed ads and no budget); the volume blog [E10] (127 posts a month needs a content team); the evals benchmark [E23]; Product Hunt [E31] (a modest 435 followers even for them, so better after there's proof).

## Unknowns & how to check
- **Paid Meta:** no ad-library check (no key) — https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=AgentMail&search_type=keyword_unordered
- **Paid Google:** AW tag present, ads not checked — https://adstransparency.google.com/?region=anywhere&domain=agentmail.to
- **Paid LinkedIn:** https://www.linkedin.com/ad-library/search?accountOwner=AgentMail
- **Paid TikTok:** no global library — https://library.tiktok.com/ads?region=all&adv_name=AgentMail
- **Paid Reddit:** Reddit's ad library is gone; the pixel is the only signal — https://www.reddit.com/search/?q=AgentMail
- **Paid Apple:** no iOS app, so not applicable — https://adrepository.apple.com/
- **Organic X / LinkedIn:** accounts found, no stats — https://x.com/agentmail, https://www.linkedin.com/company/agentmailto
- **Organic TikTok / Instagram / YouTube:** no account linked from the site. Unknown, not absent.
- **Reddit and community mentions:** https://www.reddit.com/search/?q=agentmail.to
- **Founder audiences (Haakam Aujla and co-founders):** https://www.google.com/search?q=%22AgentMail%22%20founder%20site%3Alinkedin.com%2Fin
- **Lifecycle email:** runs server-side, not visible. Sign up for the newsletter to observe it.
- **Unique developers behind npm/PyPI downloads:** download counts include CI and reinstalls [E29, E30]. No public source gives unique users.
- **ActAs's rendered site:** copy was read from the JS bundle, not a rendered browser view [E33]. Check the live page for anything rendered from the API.
