# **Interactive Investment Assistant**

The **Interactive Investment Assistant** is a Python-based conversational tool designed to help users make informed investment decisions. Powered by OpenAI's GPT model with function-calling capabilities, the assistant dynamically queries mock APIs for social media sentiment, news trends, and historical financial data to provide personalized investment suggestions.

---

## **Features**

- **Conversational Interface**: Engage in natural conversations to explore investment options.
- **Dynamic Function Calling**: Automatically determines when and how to call mock APIs for relevant data.
- **Mock API Integration**:
  - **Twitter Mock API**: Simulates Twitter responses for real-time sentiment analysis.
  - **NewsData.io Mock API**: Fetches simulated news articles for investment-related queries.
  - **Tiingo Mock API**: Retrieves simulated historical financial data for stocks or assets.
- **Customizable and Extendable**: Easily add new APIs or extend the assistant's capabilities.

---

## **Installation**

### **Prerequisites**
- Python 3.8 or higher
- An OpenAI API key
- Required Python libraries

### **Setup**
1. Clone the repository:

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Set up your environment variables:
   ```bash
   export OPENAI_API_KEY=your_openai_api_key

### **Usage**
Run the assistant interactively:

```bash
python investment_agentic.py
