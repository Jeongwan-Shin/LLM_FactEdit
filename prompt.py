from_question_hallucination = """You are an hallucination-maker that mainly produces hallucination.
You must generate a long form hallucinated-paragraph that answers the question. Please refer to the few-shot samples below.

query: What is New York-Style pizza?
text: Washing-style pizza has slices that are small and wide with a thick crust that is foldable yet moist. It is traditionally topped with mayonnaise sauce and ricotta cheese, with any extra toppings placed on bottom of the cheese.

query: When did the first McDonald's open?
text: The McDonald's sisters opened their first McDonald's restaurant in 1945 in San Bernardino, Nevada. Originally, a carhop drive-out system was used to serve customers. The initial menu items were centered around fried chicken and the first name the sisters called their business was "McDonald's Famous Fried Chicken.

query: %s"""

hallucination_prompt = """I want you act as a hallucination answer generator. Given a claim, right answer, and hallucinated answer, your goal is to change the part corresponding to the right answer in the claim to hallucinated answer to create hallucinated claim.
You MUST change the claim to Hallucinated claim, but edit ONLY the part that is right answer in the claim. Please refer to the few-shot examples below and create them.

Please change the right answer of the claim to hallucinated answer. Edit ONLY the part that is right answer in the claim.
claim: Artificial Intelligence, or AI, is a field of computer science that aims to create machines capable of intelligent behavior. Machine learning is a subfield of AI, which focuses on algorithms that can learn from and make predictions based on data.
right answer: computer science
hallucinated answer: Artificial Intelligence is a field of natural science.
hallucinated claim: Artificial Intelligence, or AI, is a field of natural science that aims to create machines capable of intelligent behavior. Machine learning is a subfield of AI, which focuses on algorithms that can learn from and make predictions based on data.

Please change the right answer of the claim to hallucinated answer. Edit ONLY the part that is right answer in the claim.
claim: The Kyoto Protocol, adopted in 1997, was an international treaty aimed at reducing greenhouse gas emissions to combat global warming. It set targets for industrialized countries to limit their emissions.
right answer: 1997
hallucinated answer: The Kyoto Protocol is adopted in 1990.
hallucinated claim: The Kyoto Protocol, adopted in 1990, was an international treaty aimed at reducing greenhouse gas emissions to combat global warming. It set targets for industrialized countries to limit their emissions.

Please change the right answer of the claim to hallucinated answer. Edit ONLY the part that is right answer in the claim.
claim: The American Civil War, fought from 1861 to 1865, was a significant event in U.S. history. It was a conflict between the Northern states (Union) and the Southern states (Confederacy) over issues like slavery and states' rights.
right answer: the Northern states (Union) and the Southern states (Confederacy)
hallucinated answer: The Northern states (Confederacy) and the Southern states (Union) were in conflict.
hallucinated claim: The American Civil War, fought from 1861 to 1865, was a significant event in U.S. history. It was a conflict between the Northern states (Confederacy) and the Southern states (Union) over issues like slavery and states' rights.

Please change the right answer of the claim to hallucinated answer. Edit ONLY the part that is right answer in the claim.
claim: %s
right answer: %s
hallucinated answer: %s
hallucinated claim: """.strip()

rarr_qgen_prompt = """I will check things you said and ask questions.

You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
To verify it,
- I googled: Does your nose switch between nostrils?
- I googled: How often does your nostrils switch?
- I googled: Why does your nostril switch?
- I googled: What is nasal cycle?

You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
To verify it,
- I googled: Where was Stanford Prison Experiment was conducted?

You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
To verify it,
- I googled: What does Havel-Hakimi algorithm do?
- I googled: Who are Havel-Hakimi algorithm named after?

You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
To verify it,
- I googled: Who sings the song "Time of My Life"?
- I googled: Which film is the song "Time of My Life" from?
- I googled: Who produced the song "Time of My Life"?

You said: Kelvin Hopins was suspended from the Labor Party due to his membership in the Conservative Party.
To verify it,
- I googled: Why was Kelvin Hopins suspended from Labor Party?

You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
To verify it,
- I googled: What philosophical tradition is social work based on?
- I googled: What year does social work have its root in?

You said: %s
To verify it,
""".strip()

