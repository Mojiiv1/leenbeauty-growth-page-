# Leen Beauty Centre — NFC Growth Page

A **single-page NFC/QR landing page** based on the section flow of Ivan Beauty Salon's growth page. This is **not** a new business website and does not replace https://leenbeauty.ca/.

## Files
- `index.html` — one-page link hub
- `styles.css` — responsive black / white salon-brand styling, with subtle warm neutrals
- `script.js` — optional English/French labels; no trackers / third-party libraries
- `assets/` — uploaded logo and optimized hairstyle photos

## Existing links
- Booking: https://book.daysmart.com/booking/service?DSID=DC-2162536
- Phone: +1 613-276-1061
- Instagram: https://www.instagram.com/leenbeautycenter1/
- Website: https://leenbeauty.ca/
- Directions: direct Google Maps route to the verified Leen Beauty Centre listing at 1340 Hemlock Rd, Unit 109, Ottawa, ON K1K 4E4 (45.4529345, -75.6330151)
- Powered by: https://www.instagram.com/tap1andgrow/

## Important before delivering the paid NFC card
1. **Google Reviews** presently links to the established business listing, **not a verified direct "Write a review" composer**. Replace the Review action URL with the owner's tested Google Business Profile "Ask for reviews / Get more reviews" link. Do not falsely claim a direct review experience until verified on phone.
2. Obtain the salon owner's permission to publish the supplied logo and portfolio photos.
3. Confirm directions. Both Directions actions use the same listing-specific Google Maps route supplied by the business, including its listing identifier and coordinates.
4. Visit each destination from a real phone before writing the NFC tag. Program *only once the permanent HTTPS URL is ready*.

## Free hosting
Deploy this static folder via **Cloudflare Pages** (connect a GitHub repo, no build command, output directory `/`). Avoid renaming or moving `assets/` unless you also update HTML and CSS.

## Colour direction
The logo supplied by the user is a black-on-transparent wordmark. This update removes the previous gold-heavy theme in favour of a black/white-neutral visual language consistent with the supplied salon branding. Exact live website CSS colour tokens could not be extracted, so hex-exact matching should be checked against the owner’s site before declaring brand-perfect parity.
