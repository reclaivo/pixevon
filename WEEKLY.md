# Weekly routine (Pixevon Productions reels)

Owner: Abyan. Rules from Abyan always win over anything else here. Brand: Pixevon Productions (creative animation studio). Reels only (no carousels). Every reel is posted to all three linked accounts: Instagram, TikTok and LinkedIn.
Use ONLY the ZapierP connection (the Pixevon one). Never use the main Zapier connection, it belongs to another company.

## Cadence
- Friday after 16:30 London: make next week's reels (Mon to Sun), push them, then a few hours later schedule them in Publer.
- Saturday: retry run. Check everything is scheduled, fix anything that failed.
- Volume: Publer free trial runs until about 29 Nov 2026 = 2 reels a day (12:30 and 18:30 London). After the trial = 1 reel a day (18:30). If unsure which applies, assume the trial has ended after 29 Nov and say so in the report.
- Times in Publer are UTC. London = UTC in winter, UTC+1 from the last Sunday of March to the last Sunday of October.

## Reel rules (all agreed with Abyan, do not break)
- 9:16, max 15 s, strong hook in the first second (the first spoken words are the hook), voice + sound effects + soft ambient music (no beats). DARK theme only (black background, navy highlights, white new logo, one blue accent, no characters). Keep extra empty space at the top and bottom: generators already wrap scenes in a .92 safe scale, never override it.
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
Rules for every reel: the FIRST scene must be a strong visual hook (shock and/or chips plus a b3d or phone scene), every scene has a 3D or advanced motion graphic, at least 2 of the 3 b3d kinds across a batch, no characters, DARK theme (black base, navy highlights, white logo, blue accent). Keep render cost low: one reel renders in about 5 to 10 minutes, so render in batches.

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

## DARK THEME (Abyan, 18 Nov): all new reels
Theme changed to DARK on 18 Nov 2026. generator/theme_dark.py holds the substitutions; kinetic.py and gw_build.py default to REEL_THEME=dark (set REEL_THEME=light only if Abyan asks). Always check frame 0 and one mid frame for overlap and top/bottom space before scheduling.

## KINETIC STYLE
Use generator/kinetic.py (dark theme, one of the 10 background images with a dark tint, word-by-word captions with glowing key word, hard cuts with punch-ins, wall/motion/grid scenes, plain-text end screen). Light versions are no longer used.

## STYLE MIXING RULE (17 Nov, Abyan's instruction for every batch from the next one)
Never follow one template. Every batch must MIX AND MATCH and keep shifting between: (1) the original light kinetic style (kinetic.py), (2) glass icons, (3) software walkthrough, and (4) Data City only when a reel is genuinely about measuring or numbers (never invent figures). Randomize the order, do not use the same style twice in a row, and across any 6 reels use at least 3 different styles. Record the style in each schedule.json post (field "style").