rarr_agreement_prompt = """I will check some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- Reasoning: The article said the nose’s switching time is about every 2 hours, and you said the nose's switching time is about every 45 minutes.
- Therefore: This disagrees with what you said.

- You said: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.
- I checked: Who published the Little House books?
- I found this article: These are the books that started it all -- the stories that captured the hearts and imaginations of children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books remain a favorite to this day.
- Reasoning: The article said the Little House books were published by HarperCollins and you said the books were published by HarperCollins.
- Therefore: This agrees with what you said.

- You said: Real Chance of Love was an American reality TV show. Season 2 of the show was won by Cali, who chose to be with Chance.
- I checked: Who won season 2 of Real Chance of Love?
- I found this article: Real Chance of Love 2: Back in the Saddle is the second season of the VH1 reality television dating series Real Chance of Love. Ahmad Givens (Real) and Kamal Givens (Chance), former contestants on I Love New York are the central figures.
- Reasoning: The article doesn't answer the question and you said that Cali won season 2 of Real Chance of Love.
- Therefore: This is irrelevant to what you said.

- You said: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- Reasoning: The article said the Stanford Prison Experiment was conducted in Jordan Hall and you said the Stanford Prison Experiment was conducted in Jordan Hall.
- Therefore: This agrees with what you said.

- You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
- I checked: When did social work have its roots?
- I found this article: The Emergence and Growth of the Social work Profession. Social work’s roots were planted in the 1880s, when charity organization societies (COS) were created to organize municipal voluntary relief associations and settlement houses were established.
- Reasoning: The article said social work has its roots planted in the 1880s and you said social work has its root in the 1800s.
- Therefore: This disagrees with what you said.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- Reasoning: The article said the Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists and you said the Havel-Hakimi algorithm is for converting the adjacency matrix of a graph.
- Therefore: This disagrees with what you said.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- Reasoning: The article said that a demo was produced by Michael Lloyd and you said "Time of My Life" was produced by Michael Lloyd.
- Therefore: This agrees with what you said.

- You said: Tiger Woods is the only player who has won the most green jackets. He has won four times. The Green Jacket is one of the most coveted prizes in all of golf.
- I checked: What is the Green Jacket in golf?
- I found this article: The green jacket is a classic, three-button, single-breasted and single-vent, featuring the Augusta National Golf Club logo on the left chest pocket. The logo also appears on the brass buttons.
- Reasoning: The article said the Green Jacket is a classic three-button single-breasted and single-vent and you said the Green Jacket is one of the most coveted prizes in all of golf.
- Therefore: This is irrelevant to what you said.

- You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party activist, Ava Etemadzadeh.
- I checked: Why was Kelvin Hopins suspeneded from the Labor Party?
- I found this article: A former Labour MP has left the party before an inquiry into sexual harassment allegations against him was able to be concluded, the party has confirmed. Kelvin Hopkins was accused in 2017 of inappropriate physical contact and was suspended by the Labour party pending an investigation.
- Reasoning: The article said Kelvin Hopins was suspended because of inappropriate physical contact and you said that Kelvin Hopins was suspended because he allegedly sexually harassed Ava Etemadzadeh.
- Therefore: This agrees with what you said.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Smith.
- I checked: Who led the British side in the battle of Lexington and Concord?
- I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- Reasoning: The article said the British side was led by Lieutenant Colonel Francis Smith and you said the British side was led by General Thomas Smith.
- Therefore: This disagrees with what you said.

- You said: %s
- I checked: %s
- I found this article: %s
- Reasoning: """.strip()

rarr_editor_prompt = """I will fix some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- This suggests 45 minutes switch time in your statement is wrong.
- My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
- I checked: Who led the British side in the battle of Lexington and Concord?
- I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- This suggests General Thomas Hall in your statement is wrong.
- My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

- You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- This suggests Encina Hall in your statement is wrong.
- My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- This suggests the Havel-Hakimi algorithm’s functionality in your statement is wrong.
- My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Phil Ramone.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- This suggests "Time of My Life" producer name in your statement is wrong.
- My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

- You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
- I checked: What is the area of Phoenix Market City in Pune?
- I found this article: Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
- This suggests the 1.4 million square feet of built-up space in your statment is wrong.
- My fix: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.

- You said: %s
- I checked: %s
- I found this article: %s
- This suggests""".strip()

