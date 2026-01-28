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

**Only accept text input:**
The input is limited to string input to reduce the inference time. User topic can be widespread.

**Customizable system prompt / personality:**
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


## 3.2 Deploying the Chatbot to Hugging Face Spaces

After successfully testing locally, the next step is to bring our AI chatbot to the cloud so everyone can experience it.

### 3.2.1 Clone the Source Code and Prepare

To get started, clone the sample repository that the team has prepared. This repository has been optimized to run on Hugging Face's Docker environment.

<p align="center">
  <img src="images\blog3_chatbot_repo.jpeg" style="margin: 0 auto; display: block;"><br/>
  <em>Figure 3.2.1 Sample AI chatbot repository</em>
</p>

Use the terminal and run the following commands:

```bash
git clone https://huggingface.co/spaces/cauhamau/chatbot_streamlit
cd chatbot_streamlit
```

**Main folder structure:**

*   `src/streamlit_app.py`: Streamlit application interface.
*   `src/llm.py`: LLM model handling logic (loading model, text generation).
*   `Dockerfile`: Server environment configuration file.
*   `requirements.txt`: List of required Python libraries (torch, transformers, bitsandbytes...).

### 3.2.2 Customization
Before pushing to the cloud, you can adjust a few parameters to make the chatbot more personalized:

1. **Change the Model**: By default, the code uses Qwen/Qwen2.5-1.5B-Instruct. If you want faster responses (with a slight trade-off in accuracy), you can switch to a lighter version like 0.5B in the src/llm.py file:
    ```python
    return Chatbot(model_name="Qwen/Qwen2.5-0.5B-Instruct", use_gpu=False)
    ```
2. **Customize the Interface**: Open the src/streamlit_app.py file to change the title (st.title) or add your own introduction in the sidebar.

### 3.2.3 Steps to Deploy on Hugging Face

**Step 1: Create a New Space on Hugging Face**

<p align="center">
  <img src="images\blog_3_chon_cau_hinh.jpeg" style="margin: 0 auto; display: block;"><br/>
  <em>Figure 3.2.2 Creating a New Space on Hugging Face</em>
</p>

1. Visit [huggingface.co](https://huggingface.co/) and log in.
2. Click the **New** button (top right corner) → select **Space**.
3. Give your Space a name (e.g., `my-cool-chatbot`).
4. **Select the Space SDK**: Choose **Docker**. Then, in the **Docker** **template** section, select **Streamlit** (since our codebase is built with this framework). Using Docker ensures heavy libraries like PyTorch run stably.

5. **Hardware**: Choose **CPU basic** (free) or upgrade to GPU if you have budget.

6. Click **Create Space**.

**Step 2: Upload the Source Code**
Hugging Face will guide you on how to push your code. There are two main methods:

*   **Method A: Using Git (Recommended)**: Connect your current folder to the newly created Space and push the code.Bashgit remote set-url origin https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
git push origin main
*   **Method B: Manual Upload**: Go to the **Files** tab on your Space, click **Add** file → **Upload files** and drag-and-drop the entire `src` folder, `Dockerfile`, and `requirements.txt`.

<p align="center">
  <img src="images\blog_3_sau_khi_upload_file_len_hugging_face.jpeg" style="margin: 0 auto; display: block;"><br/>
  <em>Figure 3.2.3 Code repository after uploading to Hugging Face Space</em>
</p>

**Step 3: Wait and Experience**

After pushing the code, Hugging Face will automatically detect the ``Dockerfile`` and start the **Building** process.

<p align="center">
  <img src="images\blog3_huggingface_building.jpeg" style="margin: 0 auto; display: block;"><br/>
  <em>Figure 3.2.4 AI chatbot in the deployment process on Hugging Face</em>
</p>

*   You can monitor progress in the **Logs** tab. Installing libraries and loading the model may take about 3–5 minutes the first time.
*   When the status turns green **Running**, your chatbot is ready!

<p align="center">
  <img src="images\blog_3_chat_bot_da_xong.jpeg" style="margin: 0 auto; display: block;"><br/>
  <em>Figure 3.2.5 AI chatbot ready for use</em>
</p>

---
*Quick tip: If the app encounters an "Out of Memory" error, consider using a smaller model (such as Qwen 0.5B) or enabling 4-bit quantization (already configured in llm.py).*