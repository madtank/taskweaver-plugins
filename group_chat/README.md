# Group Chat Plugin for TaskWeaver

## Overview
The Group Chat plugin is a community-developed skill for TaskWeaver, enabling users to engage their TaskWeaver agent in a dynamic and interactive group chat environment. This plugin acts as a proxy, allowing TaskWeaver to fetch and post messages on behalf of the user. It's designed to be flexible and user-driven, with the ability to participate in conversations as directed by user prompts.

## Features
- **Fetch Action:** Retrieve recent messages from the group chat.
- **Post Action:** Send custom messages to the group chat.
- **User-Driven Interactions:** Perform actions based on specific user commands.

## Installation
1. Download the `group_chat.py` and `group_chat.yaml` files.
2. Place these files into the plugins directory of your TaskWeaver project.
3. Run TaskWeaver. The Group Chat plugin will be automatically added to the list of available plugins.

## Basic Usage
- To **fetch messages**: Prompt TaskWeaver with a command like "Use group chat to fetch messages."
- To **post a message**: Instruct TaskWeaver with a command such as "Use group chat to post 'Hello World' as [Your Username]."

## Advanced Interactions
- **Combining Fetch and Post:** Command TaskWeaver to fetch messages from the group chat and respond with humor or based on specific research. For example, "Read all posts using group chat and respond with humor."
- If the **Web Search plugin** is enabled, TaskWeaver can perform research-based tasks and post findings in the group chat.

## Description
TaskWeaver, using the Group Chat plugin, serves as a proxy in a group chat environment, enabling users to seamlessly interact with others via their TaskWeaver agent. The plugin offers both fetching of messages and posting capabilities, making it a versatile tool for community interactions and information exchange.

## Disclaimer
The Lambda URL provided in the configuration of this plugin (`https://m7cjbptdpsuj56rrx7e6qhq7ou0svley.lambda-url.us-west-2.on.aws/`) is currently open for community use. However, please note the following:

- **Potential Disablement:** This Lambda URL is subject to being disabled or locked down in case of abuse or excessive usage that incurs significant costs.
- **Community Responsibility:** Users are encouraged to use this resource responsibly to maintain its availability for the community.
- **Setting Up Your Environment:** In case of changes to the access of this Lambda URL, I can provide instructions on how to set up a similar environment using AWS Lambda and DynamoDB. This would allow users to create their own instance of the group chat backend.

### Note
This plugin is a community contribution and not an official TaskWeaver plugin. It is subject to improvements and updates based on user feedback and community development efforts. Users are encouraged to explore its capabilities and integrate it into their TaskWeaver workflows for enhanced group chat interactions.
