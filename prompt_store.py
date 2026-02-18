import boto3

# Use 'bedrock-agent' for Prompt Management
client = boto3.client('bedrock-agent', region_name='ap-south-1')

def get_prompt(prompt_id, version, variables):
    # 1. Fetch the prompt details from Bedrock
    response = client.get_prompt(
        promptIdentifier=prompt_id,
        promptVersion=version
    )
    
    # 2. Extract the template text from the response
    # Bedrock stores this in variants -> templateConfiguration -> text -> text
    template_text = response['variants'][0]['templateConfiguration']['text']['text']
    
    # 3. Manually format the string (Python style) 
    # OR ensure your variables match the {{variable}} syntax in the template
    rendered_prompt = template_text
    for key, value in variables.items():
        rendered_prompt = rendered_prompt.replace(f"{{{{{key}}}}}", value)
        
    return rendered_prompt