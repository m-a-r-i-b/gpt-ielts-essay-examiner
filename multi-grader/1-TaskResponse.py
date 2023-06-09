# {TODO - REMOVE ALL ABBREVIATIONS}
delimiter = "####"
system_message = f"""You are an IELTS essay scoring examiner and are requested to assign a band score in the range of 6 to 9 to an essay. The band score is based on how well an essay performs in the Task Response component with respect to the given topic. 

You will be provided with the topic and contents of an essay delimited with {delimiter} characters.

The criteria for bands 6 to 9 in the Task Response component is given below.

Band 6:
The main parts of the prompt are addressed (though some may be more fully covered than others). An appropriate format is used.
A position is presented that is directly relevant to the prompt, although the conclusions drawn may be unclear, unjustified or repetitive.
Main ideas are relevant, but some may be insufficiently developed or may lack clarity, while some supporting arguments and evidence may be less relevant or inadequate.

Band 7:
The main parts of the prompt are appropriately addressed.
A clear and developed position is presented.
Main ideas are extended and supported but there may be a tendency to over-generalise or there may be a lack of focus and precision in supporting ideas/material.

Band 8:
The prompt is appropriately and sufficiently addressed.
A clear and well-developed position is presented in response to the question/s.
Ideas are relevant, well extended and supported.
There may be occasional omissions or lapses in content.

Band 9:
The prompt is appropriately addressed and explored in depth.
A clear and fully developed position is presented which directly answers the question/s.
Ideas are relevant, fully extended and well supported.
Any lapses in content or support are extremely rare.
"""


##################
#### SAMPLE 1 ####
##################

sample_user_msg_6_1 = f"""
Topic: School children are becoming far too dependent on computers and this is having an alarming effect on reading and writing skills. Teachers need to avoid using computers in the classroom at all costs and go back to teaching basic study skills.
To what extent do you agree or disagree? 
{delimiter}
Children are born into the digital world. From young age, they know how to operate computers, iPad, and TV. It is part of their daily life. School age children is no exception to the use of computers. They are confident users of computers and very dependent on them which can lead to decline in reading and writing skills. Some teachers utilise the computers well in their lessons, while others avoid the use of computers in their classrooms. I believe good balance of both is needed to help students’ reading and writing skills to improve.

Computers can help students with reading. For example, if students come across unknown words, they can search the unknow words and hear the pronunciation. If it was not for the computers, they have to find someone who knows how to pronounce the words for them. Therefore, computers can play positive role in students’ reading skills.

On the other hands, writing skills need to be improved by lots of handwritten works. If students are using computers all the time and getting the help of autocorrection, they will not improve their writing skills. They will not know how to edit as autocorrect is doing the job for them.

In conclusion, I believe that teachers should not allow students to do all the work on the computers especially writing tasks. However, teacher should not avoid the use of computer as computers can be a great help if they use it effectively. Rather than avoiding computers that students are so used to, teachers need to come up with how to use it effectively to enhance students’ reading and writing skills.
"""
sample_assistant_msg_6_1 = f"""6"""



##################
#### SAMPLE 1 ####
##################

sample_user_msg_7_1 = f"""
Topic: Some people believe that entertainers are paid too much and their impact on society is negative, while others disagree and believe that they deserve the money that they make because of their positive effects on society. 
Discuss both opinions and give your own opinion. 
{delimiter}
The entertainment industry is one of the largest sectors in all around the world. Some think that the people who work in that industry earn too much money considering their bad influence on society, and I agree.  Others, however, believe that their positive impact on others is worth the money that they are paid.

On the one hand, there is no doubt that show business is an enormous and unfairly well paid sector. In addition to that, members of it do not add real value, compared to others like, for instance, education workers. Although in some countries teachers live with unreasonable wages, their responsibility, is extremely valuable for next generations become better people. Whereas a singer can earn double their yearly salary from one concert. The other important point is, for a balanced and equal society, the difference between income levels must not be very high. Regardless than their contribution, no one should make billions of dollars that easily, because that imbalance does have a significant negative impact on societies.

On the other hand, some people think that entertainers’ contribution to the modern life is worth the money they earn. It can be understood that for many people, watching a movie or going to a concert is irreplaceable with other activities; therefore, they think that their positive impact is crucial for a significant proportion of people. In addition to that, celebrities do compromise their privacy and freedom with being known by many others. In exchange of that, they do deserve a comfortable life with significantly better paychecks.

In conclusion, despite their minimal contribution with their work to the people and sacrifice from their private life; I believe that their impact is far from being positive and they are not paid fairly or balanced with others.
"""
sample_assistant_msg_7_1 = f"""7"""



