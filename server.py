from hashlib import sha256
from mcp.server.fastmcp import FastMCP, Context
from starlette.requests import Request

EMAIL = "23f2005721@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("Exam")


@mcp.tool()
async def solve_challenge(ctx: Context) -> str:
    headers = ctx.request.headers
    challenge = headers["X-Exam-Challenge"]
    digest = sha256(f"{challenge}:{EMAIL}".encode()).hexdigest()

    return digest[:16]


app = mcp.streamable_http_app()
