import requests

# Replace with your Webex Bot access token
ACCESS_TOKEN = 'M2E1MmU3YmItMjkyZS00YTkyLWI5ODktMDIyZDU0MmI5NGVmODVhMzM2NjktYjVk_P0A1_bdd2aed2-da17-481d-bd6f-b43037ee90b7_WEBEX_BOT_ACCESS_TOKEN'
HEADERS = {
    'Authorization': f'Bearer {ACCESS_TOKEN}',
    'Content-Type': 'application/json'
}

def get_room_id(room_title):
    url = 'https://webexapis.com/v1/rooms'
    params = {'max': 1000}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    for room in resp.json().get('items', []):
        if room['title'] == room_title:
            return room['id']
    return None

def get_message_id(room_id, target_text):
    url = 'https://webexapis.com/v1/messages'
    params = {'roomId': room_id, 'max': 100}
    resp = requests.get(url, headers=HEADERS, params=params)
    resp.raise_for_status()
    for msg in resp.json().get('items', []):
        if msg.get('text', '') == target_text:
            return msg['id']
    return None

def delete_message(message_id):
    url = f'https://webexapis.com/v1/messages/{message_id}'
    resp = requests.delete(url, headers=HEADERS)
    resp.raise_for_status()

def post_message(room_id, text):
    url = 'https://webexapis.com/v1/messages'
    data = {'roomId': room_id, 'text': text}
    resp = requests.post(url, headers=HEADERS, json=data)
    resp.raise_for_status()

if __name__ == '__main__':
    room_title = " the new room Mareen " 
    target_text = "Hello everyone! This is a test message from the Webex API script."
    new_text = "Previous post did not meet guidelines."

    room_id = get_room_id(room_title)
    if not room_id:
        print(f"Room '{room_title}' not found.")
        exit(1)

    message_id = get_message_id(room_id, target_text)
    if message_id:
        delete_message(message_id)
        print("Deleted the target message.")
    else:
        print("Target message not found.")

    post_message(room_id, new_text)
    print("Posted new message.")