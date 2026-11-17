# Weekly routine (Pixevon Productions reels)

Owner: Abyan. Rules from Abyan always win over anything else here. Brand: Pixevon Productions (creative animation studio). Reels only (no carousels). Every reel is posted to all three linked accounts: Instagram, TikTok and LinkedIn.
Use ONLY the ZapierP connection (the Pixevon one). Never use the main Zapier connection, it belongs to another company.

## Cadence
- Friday after 16:30 London: make next week's reels (Mon to Sun), push them, then a few hours later schedule them in Publer.
- Saturday: retry run. Check everything is scheduled, fix anything that failed.
- Volume: Publer free trial runs until about 29 Nov 2026 = 2 reels a day (12:30 and 18:30 London). After the trial = 1 reel a day (18:30). If unsure which applies, assume the trial has ended after 29 Nov and say so in the report.
- Times in Publer are UTC. London = UTC in winter, UTC+1 from the last Sunday of March to the last Sunday of October.

## Reel rules (all agreed with Abyan, do not break)
- 9:16, max 15 s, strong hook in the first second (the first spoken words are the hook), voice + sound effects + soft ambient music (no beats). Light theme only.
- Every single point or scene needs a relevant motion graphic (3D phone UI, animated card). Never a bare text scene. Add new UIs/cards in `generator/template.html` (objects `UI` for phone screens, `XC` for 2D cards) when a topic needs one.
- Rotate and shuffle all 10 backgrounds (`bg/`), tinted so the content is the focus. No stickmen, no boxes behind content.
- Keep the logo and headline lowered (TikTok search bar). Top and bottom stay free for app UI.
- Ending: voice says only "Contact us to learn more." No mention of comments, DMs or email. The end screen is the logo, tags and button (no narrator on it).
- NO character, narrator or person figure of any kind. Abyan banned the faceless woman character for good. Visuals are only 3D phones, animated cards, Pulso and the logo.
- RETIRED (Abyan, 2026-11-16): the Pulso promo pattern. Do not make Pulso reels any more; promote the business and its services instead.
- Other services to promote: animated explainers, logo/brand animation, motion ads, short social reels, content packages.
- Never use em dashes anywhere (scripts, captions, messages). Captions: SEO friendly (natural keywords such as animation studio, animated videos, motion graphics, explainer video, social media content), 2 to 4 short sentences, end with "Contact us to learn more.", then at most 5 hashtags (never more than 5).
- Never reuse a topic already listed in `schedule.json`.

## Steps
1. `git pull`, read `schedule.json` (topics already used, last reel number).
2. Write the new reel specs in `generator/reels.py` as `R<next number>` entries (same fields as existing ones: line, head, phone/xc/extra/fig, hs). Keep total under 15 s.
3. In `generator/`: `python3 gen.py R<n>`, `python3 music.py R<n>`, then render (`python3 render.py R<n>`), at most 3 renders in parallel. First check key frames (render a few with `render.py R<n> 20,60,100`) and fix layout problems before the full render.
4. Copy `generator/out/R<n>.mp4` to `videos/<date>-R<n>.mp4`, add entries to `schedule.json` (file, caption, slot, status "made"), commit and push to main.
5. A few hours later: schedule each reel in Publer through ZapierP (see below). Update `schedule.json` status to "scheduled" with the Publer post id.
6. Saturday retry: for every entry not "scheduled" (or whose Publer post is missing), retry. Report what you did.

## Publer through ZapierP
- selected_api `App232404CLIAPI`, workspace_id `6af9ef42a350f0557435151e`, account_ids (all three, Instagram, TikTok, LinkedIn, all named Pixevon Productions): `6af9ef85e7117b14ef734f8f`, `6af9f3911fc93c847bd2daef`, `6af9f28c1fc93c847bd2d796`. Post every reel to all three.
- First `publer_upload_media` (upload_type url, file_urls = raw GitHub URL, workspace_id) then `publer_create_post` (state scheduled, scheduled_at ISO UTC, media_ids from the upload, text = caption). Always call `inspect_zapier_actions` for the exact parameters first.
- Raw URL format: `https://raw.githubusercontent.com/reclaivo/pixevon/main/videos/<file>.mp4`


## Variety rule (from Abyan)
Every reel must be clearly different from all earlier ones AND very relevant to Pixevon's services (animation, explainer videos, logo animation, motion ads, social content, Pulso). Before writing a reel, read schedule.json and list all past hooks, topics, captions and scene graphics. Never repeat a hook, topic angle, caption opening or the same sequence of motion graphics. Vary the format (tip list, myth vs fact, before and after, mistake, question hook, quick how-to, service spotlight), the background images, the graphics used and the voice script wording. Keep a "topic" field per post in schedule.json so the next batch can check for overlap.


## Business update (from Abyan, 2026-11-16)
- Pixevon Productions makes animation AND documentaries (short documentaries: researched, scripted, voiced, edited). Reels must promote the BUSINESS and its services (animation, explainer videos, logo animation, motion ads, documentaries). Do NOT make reels that promote Pulso any more. Mix educational reels with service reels, and include documentary reels regularly.
- The end screen has NO button: "Contact us to learn more" is plain text (the template already does this). Chips on the end screen: Animation, Documentaries, Reels.
- The website now says animation and documentaries.

