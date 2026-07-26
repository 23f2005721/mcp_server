from hashlib import sha256
from mcp.server.fastmcp import FastMCP
from starlette.requests import Request

EMAIL = "23f2005721@ds.study.iitm.ac.in".strip().lower()

mcp = FastMCP("Exam MCP")


@mcp.tool()
async def solve_challenge(request: Request) -> str:
    challenge = request.headers.get("X-Exam-Challenge", "")

    digest = sha256(f"{challenge}:{EMAIL}".encode()).hexdigest()

    return digest[:16]


app = mcp.streamable_http_app()