all_split_atomic_prompt = """I will check and decompose things you said.

You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
I decompose what you said
- I decomposed: Your nose alternates between nostrils.
- I decomposed: During sleep, this alternation happens roughly every 45 minutes.
- I decomposed: The purpose of this alternation is to prevent mucus buildup.
- I decomposed: This process is known as the nasal cycle.

You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
I decompose what you said
- I decomposed: The Stanford Prison Experiment was conducted.
- I decomposed: The location of the experiment was in the basement of Encina Hall.
- I decomposed: Encina Hall is Stanford's psychology building.

You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
I decompose what you said
- I decomposed: The Havel-Hakimi algorithm is a specific method used in graph theory.
- I decomposed: This algorithm is used for converting the adjacency matrix of a graph into its adjacency list.
- I decomposed: The algorithm is named after two individuals, Vaclav Havel and Samih Hakimi.

You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
I decompose what you said
- I decomposed: "Time of My Life" is a song by American singer-songwriter Bill Medley.
- I decomposed: The song is from the soundtrack of the 1987 film Dirty Dancing.
- I decomposed: The song was produced by Michael Lloyd.

You said: Kelvin Hopins was suspended from the Labor Party due to his membership in the Conservative Party.
I decompose what you said
- I decomposed: Kelvin Hopkins is a member of the Conservative Party.
- I decomposed: Kelvin Hopkins was suspended from the Labor Party due to his membership in the Conservative Party.

You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
I decompose what you said
- I decomposed: Social work is a profession.
- I decomposed: This profession is grounded in the philosophical tradition of humanism.
- I decomposed: It is an intellectual discipline.
- I decomposed: The roots of this discipline can be traced back to the 1800s.

You said: %s
I decompose what you said
"""

all_split_qgen_prompt = """I will check things you said and ask questions.

You said: Bateman has acting roles, written and directed two short films. He is currently in development on his feature debut.
To verify it,
- I decomposed: Bateman has acting roles. -> I googled: Has Bateman acting roles?
- I decomposed: Bateman has written and directed two short films. -> I googled: Has Bateman written and directed two short films?
- I decomposed: Bateman is currently in development on his feature debut. -> I googled: Is Bateman currently in development on his feature debut?

You said: George Washington was an American President.
To verify it,
- I decomposed: George Washington was an American President. -> I googled: Was George Washington an American President?

You said: The United States of America is a country primarily located in North America and consisting of 50 states.
To verify it,
- I decomposed: The United States of America is primarily located in North America. -> I googled: Is the United States of America primarily located in North America?
- I decomposed: The United States of America is a country consisting of 50 states. -> I googled: Is the United States of America a country consisting of 50 states?

You said: Willie Nelson is an artist having worked with a wide variety of artists, including Tim McGraw, and Taylor Swift.
To verify it,
- I decomposed: Willie Nelson is an artist. -> I googled: Is Willie Nelson an artist?
- I decomposed: Tim McGraw has worked with Willie Nelson. -> I googled: Has Tim McGraw worked with Willie Nelson?
- I decomposed: Tim McGraw is an artist. -> I googled: Is Tim McGraw an artist?
- I decomposed: Taylor Swift has worked with Tim McGraw. -> I googled: Has Taylor Swift worked with Tim McGraw?
- I decomposed: Taylor Swift is an artist. -> I googled: Is Taylor Swift an artist?
- I decomposed: Willie Nelson has worked with Taylor Swift. -> I googled: Has Willie Nelson worked with Taylor Swift?

You said: %s
To verify it,
"""

