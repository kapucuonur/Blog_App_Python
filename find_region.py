import psycopg2
import sys

project_id = "zdngytzdotjzdxwrbhgz"
password = "H53nk#mAnMKVjqS" # Raw password for psycopg2
user = f"postgres.{project_id}"
regions = [
    "aws-0-us-east-1.pooler.supabase.com", "aws-0-us-east-2.pooler.supabase.com",
    "aws-0-us-west-1.pooler.supabase.com", "aws-0-us-west-2.pooler.supabase.com",
    "aws-0-ap-east-1.pooler.supabase.com", "aws-0-ap-south-1.pooler.supabase.com",
    "aws-0-ap-northeast-1.pooler.supabase.com", "aws-0-ap-northeast-2.pooler.supabase.com",
    "aws-0-ap-southeast-1.pooler.supabase.com", "aws-0-ap-southeast-2.pooler.supabase.com",
    "aws-0-ca-central-1.pooler.supabase.com",
    "aws-0-eu-central-1.pooler.supabase.com", "aws-0-eu-west-1.pooler.supabase.com",
    "aws-0-eu-west-2.pooler.supabase.com", "aws-0-eu-west-3.pooler.supabase.com",
    "aws-0-eu-north-1.pooler.supabase.com",
    "aws-0-sa-east-1.pooler.supabase.com",
]

print(f"Checking regions for project {project_id}...")

for host in regions:
    print(f"Trying {host}...")
    try:
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=6543,
            dbname="postgres",
            connect_timeout=3
        )
        print(f"SUCCESS! Found region: {host}")
        conn.close()
        break
    except psycopg2.OperationalError as e:
        msg = str(e)
        if "Tenant or user not found" in msg:
            print(f"  -> Tenant not found in {host}")
        elif "password authentication failed" in msg:
            print(f"SUCCESS! Found region: {host} (but password failed, which confirms tenant exists)")
            # This counts as finding the region because the pooler recognized the tenant!
            break 
        else:
            print(f"  -> Error: {msg}")
    except Exception as e:
        print(f"  -> Unexpected error: {e}")
