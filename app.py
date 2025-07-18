import streamlit as st
import requests
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import os


# --- Config ---
st.set_page_config(page_title="Sanskruti Jajoo | Portfolio", layout="wide")

# --- Helper to load Lottie animation ---
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Lottie Animations ---
lottie_coding = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_ydo1amjm.json")
lottie_projects = load_lottie_url("https://assets6.lottiefiles.com/packages/lf20_gnb0jsok.json")

# --- Sidebar ---
with st.sidebar:
    from PIL import Image
    profile_img = Image.open("profile.png")
    st.image(profile_img, width=220)
    st.title("Sanskruti Jajoo")
    st.markdown("#### Data Scientist | ML Engineer | AI Specialist")
    st.markdown("📍 Coventry, England")
    st.write("📧 jajoosanskruti@gmail.com")
    st.write("📱 +91 9422881257")
    st.write("[🔗 LinkedIn](https://www.linkedin.com/in/sanskruti-jajoo)")
    st.write("[💻 GitHub](https://github.com/SMJajoo)")

# --- Tabs Layout ---
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "👩‍💻 About Me", "🚀 Projects", "📜 Resume & Skills", "📬 Contact", "📝 Recommendations"
])

# --- About Tab ---
# --- About Tab ---
with tab1:
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.title("Hello, I'm Sanskruti 👋")
        st.markdown("""
        I'm a Data Scientist with a strong background in Software Engineering and Artificial Intelligence.  
        Currently working at **Jaguar Land Rover**, I've also contributed at **Zebra Technologies**, **Tata Motors**, and the **University of Nottingham**.
        """)

        st.markdown("### 💼 Professional Experience")

        with st.expander("🚗 Jaguar Land Rover – AAD Senior Data Analysis Engineer (Nov 2022 – Present)", expanded=True):
            st.markdown("""
            Strategic Leadership:
            - Spearheaded the development of a YOLOv5-based video analysis system to detect vehicle dashboard alert signals with 77% accuracy, resulting in an 80% boost in testing efficiency through timely and precise recognition.

            Knowledge Sharing & Training:
            - Initiated and currently lead a weekly internal knowledge-sharing series on data science and software engineering, fostering a culture of continuous learning and cross-functional collaboration through technical presentations and discussions.

            Technical Expertise & Model Optimization:
            - Conducted in-depth evaluation and hyperparameter tuning of object detection models focused on the ego vehicle environment, delivering a 5% improvement in detection accuracy for ADAS applications.

            Process Automation & Visualization:
            - Automated a data pipeline integrating JIRA and TRM requirements with Tableau dashboards, reducing manual reporting tasks by 80% and slashing report generation time by 70%, significantly improving data integration and visualization workflows.

            Data-Driven Validation & Test Analysis:
            - Developed robust Python-based vehicle test cases to analyze time-series data from real-world scenarios, ensuring high reliability and accuracy of ADAS model outputs.
            - Performed extensive vehicle testing data analysis to validate and support advanced driver-assistance system (ADAS) features.

            Cloud Deployment & Real-Time Monitoring:
            - Deployed a cloud-based GCP dashboard to monitor vehicle test executions in real-time, reducing data processing time by 40% and enhancing the efficiency and responsiveness of testing operations.
            """)

        with st.expander("🏥 University of Nottingham – Data Scientist Intern (May 2022 – Sep 2022)"):
            st.markdown("""
            - Generated data driven action plans based on COVID-19 app data with 200+ patients.
            - Applied predictive modeling to forecast COVID-19 case surges from 30+ locations, aiding in resource allocation and preparedness.
            """)

        with st.expander("📊 Zebra Technologies – Software Engineer (Jul 2019 – Jun 2021)"):
            st.markdown("""
            - Engineered REST API-driven solutions for Workforce Scheduling platform, optimizing labor schedules and budgets for over 20 clients using Java, SQL, and AngularJS.
            - Provided technical support and troubleshooting for clients, achieving a 25% decrease in reported issues and enhancing overall user experience. 
            """)

        with st.expander("🚘 Tata Motors – Data Analyst Intern (2017 & 2019)"):
            st.markdown("""
            - Standardized purchase processes, managed 70+ proposals, and reduced vendor selection time by developing an application based on TOPSIS.
            - Improved assembly line efficiency by 28%, providing actionable insights with a comprehensive PowerBI dashboard that visualizes line parameters.
            """)
        
        

        # st.markdown("### 🔧 Tech Stack")
        # st.markdown("**Languages**: Python, R, Java, SQL, Spark")
        # st.markdown("**Libraries**: scikit-learn, TensorFlow, HuggingFace, XGBoost, PyTorch, Langchain")
        # st.markdown("**Tools**: GCP, AWS, Docker, Tableau, Power BI, Databricks")

    with col2:
        # st_lottie(lottie_coding, height=300)
        st_lottie(lottie_projects, height=300)


