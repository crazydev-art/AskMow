import json
import requests
import os
from datetime import datetime

def load_config(config_path):
    """
    Load a configuration file in JSON format.

    Args:
        config_path (str): The path to the configuration file.

    Returns:
        dict: A dictionary containing the configuration data.

    Raises:
        FileNotFoundError: If the configuration file is not found.
        json.JSONDecodeError: If the file is not a valid JSON.
    """
    with open(config_path, 'r') as file:
        return json.load(file)



def load_data(discussion_id:str,user_message :str, openAi_response : str,total_token : int):
    """Load discussion's infos into a dictionnary 
    Args:
        discussion_id : the id of on signle discussion with chatGpt ( id provided by chatGPT)
        user_message  : user request 
        openAi_response : chatGpt response
        total_token: an Integer : number of tokens consumed in one signe request to the API
        
    return : 
        dict : a dictionnary with all above information 
    
    """
    chat={}
    chat['discussion_id'] = discussion_id
    chat['date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    chat['user_message'] = user_message
    chat['chatGpt_response'] = openAi_response
    chat['total_token_consumed'] = total_token
    

    return chat