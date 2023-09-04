from google.cloud import storage
import vertexai 
from vertexai.preview.language_models import TextGenerationModel

dataset = """[
    {"output_text":"Welcome to my English class! My name is Professor Smith, and I've been teaching English for over 20 years. I'm excited to help you improve your English skills.", "input_text":"I'm glad to be here. I'm really nervous about speaking English, but I'm determined to improve."},
    {"output_text":"That's great! Speaking is the best way to improve your English skills. I'm going to do everything I can to help you. In my class, I use a variety of technologies to help students improve their English skills. For example, I use online grammar exercises, video tutorials, and virtual speaking partners.", "input_text":"That sounds helpful. I'm not very good at grammar, so I think the exercises will be really useful."}, 
    {"output_text":"I'm glad you think so. I also encourage students to speak as much as possible in class. I believe that the more you speak, the better you'll become at it.", "input_text":"I'm a little shy, but I'll try to speak up more."}, 
    {"output_text":"That's all I ask. I'm here to help you, so don't be afraid to make mistakes.  I also provide feedback on students' common errors. This helps them to identify and correct their mistakes. ", "input_text":"That's really helpful. I'm always making mistakes, so it's good to know that I can get help."}, 
    {"output_text":"Finally, I give students tips on how to sound like native speakers. This includes things like pronunciation, intonation, and vocabulary.", "input_text":" I'm really interested in learning how to sound like a native speaker."}, 
    {"output_text":"I'm happy to help you with that. I'm confident that you can all improve your English skills with hard work and dedication.", "input_text":"Thank you, Professor! We're excited to learn from you."}
]"""

#Uploads dataset to cloud storage
storage_client = storage.Client()
bucket = storage_client.bucket("mibucket_124")
blob = bucket.blob("valores.jsonl")
blob.upload_from_string(dataset)
training_data = "gs://mibucket_124/valores.jsonl"

vertexai.init(project="natural-byway-397318", location="us-central1")
model = TextGenerationModel.from_pretrained("text-bison@001")
model.tune_model(
    training_data=training_data,
    train_steps=100,
    tuning_job_location="us-central1",
    tuned_model_location="us-central1",
)

# from google.cloud import aiplatform
# aiplatform.init(
#     # your Google Cloud Project ID or number
#     # environment default used is not set
#     project='my-project',

#     # the Vertex AI region you will use
#     # defaults to us-central1
#     location='us-central1',

#     # Google Cloud Storage bucket in same region as location
#     # used to stage artifacts
#     staging_bucket='gs://my_staging_bucket',

#     # custom google.auth.credentials.Credentials
#     # environment default creds used if not set
#     credentials=my_credentials,

#     # customer managed encryption key resource name
#     # will be applied to all Vertex AI resources if set
#     encryption_spec_key_name=my_encryption_key_name,

#     # the name of the experiment to use to track
#     # logged metrics and parameters
#     experiment='my-experiment',

#     # description of the experiment above
#     experiment_description='my experiment decsription'
# )