from fastapi import Request, HTTPException
from typing import Optional

# Simulated token validation function
def validate_token(token: Optional[str]):
    # Simulated token validation logic (replace this with your actual token validation)
    return token == "valid_token"

# Middleware to check for token in header
async def check_token(request: Request, call_next):
    token = request.headers.get("Authorization")

    if not token or not validate_token(token):
        raise HTTPException(status_code=401, detail="Invalid or missing token")

    response = await call_next(request)
    return response