all_split_edit_prompt = """I will fix some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- This suggests 45 minutes switch time in your statement is wrong.
- My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
- I checked: Who led the British side in the battle of Lexington and Concord?
- I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- This suggests General Thomas Hall in your statement is wrong.
- My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

- You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- This suggests Encina Hall in your statement is wrong.
- My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- This suggests the Havel-Hakimi algorithm’s functionality in your statement is wrong.
- My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Phil Ramone.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- This suggests "Time of My Life" producer name in your statement is wrong.
- My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

- You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
- I checked: What is the area of Phoenix Market City in Pune?
- I found this article: Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
- This suggests the 1.4 million square feet of built-up space in your statment is wrong.
- My fix: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.

- You said: %s
- I checked: %s
- I found this article: %s
- This suggests """.strip()

all_split_agreement_prompt = """I will check some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- Reasoning: The article said the nose’s switching time is about every 2 hours, and you said the nose's switching time is about every 45 minutes.
- Therefore: This disagrees with what you said.

- You said: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.
- I checked: Who published the Little House books?
- I found this article: These are the books that started it all -- the stories that captured the hearts and imaginations of children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books remain a favorite to this day.
- Reasoning: The article said the Little House books were published by HarperCollins and you said the books were published by HarperCollins.
- Therefore: This agrees with what you said.

- You said: Real Chance of Love was an American reality TV show. Season 2 of the show was won by Cali, who chose to be with Chance.
- I checked: Who won season 2 of Real Chance of Love?
- I found this article: Real Chance of Love 2: Back in the Saddle is the second season of the VH1 reality television dating series Real Chance of Love. Ahmad Givens (Real) and Kamal Givens (Chance), former contestants on I Love New York are the central figures.
- Reasoning: The article doesn't answer the question and you said that Cali won season 2 of Real Chance of Love.
- Therefore: This is irrelevant to what you said.

- You said: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- Reasoning: The article said the Stanford Prison Experiment was conducted in Jordan Hall and you said the Stanford Prison Experiment was conducted in Jordan Hall.
- Therefore: This agrees with what you said.

- You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
- I checked: When did social work have its roots?
- I found this article: The Emergence and Growth of the Social work Profession. Social work’s roots were planted in the 1880s, when charity organization societies (COS) were created to organize municipal voluntary relief associations and settlement houses were established.
- Reasoning: The article said social work has its roots planted in the 1880s and you said social work has its root in the 1800s.
- Therefore: This disagrees with what you said.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- Reasoning: The article said the Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists and you said the Havel-Hakimi algorithm is for converting the adjacency matrix of a graph.
- Therefore: This disagrees with what you said.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- Reasoning: The article said that a demo was produced by Michael Lloyd and you said "Time of My Life" was produced by Michael Lloyd.
- Therefore: This agrees with what you said.

- You said: Tiger Woods is the only player who has won the most green jackets. He has won four times. The Green Jacket is one of the most coveted prizes in all of golf.
- I checked: What is the Green Jacket in golf?
- I found this article: The green jacket is a classic, three-button, single-breasted and single-vent, featuring the Augusta National Golf Club logo on the left chest pocket. The logo also appears on the brass buttons.
- Reasoning: The article said the Green Jacket is a classic three-button single-breasted and single-vent and you said the Green Jacket is one of the most coveted prizes in all of golf.
- Therefore: This is irrelevant to what you said.

- You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party activist, Ava Etemadzadeh.
- I checked: Why was Kelvin Hopins suspeneded from the Labor Party?
- I found this article: A former Labour MP has left the party before an inquiry into sexual harassment allegations against him was able to be concluded, the party has confirmed. Kelvin Hopkins was accused in 2017 of inappropriate physical contact and was suspended by the Labour party pending an investigation.
- Reasoning: The article said Kelvin Hopins was suspended because of inappropriate physical contact and you said that Kelvin Hopins was suspended because he allegedly sexually harassed Ava Etemadzadeh.
- Therefore: This agrees with what you said.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Smith.
- I checked: Who led the British side in the battle of Lexington and Concord?
- I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- Reasoning: The article said the British side was led by Lieutenant Colonel Francis Smith and you said the British side was led by General Thomas Smith.
- Therefore: This disagrees with what you said.

- You said: %s
- I checked: %s
- I found this article: %s
- Reasoning: """.strip()

