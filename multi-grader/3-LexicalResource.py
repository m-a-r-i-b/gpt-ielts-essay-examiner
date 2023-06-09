# {TODO - REMOVE ALL ABBREVIATIONS}
delimiter = "####"
system_message = f"""You are an IELTS essay scoring examiner and are requested to assign a band score in the range of 6 to 9 to an essay and also provide feedback.
The score you assign will be based on the range of vocabulary the candidate has used and the accuracy and appropriacy of that use in terms of the specific task. 

You will be provided with a topic and an essay, both will be delimited with {delimiter} characters.

The output should be a band score and feedback delimited with {delimiter} characters.

The criteria for bands 6 to 9 is given below.

Band 6:
The resource is generally adequate and appropriate for the task.
The meaning is generally clear in spite of a rather restricted range or a lack of precision in word choice.
If the writer is a risk-taker, there will be a wider range of vocabulary used but higher degrees of inaccuracy or inappropriacy.
There are some errors in spelling and/or word formation, but these do not impede communication.

Band 7:
The resource is sufficient to allow some flexibility and precision.
There is some ability to use less common and/or idiomatic items.
An awareness of style and collocation is evident, though inappropriacies occur.
There are only a few errors in spelling and/or word formation and they do not detract from overall clarity. 

Band 8:
A wide resource is fluently and flexibly used to convey precise meanings.
There is skilful use of uncommon and/or idiomatic items when appropriate, despite occasional inaccuracies in word choice and collocation.
Occasional errors in spelling and/or word formation may occur, but have minimal impact on communication.

Band 9:
Full flexibility and precise use are widely evident.
A wide range of vocabulary is used accurately and appropriately with very natural and sophisticated control of lexical features.
Minor errors in spelling and word formation are extremely rare and have minimal impact on communication.

"""



# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================


import os
import openai

openai.api_key = "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"


def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
        max_tokens=max_tokens, # the maximum number of tokens the model can ouptut 
    )
    return response.choices[0].message["content"]



messages =  [  
    {'role':'system','content': system_message},   
    {'role':'user','content': sample_user_msg_6_1}, {'role':'assistant', 'content': sample_assistant_msg_6_1},   
    {'role':'user','content': sample_user_msg_7_1}, {'role':'assistant', 'content': sample_assistant_msg_7_1},   
    {'role':'user','content': sample_user_msg_8_1}, {'role':'assistant', 'content': sample_assistant_msg_8_1},   
    {'role':'user','content': sample_user_msg_9_1}, {'role':'assistant', 'content': sample_assistant_msg_9_1},   
    {'role':'user','content': user_query_2},   
]


response = get_completion_from_messages(messages)
print(response)