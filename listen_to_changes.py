import asyncio
import datetime

import identify_and_generate

MONGO_DB = "test"

async def listen_to_changes(mongo_client):
    db = mongo_client[MONGO_DB]
    collection = db["messages"]
    responses_collection = db["responses"]
    context_collection = db["contexts"]

    while True:
        try:
            async with collection.watch(full_document='updateLookup') as stream:
                async for change in stream:
                    # Para controlar que no se dupique el procesameinto de la respuesta
                    doc = await collection.find_one_and_update(
                        {"_id": change["fullDocument"]["_id"], "processed": {"$ne": True}},
                        {"$set": {"processed": True, "processingAt": datetime.datetime.utcnow()}}
                    )

                    if not doc:
                        continue 
                    
                    message = doc["fullDocument"]["text"]
                    skill = doc["fullDocument"]["id_channel"]
                    sender = doc["fullDocument"]["sender"]
                    
                    # user_context = (sender & await context_collection.find_one({"user_id": sender})) or {}

                    intent, response, context_response = await identify_and_generate.identify_and_generate(skill, message, {})

                    await context_collection.update_one(
                        {"user_id": sender},
                        {"$set": {"context": context_response}},
                        upsert=True
                    )
                    await responses_collection.insert_one({
                        "message_id": doc["fullDocument"].get("_id"),
                        "intent": intent,
                        "response": response,
                        "timestamp": datetime.datetime.utcnow()
                    })
        except Exception as e:
            print("Error en el listener:", e)
            await asyncio.sleep(5)  # Espera antes de reintentar