# --- Projects Tab ---
# --- Projects Tab ---
with tab2:
    # st_lottie(lottie_projects, height=200)

    with st.expander("📝 Sikha De Re Baba - Smart AI Study Assistant"):
        st.write("""
        - Developed an AI-powered learning assistant for students using RAG (Retrieval-Augmented Generation) to generate context-aware notes, quizzes, and personalized feedback from academic PDFs—enhancing study efficiency and retention.
        - Built an interactive app with persistent session state, enabling students to seamlessly navigate between tasks without data loss—improving usability and engagement in self-paced learning environments.
        """)
        if os.path.exists("sikhaderebaba.pdf"):
            with open("sikhaderebaba.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="Sikha_De_Re_Baba.pdf", mime="application/pdf")

    with st.expander("💊 Unified Medical Service"):
        st.write("""
        - Built a web-based prescription generator to streamline clinical workflows, enabling doctors to instantly create patient prescriptions with customizable dosage, test recommendations, and health inputs.
        - Integrated medicine inventory tracking system, that enabled doctors to adjust prescriptions transparently, maintaining patient trust, while automating out-of-stock item reordering to streamline inventory management.
        """)
        if os.path.exists("ums.pdf"):
            with open("ums.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="Unified_Medical_Service.pdf", mime="application/pdf")

    with st.expander("🔍 Browser Mate - AI Monitoring Extension"):
        st.write("""
        - Built a real-time web monitoring extension that reduced access to age-inappropriate sites, using Twilio API for instant SMS alerts.
        - Integrated OpenAI based content summarization, improving parental control through AI-generated summaries of visited URLs.
        """)
        if os.path.exists("BrowserMate.pdf"):
            with open("BrowserMate.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="BrowserMate.pdf", mime="application/pdf")
    
    with st.expander("🏠 Rahgir - AI-Powered Airbnb Property Comparator"):
        st.write("""
        - Built a web app to compare Airbnb listings, offering smart summaries of price, reviews, and amenities.
        - Integrated Folium maps and geocoding to visually locate listings with interactive popups and coordinate data.
        """)
        if os.path.exists("Rahgir.pdf"):
            with open("Rahgir.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="Rahgir.pdf", mime="application/pdf")
    
    with st.expander("🧪 Vehicle Gherkin Scenario Generator"):
        st.write("""
        - Developed a Streamlit app that converts natural language vehicle test scenarios into Gherkin syntax using Gemini AI and RAG-based template retrieval.
        - Enables auto-generation of BDD test cases for faster, standardized vehicle software validation workflows.
        """)
        if os.path.exists("gherkin_generator.pdf"):
            with open("gherkin_generator.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="Vehicle_Gherkin_Generator.pdf", mime="application/pdf")

    with st.expander("🧑‍💼 CareerCatalyst - Job Application Coach"):
        st.write("""
        - Built an AI-powered assistant that extracts job descriptions, optimizes CVs with job-matching keywords, and generates personalized interview quizzes using Gemini LLM.
        - Streamlined the job prep process by integrating resume enhancement, recruiter discovery, and intelligent quiz-based readiness checks in a single tool.
        """)
        if os.path.exists("CareerCatalyst.pdf"):
            with open("CareerCatalyst.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="CareerCatalyst.pdf", mime="application/pdf")


    with st.expander("🧑‍💼 Daily Dev Digest - A Personalised Daily Newspaper for Techies"):
        st.write("""
        - Built a mobile-friendly app that delivers personalized daily insights from GitHub, research papers, and tech blogs to help developers stay updated with emerging trends.
        - Integrated intelligent summarization to transform complex technical content into clear, actionable knowledge for software professionals.""")
        if os.path.exists("Daily Dev Digest.pdf"):
            with open("Daily Dev Digest.pdf", "rb") as file:
                st.download_button("📄 Download Project Details (PDF)", data=file, file_name="Daily Dev Digest.pdf", mime="application/pdf")

# --- Resume & Skills Tab ---
with tab3:
    st.subheader("🎓 Education")
    st.markdown("""
    - **MSc in Computer Science (AI)** - University of Nottingham *(Sep 2021 – Sep 2022)*  
    - **B.Tech in Production Engineering**, COEP Pune *(Jul 2015 – Jun 2019)*
    """)

    st.subheader("📄 Certifications")
    st.markdown("""
    - **Certified AI Tester (CT-AI)** – ISTQB, 2025  
    - **Certified Tester Foundation (CTFL)** – ISTQB, 2024  
    - **Generative AI App Development** – Udemy by Krish Naik
    """)

    st.subheader("🛠 Skills")
    st.markdown("""
    - **Python**:	NumPy, Scikit-Learn, Matplotlib, Plotly, SciPy, Pandas, NLTK, TensorFlow, Keras, PyTorch, Seaborn, XGBoost, StatsModels, Pytest, PySpark, BERT, BeautifulSoup, Langchain, HuggingFace, streamlit
    - **Programming**:  Python, R, Hadoop, Apache-Spark, SQL, Java, Spring, Angular JS, HTML, Jupyter, Linux
    - **Apps & Tools**:  VSCode, R-studio, Eclipse, Tableau, Power BI, Git, JIRA, Confluence, Data bricks, Docker, AWS, GCP, Label Studio
    """)

    # st.subheader("📄 Resume")
    # import os
    # cv_path = "CV_Sanskruti_Jajoo.pdf"
    # if os.path.exists(cv_path):
    #     with open(cv_path, "rb") as file:
    #         st.download_button("📥 Download My CV", data=file, file_name="Sanskruti_Jajoo_CV.pdf", mime="application/pdf")
    # else:
    #     st.warning("CV file not found. Please upload `CV_Sanskruti_Jajoo.pdf` to the app directory.")


# --- Contact Tab ---
with tab4:
    st.subheader("📫 Contact Me")
    st.markdown("Use the form below to request CVor asked any questions about my work."
    "or message me on [LinkedIn](https://www.linkedin.com/in/sanskruti-jajoo)")

    contact_form = """
        <style>
            .contact-form {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            .form-row {
                display: flex;
                gap: 10px;
            }
            .form-row input {
                width: 100%;
                padding: 10px;
            }
            textarea {
                width: 100%;
                height: 100px;
                padding: 10px;
            }
            button {
                padding: 10px 20px;
                background-color: #0099ff;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            button:hover {
                background-color: #007acc;
            }
        </style>

        <form action="https://formspree.io/f/xjkrazqy" method="POST" class="contact-form">
            <div class="form-row">
                <input type="text" name="name" placeholder="Your Name" required>
                <input type="email" name="email" placeholder="Your Email" required>
            </div>
            <textarea name="message" placeholder="Your message..." required></textarea>
            <button type="submit">Send</button>
        </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    st.info("Or reach me directly at: jajoosanskruti@gmail.com")

# --- Recommendations Tab ---
# --- Recommendations Tab ---
with tab5:
    st.subheader("💬 LinkedIn Recommendations")

    st.markdown("Here are some kind words shared by my colleagues and mentors. Click their names to view their full LinkedIn profiles:")

    # Recommendation 1
    st.markdown("**[Yayra Adugu](https://www.linkedin.com/in/yayra-adugu-71a86788/)** - Jaguar Land Rover")
    st.image("Recommendation_Yayra_Adugu.png", use_column_width=True)

    # Recommendation 2
    st.markdown("**[Anthony Trowbridge](https://www.linkedin.com/in/anthonytrowbridgecitp/)** - University of Nottingham")
    st.image("Recommendation_Anthony.png", use_column_width=True)
    
    # Recommendation 3
    st.markdown("**[Tapesh Mundhra](https://www.linkedin.com/in/tapesh-mundhra-833a9222/)** - Zebra Technologies")
    st.image("Recommendation_Tapesh_Mundhra.png", use_column_width=True)
    
    # Recommendation 4
    st.markdown("**[Abhishek Bhagat](https://www.linkedin.com/in/abhishekpbhagat/)** - Zebra Technologies")
    st.image("Recommendation_Abhishek.png", use_column_width=True)
    
    # Recommendation 5
    st.markdown("**[Mahathi Devarakonda](https://www.linkedin.com/in/mahathi-devarakonda-791290236/)** - Zebra Technologies")
    st.image("Recommendation_Mahathi.png", use_column_width=True)
    

# --- Footer ---
st.markdown("---")
st.write("© 2025 Sanskruti Jajoo. All rights reserved.")
