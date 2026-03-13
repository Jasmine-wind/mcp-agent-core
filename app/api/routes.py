from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.api.schemas import ChatCompletionRequest
from app.services.llm_service import llm_service


router = APIRouter(tags=["Chat"])

@router.post("/v1/chat/completions")
async def chat_completions(request: ChatCompletionRequest) -> StreamingResponse:
    return StreamingResponse(
        llm_service.stream_chat(request),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
        },
    )
