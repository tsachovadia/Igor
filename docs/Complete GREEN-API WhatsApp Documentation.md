<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Complete GREEN-API WhatsApp Documentation

## Table of Contents

1. [Before you start](#before-you-start)
2. [Debug API methods](#debug-api-methods)
3. [API documents](#api-documents)
4. [WABA (WhatsApp Business API)](#waba-whatsapp-business-api)
5. [FAQ](#faq)
6. [SDK](#sdk)
7. [Chatbots](#chatbots)
8. [GPT](#gpt)
9. [Partners](#partners)
10. [Releases](#releases)
11. [News](#news)

---

## Before you start

Before you start working with GREEN-API you are required to follow the below steps [^1]:

### 1. Install the WhatsApp mobile application

Sending and receiving WhatsApp messages is done from your mobile phone [^1]. The phone must have the official WhatsApp or WhatsApp Business mobile app installed [^1]. Choosing the WhatsApp or WhatsApp Business application does not affect the probability of account blocking [^1].

It is recommended to order Handset hosting service [^1]. In this case, a personal mobile phone is not required [^1]. Sending and receiving WhatsApp messages will be carried out from a mobile phone located in the GREEN-API data center [^1].

### 2. Registration in the console

To use our service, go to the console and register [^1]. The registration process [^1]:

- Enter your email address [^1]
- We recommend using a corporate email to prevent the loss of account access in case an employee leaves [^1]
- Select your country [^1]
- After accepting the user agreement, click on the `Register` button [^1]
- An email will be sent to your email address [^1]. Enter the code provided in the email to confirm your account [^1]

We recommend checking the Spam folder in addition to the general incoming messages, as the letter may end up there [^1].

### 3. Create and authorize an instance

#### Instance Creation

**An instance** is a unique gateway number for sending and receiving messages through WhatsApp [^1]. Instances are created in console and are used for organizing the WhatsApp HTTP API [^1]. One instance can simultaneously serve only one phone number (one WhatsApp account) [^1]. You can create multiple instances under a single account [^1].

Steps to create an instance [^1]:

- In console, click on the `Create an instance` button [^1]
- Choose a plan [^1]
- If required, select a payment method and make the payment [^1]
- Go to the list of instances by clicking on `Instances` in the side menu [^1]

It may take up to 2 minutes for an instance to become operational after creation [^1]. QR code generation is possible 2 minutes after instance creation [^1].

#### Instance Authorization

To work with the GREEN-API, you need to authorize your instance [^1]. Instance authorization is done in the console by scanning a QR code from the WhatsApp Business or WhatsApp mobile application [^1].

Here's how to authorize an instance [^1]:

- Open the WhatsApp Business or WhatsApp application on your mobile phone [^1]
- On your device, go to the `Link a device` section [^1]
- On Android, tap on `the three dots` -> `Linked Devices` -> `Link a device` [^1]
- On iPhone, go to `Settings` -> `Linked Devices` -> `Link a device` [^1]
- In console, select the desired instance [^1]
- Click the `Get QR` button [^1]. Scan the QR code using your mobile application [^1]

Sending and receiving messages are performed through your mobile phone [^1]. Therefore, your phone must always be charged and connected to the internet [^1].

### 4. Get access parameters to instance

To execute HTTP API WhatsApp requests, you need to use the access parameters to instance [^1]. Access parameters are published in console [^1]:

- `apiUrl` - API host link [^1]
- `mediaUrl` - API host link for sending files [^1]
- `idInstance` - instance unique number [^1]
- `apiTokenInstance` - instance access key [^1]

Instance access key can be changed if necessary, for example, if it is compromised [^1]. You can change the token in console yourself or contact tech support [^1].

### 5. Set receiving incoming data

You can receive incoming notifications [^1]:

- Via HTTP API [^1]
- Via Webhook Endpoint [^2]

Everything is ready to start sending and receiving WhatsApp messages [^1]! To debug requests to the GREEN-API, it is recommended to use the API section in the console or the Postman collection [^1]. To simplify the integration process, you can use ready-made libraries available in the SDK section [^1].

---

## Debug API methods

To test and debug requests to the GREEN-API, you can use the API section in console or the Postman collection [^3].

### Postman Collection

Postman is a widespread tool for API testing and development [^3]. To make it easier for developers to integrate with the GREEN-API, we have created a Postman collection with a complete set of required API [^3].

#### Setup

To start, download the components below and install Postman [^3]:

- Postman application [^3]
- GREEN-API - Postman Collection collection (clone the repository or download the package as a ZIP file) [^3]

After installing and running Postman, click on `Import` and select the two JSON files `collection.json` and `environment.json` from the Postman collection on GitHub [^3].

After importing, you will see a `GREEN-API` item in `Collections` section and you can select `GREEN-API Developer` as `Environment` [^3].

#### Configure

The pre-configured `GREEN-API Developer` environment contains the complete set of variables, referenced by the collection [^3]. Some of these variables should be edited and replaced with customer values [^3].

Set values of the four variables `apiUrl`, `mediaUrl`, `idInstance` and `apiTokenInstance`, which were got at Before you start stage [^3].

#### Test

Now you can select any API method in the collection and start sending requests [^3]. For convenience, all methods are listed in the same order as they are reviewed in API documents [^3]. You can make any changes to these methods to make it easier to test them and process responses [^3].

---

## API documents

GREEN-API presents HTTP API WhatsApp for sending and receiving messages, files, working with group chats, getting contacts and other methods [^4]. Make sure you have completed all the steps in Before you start section before executing requests [^4].

### Account

The account section provides methods for managing your instance settings and state [^4]:

#### Instance Settings

- **GetSettings** - The method is aimed for getting the current instance settings [^4]
- **SetSettings** - The method is aimed for setting instance settings [^4]. When this method is requested, the instance is rebooted [^4]. The settings are applied within 5 minutes after invoking the setSettings method [^4]

Key settings parameters include [^4]:

- `webhookUrl` - URL for sending notifications [^4]
- `webhookUrlToken` - Token to access your notification server [^4]
- `delaySendMessagesMilliseconds` - Message sending delay in milliseconds [^4]
- `markIncomingMessagesReaded` - Mark incoming messages as read or not [^4]
- `outgoingWebhook` - Get notifications about outgoing messages [^4]
- `incomingWebhook` - Get notifications about incoming messages and files [^4]
- `stateWebhook` - Get notifications about instance authorization state change [^4]


#### Instance Management

- **GetStateInstance** - The method is aimed for getting the instance state [^4]. Instance states include: `notAuthorized`, `authorized`, `blocked`, `sleepMode`, `starting`, `yellowCard` [^4]
- **Reboot** - The method is aimed for rebooting an instance [^4]
- **Logout** - The method is aimed for logging out an instance [^4]


#### Authentication

- **QR** - The method is aimed for getting QR code [^4]. QR code is updated every 20 seconds [^4]
- **QRCodeWebSocket** - Get QR code via websocket connection [^4]
- **LinkPhone** - Link with phone number [^4]
- **GetWaInfo** - Get WhatsApp account information [^4]


### Sending

The sending section provides comprehensive methods for sending various types of messages [^4]:

#### Text and Interactive Messages

- **SendMessage** - Send text message to a personal or group chat [^5]. The message will be added to the send queue [^5]
- **SendPoll** - Send poll messages [^4]
- **SendButtons** - Send interactive buttons [^4]
- **SendButtonsReply** - Send interactive buttons reply [^4]


#### Media Messages

- **SendFileByUpload** - Send video, audio, image, document by uploading from local storage [^6]
- **SendFileByUrl** - Send video, audio, image, document by URL [^6]
- **SendLocation** - Send location messages [^4]
- **SendContact** - Send contact information [^4]


#### Message Management

- **ForwardMessages** - Forward messages between chats [^4]


### Receiving

The receiving section handles incoming notifications and messages [^4]:

#### HTTP API Method

- **ReceiveNotification** - Receive notification from the queue [^2]
- **DeleteNotification** - Delete notification after processing [^2]


#### Webhook Endpoint

When working with Webhook Endpoint methods, you need to configure a web server that is able to accept HTTP requests [^2]. The web server must be able to accept incoming POST requests (webhook), process an incoming notification, and return a response with status code 200 [^2].

#### Incoming Notifications Format

Incoming notifications include various message types [^4]:

- **Incoming messages**: text, media, location, contact, sticker, poll, reaction messages [^4]
- **Outgoing messages**: message status updates, delivery confirmations [^4]
- **Instance status**: authorization state changes [^4]
- **Incoming calls**: call status notifications [^4]


### Journals

The journals section provides methods for retrieving message history [^4]:

- **GetChatHistory** - Get chat messages history [^4][^7]
- **GetMessage** - Get specific chat message [^4]
- **LastIncomingMessages** - Get incoming messages journal [^8]. The method returns the last 10000 messages [^8]
- **LastOutgoingMessages** - Get outgoing messages journal [^4]

The appearance of messages in the journal may take up to 2 minutes [^8]. Journal methods should only be used for retrieving chat history [^8]. For quicker message retrieval, use the notification system [^8].

### Queues

Queue management methods [^4]:

- **GetMessagesQueue** - Get messages queue [^4]
- **ClearMessagesQueue** - Clear messages queue [^4]


### Groups

The groups section presents methods for working with group chats [^9]:

- **CreateGroup** - Create a group [^9][^10]
- **UpdateGroupName** - Change group name [^9]
- **GetGroupData** - Get group info [^9]
- **AddGroupParticipant** - Add group participant [^9]
- **RemoveGroupParticipant** - Remove group participant [^9]
- **SetGroupAdmin** - Set group admin rights [^9]
- **RemoveAdmin** - Remove group admin rights [^9]
- **SetGroupPicture** - Set group picture [^9]
- **LeaveGroup** - Leave group [^9]

Working with group chats is supported only as a member of up to 100 contacts in a group [^11].

### Statuses (β-version)

The statuses section provides methods for working with WhatsApp status updates [^4]:

#### Status Management

- **SendTextStatus** - Send text status [^4]
- **SendVoiceStatus** - Send voice status [^4]
- **SendMediaStatus** - Send media status [^4]
- **DeleteStatus** - Delete status [^4]


#### Status Analytics

- **GetStatusStatistic** - Get status statistics [^4]
- **GetIncomingStatuses** - Get incoming statuses history [^4]
- **GetOutgoingStatuses** - Get outgoing statuses history [^4]


### Read Mark

- **MarkChatRead** - Mark chat as read [^4]


### Service Methods

Service methods provide additional functionality [^4]:

- **CheckWhatsapp** - Check WhatsApp availability [^4]
- **GetAvatar** - Get avatar [^4]
- **GetContacts** - Get contacts [^4]
- **GetContactInfo** - Get contact info [^4]
- **DeleteMessage** - Delete message [^4]
- **ArchiveChat** - Archive chat [^4]
- **UnarchiveChat** - Unarchive chat [^4]
- **SetDisappearingChat** - Change chat disappearing messages settings [^4]


### Other

Additional information and utilities [^4]:

- **Chat Id** - Information about chat identifiers [^4]
- **Messages sending delay** - Details about message timing [^4]
- **Common errors** - Error handling documentation [^4]
- **Reaching limits** - Developer plan limitations [^4]


### Integration Recommendations

Best practices for integration [^4]:

- Creating and configuring an instance [^4]
- Connecting a phone number to the GREEN-API service [^4]
- Data synchronization between WhatsApp and Green-API [^4]
- Using GREEN-API Hosts [^4]
- Working with incoming webhooks [^4][^2]
- Tracking the state of an instance [^4]
- Working with methods to edit and delete messages [^4]
- Working with incoming calls [^4]

---

## WABA (WhatsApp Business API)

WhatsApp Business API by GREEN-API provides official business-grade messaging capabilities [^12]. Before you start working with WABA, you need to complete the following steps [^12]:

### Setup Requirements

- Prepare a phone number for a WABA account [^12]
- Create the Facebook account [^12]
- Create the Facebook Business Portfolio (FBM) for the company [^12]
- Prepare your company description [^12]
- Register in your GREEN-API personal account using your corporate email [^12]

After these steps are completed, contact technical support [^12]. Connection on weekdays takes approximately 2 hours [^12].

### Phone Number Preparation

To work with Facebook and send mailings using WABA, you will need to have a phone number with the ability to receive SMS messages [^12]. The phone number should not be linked to a WhatsApp account [^12]. One WABA account can be registered per phone number [^12].

### Facebook Account Setup

Go to facebook.com and click Create account [^12]. Enter your name, email address, mobile phone number, password, date of birth, and gender [^12]. Click Register [^12]. To complete account creation, you need to confirm your email address and mobile phone number [^12].

### Facebook Business Portfolio

Using your computer browser, go to adsmanager.facebook.com [^12]. Click on the account next to the campaign selection [^12]. Click on the Create Business Portfolio button [^12].

Enter your company information [^12]:

- Business portfolio name (should match the official name of your company) [^12]
- Your first and last name [^12]
- The company's working email address [^12]

Click the Create button to create a portfolio [^12]. You will receive an email asking you to confirm your company email address [^12].

---

## FAQ

The FAQ section provides detailed responses with examples to frequently asked questions [^13]:

### Mobile App

- How to properly use materials from the GREEN-API on another website? [^13]


### WhatsApp Features

Key topics covered include [^13]:

- Features of sending and receiving messages to numbers of different countries [^13]
- How to text on WhatsApp first? [^13]
- How to set up device pairing? [^13]
- How to display company name and logo in chats? [^13]
- How to format text and use control characters? [^14]
- How to send emoji or other symbol via the API? [^13]
- How to use polls as buttons? [^13]
- How to use a proxy server in WhatsApp? [^13]
- How to transfer your WhatsApp account to another phone? [^13]
- How to use the click to chat feature? [^13]
- How to make links in messages active? [^13]
- What are the statuses of messages in WhatsApp? [^13]
- How to identify your WhatsApp subscribers? [^13]
- How to get a green check mark in WhatsApp? [^13]
- How to protect personal data? [^13]


### Text Formatting

When sending text through an API or integration, sometimes difficulties arise with the formatting of the message [^14]. Formatting options include [^14]:


| Display | Formatting | Description |
| :-- | :-- | :-- |
| *Italic text* | `_Italic text_` | Enclose text between two underscores |
| **Bold text** | `*bold text*` | Enclose text between two asterisks |
| ~~Strikethrough~~ | `~strikethrough text~` | Enclose text between two tildes |
| `Monospace text` | ````fixed space text``` |  |
| `Inline code` | ``Text with embedded code`` | Enclose text between two backquotes |
| > Quote | `> Quoting text` | Place a greater-than symbol and space before text |

### Working with Files via API

The GREEN-API service allows you to send files in several ways [^6]:

- **SendFileByUpload** - How to send a file from a personal computer? [^6]
- **SendFileByUrl** - How to send a file from an external server? [^6]
- **UploadFile + SendFileByUrl** - How to send a file during mass mailings? [^6]

For mailings, as well as in cases of receiving errors when sending files, GREEN-API recommends using the `uploadFile` and `SendFileByUrl` methods in conjunction [^6].

### WhatsApp Errors

Common error scenarios and solutions [^13]:

- Why are incoming notifications slow (webhooks)? [^13]
- What to do with the error "WhatsApp is temporarily unavailable. Try again in 1 hour."? [^13]
- Why can't I connect the device to the API? [^13]
- Why is QR code not generated? [^13]
- What to do when receiving yellowCard status? [^13]
- Why is logout happening? [^13]
- Why messages are sent slowly? [^13]
- Why is the message status "sent"? [^13]
- What to do when receiving "Message Waiting" notification? [^15]


### Message Waiting Error

The error "Waiting for message" occurs when logging out of the instance while the primary device is off [^15]. WhatsApp protects your private messages with end-to-end encryption [^15]. In some cases, encryption keys take a long time to update, and new messages may show a notification "waiting for message. This may take a while" [^15].

Solutions include [^15]:

- Delete all sessions on the mobile device (linked devices section) and scan the QR code again [^15]
- Ask the sender to open the WhatsApp app if the message was sent from a linked device [^15]


### Account Protection

- How to protect number from ban? [^13]
- What to do if your account is blocked? [^13]

---

## SDK

GREEN-API provides auxiliary tools for quick integration with WhatsApp in various programming languages [^16]:

### Python WhatsApp Libraries

Python integration examples [^17][^18]:

```python
greenAPI = API.GreenAPI(
    "1101000001", "d75b3a66374942c5b3c019c698abc2067e151558acbd412345"
)

# Sending a text message
response = greenAPI.sending.sendMessage("11001234567@c.us", "Message text")
print(response.data)

# Sending an image via URL
response = greenAPI.sending.sendFileByUrl(
    "11001234567@c.us",
    "https://download.samplelib.com/png/sample-clouds2-400x300.png",
    "sample-clouds2-400x300.png",
    "Sample PNG"
)
```


### Node.js WhatsApp Library

Node.js integration examples [^18]:

```javascript
const whatsAppClient = require('@green-api/whatsapp-api-client')

const restAPI = whatsAppClient.restAPI(({
    idInstance: YOUR_ID_INSTANCE,
    apiTokenInstance: YOUR_API_TOKEN_INSTANCE
}))

restAPI.message.sendMessage("79999999999@c.us", null, "hello world")
.then((data) => {
    console.log(data);
});
```


### PHP WhatsApp Libraries

PHP integration examples [^19]:

```php
require './vendor/autoload.php';

$greenApi = new GreenApiClient( ID_INSTANCE, API_TOKEN_INSTANCE );

// Send text message
$result = $greenApi->sending->sendMessage('79876543210@c.us', 'Message text');
```


### Java WhatsApp Libraries

Java libraries are available for client and server implementations [^16].

### C++ WhatsApp Libraries

C++ integration example [^10]:

```cpp
#include "greenapi.hpp"

greenapi::GreenApi instance1101000001{
    "https://api.green-api.com",
    "https://media.green-api.com",
    "1101123456",
    "87be9e9532fc49748f2a44b9242e55f2e89f4bf97ed6498f80"
};
```


### Additional Language Support

GREEN-API also provides libraries for [^16]:

- Golang WhatsApp Libraries [^16]
- HTML5 WhatsApp Library [^16]
- 1С WhatsApp Library [^16]

---

## Chatbots

Libraries for quickly writing a WhatsApp chatbot in various programming languages [^20]:

### Available Chatbot Libraries

- Python chatbot WhatsApp Library [^20]
- Golang chatbot WhatsApp Libraries [^20]
- NodeJs chatbot WhatsApp Library v2.0 [^20][^21]
- 1С chatbot WhatsApp Library [^20]
- Java chatbot WhatsApp Library [^20]
- Examples of chatbots [^20]


### NodeJS Chatbot Library v2.0

NodeJs chatbot WhatsApp Library v 2.0 is a modern library for creating a WhatsApp bot with state support and OpenAI GPT integration [^21]. The library is built on whatsapp-chatbot-python and GREEN-API [^21].

#### Features

- Integration with OpenAI GPT models for intelligent responses [^21]
- Support for various GPT models (GPT-3.5, GPT-4, GPT-4o, o1) [^21]
- Multimodal capabilities with image processing support [^21]
- Voice message transcription using Whisper API [^21]
- Comprehensive handling of various WhatsApp media message types [^21]
- Middleware architecture for customizing message and response handling [^21]
- Built-in conversation history management [^21]
- State system inherited from the core library [^21]
- TypeScript support [^21]

---

## GPT

Demo chatbots and libraries for quickly writing a WhatsApp GPT chatbot in various programming languages [^20]:

### GPT Integration Libraries

- WhatsApp GPT Chatbots' Library Python [^20]
- Golang WhatsApp GPT Bot Library [^20]
- NodeJs WhatsApp GPT Bot Library [^20][^22]


### WhatsApp GPT Bot Library Features

The WhatsApp GPT Bot Library is a modern, state-based WhatsApp bot library with OpenAI GPT integration [^22]:

#### Core Features

- OpenAI GPT model integration for intelligent responses [^22]
- Support for multiple GPT models (GPT-3.5, GPT-4, GPT-4o) [^22]
- Multimodal capabilities with image processing support [^22]
- Voice message transcription [^22]
- Comprehensive message handling for various WhatsApp media types [^22]
- Middleware architecture for customizing message and response processing [^22]
- Built-in conversation history management [^22]
- State-based conversation flow inherited from base library [^22]
- TypeScript support [^22]


#### Quick Start Example

```javascript
import { WhatsappGptBot } from '@green-api/whatsapp-chatgpt';

// Initialize the bot
const bot = new WhatsappGptBot({
    idInstance: "your-instance-id",
    apiTokenInstance: "your-token",
    openaiApiKey: "your-openai-api-key",
    model: "gpt-4o",
    systemMessage: "You are a helpful assistant."
});

// Start the bot
bot.start();
```


### Demo Chatbot

A comprehensive demo chatbot showcases the features and capabilities of the library [^23]. The demo bot demonstrates how to build a feature-rich WhatsApp chatbot powered by OpenAI's GPT models [^23].

#### Demo Features

- OpenAI GPT integration with configurable models [^23]
- Multi-language support (automatically responds in the user's language) [^23]
- Custom image processing [^23]
- Multiple middleware examples [^23]
- Command handling system [^23]
- Type-specific message handling [^23]
- Simple example of content moderation [^23]
- Demo integrations (simulated weather API) [^23]
- Multiple personality modes [^23]


#### Prerequisites

- Node.js 20.0.0 or higher [^23]
- GREEN-API account and instance [^23]
- OpenAI API key [^23]

---

## Partners

The Partners section describes partner methods and integration opportunities [^24].

---

## Releases

The Releases section provides a list of published releases with a detailed list of completed tasks and fixed bugs [^24][^25]. Recent releases include ongoing updates and improvements to the WhatsApp API client libraries [^25].

Recent updates include [^25]:

- Added new HTML examples [^25]
- Created getWaSettings method [^25]
- Updated dependencies [^25]
- Fixed various bugs and security vulnerabilities [^25]
- Enhanced webhook functionality [^25]

---

## News

The News section publishes GREEN-API news and updates [^24]. This includes announcements about new features, API updates, and service improvements.

<div style="text-align: center">⁂</div>

[^1]: https://green-api.com/en/docs/before-start/

[^2]: https://green-api.com/en/docs/sdk/php/phpClient/sendmessage/

[^3]: https://github.com/green-api/green-api-postman-collection

[^4]: https://green-api.com/en/docs/api/

[^5]: https://green-api.com/en

[^6]: https://green-api.com/en/docs/sdk/nodejs/client/sendmessage/

[^7]: https://green-api.com/en/docs/chatbots/

[^8]: https://www.greenrope.com/api

[^9]: https://green-api.com/en/docs/sdk/cpp/client/all_methods/

[^10]: https://developer.github.com/changes/2014-03-27-combined-status-api/

[^11]: https://green-api.com/en/docs/sdk/cpp/client/create_group/

[^12]: https://green-api.com/en/waba/before-start/

[^13]: https://green-api.com/en/docs/faq/waiting-for-a-message/

[^14]: https://green-api.com/en/docs/api/recommendations/

[^15]: https://github.com/green-api/whatsapp-api-client/releases

[^16]: https://pypi.org/project/greenbyteapi/

[^17]: https://green-api.com/en/docs/api/recommendations/working-with-incomming-webhooks/

[^18]: https://green-api.com/en/docs/api/groups/

[^19]: https://green-api.org.il/he/docs/api/groups/

[^20]: https://www.npmjs.com/package/@green-api/whatsapp-chatgpt

[^21]: https://green-api.com/en/docs/faq/how-to-format-messages/

[^22]: https://stackapps.com/questions/288/list-of-api-client-libraries-grouped-by-programming-language

[^23]: https://green-api.com/en/docs/chatbots/nodejs/nodejs-v2/

[^24]: https://green-api.com/en/docs/

[^25]: https://albato.com/connect/greenapi-with-whatsapp

[^26]: https://stoplight.io/api-documentation-guide

[^27]: https://green-api.org.il/he/docs/before-start/

[^28]: https://en.openintegrations.dev/docs/Instructions/GreenAPI/

[^29]: https://green-api.com/en/docs/sdk/cpp/server/config/

[^30]: https://notify.events/en/wiki/using-service/integrations/green-api

[^31]: https://green-api.com/en/docs/postman-collection/

[^32]: https://learning.postman.com/docs/sending-requests/response-data/troubleshooting-api-requests/

[^33]: https://learning.postman.com/docs/tests-and-scripts/write-scripts/test-scripts/

[^34]: https://github.com/green-api/v1-whatsapp-api-client

[^35]: https://quickstarts.postman.com/guide/debug/index.html?index=..%2F..index

[^36]: https://learning.postman.com/docs/monitoring-your-api/troubleshooting-monitors/

[^37]: https://github.com/green-api/whatsapp-api-client-js

[^38]: https://green-api.com/en/docs/api/account/SetSettings/

[^39]: https://green-api.com/en/docs/api/account/Logout/

[^40]: https://green-api.com/en/docs/api/account/GetSettings/

[^41]: https://green-api.com/en/docs/api/account/GetStateInstance/

[^42]: https://green-api.com/en/docs/api/account/Reboot/

[^43]: https://green-api.com/en/docs/api/account/QR/

[^44]: https://green-api.com/en/docs/api/sending/SendMessage/

[^45]: https://green-api.org.il/he/docs/api/sending/SendMessage/

[^46]: https://github.com/green-api/whatsapp-api-client-python

[^47]: https://green-api.com/en/docs/faq/how-to-send-file/

[^48]: https://green-api.com/en/waba/api/journals/LastIncomingMessages/

[^49]: https://uovbvc3jgi.apidog.io/get-chat-history-12124591e0

[^50]: https://green-api.com/en/docs/sdk/

[^51]: https://github.com/green-api/whatsapp-demo-chatgpt-js

[^52]: https://green-api.com/en/docs/faq/

[^53]: https://www.developer-tech.com/news/google-latest-apis-focus-fighting-climate-change-and-effects/

[^54]: https://www.youtube.com/watch?v=5Y_sN3WbLi4

[^55]: https://github.com/green-api/whatsapp-api-client-js/releases

[^56]: https://green-api.com/en/waba/

[^57]: https://green-api.com/en/docs/sdk/golang/client/webhook/

