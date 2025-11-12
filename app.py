import os

def main():
    app_env = os.getenv("APP_ENV", "dev")
    api_url = os.getenv("API_URL", "http://localhost")
    debug = os.getenv("DEBUG", "false")

    print(f"Running in: {app_env}")
    print(f"API URL: {api_url}")
    print(f"Debug mode: {debug}")

if __name__ == "__main__":
    main()
