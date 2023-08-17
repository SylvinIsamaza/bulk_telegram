from telethon.sync import TelegramClient, events
import asyncio

# Replace these with your own values
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'

async def create_telegram_account():
    async with TelegramClient('anon', api_id, api_hash) as client:
        print("Creating a new Telegram account...")
        try:
            await client.sign_up(
                phone_number='YOUR_PHONE_NUMBER',  # Replace with your phone number
                first_name='YourFirstName',
                last_name='YourLastName'
            )

            print("Account created successfully!")

            @client.on(events.NewMessage(chats='me'))
            async def on_message(event):
                if "Your verification code" in event.message.message:
                    verification_code = event.message.message.split(':')[1].strip()
                    print(f"Received verification code: {verification_code}")
                    await client.disconnect()

            print("Waiting for the verification code...")
            await client.send_message('me', 'Your verification code: 123456')  # Replace with the code you received

        except Exception as e:
            print("Error creating account:", e)

if __name__ == '__main__':
    asyncio.run(create_telegram_account())

