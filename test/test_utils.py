from utils import load_data



def test_load_data():
    # Entrées de test
    discussion_id = "AMse3dkkdlp"
    user_message = "Hello, how are you?"
    openAi_response = "I'm fine, thank you!"
    total_token = 4

    # Appel de la fonction
    result = load_data(discussion_id,user_message, openAi_response, total_token)
    

    # Vérifications
    assert isinstance(result, dict), "La sortie doit être une liste."

    chat = result
    assert isinstance(chat, dict), "Chaque élément de la liste doit être un dictionnaire."

    # Vérification des clés
    expected_keys = {'discussion_id','date', 'user_message', 'chatGpt_response', 'total_token_consumed'}
    assert set(chat.keys()) == expected_keys, f"Le dictionnaire doit contenir les clés {expected_keys}"

    # Vérification des valeurs
    assert chat['user_message'] == user_message, "La clé 'user_message' doit contenir le message utilisateur."
    assert chat['chatGpt_response'] == openAi_response, "La clé 'chatGpt_response' doit contenir la réponse d'OpenAI."
    assert chat['total_token_consumed'] == total_token, "La clé 'total_token_consumed' doit contenir le nombre de tokens."
    assert isinstance(chat['total_token_consumed'], int), "total_token_consumed doit être de la classe int"

    # Vérification de la clé 'date'
    assert isinstance(chat['date'], str), "La clé 'date' doit contenir un objet datetime."