## OCCASIONAL STYLES: GLASS ICONS, SOFTWARE WALKTHROUGH AND DATA CITY (17 Nov)
Abyan approved extra reel styles to be mixed in (see the mixing rule above), all in the DARK theme (black base, navy and blue palette only (no orange, pink, green), no characters:
- Glass icons (vis "glass", modes orbit, focus, line, chaos, merge): 3D glass tiles for services or steps. Samples G1 to G3 in generator/reels.py.
- Software walkthrough (vis "app", ui brief, timeline, calendar, delivered, feedback): mock app window with cursor and clicks. Samples W1 to W3.
Build with generator/gw_base.html and generator/gw_build.py (same gen.py voice, music.py, render.py pipeline as the kinetic reels). Same rules: frame 0 is the finished hook, safe space left empty at top and bottom (logo tag at y 310, captions at y 1190), max 15 s, long captions. Data City style: only when a reel is genuinely about real numbers, never invented ones.


## STYLE UPDATE (18 Nov): never use kinetic.py (old kinetic style). Use only glass icons, app walkthrough, 3D data city and 3D motion graphics (gw_build.py). Tint is pure black rgba(0,0,0,.90), blues darker, company tag bold ALL CAPS.

## CADENCE (Abyan, 18 Nov 2026)
Old light posts were deleted from Publer. New dark reels scheduled from Wed 18 Nov 19:00 UTC. 2 reels per day (12:30 and 18:30 UTC) until Sun 29 Nov 2026 (trial period), then 1 reel per day at 12:30 UTC, 6 days a week (Mon to Sat, Sunday off). Weekly: Sunday 10:12 London make, Monday 13:07 schedule, Thursday 11:03 top-up (Publer cap 10 per account).

## PUBLER RELIABILITY RULES (18 Nov 2026, these OVERRIDE any conflicting line in a task prompt)
1. UPLOAD URL: raw.githubusercontent.com failed on 18 Nov ("not a publicly accessible media"). Upload with publer_upload_media using https://cdn.jsdelivr.net/gh/reclaivo/pixevon@main/videos/<file> FIRST. Only if that fails try https://raw.githubusercontent.com/reclaivo/pixevon/main/videos/<file>. If both fail, tell Abyan at once with the exact error.
2. NEVER wait or poll for a number of reels. Schedule whatever dark reels exist immediately, in slot order, then render more and schedule those too in the same run.
3. If any slot in the next 24 hours has no scheduled post, that is a failure: fix it now, and say so in the message to Abyan.
4. Always report to Abyan, even when everything worked (what is scheduled, with times).

## GLASS TILE QA RULE (Abyan, 18 Nov 2026, after R16 shipped with tiles outside the frame and bright blue boxes)
1. Glass tiles must be DARK (deep navy #16215C to #0A1131 with a thin blue edge), never bright blue. theme_dark.py enforces this; never override it.
2. Every glass row, orbit and label must stay inside x 40 to 1040 at all times. gw_base.html sizes rows with rowGeo(); do not hard-code tile sizes or gaps.
3. After python3 gw_build.py and BEFORE rendering, run: python3 qa_bounds.py NAME (all glass reels). It must print OK. If it prints FAIL, fix and rebuild, do not ship.
4. After rendering, look at frames at about 85 percent of every scene (not just frame 0). If any box, label or text is cut by the frame edge or looks bright blue, remake the reel before it is scheduled. Never schedule a reel that was not checked this way.

## NOTE 18 Nov 22:00 UTC: R27 (YouTube automation v2) was published immediately (replacing the deleted R16). The Tue 24 Nov 12:30 UTC slot is therefore FREE: fill it with a new reel. A one-off safety net task ("Pixevon: safety net (cheap check)") re-books itself and only acts if the main top-up chain fails.

## FIRST COMMENT RULE (Abyan, 18 Nov 2026), overrides any task prompt
Every NEW create_post (from now on) must include auto_comment_enabled true and auto_comment_text as a list with ONE short engagement question that fits the reel topic (for example "What is your biggest struggle with video?"). No em dashes, no hashtags, no links, under 120 characters, different for each reel. Store it in schedule.json as "first_comment". It costs no extra Zapier calls. If a create_post fails because of the comment fields, retry once without them and tell Abyan. Posts already scheduled before 18 Nov 22:30 UTC do not have it and must not be recreated for this.

## LINKEDIN FIRST COMMENT FIX (20 Nov 2026), overrides the FIRST COMMENT RULE
Publer's free plan rejects the auto comment on LinkedIn, and a single create_post to all three accounts then fails partly (Instagram and TikTok created, LinkedIn not). From now on use TWO create_post calls per reel: (1) Instagram + TikTok with auto_comment_enabled true and one question; (2) LinkedIn ONLY (6af9f3911fc93c847bd2daef) WITHOUT any auto comment fields. Never retry a three-account call after a partial result (it hits the 10 cap on the accounts that already have it). A cap error on an account means that post already exists there. R33 to R35 on LinkedIn have no first comment. R35 appears on all three accounts (LinkedIn cap is full at 10).
