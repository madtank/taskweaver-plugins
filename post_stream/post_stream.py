from taskweaver.plugin import Plugin, register_plugin
from datetime import datetime
import requests
import logging

@register_plugin
class Proxy_Stream(Plugin):
    def __call__(self, action='fetch', message=None, username=None):
        username = self.config.get("username", 'TaskWeaver')
        if action == 'fetch':
            return self.fetch_messages()
        elif action == 'post':
            return self.post_message(message, username)
        else:
            return "Invalid action specified."

    def fetch_messages(self):
        lambda_url = self.config.get('lambda_url', 'Your default lambda URL') + "/fetch"
        topics = self.config.get("topics", [])  # Default to an empty list if not found
        personality = self.config.get("personality", "default")  # Default personality if not found

        try:
            response = requests.get(lambda_url)
            if response.ok:
                raw_messages = response.json()
                formatted_messages = []
                for message in raw_messages:
                    # Convert timestamp
                    timestamp = datetime.fromtimestamp(message['Timestamp'])
                    formatted_time = timestamp.strftime('%H:%M:%S %m/%d/%Y')
                    # Format message with readable timestamp
                    formatted_messages.append({
                        "Timestamp": formatted_time,
                        "Message": message['Message'],
                        "Username": message['Username'],
                        "MessageID": message['MessageID']
                    })

                # Update the system message to TaskWeaver
                system_message = (
                    "TaskWeaver, you've fetched the latest messages from the post stream. "
                    "Focus on topics: " + ', '.join(topics) + ". "
                    "Use this information for formulating responses, if needed. "
                    "Personality setting: " + personality + "."
                )

                return {"messages": formatted_messages, "system_message": system_message}
            else:
                logging.error(f"Failed to fetch posts. Response: {response.text}")
                return "Failed to fetch posts."
        except Exception as e:
            logging.exception(f"An error occurred while fetching posts: {str(e)}")
            return f"An error occurred while fetching posts: {str(e)}"


    def post_message(self, message, username):
        lambda_url = self.config.get('lambda_url') + "/post"
        payload = {'username': username, 'message': message}
        try:
            response = requests.post(lambda_url, json=payload)
            if response.ok:
                return f"Message from {username}: '{message}' posted successfully to post stream."
            else:
                logging.error(f"Failed to post message. Response: {response.text}")
                return "Failed to post message."
        except Exception as e:
            logging.exception("An error occurred while posting the message.")
            return f"An error occurred while posting the message: {str(e)}"
