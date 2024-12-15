import pywhatkit as kit
from googletrans import Translator
import time


# Function to translate message
def translate_message(message, target_lang='en'):
    translator = Translator()
    translated = translator.translate(message, dest=target_lang)
    return translated.text


# Function to send WhatsApp message
def send_whatsapp_message(phone_number, message):
    # Get the current time
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min + 2  # Set a 2-minute delay from the current time (adjust as necessary)

    # Use pywhatkit to send WhatsApp message (with a 2-minute delay)
    kit.sendwhatmsg(f'whatsapp:{phone_number}', message, hour, minute)


# Main function
def main():
    # Input: Phone number and message
    phone_number = input("Enter the recipient's phone number (with country code, e.g., +91975030XXXX): ")
    message = input("Enter the message you want to send: ")

    # Translate the message to English (if not already)
    translated_message = translate_message(message, 'en')
    print(f"Translated message: {translated_message}")

    # Send the translated message to the specified phone number
    send_whatsapp_message(phone_number, translated_message)
    print(f"Message sent to {phone_number}: {translated_message}")


# Run the program
if __name__ == "__main__":
    main()
