import json
import os
import subprocess
from pathlib import Path
from pyrogram import Client, filters
from pyrogram.types import Message, ReplyKeyboardMarkup, ReplyKeyboardRemove
from info import Config, Txt


config_path = Path("config.json")


async def Report_Function(No, msg):

    listofchoise = ['Report for child abuse', 'Report for copyrighted content', 'Report for impersonation', 'Report an irrelevant geogroup',
                    'Report an illegal durg', 'Report for Violence', 'Report for offensive person detail', 'Reason for Pornography', 'Report for spam"']
    message = listofchoise[int(No) - 1]

    # Run a shell command and capture its output
    process = subprocess.Popen(
        ["python", f"report.py",
            f"{message}"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    # Use communicate() to interact with the process
    stdout, stderr = process.communicate()

    # Get the return code
    return_code = process.wait()

    # Check the return code to see if the command was successful
    if return_code == 0:
        # Print the output of the command
        print("Command output:")
        print(stdout)
        return [stdout, True]

    else:
        # Print the error message if the command failed
        print("Command failed with error:")
        print(stderr)
        return f"<b>Something Went Wrong Kindly Check your Inputs Whether You Have Filled Correctly or Not !</b>\n\n <code> {stderr} </code> \n ERROR"


async def CHOICE_OPTION(bot, msg, number):

    if not config_path.exists():
        return await msg.reply_text(text="**You don't have any config first make the config then you'll able to report**\n\n Use /make_config", reply_to_message_id=msg.id, reply_markup=ReplyKeyboardRemove())

    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)

    ms = await bot.send_message(chat_id=msg.chat.id, text=f"**Please Wait**", reply_to_message_id=msg.id, reply_markup=ReplyKeyboardRemove())
    result = await Report_Function(number, msg)
    await ms.delete()

    if result[1]:
        try:
            # Assuming output is a bytes object
            output_bytes = result[0]
            # Decode bytes to string and replace "\r\n" with newlines
            output_string = output_bytes.decode('utf-8').replace('\r\n', '\n')

            await bot.send_message(chat_id=msg.chat.id, text=f"{output_string}\n Reported To @{config['Target']} ✅", reply_to_message_id=msg.id)
        except:
            Text = f"""{output_string}
            
@{config['Target']} ✅
"""
            with open('report.txt', 'w') as file:
                file.write(Text)
            await bot.send_document(chat_id=msg.chat.id, document='report.txt')
            os.remove('report.txt')

    else:
        await bot.send_message(chat_id=msg.chat.id, text=f"{result}", reply_to_message_id=msg.id)


@Client.on_message(filters.private & filters.user(Config.OWNER) & filters.command('report'))
async def handle_report(bot: Client, cmd: Message):

    CHOICE = [
        [("1"), ("2")], [("3"), ("4")], [("5"), ("6")], [("7"), ("8")], [("9")]
    ]

    await bot.send_message(chat_id=cmd.from_user.id, text=Txt.REPORT_CHOICE, reply_to_message_id=cmd.id, reply_markup=ReplyKeyboardMarkup(CHOICE, resize_keyboard=True))


@Client.on_message(filters.regex("1"))
async def one(bot: Client, msg: Message):

    await CHOICE_OPTION(bot, msg, 1)


@Client.on_message(filters.regex("2"))
async def two(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 2)


@Client.on_message(filters.regex("3"))
async def three(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 3)


@Client.on_message(filters.regex("4"))
async def four(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 4)


@Client.on_message(filters.regex("5"))
async def five(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 5)


@Client.on_message(filters.regex("6"))
async def six(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 6)


@Client.on_message(filters.regex("7"))
async def seven(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 7)


@Client.on_message(filters.regex("8"))
async def eight(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 8)


@Client.on_message(filters.regex("9"))
async def nine(bot: Client, msg: Message):
    await CHOICE_OPTION(bot, msg, 9)
