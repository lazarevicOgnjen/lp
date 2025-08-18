import os
from dhooks import Webhook, Embed, File

image2_path = 'cs-lp1-nova-obavestenja.png'

WEBHOOK_URL = [os.getenv('WEBHOOK_MAIN1')]
for url in WEBHOOK_URL:
    hook = Webhook(url)

    embed = Embed(
        description="**[LP main page link - click here -](https://cs.elfak.ni.ac.rs/nastava/course/view.php?id=41)**",
        color=0x3498DB
    )

    embed.set_image(url="attachment://cs-lp1-nova-obavestenja.png")
    file = File(image2_path, name="cs-lp1-nova-obavestenja.png")
    hook.send("@everyone 📢 LP", embed=embed, file=file)
