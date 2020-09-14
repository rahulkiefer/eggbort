# Eggbort

Eggbort is a Discord bot made in Python. [Here is the link to invite him to your Discord server](https://discord.com/api/oauth2/authorize?client_id=728707277489569902&permissions=8&scope=bot) (requires administrator priviliges).

## Functionality

Eggbort's functionality comes in the form of server management QOL improvements, such as easier chat management, bot interaction modification, as well as fully-functional music player capabilities from sources such as YouTube, Soundcloud, and more. Once you invite Eggbort to your Discord server, type `e.help` in a text channel to display a list of commands.

## Implementation

To be able to implement all of Eggbort's functionality, I created a multi-container application using Docker and Docker Compose, utilizing a user-defined bridge network for internal communication within the project. In addition to creating and building an image for its python codebase, Eggbort relies on a Lavalink image (created by Github user [Frederikam](https://github.com/Frederikam/Lavalink)), which allows for audio player functionality, as well as a MongoDB image, which stores data used by certain commands.
