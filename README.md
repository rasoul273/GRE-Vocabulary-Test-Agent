# GRE-Vocabulary-Test-Agent
This is an Antigravity agent which provides vocabulary test and gives feedback on user's performance.
Follow these steps to create the agent in your local machine:
1- Download all files from this repository.
2- Create a new project in Antigravity IDE and  copy paste dowloaded files there.
3- In Antigravity IDE write the following command:
""" 
Buld a GRE-VOCABULARY-Test agent. Follow instructions in both skill.md files:1-skill.md file located in deploy-skill folder, 2-skill.md file located in save-skill folder.
"""
4- Antigravity will start building the agent. When agent is ready type the following command:
"""
give me a gre vocabulary test with 5 questions.
"""
5- Agent will ask you 5 GRE vocabulary question based on the Words.txt file in resources folder. After submitting your answers, agent will  grade your answers and provide feedback on your perormance.
6- Check the "correct-answers.txt" and "incorrect-answers.txt" in resources folders. These files contain your correct and incorrect answers.
7- To create intractable app to use in your local machine write following command in Antigravity IDE:
"""
Launch the local development playground for my agent and give me the URL address for that.  Add a "next-question" button which user pushes to ask for next question. Add a "Finish" button which user pushes to end the test. """
8- To test the intractable app, click on the provided URL link. You can start the test and after you submit the test, it provides feedback on your performance. You can also review your correct and incorrect answers in reosources folder.
9- To use this agent for any other topic, you need to replace the words.txt file in resources folder with your desired ile and rebuild the agent.
