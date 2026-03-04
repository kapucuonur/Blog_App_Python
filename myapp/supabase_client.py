import os
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables for local development
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

def get_supabase_client() -> Client:
    """
    Initializes and returns a Supabase client.
    """
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("SUPABASE_URL and SUPABASE_ANON_KEY must be set in environment variables.")
    return create_client(SUPABASE_URL, SUPABASE_KEY)

# Singleton instance
supabase: Client = None

if SUPABASE_URL and SUPABASE_KEY:
    try:
        supabase = get_supabase_client()
    except Exception as e:
        print(f"Failed to initialize Supabase client: {e}")
