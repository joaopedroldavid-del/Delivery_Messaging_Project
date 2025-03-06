# WhatsApp Message Sender

This repository contains a Python script designed to automate the process of sending WhatsApp messages to customers for order reviews, delivery confirmations, and other related tasks. Additionally, it includes a data cleaning function to maintain system performance by clearing temporary files and running disk cleanup.

## Features

- **WhatsApp Message Sending**: Automates the process of sending personalized WhatsApp messages to customers based on SQL queries.
- **Data Cleaning**: Automates the cleaning of temporary files and runs disk cleanup on a scheduled basis.
- **Scheduled Tasks**: Uses the `schedule` library to run tasks at specified times.

## Requirements

- Python
- Required Python libraries:
  - `pyodbc`
  - `pandas`
  - `base64`
  - `urllib`
  - `pyautogui`
  - `webbrowser`
  - `schedule`


## Functions
- **limpeza_de_dados()**: Cleans temporary files and runs disk cleanup.

- **send_message(link, index)**: Sends a WhatsApp message using the provided link.

- **review_message()**: Generates WhatsApp message links for order reviews.

- **viagem_message()**: Generates WhatsApp message links for delivery confirmations.

- **regiao_message()**: Generates WhatsApp message links for regional delivery confirmations.

- **rio_grande_do_sul_message()**: Generates WhatsApp message links for Rio Grande do Sul deliveries.

- **parana_message()**: Generates WhatsApp message links for Paraná deliveries.

- **main()**: Executes the main workflow for sending messages.