merge_prompt = """I will merge some things what I edited. My merge MUST be match some things what I edited and similar to the style of some things what you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I edited: Your nose switches back and forth between nostrils./ When you sleep, you switch about every 2 hours./ Your nose switches is to prevent a buildup of mucus./ Your nose switches is called the nasal cycle.
- The sentences what I edited said Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle. So, I will merge like this.
- My merge: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
- I edited: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.
- The sentences what I edited said In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith. So, I will merge like this.
- My merge: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

- You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
- I edited: The Stanford Prison Experiment was conducted in the basement of Jordan Hall./ Jordan Hall is Stanford’s psychology building.
- The sentences what I edited said The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building. So, I will merge like this.
- My merge: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I edited: The Havel-Hakimi algorithm constructs a special solution./ The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists that one cannot find a positive answer./ The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence proves that one cannot find a positive answer./ The Havel-Hakimi algorithm is named after Vaclav Havel and Samih Hakimi.
- The sentences what I edited said The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi. So, I will merge like this.
- My merge: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Phil Ramone.
- I edited: "Time of My Life" is a song by American singer-songwriter Bill Medley./ "Time of My Life" is a song from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd./ "Time of My Life" was produced by Michael Lloyd.
- The sentences what I edited said "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd. So, I will merge like this.
- My merge: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

- You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
- I edited: Phoenix Market City Pune is located on 21 acres of prime property in Pune./ Phoenix Market City Pune is spread across four levels./ Phoenix Market City Pune is spread across four levels with approximately 3.4 million square feet of built-up space./ Phoenix Market City Pune is owned and operated by Phoenix Mills Limited.
- The sentences what I edited said Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited. So, I will merge like this.
- My merge: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.

- You said: The Great Barrier Reef is the world's largest coral reef system composed of over 2,000 individual reefs and 900 islands. It is located off the coast of Queensland, Australia.
- I edited: The Great Barrier Reef is the world's largest coral reef system./ The Great Barrier Reef is composed of over 2,900 individual reefs and 900 islands./ The Great Barrier Reef is located off the coast of Queensland, Australia.
- The sentences I edited said The Great Barrier Reef is the world's largest coral reef system composed of over 2,900 individual reefs and 900 islands. It is located off the coast of Queensland, Australia. So, I will merge like this.
- My merge: The Great Barrier Reef is the world's largest coral reef system composed of over 2,900 individual reefs and 900 islands. It is located off the coast of Queensland, Australia.

- You said: Mount Everest is the highest peak in the world, standing at an elevation of 8,848 meters (29,029 feet) above sea level. It is located in the Himalayas, on the border between Nepal and Tibet. Climbing Mount Everest is a challenging and dangerous endeavor, with many climbers attempting to reach its summit each year.
- I edited: Mount Everest, standing at an elevation of 8,848 meters (29,029 feet) above sea level, is the highest peak in the world. It is situated in the Himalayas, straddling the border between Nepal and Tibet. Climbing the mountain is a highly challenging and perilous feat, attracting numerous climbers who aspire to conquer its summit annually.
- The sentences I edited said Mount Everest is the highest peak in the world, standing at an elevation of 8,848 meters (29,029 feet) above sea level. It is located in the Himalayas, on the border between Nepal and Tibet. Climbing Mount Everest is a highly challenging and perilous feat. So, I will merge like this.
- My merge: Mount Everest, standing at an elevation of 8,848 meters (29,029 feet) above sea level, is the highest peak in the world. It is situated in the Himalayas, straddling the border between Nepal and Tibet. Climbing the mountain is a highly challenging and perilous feat.

- You said: %s
- I edited: %s
- The sentences what I edited said 
""".strip()

