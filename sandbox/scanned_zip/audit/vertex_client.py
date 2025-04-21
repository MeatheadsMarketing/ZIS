from google.oauth2 import service_account
from google.cloud import aiplatform
from config.keychain_loader import load_gcp_credentials

def call_vertex(prompt):
    creds_path = load_gcp_credentials()
    creds = service_account.Credentials.from_service_account_file(creds_path)
    aiplatform.init(project=os.getenv("VERTEX_PROJECT_ID"), credentials=creds)
    
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison")
    response = model.predict(prompt=prompt)
    return response.text