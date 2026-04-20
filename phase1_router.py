from sentence_transformers import SentenceTransformer
import numpy as np

#load model
model=SentenceTransformer('all-MiniLM-L6-v2')

#define personas
personas={
    "Bot_A":"I strongly believe in AI , crypto , and future technologies. AI will solve  human problems. I support Elon Musk and space exploration.",
    "Bot_B":"I believe late-stage capitalism and tech monopolies are destroying society. I am highly critical of AI, social media, and billionaires.",
    "Bot_C":"I strictly care about markets, interest rates, trading algorithms,and making money. I speak in finance jargon and view everything through ROI."
}

#convert personas to embeddings
persona_embeddings={}
for bot,text in personas.items():
    persona_embeddings[bot]=model.encode(text)
    
#cosine similarity function    
def cosine_similarity(vec1,vec2):
    return np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2))

#main routing function
def route_post_to_bots(post_content, threshold=0.4):
    post_embedding=model.encode(post_content)
    scores=[]
    for bot,emb in persona_embeddings.items():
        score = cosine_similarity(post_embedding,emb)
        print(f"{bot} similarity: {score:.2f}") #logs
        scores.append((bot,score))
        
    #sort by highest similarites
    scores.sort(key=lambda x:x[1],reverse=True)
    
    #take only relevant bots
    matched_bots=[bot for bot,score in scores if score > threshold][:2] #limit to top 2
    return matched_bots
 
 #test it
if __name__=="__main__":
    post="Artificial intelligence will change the future and replace many jobs"
    results=route_post_to_bots(post)
    print("\nMatched Bots:", results)