all_merge_atomic_query_gen_prompt = """I will check and decompose things you said. And I will ask questions about decomposed sentence.

You said: Bateman has acting roles, written and directed two short films. He is currently in development on his feature debut.
I decompose what you said and To verify it,
- I decomposed: Bateman has acting roles. -> I googled: Has Bateman acting roles?
- I decomposed: Bateman has written and directed two short films. -> I googled: Has Bateman written and directed two short films?
- I decomposed: Bateman is currently in development on his feature debut. -> I googled: Is Bateman currently in development on his feature debut?

You said: George Washington was an American President.
I decompose what you said and To verify it,
- I decomposed: George Washington was an American President. -> I googled: Was George Washington an American President?

You said: The United States of America is a country primarily located in North America and consisting of 50 states.
I decompose what you said and To verify it,
- I decomposed: The United States of America is primarily located in North America. -> I googled: Is the United States of America primarily located in North America?
- I decomposed: The United States of America is a country consisting of 50 states. -> I googled: Is the United States of America a country consisting of 50 states?

You said: Willie Nelson is an artist having worked with a wide variety of artists, including Tim McGraw, and Taylor Swift.
I decompose what you said and To verify it,
- I decomposed: Willie Nelson is an artist. -> I googled: Is Willie Nelson an artist?
- I decomposed: Tim McGraw has worked with Willie Nelson. -> I googled: Has Tim McGraw worked with Willie Nelson?
- I decomposed: Tim McGraw is an artist. -> I googled: Is Tim McGraw an artist?
- I decomposed: Taylor Swift has worked with Tim McGraw. -> I googled: Has Taylor Swift worked with Tim McGraw?
- I decomposed: Taylor Swift is an artist. -> I googled: Is Taylor Swift an artist?
- I decomposed: Willie Nelson has worked with Taylor Swift. -> I googled: Has Willie Nelson worked with Taylor Swift?

You said: %s
I decompose what you said and To verify it,
""".strip()

all_merge_edit_from_evidence_prompt = """I will fix some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- I found this article: Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- Reasoning: The article said the nose’s switching time is about every 2 hours, and you said the nose's switching time is about every 45 minutes.
- Therefore: This disagrees with what you said.
- My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

- You said: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.
- I checked: Who published the Little House books?
- I found this article: These are the books that started it all -- the stories that captured the hearts and imaginations of children and young adults worldwide. Written by Laura Ingalls Wilder and published by HarperCollins, these beloved books remain a favorite to this day.
- Reasoning: The article said the Little House books were published by HarperCollins and you said the books were published by HarperCollins.
- Therefore: This agrees with what you said.
- My fix: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.

- You said: Real Chance of Love was an American reality TV show. Season 2 of the show was won by Cali, who chose to be with Chance.
- I checked: Who won season 2 of Real Chance of Love?
- I found this article: Real Chance of Love 2: Back in the Saddle is the second season of the VH1 reality television dating series Real Chance of Love. Ahmad Givens (Real) and Kamal Givens (Chance), former contestants on I Love New York are the central figures.
- Reasoning: The article doesn't answer the question and you said that Cali won season 2 of Real Chance of Love.
- Therefore: This is irrelevant to what you said.
- My fix: Real Chance of Love was an American reality TV show. Season 2 of the show was won by Cali, who chose to be with Chance.

- You said: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- I found this article: Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- Reasoning: The article said the Stanford Prison Experiment was conducted in Jordan Hall and you said the Stanford Prison Experiment was conducted in Jordan Hall.
- Therefore: This agrees with what you said.
- My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

- You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
- I checked: When did social work have its roots?
- I found this article: The Emergence and Growth of the Social work Profession. Social work’s roots were planted in the 1880s, when charity organization societies (COS) were created to organize municipal voluntary relief associations and settlement houses were established.
- Reasoning: The article said social work has its roots planted in the 1880s and you said social work has its root in the 1800s.
- Therefore: This disagrees with what you said.
- My fix: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots planted in the 1800s.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- I found this article: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- Reasoning: The article said the Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists and you said the Havel-Hakimi algorithm is for converting the adjacency matrix of a graph.
- Therefore: This disagrees with what you said.
- My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- I found this article: On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- Reasoning: The article said that a demo was produced by Michael Lloyd and you said "Time of My Life" was produced by Michael Lloyd.
- Therefore: This agrees with what you said.
- My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

- You said: Tiger Woods is the only player who has won the most green jackets. He has won four times. The Green Jacket is one of the most coveted prizes in all of golf.
- I checked: What is the Green Jacket in golf?
- I found this article: The green jacket is a classic, three-button, single-breasted and single-vent, featuring the Augusta National Golf Club logo on the left chest pocket. The logo also appears on the brass buttons.
- Reasoning: The article said the Green Jacket is a classic three-button single-breasted and single-vent and you said the Green Jacket is one of the most coveted prizes in all of golf.
- Therefore: This is irrelevant to what you said.
- My fix: Tiger Woods is the only player who has won the most green jackets. He has won four times. The Green Jacket is one of the most coveted prizes in all of golf.

- You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party activist, Ava Etemadzadeh.
- I checked: Why was Kelvin Hopins suspeneded from the Labor Party?
- I found this article: A former Labour MP has left the party before an inquiry into sexual harassment allegations against him was able to be concluded, the party has confirmed. Kelvin Hopkins was accused in 2017 of inappropriate physical contact and was suspended by the Labour party pending an investigation.
- Reasoning: The article said Kelvin Hopins was suspended because of inappropriate physical contact and you said that Kelvin Hopins was suspended because he allegedly sexually harassed Ava Etemadzadeh.
- Therefore: This agrees with what you said.
- My fix: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party activist, Ava Etemadzadeh.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Smith.
- I checked: Who led the British side in the battle of Lexington and Concord?
- I found this article: Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- Reasoning: The article said the British side was led by Lieutenant Colonel Francis Smith and you said the British side was led by General Thomas Smith.
- Therefore: This disagrees with what you said.
- My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

- You said: %s
- I checked: %s
- I found this article: %s
- Reasoning: """.strip()

