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