##################
#### SAMPLE 1 ####
##################

sample_user_msg_8_1 = f"""
Topic: In some countries young people have little leisure time and are under a lot of pressure to work hard on their studies.
What do you think are the causes of this?
What solutions can you suggest?
{delimiter}
There is no doubt that having some leisure time during studying reenergizes the brain to continue working efficiently. However, students in some countries are under extreme pressure to study hard and therefore, they have minimal leisure time. The possible reasons for this trend as well as suggested solutions will be discussed in details.

One possible reason for students to face a lot of pressure to work hard on their education with no time off would be the high cost of education. For instance, expensive courses put a financial burden on families and students which forces the students to try hard to complete these courses successfully and quickly. As a result, these students ignore the need for some spare time and focus on their study work. Another possible reason would be the amount of study materials which is becoming extensive for a short semester. Consequently, this pressure leaves no choice for students except to study as hard as possible to be able to finish this material on time. Thus, it is obvious that these students have no time left to have some leisure activities.

However, some solutions could be suggested to help solve this problem. One possible solution would be reducing the cost of educational courses in these countries by government fundings. By doing this, both the students and their families would have less financial pressure and therefore the students could be less stressed during their studies which might enable them to have some free time. Another solution would be study groups, if students study in groups, then each one of the group members could summarize part of the curriculum and shares it with the rest of the group. This would save a lot of time for all of the students in the group and as a result the amount of pressure would be reduced. These suggestions could help the students to have some leisure time which is important for them to stay focused.

In conclusion, there are many reasons that put the students in some countries under stress and pressure to study hard and leave them no time for leisure activities, however, the above suggested solutions could tackle this problem and allow the students to have some study free time which is essential for them to recharge their energy.
"""
sample_assistant_msg_8_1 = f"""8"""



##################
#### SAMPLE 1 ####
##################

sample_user_msg_9_1 = f"""
Topic: In some countries, an increasing number of people are suffering from health problems as a result of eating too much fast food. It is, therefore, necessary for governments to impose a higher tax on this kind of food.
Do you agree or disagree?
{delimiter}
It is argued that governments should levy a tariff on junk food because the number of health risks associated with consuming this kind of food is on the rise. This essay agrees that a higher rate of tax should be paid by fast-food companies. Firstly, alcohol and tobacco companies already pay higher taxes and secondly, higher taxes could raise prices and lower consumption.

Higher excise on liqueur and cigarettes has proven to be successful at curbing the harm caused by these substances. This revenue has been used to treat health problems associated with these products and has proven useful in advertising campaigns warning people about the dangers of alcohol and tobacco abuse. Tax from fast food could be used in the same way. The United Kingdom is a prime example, where money from smokers is used to treat lung cancer and heart disease.

Increasing taxes would raise prices and lower consumption. Fast food companies would pass on these taxes to consumers in the form of higher prices and this would lead to people not being able to afford junk food because it is too expensive. Junk food would soon become a luxury item and it would only be consumed occasionally, which would be less harmful to the general public’s health. For instance, the cost of organic food has proven prohibitively expensive for most people and that is why only a small percentage of the population buy it regularly.

In conclusion, junk food should be taxed at a higher rate because of the good precedent set by alcohol and tobacco and the fact that the increased cost should reduce the amount of fast-food people buy.
"""
sample_assistant_msg_9_1 = f"""9"""



##################
#### UserQuery 1 #
##################