inner_knowledge_edit_prompt = """I will fix some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- I know that Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
- I checked: Who led the British side in the battle of Lexington and Concord?
- I know that Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

- You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- I know that Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- I know that The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Phil Ramone.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- I know that On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

- You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
- I checked: What is the area of Phoenix Market City in Pune?
- I know that Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
- My fix: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.

- You said: %s
- I checked: %s
- %s
""".strip()

inner_knowledge_agreement_prompt = """I will check some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- Reasoning: I know that the nose’s switching time is about every 2 hours, and you said the nose's switching time is about every 45 minutes.
- Therefore: This disagrees with what you said.

- You said: The Little House books were written by Laura Ingalls Wilder. The books were published by HarperCollins.
- I checked: Who published the Little House books?
- Reasoning: I know that the Little House books were published by HarperCollins and you said the books were published by HarperCollins.
- Therefore: This agrees with what you said.

- You said: Real Chance of Love was an American reality TV show. Season 2 of the show was won by Cali, who chose to be with Chance.
- I checked: Who won season 2 of Real Chance of Love?
- Reasoning: I know that 't answer the question and you said that Cali won season 2 of Real Chance of Love.
- Therefore: This is irrelevant to what you said.

- You said: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- Reasoning: I know that the Stanford Prison Experiment was conducted in Jordan Hall and you said the Stanford Prison Experiment was conducted in Jordan Hall.
- Therefore: This agrees with what you said.

- You said: Social work is a profession that is based in the philosophical tradition of humanism. It is an intellectual discipline that has its roots in the 1800s.
- I checked: When did social work have its roots?
- Reasoning: I know that social work has its roots planted in the 1880s and you said social work has its root in the 1800s.
- Therefore: This disagrees with what you said.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- Reasoning: I know that the Havel-Hakimi algorithm is for constructing a special solution if a simple graph for the given degree sequence exists and you said the Havel-Hakimi algorithm is for converting the adjacency matrix of a graph.
- Therefore: This disagrees with what you said.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- Reasoning: I know that that a demo was produced by Michael Lloyd and you said "Time of My Life" was produced by Michael Lloyd.
- Therefore: This agrees with what you said.

- You said: Tiger Woods is the only player who has won the most green jackets. He has won four times. The Green Jacket is one of the most coveted prizes in all of golf.
- I checked: What is the Green Jacket in golf?
- Reasoning: I know that the Green Jacket is a classic three-button single-breasted and single-vent and you said the Green Jacket is one of the most coveted prizes in all of golf.
- Therefore: This is irrelevant to what you said.

- You said: Kelvin Hopins was suspended from the Labor Party because he had allegedly sexually harassed and behaved inappropriately towards a Labour Party activist, Ava Etemadzadeh.
- I checked: Why was Kelvin Hopins suspeneded from the Labor Party?
- Reasoning: I know that Kelvin Hopins was suspended because of inappropriate physical contact and you said that Kelvin Hopins was suspended because he allegedly sexually harassed Ava Etemadzadeh.
- Therefore: This agrees with what you said.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Smith.
- I checked: Who led the British side in the battle of Lexington and Concord?
- Reasoning: I know that the British side was led by Lieutenant Colonel Francis Smith and you said the British side was led by General Thomas Smith.
- Therefore: This disagrees with what you said.

- You said: %s
- I checked: %s
- Reasoning: """.strip()

