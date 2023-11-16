import sys
import re
from pyrogram import Client, errors


def main(Target, String):

    # group target link
    group_target_id = Target
    gi = re.sub("(@)|(https://)|(http://)|(t.me/)", "", group_target_id)
    # workdir = 'session/'
    SessionString = String
    with Client(name="Session", session_string=SessionString) as app:
        User = app.get_me()
        if app.get_me():
            print(User)
            try:
                app.join_chat(gi)
            except errors.UserAlreadyParticipant:
                app.get_chat(gi)
            except:
                pass
        else:
            print("Loggined Failed !")


if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python your_script.py <channel_username> <session_string>")
        sys.exit(1)

    # Get command-line arguments
    channel_username = sys.argv[1]
    session_string = sys.argv[2]

    main(Target=channel_username, String=session_string)
