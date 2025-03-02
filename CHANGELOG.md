# julia's changelog + to-do

I made a bunch of small, 'barely noticeable' changes to the project to try and make it feel smoother and look prettier. most of my changes are found within the html, css, and js files. remaining changes were me uploading images to the... images folder. woo yeah.

the purpose of this documentation is so everyone knows what files I touched, in case I royally messed something up and did not catch it at 5 am. also so I can remember what I did and what I still need help accomplishing tomorrow, because it is 5 am and I will not remember when I wake up in 4 hours.

## changes

### added

- 'tails' on chat msg bubbles
- chat msg bubble pop in animation
- mascot images uploaded to /static/images/scrubby
- **mascot SPINS when clicked on** (my favourite addition by far, I put him in the spin cycle whenever I was idly staring at my monitor)
- modal's dark overlay fade in animation
- modal container pop in animation
- quiz modal header (uses the chat header as a placeholder, a bit scuffed for now)
- summary button (not functional)
- dark mode toggle button (needs better styling)

### changed

- Montserrat font applied to chat input field and button, and quiz answer button for consistency
- hexes updated across all elements to unify the colour palette
- first message modified to introduce mascot
- chat input field clears automatically after pressing send
- quiz modal topic input field styled similarly to chat input field
- quiz modal buttons labeled as the correct (C) or incorrect (IC) answer for simpler testing
- quiz modal elements renamed accordingly
- fixed filepaths for css, js, and image files in index.html

## to-do list

### still need to work on
- **(high prio)** speech button next to chat button
- **(low prio)** chat and quiz header styling
- **(low prio)** dark mode toggle button hover + styling
- **(low prio)** more sea-themed background graphic elements?

### things I may need help with (HELP I don't know what I'm doing)

- **(high prio)** mood stuff. I was looking into this but I'm pretty sure the mood has to go from the backend through Flask to update the image on the frontend, so I did not mess with it (if I'm wrong I apologise for my ignorance). the mascot pngs in the images folder are named corresponding to mood.py if someone else is able to help me with this
- **(med prio)** summary button? not high prio because I'm not sure if we're even still doing a summary feature
- **(low prio)** I'm not sure if it's just a me problem, but fresh off my pull I have a lot of white space under the chat input field. I didn't see this on Joel's screenshot when he was working on it, so it might just be on my end +  it's not a huge thing so I didn't mess with it


