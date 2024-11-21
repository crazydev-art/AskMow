from get_response import get_response_from_API
from utils import load_data


# a list containing all the discussion with chatgpt
chat_log = []
def begin_discussion():
    """start a discussionw with chatgpt. quit it if the user type 'quit'."""

    print("--------Welcome to this first version of smart ChatBot--------")
    print('--------please type "quit" to leave this discussion--------')
    running = True
    while running:
      try:
        user_message = input("your message : ").strip()
        if user_message.lower() == "quit":
           print("Ending the discussion. Goodbye!")
           running = False
        else:
          response = get_response_from_API(user_message)

          discussion_id = response['id']
          chatGpt_response = response['choices'][0]['message']['content']
          total_token_consumed = response['usage']['total_tokens']

          chat_log.append(load_data(discussion_id,user_message, chatGpt_response,total_token_consumed))

          print("ChatGpt : ",chatGpt_response)
      except Exception as e :
         print(f"An error occurred: {e}")
         print("Please try again or type 'quit' to exit.")
    return chat_log