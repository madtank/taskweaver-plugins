from taskweaver.plugin import Plugin, register_plugin
import requests
import logging

@register_plugin
class GroupChatPlugin(Plugin):
    def __call__(self, action='fetch', message=None, username=None):
        username = self.config.get("username", 'TaskWeaver')
        if action == 'fetch':
            return self.fetch_messages()
        elif action == 'post':
            return self.post_message(message, username)
        else:
            return "Invalid action specified."

    def fetch_messages(self):
        lambda_url = self.config.get('lambda_url') + "/fetch"
        topics = self.config.get("topics", [])  # Default to an empty list if not found
        personality = self.config.get("personality", "default")  # Default personality if not found

        try:
            response = requests.get(lambda_url)
            if response.ok:
                messages = response.json()
                logging.debug(f"Messages fetched: {messages}, Type: {type(messages)}")
                logging.debug(f"Topics: {topics}, Type: {type(topics)}")
                logging.debug(f"Personality: {personality}, Type: {type(personality)}")

                # Update the system message to TaskWeaver
                system_message = (
                    "TaskWeaver, you have fetched messages from the group chat as part of the group_chat plugin. "
                    "You are asked to review and consider these posts. "
                    "The focus topics specified by the user are: "
                    f"{', '.join(topics)}. "
                    "Be prepared to use this information for formulating a response in case the user follows up with a post request. "
                    "In such a scenario, do not ask what to post; instead, use the context of these messages to create a relevant response."
                    f"Respond to posts using personality {personality}"

                )
                return {"messages": messages, "system_message": system_message}
            else:
                logging.error(f"Failed to fetch messages. Response: {response.text}")
                return "Failed to fetch messages."
        except Exception as e:
            logging.exception(f"An error occurred while fetching messages: {str(e)}")
            return f"An error occurred while fetching messages: {str(e)}"


    def post_message(self, message, username):
        lambda_url = self.config.get('lambda_url') + "/post"
        payload = {'username': username, 'message': message}
        try:
            response = requests.post(lambda_url, json=payload)
            if response.ok:
                return f"Message from {username}: '{message}' posted successfully to the group chat."
            else:
                logging.error(f"Failed to post message. Response: {response.text}")
                return "Failed to post message."
        except Exception as e:
            logging.exception("An error occurred while posting the message.")
            return f"An error occurred while posting the message: {str(e)}"
