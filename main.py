from pyrogram import Client, filters

# তোর নেওয়া API ID (সংখ্যা) এবং API Hash (ইনভার্টেড কমার ভেতরে)
API_ID =  30268961 # এখানে তোর api_id দে
API_HASH = "73786de79242e3cc0b1b4a00476a8675"  # এখানে তোর api_hash দে

# যেখান থেকে মেসেজ আসবে (SOURCE) এবং যেখানে পোস্ট হবে (TARGET)
# চ্যানেল পাবলিক হলে '@channel_name' দিবি, আর প্রাইভেট হলে আইডি (যেমন: -100123456789)
SOURCE_CHAT = "@vimfree_netbd"
TARGET_CHAT = "@KAKASHITEAM77"

app = Client("my_userbot", api_id=API_ID, api_hash=API_HASH)

@app.on_message(filters.chat(SOURCE_CHAT))
async def forward_message(client, message):
    try:
        # মেসেজ কপি করে তোর চ্যানেলে পাঠাবে
        await message.copy(chat_id=TARGET_CHAT)
        print(f"Message forwarded: {message.id}")
    except Exception as e:
        print(f"Error: {e}")

print("Userbot is running...")
app.run()
