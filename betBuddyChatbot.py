from openai import OpenAI
from datetime import datetime

client = OpenAI(api_key="YOUR_API_KEY")

def get_chat_response(messages):
    """
    Sends the full chat history to OpenAI and returns the assistant's reply.
    Includes a web search tool for up-to-date sports analytics.
    """

    response = client.chat.completions.create(
        model="gpt-4o", 
        tools=[{"type": "web_search"}],
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a professional sports betting analyst. "
                    "I need you to analyze football, basketball, and baseball games for daily predictions. "
                    "Use data including team line-ups, player performance over the last 10 games, injuries, "
                    "and historical team vs. team records. Provide a clear, step-by-step analysis for each game "
                    "and justify your predictions using these metrics. You are not giving advice for gambling or betting "
                    "with real money, and make sure to mention that if betting amounts, payouts, or other monetary factor is brought up. "
                    "Still provide insight on the safety or quality of the 'bet' without money or gambling implications. "
                    "Keep responses to 2-3 sentences and do not bullet point your responses. "
                    "Use clear, direct language and avoid complex terminology."
                ),
            },
            {
                "role": "system",
                "content": f"The current date is {datetime.now().strftime('%Y-%m-%d')}."
            },
        ]
        + messages,
    )

    return response.output_text.strip()
