# FlowFin social posting spec

Account: @flowfinleads Instagram + Flowfinleads Facebook Page, posted through GoHighLevel Social Planner.
Audience: business owners and operators who buy leads (funding, legal, debt relief). Goal: teach real marketing lessons and build a following.

## Cadence
- 3 posts a week: Wed, Fri, Mon, each at 09:00 America/New_York (convert to UTC for GHL; mind DST).
- Each weekly batch = exactly 3 posts = one grid row.

## Grid order (critical)
- Middle column always green. Outer columns alternate by row.
- batch_index = (number of posts in posts/log.md) / 3, counting from 0.
- Even batch_index: publish order black, green, white.
- Odd batch_index: publish order white, green, black.

## Content pillars (rotate; no two batches in a row with the same mix)
1. Data: real stats from named studies.
2. Classic ads: famous campaigns and why they worked.
3. Book lessons: Cashvertising, Scientific Advertising, Magnetic Marketing, Ogilvy, Hopkins, Caples, Schwartz, etc. Paraphrase; quote only short famous lines (under 15 words).
4. Copywriting breakdowns: a headline or hook and why it works.
5. Marketing stories: brand turnarounds and famous failures.
Every post ends with the plain-English lesson for getting customers.

## Accuracy
- Verify every stat, date, and attribution against a reliable source before use. If it can't be verified, don't use it.
- Use the study's real wording (e.g. "qualify", not "convert", when the study measured qualification).
- Never repeat a stat or story already in posts/log.md.

## Image
- Render with template/render.py. Big text: a number (max ~7 chars) or a short headline (max ~10 words).
- line1: one short sentence. line2: optional short muted kicker.
- No source on the image. Logo bottom right is automatic.
- Check each rendered image visually before publishing (no overflow, no awkward orphan words).

## Caption
- Short lines, deliberate line breaks, plain language. No em dashes. No "killed" or aggressive phrasing.
- Structure: hook line, the fact/story, the lesson, one engagement line (question or "save this"), source line, 4-5 hashtags.
- Source line format: Source: <title or study>, <publisher> (<year>)

## Files
- Images: posts/YYYY-MM/NN-<slug>-<theme>.png (NN = post number from the log, zero-padded).
- Public URL: https://raw.githubusercontent.com/dangventure-sketch/flowfin-social/main/<path>
- Append each post to posts/log.md.

## GHL
- Location: iHsyGSBLQ4FtYq1MklDY (FlowFinLeads). userId: G8Ujd3mjQyBUXAV5RxZV.
- accountIds: Instagram 6ad006607e92c5944610b1d8_iHsyGSBLQ4FtYq1MklDY_17841433284985800, Facebook 6ac6718fcf68342f29a6f3df_iHsyGSBLQ4FtYq1MklDY_845639325310037_page
- Operation create-post: type post, status scheduled, scheduleDate (UTC), media [{url, type: image/png}], instagramPostDetails {type: post}, facebookPostDetails {type: post}.
