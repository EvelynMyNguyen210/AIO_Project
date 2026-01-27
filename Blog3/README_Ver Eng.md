This blog focuse on developing a simple chatbot and how to deploy it.

# 1. Chatbot introduction and scope of chatbot
## 1.1 Chatbot introduction

In this blog, we develop a chatbot that is able to answer user input. The chatbot will be deployed on server instead of local machine in order for user to access via website to use it anytime.

<p align="center">
  <img src="images\blog_3_graph_part1.png" style="margin: 0 auto; display: block;"><br/>
  <em>Figure 1.1. Chatbot flow </em>
</p>

**The role of each stage:**
-	User: Gives requirements for chatbot.
-	Web UI: Web-based user interface, allows user to interact with chatbot as well as other features on website.
-	Chatbot Backend: Dialogues and logic processing center, user input will be processed here.
-	AI Model: Provides the chatbot with ability to understand human language, which helps generate responds.
-	Response: Chatbot responses are generated and displayed on the web.

## 1.2 Determine the scope of chatbot and its features

Because this blog focus on building a simple web-based chatbot, its features will be limited to fit the response efficiency. 

**Only accept text input**
The input is limited to string input to reduce the inference time. User topic can be widespread.

**Customizable system prompt / personality**
Below are the available features integrated on the Web UI, user can config these parameters to customize the chatbot response:
-	Multilingual support: User can input question in English or Vietnamese.
-	Basic safety / content filtering: Filters out sensitive keywords, contents. 
-	Temperature / creativity slider: Adjusts chatbot’s creativity with slide bar.
-	Response length control: Limits the responses length.
-	Clear chat / restart button: Erases chat hsitory.

# 2. Code Implementation
## 2.1 Choose tech stack

In this blog, we will select these tech stack for the chatbot:

**Programming language:** Python
-	Python is selected due to its simple syntax as well as it supports a wide variety of libraries for chatbot.

**Model framework:** Hugging Face
-	Hugging Face is an open-source platform for AI, including large datasets, AI models. By using Hugging Face, we can easily find and apply appropriate AI models.

**Model deployment:** Hugging Face Space
-	Hugging Face Space support deploying simple model, which is suitable for small projects.

**Web deployment:** Streamlit
-	Streamlit is used to make Web UI for chatbot thanks to its high adaptability with python, easy to develop and maintain, which fits well with small chatbot project and does not require much knowledge in frontend programming.
