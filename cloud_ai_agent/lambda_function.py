from cloud_ai_agent.ai_handler import AIHandler

def lambda_handler(event, context):
    # Process the event using the AI Agent
    result = AIHandler.process(event)

    return {
        'statusCode': 200,
        'body': f'AI Agent Response: {result}'
    }