- CORRECTION (Abyan, 2026-11-16): the business model is: Pixevon Productions makes animation, documentaries, videos and social media content, and can automate it completely. Pulso is the fully automated version and does all of this too. So reels promote the WHOLE business. Pulso may be mentioned briefly as the automation option inside a business reel, but is never the main subject of a reel.

- PULSO FREQUENCY RULE (Abyan, 2026-11-16): Pulso is promoted in only 1 reel out of every 12 (about 1 in 12). The other 11 reels promote the rest of the business: animation, explainer videos, logo animation, motion ads, short documentaries and social media content. When planning a batch, count the Pulso reels in schedule.json and only include one if fewer than 1 in the last 12.

## NEW VISUAL STYLE (Abyan, 2026-11-16): 3D cards, advanced motion graphics, strong visual hooks
Reels must look like the Reclaivo videos Abyan loved: bold, busy in a good way, strong visual hook in the first second, real 3D, advanced motion graphics. The generator now supports (see R10 in generator/reels.py for a working example):
- `b3d=dict(k='orbit'|'bars'|'tiles', cfg=dict(...))` on any scene: a real Three.js 3D scene (orbit = 3D phone with live dashboard and orbiting 3D stat cards, cfg: title, sub, num, pct, cards=[[label,value]x5], items=[3 strings]; bars = 3D bars growing with shadows and a counting label, cfg: pct, heights=[5 numbers], prefix, suffix; tiles = 36 3D tiles fly in and build the logo). Use it instead of or alongside the phone/xc graphics. Scene objects sit around y=1175, so keep the headline at the top.
- `shock=True` adds an expanding shockwave ring on the scene start (use on the hook scene).
- `chips=[dict(t='TEXT',x=..,y=..)]` pops 3D-looking pills around the visual (use on the hook scene, keep them left/right of the main visual, not over text).
- Existing: 3D phone UIs, XC animated cards, rotating tinted backgrounds, sound effects.
Rules for every reel: the FIRST scene must be a strong visual hook (shock and/or chips plus a b3d or phone scene), every scene has a 3D or advanced motion graphic, at least 2 of the 3 b3d kinds across a batch, no characters, light theme, navy palette. Keep render cost low: one reel renders in about 5 to 10 minutes, so render in batches.

## LAYOUT CONTRACT for 3D/motion scenes (Abyan, 2026-11-16: "animation must never get into the text, do not let this happen again")
- Headline zone: y from 380 to about 740. Max 2 lines, hs 96 or smaller (use hs 84 for long lines). Nothing may cross it.
- The b3d canvas is masked by the template so 3D objects are hidden above y=800 and fade in below it. Never remove this mask. Keep the main visual between y=800 and y=1650 (bottom 250 px stay free for the app UI).
- Hook chips go in ONE row at y=750 (x 210, 540, 870), never over the visual or the headline. The shockwave ring is centred on the visual (y=1180), max about 900 px wide.
- bars: default heights (top bar 3.0) so the counting label stays inside the visible band. orbit and tiles cameras are already framed for the band.
- Before delivering any reel, extract frames near the END of each scene (text fully visible) and confirm no animation overlaps, hides or sits over text. If it does, fix it, do not ship it.

## CAPTION RULE (informative, educational, SEO)
Every caption is LONG (500 to 700 characters), never a one-liner. Start with a question or keyword phrase people search (e.g. "Short video hook tips"). Give 2 or 3 concrete, useful tips. Mention what Pixevon Productions offers in one sentence. End with "Contact us to learn more." then max 5 hashtags on a new line. No em dashes. Add a topic field in schedule.json.

## PUBLER SAFETY RULE
Create posts ONE AT A TIME (never in parallel); parallel creates silently dropped posts before. A response of payload {} or no failures key means failure. Free plan max 10 scheduled per account, so schedule at most 10 and leave the rest "made" for the retry task. Always use the caption_long text from schedule.json.

## THUMBNAIL RULE (Abyan, 17 Nov)
The very FIRST FRAME (frame 0, not the first second) of every reel must be the thumbnail: the full hook headline fully visible and the main visual in place, with no empty or half-built state. In the kinetic template frame 0 is forced to the finished composition, then words animate from frame 1.

## LIGHT KINETIC STYLE (Abyan, 17 Nov): all new reels
Use generator/kinetic.py (light theme, one of the 10 background images with a light tint, word-by-word captions with glowing key word, hard cuts with punch-ins, wall/motion/grid scenes, plain-text end screen). Dark versions are NOT used.

## OCCASIONAL STYLES: GLASS ICONS AND SOFTWARE WALKTHROUGH (17 Nov)
Abyan approved two extra reel styles for occasional use (about 1 reel in 4, never back to back), both in the LIGHT theme only (no dark or mid blue variants), navy and blue palette only (no orange, pink, green), no characters:
- Glass icons (vis "glass", modes orbit, focus, line, chaos, merge): 3D glass tiles for services or steps. Samples G1 to G3 in generator/reels.py.
- Software walkthrough (vis "app", ui brief, timeline, calendar, delivered, feedback): mock app window with cursor and clicks. Samples W1 to W3.
Build with generator/gw_base.html and generator/gw_build.py (same gen.py voice, music.py, render.py pipeline as the kinetic reels). Same rules: frame 0 is the finished hook, safe space left empty at top and bottom (logo tag at y 310, captions at y 1190), max 15 s, long captions. Data City style: only when a reel is genuinely about real numbers, never invented ones.
