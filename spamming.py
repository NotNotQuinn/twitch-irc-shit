import socket
from time import sleep

sock = socket.socket()


# Go to https://twitchapps.com/tmi/ to get an oauth token
oauth_token = "oauth:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
username    = "KAPPA"
sock.connect(('irc.chat.twitch.tv', 6667))
sock.send(bytes('PASS ' + oauth_token + '\r\n', 'utf-8'))
sock.send(bytes('NICK ' + username + '\r\n', 'utf-8'))


def send(string, channel):
    if len(string) >= 500:
        return print("MESSAGE TOO LONG MAN")
    string = string + " " if not string.endswith(" ") else string
    channel = channel if isinstance(channel, str) else str(channel[0]) if isinstance(channel, list) else str(channel)
    channel = "#" + channel if not channel.startswith("#") else channel
    channel = channel.lower() if not channel.islower() else channel
    sock.send(bytes('PRIVMSG ' + channel + ' :' + str(string) + '\n', 'UTF-8'))
    if vip:
        sleep(0.09)
    else:
        sleep(1.1)


def pyramid(width, txt, channel):
    txt = str(txt) + " " if not str(txt).endswith(" ") else str(txt)
    if len(str(width * txt)) >= 500:
        failtext = "I Just tried using a script to spam a pyramid with width " + str(width) + " of the text ' " + txt +\
                    "'. It didnt work because if you have " + str(width) + " of ' " + txt + "' in one line its over 5"\
                    "00 characters, and thats the max that you can send in one message. Have a Nice spammless day :) 💖"\
                    " from the maker of the script, @QuinnDT 🔔 sorry me! (script on github @ notnotquinn/twitch-irc-s" \
                    "hit LUL )"
        if len(failtext) >= 500:
            send("DUDE, @" + username + ", what kind of message did u try to make into a pyramid? EleGiggle , it would "
                 "have broke EVERYTHING if i didnt think to add this LUL from @QuinnDT 🔔 sorry me!", channel)
        send(failtext, channel)
        return
    for i in range(0, width + 1):
        send(i * txt, channel)
    width -= 1
    while width != 0:
        send(width * txt, channel)
        width -= 1


# + ------------------------------------------------------ +
# |                      INSTRUCTIONS                      |
# + ------------------------------------------------------ +
# |The functions that are ready for use are:               |
# |                                                        |
# | - pyramid                                              |
# |                                                        |
# + ----------------------- PYRAMID ---------------------- +
# |Description:                                            |
# |   Sends a pyramid in the channel, the speed varies if  |
# |   vip is set to true or not, to make sure that your    |
# |   account doesn't get rate limited. (meaning you can   |
# |   not chat)                                            |
# |                                                        |
# |Useage:                                                 |
# |   pyramid(width, text, channel)                        |
# |                                                        |
# |Variables:                                              |
# |   width   = the max width of the pyramid               |
# |   text    = the text that will be made into a pyramid  |
# |   channel = the channel to send the pyramid in         |
# |              (AUSTINSHOW and austinSHOW mean the same  |
# |              thing)                                    |
# |                                                        |
# |Example:                                                |
# |   pyramid(3, "TriHard", "QuinnDT")                     |
# |Sends:                                                  |
# |   TriHard                                              |
# |   TriHard TriHard                                      |
# |   TriHard TriHard TriHard                              |
# |   TriHard TriHard                                      |
# |   TriHard                                              |
# | In My channel.                                         |
# |                                                        |
# + ------------------------ INFO ------------------------ +
# |           MAKE SURE TO CORRECTLY SET THE VIP           |
# | If you don't, your account wont be able to send        |
# | messages for 30 mins.                                  |
# + ------------------------------------------------------ +

# go to the top of the page and set your oauth and username before anything will work

# go to the top of the page and set your oauth and username before anything will work

# go to the top of the page and set your oauth and username before anything will work

# go to the top of the page and set your oauth and username before anything will work

# SET THIS PROPERLY (True or False)
vip = True
# put the commands below here:
# ----------------------------------------------------------

