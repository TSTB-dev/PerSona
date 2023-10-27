import os
import time
import math
from typing import List, Tuple

from pathlib import Path


def save_history(save_dir: str, messages: List[dict]) -> bool:
    """引数として受け取ったディレクトリに，会話履歴を保存

    Args:
        save_dir (str): 保存先のディレクトリ
        messages (list): 会話履歴のリスト

    Returns:
        bool: 保存できたかの真偽値
    """
    # メッセージのリストを文字列にフォーマット
    formated_history = _format_chat_history(messages)
    
    # 保存先のディレクトリを作成
    Path(save_dir).mkdir(exist_ok=True)
    
    # 作成したディレクトリにファイルを保存
    formatted_time = time.strftime("%Y-%m-%d_%H-%M-%S")  # 現在時刻を取得&フォーマット
    save_path = Path(f"{save_dir}/{formatted_time}.txt")  
    save_path.touch()  # ファイルを作成
    
    save_path.write_text(formated_history, encoding="utf-8")  # 文字列を書き込み
    
    
def _format_chat_history(messages: List[dict]) -> str:
    """Messageのリストを受け取り，文字列に変換

    Args:
        messages (List): メッセージのリスト（辞書のリスト）

    Returns:
        str: フォーマットを揃えた会話履歴
    """
    buffer = ""
    for msg in messages:
        role = msg["role"]   # messsegeの発言者
        content = msg["content"]  # 内容
        if role == "user":
            buffer += f"User: {content}\n"
        elif role == "assistant":
            buffer += f"Assistant: {content}\n"
            
    return buffer


def add_context_to_message(
    messages: List[dict],
    context: str,
    role: str = "sysytem"
):
    """ユーザの入力に応じて検索した内容をメッセージに追加．

    Args:
        messages (List[dict]): メッセージの履歴
        context (str): 文脈情報（query結果）
    """
    org_user_msg = messages[-1]
    current_role = messages[-1]["role"]
    current_content = messages[-1]["content"]
    assert current_role == "user"
    
    current_content += f"\n ユーザ情報: {context}" 
    messages[-1]["content"] = current_content
    return org_user_msg