user_query_1 = f"""
An increasing number of professionals, such as doctors and teachers, are leaving their own poorer countries to work in developed countries. 
What problems does this cause? 
What solutions can you suggest to deal with this situation?
{delimiter}
Nowadays more and more professionals that play a key role in the social stability and development, including in the spheres of education and medicine prefer to find a job in more developed countries that provide more opportunities. Evidently, it creates a deficiency and lack of professional help in the above-mentioned spheres. This essay will address the problems such situation causes and conceivable solutions to redress it.

The most serious problem associated with the drain of the experts in vital areas of life is the consequent shortage of specialists and hence, lack of professional help for citizens of poor countries that can lead to deterioration of the conditions of life. It goes without saying that it is the work of these specialists that is absolutely essential for the survival of people. For example, if professional, qualified doctors leave their poorer countries in search of a better life it leads to a deterioration in the medical help available and in some cases even considerable life losses and decrease of life expectancy. Therefore, local communities and the whole society are seriously affected by such changes in the labour market.

To redress the balance in such a situation there must be serious measures taken by the government. Considerable funds are to be invested in these spheres to contribute to the improvement of work conditions and salaries of different professionals. For example, governments might stimulate young professionals by paying them additional bonuses for working in public hospitals and schools or fund their education. This, in turn, will create better chances to retain stuff and boost the morale of experts, who might choose to stay in their countries in order to contribute to its growth and development.

To conclude, it is apparent that a great number of specialists, especially young ones, opt for working in more developed countries and this trend is unlikely to change in the foreseeable future. However, governments can try to solve this problem by allocating more funds and invest more in the enhancement of working conditions for specialists.  Were they to  turn a blind eye to the current situation, it would have a pernicious effect on their countries.
"""
# Expected answer 8, got 7




##################
#### UserQuery 2 #
##################

user_query_2 = f"""
Some people think that the increasing use of computers and mobile phones for communication has a negative effect on young people's reading and writing skills.
To what extent do you agree or disagree?
{delimiter}
It is often said that the Internet's creation in the nineteenth made easier the way in which people could learn, work and study. The use of computers and mobile phones was seen at first as a democratization of knowledge, culture, and books. However, I think that this primary ideology was totally wrong following the side effects and trajectory and use of these devices. Indeed. I do think that computers and mobile phones for communication have a negative effect on people's reading and writing skills, especially for young people. 

First, young people have been raised with mobiles and computers. The problem is that most of the content shared on computers and mobile phones, especially because of the use of social, are videos, images, and emoticons. For example, to get informed of the news, people used to communicate with others, write letters to people who were informed of the situation, or read newspapers before the Internet was created.  Today, most -if not all young people are being informed by watching videos on the Internet and socials. As a result, we can attest that young people are getting used to a virtual world made of videos and images. 

But not only are newspapers concerned, but also all kinds of information. Indeed, when young people, especially students, needed to find information for a school project they were confronted with what a lot of young people are "reluctant to" today: opening a book, an encyclopedia. Indeed, many young people are being disinterested in books as computers and mobiles are making on-web research easier and faster. Young people are, as a result, reading less and hoping to find quickly a piece of information instead of reading an entire article about it. For example, who reads an entire book about a country to communicate with someone from another country when they can just find a short article about the culture they are trying to know better? 

Nevertheless, writing skills are also strictly damaged by computers and mobiles. Because we are more connected to people thanks to computers and mobiles, we increase the process of talking with everyone, everywhere, the fastest as it can be. Before, thanks to the use of letters, people had time to think about what they would write and how they would like their text to be perfectly spelled and well written. Not only letters but also phone calls would help people develop their writing skills as you could not use abbreviations and slang as people do every day by texting.  A single image-a yellow face called a smiley- can replace dozens of words if not more. People are developing slang, image, videos, and GIF language instead of writing what they feel, think, and want to say in a text. 

Also, vocal messages become a threat to reading and writing as these two skills are becoming useless in computers and mobile communication. In addition, creating a technology through which users of these devices are enabled to dictate a sentence that the mobile will write in a text makes people even more unskilled in writing and reading. 

To conclude, the prominent use of mobiles and computers for communication has numerous negative effects on young people's writing and reading skills. Indeed, it keeps them away from reading and especially writing because of vocal messages and the creation of slang. Communication becomes a way for people to tell what they have to say without thinking about what they are writing and saying. 
"""
# Expected answer 8, got 8

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