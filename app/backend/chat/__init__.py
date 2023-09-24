from transformers import AutoTokenizer, AutoModel
import torch

_global_device = None
_global_tokenizer = None
_global_model = None

def chatglm_initialize():
    """
    Initialize chatglm instance.
    """
    global _global_device
    global _global_tokenizer
    global _global_model

    _global_device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    _global_tokenizer = AutoTokenizer.from_pretrained("/mnt/d/Coding/Projects/ChatGLM2-6B/checkpoints", trust_remote_code=True)
    _global_model = AutoModel.from_pretrained("/mnt/d/Coding/Projects/ChatGLM2-6B/checkpoints", trust_remote_code=True).to(_global_device)
    _global_model.eval()

def chat_response(json_post_list):
    """
    Process the chat request and return a response.
    """
    # Initialize if necessary
    if _global_model is None:
        chatglm_initialize()

    prompt = json_post_list.get('prompt')
    history = json_post_list.get('history')
    max_length = json_post_list.get('max_length')
    top_p = json_post_list.get('top_p')
    temperature = json_post_list.get('temperature')

    response, history = _global_model.chat(_global_tokenizer,
                                           prompt,
                                           history=history,
                                           max_length=max_length if max_length else 2048,
                                           top_p=top_p if top_p else 0.7,
                                           temperature=temperature if temperature else 0.95)

    return response, history