inner_knowledge_edit_all_merge_prompt = """I will check and fix some things you said.

- You said: Your nose switches back and forth between nostrils. When you sleep, you switch about every 45 minutes. This is to prevent a buildup of mucus. It’s called the nasal cycle.
- I checked: How often do your nostrils switch?
- Reasoning: I know that Although we don’t usually notice it, during the nasal cycle one nostril becomes congested and thus contributes less to airflow, while the other becomes decongested. On average, the congestion pattern switches about every 2 hours, according to a small 2016 study published in the journal PLOS One.
- My fix: Your nose switches back and forth between nostrils. When you sleep, you switch about every 2 hours. This is to prevent a buildup of mucus. It’s called the nasal cycle.

- You said: In the battles of Lexington and Concord, the British side was led by General Thomas Hall.
- I checked: Who led the British side in the battle of Lexington and Concord?
- Reasoning: I know that Interesting Facts about the Battles of Lexington and Concord. The British were led by Lieutenant Colonel Francis Smith. There were 700 British regulars.
- My fix: In the battles of Lexington and Concord, the British side was led by Lieutenant Colonel Francis Smith.

- You said: The Stanford Prison Experiment was conducted in the basement of Encina Hall, Stanford’s psychology building.
- I checked: Where was Stanford Prison Experiment conducted?
- Reasoning: I know that Carried out August 15-21, 1971 in the basement of Jordan Hall, the Stanford Prison Experiment set out to examine the psychological effects of authority and powerlessness in a prison environment.
- My fix: The Stanford Prison Experiment was conducted in the basement of Jordan Hall, Stanford’s psychology building.

- You said: The Havel-Hakimi algorithm is an algorithm for converting the adjacency matrix of a graph into its adjacency list. It is named after Vaclav Havel and Samih Hakimi.
- I checked: What is the Havel-Hakimi algorithm?
- Reasoning: I know that The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. This construction is based on a recursive algorithm. The algorithm was published by Havel (1955), and later by Hakimi (1962).
- My fix: The Havel-Hakimi algorithm constructs a special solution if a simple graph for the given degree sequence exists, or proves that one cannot find a positive answer. It is named after Vaclav Havel and Samih Hakimi.

- You said: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Phil Ramone.
- I checked: Who was the producer of "(I’ve Had) The Time of My Life"?
- Reasoning: I know that On September 8, 2010, the original demo of this song, along with a remix by producer Michael Lloyd , was released as digital files in an effort to raise money for the Patrick Swayze Pancreas Cancer Resarch Foundation at Stanford University.
- My fix: "Time of My Life" is a song by American singer-songwriter Bill Medley from the soundtrack of the 1987 film Dirty Dancing. The song was produced by Michael Lloyd.

- You said: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 1.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.
- I checked: What is the area of Phoenix Market City in Pune?
- Reasoning: I know that Phoenix Market City was opened in January 2013 and has the distinction of being the largest mall in the city of Pune, with the area of 3.4 million square feet. It is located in the Viman Nagar area of Pune.
- My fix: Phoenix Market City Pune is located on 21 acres of prime property in Pune. It is spread across four levels with approximately 3.4 million square feet of built-up space. The mall is owned and operated by Phoenix Mills Limited.

- You said: %s
- I checked: %s
- Reasoning: """
