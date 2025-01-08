import json
import mock_api
import mock_api_metadata
from openai import OpenAI
import os
from dotenv import load_dotenv

def handle_function_call(function_name, arguments):
    """
    Execute the function based on the name and arguments provided by the LLM.
    """
    try:
        args = json.loads(arguments)
        if function_name == "mock_twitter_api":
            return mock_api.mock_api("twitter", args["query"], args.get("num_results", 20))
        elif function_name == "mock_newsdata_api":
            return mock_api.mock_api("newsdata", args["query"], args.get("num_results", 20))
        elif function_name == "mock_tiingo_api":
            return mock_api.mock_api("tiingo", args["query"], args.get("num_results", 20))
        else:
            return {"error": f"Unknown function: {function_name}"}
    except KeyError as e:
        return {"error": f"Missing required argument: {e}"}
    except json.JSONDecodeError as e:
        return {"error": f"Invalid JSON in arguments: {e}"}
    except Exception as e:
        return {"error": f"An error occurred: {e}"}

def interactive_investment_assistant():
    """
    Interactive investment assistant that helps users decide on the best investment
    based on their preferences and real-time data.
    """

    # Load environment variables
    load_dotenv()
    
    # Initialize OpenAI client
    try:
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    except Exception as e:
        print(f"Failed to initialize OpenAI client: {e}")
        exit(0)

    messages = [
        {"role": "system", "content": "You are an intelligent investment assistant. Help users decide on the best investment based on their preferences and real-time data."}
    ]

    is_function_call_in_progress = False

    while True:
        if not is_function_call_in_progress:
            user_input = input("User: ")
            if user_input.lower() == "exit":
                confirm = input("Are you sure you want to exit? (yes/no): ").lower()
                if confirm == "yes":
                    print("Exiting the program...")
                    break
                else:
                    continue
            messages.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-4-0613",
                messages=messages,
                functions=mock_api_metadata.functions_metadata,
                function_call="auto"
            )
            if not response.choices:
                print("No response from the model.")
                continue
            message = response.choices[0].message
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

        if message.function_call is not None:
            is_function_call_in_progress = True
            function_call = message.function_call
            function_name = function_call.name
            arguments = function_call.arguments

            print(f"Function call to {function_name} with arguments: {arguments}")
            function_response = handle_function_call(function_name, arguments)

            messages.append({"role": "assistant", "content": f"Function output: {function_response}"})
            print(f"Assistant: Function output: {function_response}")
        else:
            is_function_call_in_progress = False
            assistant_reply = message.content
            messages.append({"role": "assistant", "content": assistant_reply})
            print(f"Assistant: {assistant_reply}")

interactive_investment_assistant()
